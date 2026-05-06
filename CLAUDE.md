# PPT2PPT · Claude 项目指令

## 项目性质

把内容密集的工作汇报 pptx 重新设计为沉稳商务风、**可继续编辑**的 pptx。

三层产物:
- **v0 视觉层** — `redesign.py` + `content.py` → `output.pptx`(详情面 15 页)
- **v1 叙事层** — `/rewrite-action-title` skill → `content_action_<tone>.py`
- **v2 信息密度层** — `/rewrite-presentation` skill → `content_presentation_<tone>.py` + `redesign_presentation.py` → `output-presentation.pptx`(演讲面 6 页)

## 关键约定

- **数据/视图分离**：`content*.py` 只放数据,`redesign*.py` 只放版式。改内容不要动 `redesign*.py`。
- **示例数据 vs 真实数据**：仓库里 `content.py` / `content_presentation.py` 是虚构示例(开源所需);真实数据放本地 `content_real.py`(已 gitignore)。
- **不要 commit pptx**：`*.pptx` 已在 `.gitignore`。任何工作汇报 pptx 都视为含敏感数据。
- **字体**：固定 `Microsoft YaHei`(跨平台 fallback 到苹方/思源黑),不要随意改。
- **v1 / v2 是新增不动旧** — v2 不动 v1 的 `redesign.py`,v1 自动产物 `content_action_<tone>.py` 和 v2 自动产物 `content_presentation_<tone>.py` 都在根目录(便于 `cp` 切换)。

## 验证流程

```bash
# 详情面
.venv/bin/python redesign.py
soffice --headless --convert-to pdf output.pptx
pdftoppm -r 150 output.pdf preview -png

# 演讲面
.venv/bin/python redesign_presentation.py
soffice --headless --convert-to pdf output-presentation.pptx
pdftoppm -r 150 output-presentation.pdf preview_pres -png
```

注意:LibreOffice 渲染中文会回退字体(看起来像仿宋);用 PowerPoint/Keynote 实际打开才是雅黑/苹方。**不要因 LibreOffice 渲染异常去改字体设置**。

## 设计系统(不要随意改)

- 主背景：`#0F1B2E`(封面/章节/结尾)
- 内容页背景：`#F7F8FA`
- 主色深蓝：`#1F2A44`
- 暖金点缀：`#C28C4C`
- 状态色：完成 `#0E9F6E` · 进行 `#33537E` · 待启动 `#C0C8D4` · 警示 `#E97316`

## 页面类型 → 函数映射

### 详情面(`redesign.py` · 12 种页型)

| 类型 | 函数 |
|---|---|
| 封面 / 结尾 | `slide_cover` / `slide_closing` |
| 目录 | `slide_toc` |
| 章节分隔 | `slide_section` |
| 矩阵 | `slide_matrix_product` / `slide_matrix_brand` |
| 大字问题 | `slide_problems` |
| OKR 表 | `slide_okr` |
| 真甘特图 | `slide_gantt` |
| 季度计划 | `slide_plan` |
| 账号数据 | `slide_accounts` |

### 演讲面(`redesign_presentation.py` · 复用 v1 utils + 2 种新页型)

| 类型 | 函数 |
|---|---|
| 封面 / 结尾 | 复用 v1 `slide_cover` / `slide_closing` |
| 观点页(大字 Action Title + 3 numbered points) | `slide_keypoint` |
| 节奏页(大字 Action Title + 3 lane 卡片) | `slide_milestone` |

## v2 演讲面字数硬约束

`slide_milestone` 的 lane 卡片在版式里有空间限制,超字数会换行截断:
- `lane.task` ≤ **14 中文字**
- `lane.outcome` 单段 ≤ **8 中文字**,三段总长(箭头不计)≤ **26 字**

合并 lane 时若 v1 两个 group.task 原文串联超字数,**必须改写为统一动作**(例:"V7 迭代 + AI 辅助能力部署" → "V7 + AI 辅助上线")。详见 `prompts/rewrite_presentation.md` 规则 4。

## 常见坑

- `add_textbox` 字号超过 ~340pt 时单 textbox 装不下两个汉字,会被截断(章节页大数字踩过)。
- 甘特图行数变多时,底部图例容易和页脚 7.05" 撞,注意控制 `row_h`。
- python-pptx 的 `font.name` 会同时设置 `latin` 和 `ea`;中英混排用 `set_run` 显式分别设置。
- 演讲面 `slide_keypoint` / `slide_milestone` 的字数约束在 prompt 模板里,不在 Python 校验 — 手写 master 也要遵守。
