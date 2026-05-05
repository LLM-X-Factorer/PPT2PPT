# PPT2PPT · Claude 项目指令

## 项目性质

把内容密集的工作汇报 pptx 重新设计为沉稳商务风、**可继续编辑**的 pptx。
核心交付物是 `redesign.py`（设计 + 生成）+ `content.py`（数据）。

## 关键约定

- **数据/视图分离**：`content.py` 只放数据，`redesign.py` 只放版式。改内容不要动 `redesign.py`。
- **示例数据 vs 真实数据**：仓库里 `content.py` 是虚构示例（开源所需）；真实数据放本地 `content_real.py`（已 gitignore）。
- **不要 commit pptx**：`*.pptx` 已在 `.gitignore`。任何工作汇报 pptx 都视为含敏感数据。
- **字体**：固定 `Microsoft YaHei`（跨平台 fallback 到苹方/思源黑），不要随意改。

## 验证流程

```bash
.venv/bin/python redesign.py                                   # 生成 output.pptx
soffice --headless --convert-to pdf output.pptx                # 转 PDF
pdftoppm -r 150 output.pdf preview -png                        # 转 PNG 看效果
```

注意：LibreOffice 渲染中文会回退字体（看起来像仿宋）；用 PowerPoint/Keynote 实际打开才是雅黑/苹方。**不要因 LibreOffice 渲染异常去改字体设置**。

## 设计系统（不要随意改）

- 主背景：`#0F1B2E`（封面/章节/结尾）
- 内容页背景：`#F7F8FA`
- 主色深蓝：`#1F2A44`
- 暖金点缀：`#C28C4C`
- 状态色：完成 `#0E9F6E` · 进行 `#33537E` · 待启动 `#C0C8D4` · 警示 `#E97316`

## 页面类型 → 函数映射

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

## 常见坑

- `add_textbox` 字号超过 ~340pt 时单 textbox 装不下两个汉字，会被截断（章节页大数字踩过）。
- 甘特图行数变多时，底部图例容易和页脚 7.05" 撞，注意控制 `row_h`。
- python-pptx 的 `font.name` 会同时设置 `latin` 和 `ea`；中英混排用 `set_run` 显式分别设置。
