# v2 路线图 · 双层 Deck

> **本文件是 v2 工作的 onboarding 文档。下一会话从这里开始。**
>
> 阅读顺序: 本文件 → [v1-design-philosophy.md](v1-design-philosophy.md) → [`prompts/rewrite_action_title.md`](../prompts/rewrite_action_title.md) → [`CLAUDE.md`](../CLAUDE.md)

---

## v2 要回答的核心问题

工作汇报场景的根本张力**不**是"标题极简 vs 描述",**是"演讲极简 vs 工作量证明"**:

- 用户(汇报人)想要的是: 一份能让听众**当场听懂判断**的 PPT — 极少 bullet,每页一个观点
- 老板(听众)需要的是: 一份能**看到工作量**的 PPT — 全量任务、KR、数据,证明"我干了活"

v1 只做到"标题层做减法"。items / KR / 任务名 / 账号 metric 还是全量保留。所以 v1 输出的 PPT 仍然是"信息密集的 PPT,只不过标题更精炼"。

**v2 的目标**: 从一份输入,产出**两份**输出 —

- **演讲面(presentation)**: 极简,每页只有结论 + 一两个支撑,服务讲者临场叙事
- **详情面(appendix / leave-behind)**: 全量保留,服务事后查阅、工作量证明

汇报现场翻演讲面,被问细节时翻详情面。或者: 演讲发演讲面,会后发详情面。

---

## v1 已完成的状态(v2 不要重复做)

[v1-design-philosophy.md](v1-design-philosophy.md) 有完整描述。简化版:

- ✅ Action Title — 标题是结论而非标签
- ✅ B 修复 — title/subtitle/items 三层互补不复述
- ✅ Tone 三档 — internal/balanced/external 力度旋钮
- ✅ Skill 形态 — `/rewrite-action-title <tone>` slash command
- ✅ 单一真相源 prompt 模板 — `prompts/rewrite_action_title.md`
- ✅ Demo 数据上的三档 mock 验证(标题、items 力度联动)

**v2 要复用的 v1 资产**:

- `redesign.py` 的设计系统(沉稳商务风、12 种页型、字体、颜色) — **不要动**
- prompt 模板的 schema(Action Title 原则、tone 词典) — **可扩展不可破坏**
- skill 形态(slash command + prompts/) — v2 应该是新增 skill,不是改 v1 skill

---

## v2 的产品形态(候选 · 待 v2 第一个会话决策)

### 形态 A: 双独立 pptx

输入 `content.py` → 输出两份独立 pptx:
- `output-presentation.pptx` — 演讲面,可能 8-10 页(只保留每个 section 的结论页)
- `output-appendix.pptx` — 详情面,15+ 页(保留 v1 的全量内容)

**优点**: 文件清晰、用户可以分别发送
**缺点**: 双倍 pptx 维护成本、字体/品牌一致性要 cover 两份

### 形态 B: Speaker Notes 嵌入

PowerPoint 原生支持 speaker notes(讲者备注)。一份 pptx 同时包含:
- 幻灯片正文 = 演讲面(极简)
- 幻灯片备注 = 详情面(全量)

**优点**: 单一 pptx 文件、PowerPoint 原生支持
**缺点**: 备注不是"独立呈现",会后发出去对方看不到详情

### 形态 C: 双层渲染同一 schema

content.py 加一个层级标识(每个 item 标记 `tier: presentation | appendix`)。redesign.py 接受 `--mode=presentation|appendix` 参数,渲染对应密度的 pptx。

**优点**: 单一数据源、两种密度按需渲染
**缺点**: schema 变复杂、redesign.py 要改(违反 v1 "不动 redesign.py" 约定)

### 形态 D: Appendix 折叠到 Section 末尾

一份 pptx,15 页演讲面 + 15 页详情面拼接。演讲时用前 15 页,被问细节时翻到后 15 页。

**优点**: 单文件、用户控制呈现节奏
**缺点**: 30 页过长、视觉上有"两份"感

**第一个会话的关键决策**: 选 A / B / C / D 哪一种(或新方案),决定 v2 整个工程形态。

---

## v2 的核心技术挑战

不论选哪种形态,v2 真正难的是**"演讲面的内容怎么从全量数据里提炼出来"**。这是 v1 没碰过的问题。

### 挑战 1: 演讲页的页数怎么决定

15 页全量 → 演讲面应该多少页? 8 页? 5 页?

候选思路:
- 按 section 折叠: 产品 1 张总结页 + 品牌 1 张总结页 + 节奏 1 张甘特 = 3-5 页
- 按"必讲"标记: 数据里加 `must_say: bool`,演讲面只渲染 must_say 的页面
- 按 OKR 结构: 演讲面就是封面 + 现状 + 目标 + 节奏 + 结尾,5 页骨架

### 挑战 2: 演讲页的内容是什么

不是"原页内容删一半",是"重新设计这一页的内容":
- 原 PRODUCT_MATRIX 4 个 tier × 4 字段 = 16 块信息
- 演讲版 PRODUCT_MATRIX 应该是: **1 句结论 + 4 个 tier 名 + 1 个最关键判断**(比如"标准版扛营收")
- 这是新的页面类型,需要新的版式函数

### 挑战 3: 如何保证两面叙事一致

演讲面说"标准版扛营收",详情面 PRODUCT_MATRIX 必须支撑这个判断。两面是同一份事实的两种密度,**绝对不能互相矛盾**。

prompt 设计上需要:
- 先生成详情面的"判断"(也就是 v1 的 Action Title)
- 再从判断出发倒推演讲面的"骨架"
- 演讲面是详情面的"摘要",不是独立创作

### 挑战 4: tone 三档是否依然适用

直觉: 演讲面更需要 tone 三档(因为面对的是听众,语气敏感)。详情面 tone 可以中性化(因为是事后查阅,信息密度优先于语气)。

但如果两面 tone 不一致,讲者临场说"营收全压标准版"(internal),听众翻详情看到"标准版稳步领跑"(external),会精神分裂。

**待思考**: tone 三档是否只作用于演讲面? 还是两面同步? 还是可独立设置?

---

## v2 起手建议(下一会话从这里开始)

### Step 0: 复习 v1

读这三份文件,确保 v1 设计哲学 fully loaded:

1. [`docs/v1-design-philosophy.md`](v1-design-philosophy.md)
2. [`prompts/rewrite_action_title.md`](../prompts/rewrite_action_title.md)
3. [`audit.md`](audit.md) 末尾的三档对比表

### Step 1: 拍板形态

回答 "v2 的产品形态" 那一节的 A/B/C/D 选哪个。这是 v2 整个工程形态的第一个决策,后续都围绕它展开。

**我的初步倾向是 A(双独立 pptx)**, 理由:
- 文件分离最干净,用户可以分别发送
- 不污染 v1 的 redesign.py(v2 加新版式函数到独立文件 `redesign_presentation.py`)
- speaker notes 在 LibreOffice 转 PDF 时丢失,A 不依赖工具栈
- D 方案 30 页太长

但建议下一会话**先**和用户确认这个倾向,不要直接落地。

### Step 2: 设计演讲面的"页面骨架"

用 demo 数据手写一份 5-7 页的演讲面 content,看视觉效果。这是 v2 的 v0(对应 v1 的"先手写 content_action.py 再工具化")。

骨架候选:
1. 封面(同 v1)
2. 一页讲产品(标准版扛营收,两端在打 Q3 / 三件事打透)
3. 一页讲品牌(传播没方法论,Q2 跑通三链路)
4. 一页讲节奏(Q1 在轨,Q2 节点)
5. 结尾(同 v1)

5 页骨架挑战版式函数能不能复用——可能需要新的 `slide_summary` 函数。

### Step 3: 验证"两面叙事一致"

跑出演讲面 5 页 + 详情面 15 页,把演讲面的每个判断在详情面找到对应的支撑证据,确认不矛盾。

### Step 4: 工具化为新 skill

一旦 v2 的演讲面骨架稳定,封装为 `/rewrite-presentation` slash command,产出 `content_presentation.py` + `content_appendix.py`(对应形态 A)。

复用 v1 的 prompt 模板形态: 新增 `prompts/rewrite_presentation.md` 引用 `prompts/rewrite_action_title.md` 的 tone 词典。

---

## v2 设计哲学(传承 v1 的)

继承 v1 的核心约束:

1. **数据 / 视图分离** — `content_*.py` 只放数据,`redesign*.py` 只放版式
2. **不要 commit pptx** — pptx / pdf / preview 都已 gitignore
3. **真实数据保护** — `content_real.py` / `*_real.md` 已 gitignore
4. **字体固定** — Microsoft YaHei,跨平台 fallback
5. **Skill 形态优于 Python 脚本** — 利用 Claude Code 的对话式判断能力

### v2 新增的设计哲学

1. **两面叙事一致** — 演讲面是详情面的精炼摘要,不是独立创作。不允许两面之间有事实/判断矛盾。
2. **Appendix 不是缩水** — 详情面的设计目标是"被翻到时能立刻提供证据",不是演讲面的废稿
3. **演讲面页数克制** — 5-7 页是上限。一旦超过 10 页,就说明 v2 没真正做减法,只是把 v1 又压扁了

---

## 反向负面清单(v2 不要做的事)

- ❌ 不要重做 Action Title(v1 已完成,直接复用)
- ❌ 不要做"自动从原始 pptx 解析为 content.py"(那是 v3 议题,先把 v2 形态做对)
- ❌ 不要追求"完全自动化"(skill 形态依赖 Claude Code 的对话判断,这是优点不是缺点)
- ❌ 不要碰 redesign.py 的现有 12 种页型(v2 新增独立函数,不动现有版式)
- ❌ 不要为了"创新"破坏 v1 已稳定的 schema 兼容(content_action_*.py 必须能继续被 redesign.py 跑)

---

## 成功标准

v2 v0 完成状态:

- [x] 同一份 demo 数据产出两份 pptx: `output-presentation.pptx`(6 页) + `output.pptx`(15 页)
- [x] 演讲面每页一个观点 + 不超过 3 个支撑 bullet
- [x] 详情面保留 v1 的全部信息密度(`redesign.py` 一行未动)
- [x] 两面的 Action Title / 判断完全一致(事实层禁区 + 字数硬约束 + mock 验证)
- [x] 工具化封装为 `/rewrite-presentation` slash command,可独立调用(balanced 档 mock 验证通过)
- [ ] 真实数据(content_real.py)上跑通至少一次,验证不只在 demo 上 work
- [ ] internal / external 两档 mock 验证(类比 v1 commit `44cfa7e`)

v2 v0 形态决策 = **A 双独立 pptx**。新增独立文件 `redesign_presentation.py` / `prompts/rewrite_presentation.md` / `.claude/commands/rewrite-presentation.md`,不动 v1 的 `redesign.py` 和现有 skill。

如果你拿着两份 PPT 上台讲一次,能感受到"演讲面服务叙事 / 详情面给老板看"的张力被解决——v2 就达成了"PPT 应该做减法"的初心。
