---
description: 把 content.py 重写为 Action Title 版本(指定 tone 档位)
argument-hint: [tone] · 可选 internal | balanced | external · 默认 balanced
---

# /rewrite-action-title

把当前 `content.py` 按 Action Title 原则 + tone 力度档位重写,输出到 `content_action_<tone>.py`,并在 `rewrite_audit.md` 末尾追加本次审计。

## 触发输入

`$ARGUMENTS` = tone 档位,合法值:`internal` / `balanced` / `external`。空值时默认 `balanced`。其他值直接报错并停止,不要猜测。

## 执行步骤

按顺序完成,**不要跳过任何一步**:

### 1. 解析参数

- 读 `$ARGUMENTS`,trim 空白
- 若为空 → tone = `balanced`
- 若为 `internal` / `balanced` / `external` 之一 → tone = 该值
- 否则 → 报错 "tone 必须是 internal/balanced/external 之一,收到: <值>",停止

### 2. 加载 prompt 模板

Read `prompts/rewrite_action_title.md` 全文,这是本次重写的**唯一规则源**。

### 3. 加载输入数据

Read `content.py` 全文。这是被重写的源数据。

### 4. 按 prompt 模板执行重写

对照 prompts/rewrite_action_title.md 的:
- "要重写的字段"清单 — 决定改哪些
- "不动的字段"白名单 — 决定不改哪些
- "Action Title 三大原则" — 决定怎么改 title/subtitle
- "items 力度联动" — 决定 PROBLEMS 页的 head/desc 怎么改
- "tone 力度档位" + "力度词典" — 决定本次 tone 档的修辞特征
- "已知边界" — 避开已知陷阱

特别注意:
- 数字硬编码标题(如 "X 项已交付")要**实际数过 items 才填**,不要瞎填
- 专有名词(产品名 / 账号名 / 公司名)**保留原样**
- 三档红线:balanced 不是平均、external 不退化为信息墙、internal 不滑成黑话

### 5. 写出结果

Write 完整重写后的 Python 文件到 `content_action_<tone>.py`(保持 schema、可运行)。

文件头部 docstring 要写明:
```
"""Action Title 重写版 · tone={tone} · 基于 content.py 自动生成

由 /rewrite-action-title 命令产出。
切换为当前数据:cp content_action_<tone>.py content.py && python redesign.py
"""
```

### 6. 追加审计

在 `rewrite_audit.md` 末尾追加一段(用 Edit 工具,不要用 Write 覆盖):

```markdown

---

## v1 自动重写 · {YYYY-MM-DD} · tone={tone}

- 输入: content.py
- 输出: content_action_<tone>.py
- 改动概要(本次最有代表性的 3 条 title 改写):
  - PRODUCT_MATRIX: <原> → <新>
  - PRODUCT_PROBLEMS: <原> → <新>
  - <第三处自选>
- items 联动: <说明 PROBLEMS 页 items 是否按 tone 重写>
```

### 7. 报告产出

向用户报告:
- 写入了哪个文件
- 关键改动 3-5 条(简短)
- 切换命令:`cp content_action_<tone>.py content.py && .venv/bin/python redesign.py`
- 提示用户:不满意可以 `/rewrite-action-title <其他tone>` 跑别的档位对比

## 不要做的事

- 不要修改 `content.py` 本身
- 不要覆盖 `content_action.py`(那是 v1 commit 的 master)
- 不要修改 `redesign.py`
- 不要修改 OKR 的 krs / 甘特任务名 / 产品名 / 价格 / 数据
- 不要为了"完整"而擅自加新字段或动 schema
