# PPT2PPT

把内容密集、emoji 凑色块的工作汇报 pptx,重新设计为沉稳商务风、可继续编辑、**有明确观点**的 pptx。

![cover](docs/preview/page-01.png)

---

## 项目分层

| 层 | 解决什么 | 状态 |
|---|---|---|
| **v0 · 视觉层** | 信息密集的 pptx → 沉稳商务风的版式重排 | ✅ 已完成 (`redesign.py`) |
| **v1 · 叙事层** | 描述性标题 → Action Title · 标题 / items 互补不复述 · 三档语气适配场景 | ✅ 已完成 (Claude Code Skill) |
| **v2 · 信息密度层** | 一份输入 → 演讲面(极简) + 详情面(全量),两面叙事一致 | 🟡 [路线图就绪](docs/v2-roadmap.md) |

完整设计哲学: [docs/v1-design-philosophy.md](docs/v1-design-philosophy.md) · [docs/v2-roadmap.md](docs/v2-roadmap.md)

---

## 预览(v0 版式)

| 产品矩阵 | 年度 OKR |
|---|---|
| ![](docs/preview/page-04.png) | ![](docs/preview/page-06.png) |

| Q1 进度(真甘特图) | Q2 计划 |
|---|---|
| ![](docs/preview/page-07.png) | ![](docs/preview/page-08.png) |

> 截图来自 LibreOffice 渲染,中文回退到了仿宋字体;用 PowerPoint / Keynote 打开是雅黑 / 苹方。

---

## 设计原则

- **可编辑优先** — 输出真矢量 pptx,不是图片化导出。打开后可继续在 PowerPoint / Keynote 里改字、调位置。
- **重排版而非堆模板** — 解析原文 → 提炼为结构化字段 → 按汇报场景重组信息架构 → 程序化生成。
- **克制** — 纯文字内容不强行塞插图;emoji 假色块替换为真甘特图;表格做行级分层。
- **每页一个观点(v1)** — Action Title 替代描述性标题。让动词 / 判断 / 数字进入标题。
- **力度可调(v1)** — 同一份事实有 internal / balanced / external 三种语气版本,适配不同场景。

---

## v1 · Claude Code Skill 用法

v1 以 Claude Code Skill 形态交付。无需 API key,在 Claude Code 里直接跑 slash command。

```
/rewrite-action-title balanced     # 跨部门 / 对上级用(默认)
/rewrite-action-title internal     # 部门内部 / 复盘会用(尖锐)
/rewrite-action-title external     # 投资人 / 客户 / 媒体用(建设性)
```

输出: `content_action_<tone>.py`,审计追加到 `rewrite_audit.md`。

切换为当前数据生成 pptx:

```bash
cp content_action_balanced.py content.py
.venv/bin/python redesign.py
# → output.pptx
```

skill 实现:
- [`prompts/rewrite_action_title.md`](prompts/rewrite_action_title.md) — 单一真相源 prompt 模板
- [`.claude/commands/rewrite-action-title.md`](.claude/commands/rewrite-action-title.md) — slash command 入口

三档对比效果见 [docs/v1-design-philosophy.md](docs/v1-design-philosophy.md) 末尾的对照表。

---

## v0 · 视觉层用法

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python redesign.py
# → output.pptx
```

仓库自带的 `content.py` 是一份虚构示例数据。把里面的字段替换成你自己的内容即可。

---

## 设计系统

| 用途 | 颜色 |
|---|---|
| 主背景(封面 / 章节 / 结尾) | `#0F1B2E` 极深蓝 |
| 内容页背景 | `#F7F8FA` 浅灰 |
| 卡片底 | `#FFFFFF` |
| 主色 / 数据强调 | `#1F2A44` 深蓝 |
| 暖金点缀(标签 / 装饰条 / 序号) | `#C28C4C` |
| 状态色 | `#0E9F6E` 完成 · `#33537E` 进行 · `#C0C8D4` 待启动 · `#E97316` 警示 |

字体: `Microsoft YaHei`(跨平台时回退到苹方 / 思源黑)。

---

## 页面类型(15 页结构)

```
1  封面
2  目录
3  PART 01 · 产品(章节分隔)
4  产品矩阵(4 层级横向卡片)
5  产品 · 当前问题(大数字 + 卡片)
6  产品 · 年度 OKR(行级分层表)
7  产品 · Q1 进度(真甘特图)
8  产品 · Q2 计划(三栏月度表)
9  PART 02 · 品牌(章节分隔)
10 品牌工作(4 层级 + 子项)
11 品牌 · 当前问题
12 品牌 · 年度 OKR
13 品牌 · Q1 进度(9 张账号卡片)
14 品牌 · Q2 计划
15 结尾页
```

---

## 文件

### 数据层
- `content.py` — 当前在用的数据(可被 cp 切换)
- `content_action.py` — v1 手写 master(balanced + B 修复)
- `content_action_<tone>.py` — skill 自动产出的三档版本
- `content_real.py` — 本地真实数据(gitignored)

### 工程层
- `redesign.py` — 设计系统常量 + 通用绘制工具 + 各页面生成函数 + 主流程

### Skill 层
- `prompts/rewrite_action_title.md` — Action Title 重写 prompt 模板
- `.claude/commands/rewrite-action-title.md` — slash command 入口
- `rewrite_audit.md` — 每次重写的审计日志

### 文档
- `docs/v1-design-philosophy.md` — v1 完整设计哲学
- `docs/v2-roadmap.md` — v2 路线图(下一阶段工作 onboarding 文档)
- `docs/preview/` — README 用的 demo 截图

---

## 已知限制

- LibreOffice 转 PDF 时中文会回退到非雅黑字体;用 PowerPoint / Keynote 打开是正常的雅黑/苹方。
- 当前内容硬编码在 `content.py`,换 PPT 需要重写数据(自动解析 pptx → content.py 是 v3 议题)。
- v1 只在标题层做减法,items / KR / 任务名仍是全量保留 — 真正解决"做减法"在 v2。

---

## 路线图

- [x] **v0** — 视觉层重排(redesign.py · 沉稳商务风 · 12 种页型)
- [x] **v1** — 叙事层重写(Action Title + B 修复 + tone 三档 + Claude Code Skill)
- [ ] **v2** — 信息密度层(双层 deck:演讲面 + 详情面 · [详细路线图](docs/v2-roadmap.md))
- [ ] **v3** — 输入端(自动解析任意 pptx → content.py · 免去手写)
- [ ] **v4+** — 多主题 / CLI 封装 / 跨场景

---

## 协议

MIT
