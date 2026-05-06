---
description: 把 v1 详情面数据提炼为 v2 演讲面 6 页(指定 tone 档位)
argument-hint: [tone] · 可选 internal | balanced | external · 默认 balanced
---

# /rewrite-presentation

把 v1 详情面数据(`content_action_<tone>.py` 或 `content.py`)按演讲面摘要规则 + tone 力度档位提炼为 6 页演讲面,输出到 `content_presentation_<tone>.py`,并在 `docs/audit.md` 末尾追加本次审计。

## 触发输入

`$ARGUMENTS` = tone 档位,合法值:`internal` / `balanced` / `external`。空值时默认 `balanced`。其他值直接报错并停止,不要猜测。

## 执行步骤

按顺序完成,**不要跳过任何一步**。

### 1. 解析参数

- 读 `$ARGUMENTS`,trim 空白
- 若为空 → tone = `balanced`
- 若为 `internal` / `balanced` / `external` 之一 → tone = 该值
- 否则 → 报错 "tone 必须是 internal/balanced/external 之一,收到: <值>",停止

### 2. 加载 prompt 模板

Read 以下两份文件全文,这是本次重写的**唯一规则源**:

1. `prompts/rewrite_presentation.md` — 演讲面摘要规则 + 6 页 schema + 硬约束清单
2. `prompts/rewrite_action_title.md` — Action Title 三原则 + tone 力度词典(被前者引用)

### 3. 选定输入数据

按以下优先级选择输入:

1. 若 `content_action_<tone>.py` 存在 → 用它作为输入(详情面已与目标 tone 对齐,两面 tone 自动一致)
2. 否则 → 用 `content.py` 作为输入,**记录 warn**:"未发现匹配 tone 的详情面,两面 tone 一致性需要用户手动校验"

Read 选定文件全文。

### 4. 按 prompt 模板执行重写

对照 `prompts/rewrite_presentation.md` 的:
- "演讲面 6 页 schema" — 决定输出结构
- "摘要规则 1-5" — 决定每页怎么从 v1 提炼
- "tone 三档" — 决定 KEYPOINT/MILESTONE title 的修辞强度
- "两面叙事一致 · 硬约束清单" — 写完后逐项核对

特别注意:
- COVER / CLOSING **逐字段复用 v1**,不要"优化"
- KEYPOINT.points 三条 head/desc 与 v1 PROBLEMS.items **一字不差**
- MILESTONE.lanes 数量必须 = 3,若 v1 有 5 group,按 prompt 规则合并
- title 的 tone 滑动**只动修辞,不动事实**

### 5. 写出结果

Write 完整 Python 文件到 `content_presentation_<tone>.py`(保持 schema、可被 `redesign_presentation.py` 跑通)。

文件头 docstring 见 prompt 模板"输出与审计"一节。

### 6. 自我核对硬约束

逐项过 prompt 模板"两面叙事一致 · 硬约束清单"的 8 条。任何一条不通过,**回到第 4 步重写,不要凑合输出**。

### 7. 追加审计

用 Edit 工具(不要用 Write 覆盖)在 `docs/audit.md` 末尾追加 prompt 模板里的审计模板,填实数据。

### 8. 报告产出

向用户报告:
- 写入了哪个文件
- 4 个 KEYPOINT/MILESTONE title 的判断(简短引用)
- 输入文件来源(content_action_<tone>.py 或 content.py)+ 是否需要手动校验两面 tone
- 渲染命令:
  ```bash
  cp content_presentation_<tone>.py content_presentation.py && .venv/bin/python redesign_presentation.py
  soffice --headless --convert-to pdf output-presentation.pptx
  pdftoppm -r 150 output-presentation.pdf preview_pres -png
  ```
- 提示用户:配套的详情面渲染:`cp content_action_<tone>.py content.py && .venv/bin/python redesign.py`

## 不要做的事

- 不要修改 `content.py` / `content_action_*.py`(那些是输入)
- 不要修改 `redesign.py` / `redesign_presentation.py`
- 不要修改 `content_presentation.py`(那是 v2 master,手写示例)
- 不要重写 PROBLEMS items / Q2 group.task(事实层禁区)
- 不要为了"演讲化"超过 6 页
- 不要发明新的页型或新的 schema 字段
