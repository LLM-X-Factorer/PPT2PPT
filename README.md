# PPT2PPT

> 把内容密集的工作汇报 pptx,重新设计为沉稳商务风、可继续编辑、有明确观点的双层 deck。

![cover](docs/preview/page-01.png)

---

## 这是什么

PPT2PPT 不是模板套用工具,也不是 AI 一键生成 PPT 工具。

它是把一份**已经存在的工作汇报 pptx**,经过结构化提炼后,重新生成为一份**有观点、可编辑、视觉沉稳**的 pptx——并能一次性产出**演讲面(6 页极简)+ 详情面(15 页全量)**两个独立 deck。

- **输入** — 内容密集的工作汇报 pptx(emoji 假色块 / 全表格 / 描述性标题)
- **输出** — 沉稳商务风的 pptx + 可选的演讲面精简版

---

## 解决什么问题

工作汇报场景有一个根本张力:

- **汇报人想要的** — 一份能让听众**当场听懂判断**的 PPT,极少 bullet,每页一个观点
- **老板需要的** — 一份能**看到工作量**的 PPT,全量任务、KR、数据,证明"我干了活"

这两个需求在一份 PPT 里互相打架:
- 做减法 → 老板觉得你没干活
- 堆细节 → 听众听不懂判断

行业现状是把这个矛盾按在一份 pptx 里凑合,结果就是**信息密集、emoji 凑色块、标题是结构标签("当前问题"、"Q2 计划")**的工作汇报模板。读完没人记得你的判断是什么。

---

## 思路 · 三层张力拆解

PPT2PPT 把矛盾**拆成三层独立解决**:

| 层 | 解决什么 | 产物 |
|---|---|---|
| **v0 · 视觉层** | 信息密集 → 沉稳商务风版式 | `redesign.py` — 12 种页型 |
| **v1 · 叙事层** | 描述性标题 → 结论式 Action Title;同一份事实三档语气 | Skill `/rewrite-action-title` |
| **v2 · 信息密度层** | 一份输入 → 演讲面 6 页 + 详情面 15 页双独立 deck | Skill `/rewrite-presentation` |

汇报现场翻演讲面,被问细节切到详情面。或者:会前发演讲面,会后发详情面。**演讲极简 vs 工作量证明**两个需求各得其所。

完整设计哲学: [docs/v1-design-philosophy.md](docs/v1-design-philosophy.md) · [docs/v2-roadmap.md](docs/v2-roadmap.md)

---

## 解决效果

### v1 · 标题改写(同一份事实,三档语气)

| 原文(描述标签) | balanced(默认) | internal(尖锐) | external(建设性) |
|---|---|---|---|
| 产品矩阵 | 增长压在标准版上,两端缺路径 | 营收全压标准版,其他三层都没跑出来 | 标准版稳步领跑,两端持续布局 |
| 产品 · 当前问题 | 三个卡点决定 Q3 增速 | 三个硬伤决定 Q3 能不能涨 | 三大引擎驱动 Q3 增长 |
| 品牌 · 当前问题 | 传播待沉淀方法论 · 新品冷启动待破局 | 传播完全没方法论 · 新品冷启动全靠运气 | 传播方法论建设中 · 新品冷启动机制升级 |
| 9 个账号现状 | 9 个账号在跑:5 个跑通 · 4 个待破 | 9 个账号 · 5 个真在跑 · 4 个躺着 | 9 个账号矩阵:5 个跑通模型 · 4 个进入优化阶段 |

**事实层(KR / 数字 / 任务名)三档共享,只滑修辞**。三档同时验证(`docs/audit.md`),不允许 title 是 external 但 items 还是 internal 力度的精神分裂。

### v2 · 双 deck(同一份输入,两种密度)

**详情面(15 页 · 工作量证明)**

| 产品矩阵 | 年度 OKR |
|---|---|
| ![](docs/preview/page-04.png) | ![](docs/preview/page-06.png) |

| Q1 真甘特图 | Q2 季度计划 |
|---|---|
| ![](docs/preview/page-07.png) | ![](docs/preview/page-08.png) |

**演讲面(6 页 · 现场叙事)**

```
1  封面               4  品牌现状(传播没方法论)
2  产品现状(三个卡点) 5  品牌节奏(Q2 三链路)
3  产品节奏(Q2 三件事)6  结尾
```

每页 1 观点 + ≤ 3 支撑。**两面叙事一致**——演讲面是详情面的精炼摘要,事实层禁止矛盾(`KEYPOINT.points` 与 v1 `PROBLEMS.items` 一字不差)。

> 截图来自 LibreOffice 渲染,中文字体回退到了仿宋;用 PowerPoint / Keynote 打开是雅黑 / 苹方。

### 验证状态

`v0.3.0` 完成 **三档 × 真实数据完整闭环**:

| 档位 | red line | 结果 |
|---|---|---|
| balanced | 中性事实判断 | ✓ |
| internal | 容许尖锐 / 不容许内部黑话 | ✓ 暴露 2 漏洞 → 修补 prompt → 通过 |
| external | 必须保留主谓宾 / 不退化为信息墙 | ✓ |

详情见 [`docs/audit.md`](docs/audit.md)。

---

## 设计原则

- **可编辑优先** — 输出真矢量 pptx,不是图片导出。打开后可继续在 PowerPoint / Keynote 改字 / 调位置
- **重排版而非堆模板** — 解析原文 → 提炼为结构化字段 → 按汇报场景重组信息架构 → 程序化生成
- **克制** — 纯文字内容不强行塞插图;emoji 假色块替换为真甘特图;表格做行级分层
- **每页一个观点(v1)** — Action Title 替代描述性标题,让动词 / 判断 / 数字进入标题
- **力度可调(v1)** — 同一份事实有 internal / balanced / external 三档语气
- **两面叙事一致(v2)** — 演讲面是详情面的精炼摘要,事实层禁止矛盾
- **数据 / 视图分离** — `content*.py` 只放数据,`redesign*.py` 只放版式,改内容不动版式

---

## 快速开始

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

仓库自带的 `content.py` 是一份虚构示例数据。把字段换成你自己的内容即可。

```bash
# 详情面(15 页 · 工作量证明)
.venv/bin/python redesign.py
# → output.pptx

# 演讲面(6 页 · 现场叙事)
.venv/bin/python redesign_presentation.py
# → output-presentation.pptx
```

---

## v1 / v2 Skill 用法

Skill 跑在 [Claude Code](https://github.com/anthropics/claude-code) 里,无需 API key。

```
# v1 · 改标题
/rewrite-action-title balanced     # 跨部门 / 对上级
/rewrite-action-title internal     # 部门内部 / 复盘会
/rewrite-action-title external     # 投资人 / 客户 / 媒体

# v2 · 提炼演讲面(每页 1 观点 + ≤ 3 支撑)
/rewrite-presentation balanced
/rewrite-presentation internal
/rewrite-presentation external
```

**输入**: `content.py`(v1)或 `content_action_<tone>.py`(v2,若已跑过 v1)
**输出**: `content_action_<tone>.py` / `content_presentation_<tone>.py`,审计追加到 `docs/audit.md`

切换数据 → 渲染:

```bash
cp content_action_balanced.py content.py && .venv/bin/python redesign.py
cp content_presentation_balanced.py content_presentation.py && .venv/bin/python redesign_presentation.py
```

skill 实现:
- [`prompts/rewrite_action_title.md`](prompts/rewrite_action_title.md) — Action Title + tone 词典(单一真相源)
- [`prompts/rewrite_presentation.md`](prompts/rewrite_presentation.md) — 演讲面摘要规则 + 6 页 schema + 字数硬约束
- [`.claude/commands/rewrite-action-title.md`](.claude/commands/rewrite-action-title.md) · [`.claude/commands/rewrite-presentation.md`](.claude/commands/rewrite-presentation.md) — slash command 入口

---

## 真实数据保护

**任何工作汇报 pptx 都视为含敏感数据**:

- `*.pptx` / `*.pdf` / `preview*.png` 已 gitignore
- 真实业务 content 文件 `content_real.py` / `content_*_real_*.py` 已 gitignore(`*_real*.py` 通配)
- `audit.md` 只记录元信息(维度通过表 + prompt 漏洞 / 修补),不写真实业务判断

切换真实数据的工作流:

```bash
cp content_real.py content.py
# ... 跑 skill / 渲染 / 验证 ...
cp /tmp/demo_backup/content.py content.py   # 恢复 demo
```

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

## 文件结构

```
PPT2PPT/
├── content.py                          # 当前在用的详情面数据(可被 cp 切换)
├── content_action.py                   # v1 手写 master
├── content_action_<tone>.py            # v1 skill 自动产出三档
├── content_presentation.py             # v2 演讲面数据(可被 cp 切换)
├── content_presentation_<tone>.py      # v2 skill 自动产出三档
├── content_real.py                     # 真实数据(gitignored)
├── redesign.py                         # 详情面渲染(12 种页型)
├── redesign_presentation.py            # 演讲面渲染(6 页 · 复用 v1 utils)
├── prompts/                            # skill 单一真相源 prompt
├── .claude/commands/                   # slash command 入口
├── docs/
│   ├── v1-design-philosophy.md
│   ├── v2-roadmap.md
│   ├── audit.md                        # 每次 skill 重写的审计日志
│   ├── tone-variants.md
│   └── preview/                        # 渲染截图
└── requirements.txt
```

---

## 路线图

- [x] **v0** — 视觉层重排(redesign.py · 12 种页型)
- [x] **v1** — 叙事层重写(Action Title + tone 三档 + Skill)
- [x] **v2** — 信息密度层(演讲面 6 页 + 详情面 15 页 + Skill)
- [x] **v0.3.0** — 三档 × 真实数据完整闭环 + prompt 模板稳定化
- [ ] **v3** — 输入端(自动解析任意 pptx → content.py · 免去手写)
- [ ] **v4+** — 多主题 / CLI 封装 / 跨场景

---

## 文档

- [docs/v1-design-philosophy.md](docs/v1-design-philosophy.md) — v1 完整设计哲学
- [docs/v2-roadmap.md](docs/v2-roadmap.md) — v2 路线图与设计决策
- [docs/audit.md](docs/audit.md) — 每次 skill 重写的审计日志(包含真实数据验证元信息)
- [docs/tone-variants.md](docs/tone-variants.md) — 三档语气对比设计笔记

---

## 已知限制

- LibreOffice 转 PDF 时中文会回退到非雅黑字体;用 PowerPoint / Keynote 打开是正常的雅黑 / 苹方
- 当前内容硬编码在 `content.py`,换 PPT 需要重写数据(自动解析 pptx → content.py 是 v3 议题)
- 演讲面字段有字数硬约束(`MILESTONE.title` 冒号子句单元素 ≤ 3 字 / `lane.outcome` 单段 ≤ 7 字);手写或 skill 输出超长会在版式里被截断换行

---

## 协议

MIT
