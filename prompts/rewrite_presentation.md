# Rewrite Presentation · Prompt 模板

> **单一真相源**：v2 演讲面重写的全部规则,本文件 + [`rewrite_action_title.md`](rewrite_action_title.md) 双文件协同,前者定义"演讲面摘要规则",后者定义"Action Title + tone 力度词典"(本文件直接引用,不重复定义)。

## 任务

从 v1 详情面数据(`content.py` 或 `content_action_<tone>.py`)提炼出 **6 页演讲面**数据,输出到 `content_presentation_<tone>.py`,可以直接被 `redesign_presentation.py` 渲染。

演讲面服务**讲台叙事**:每页一个观点 + 不超过 3 个支撑。详情面服务事后查阅。两面是同一份事实的两种密度,**绝不允许互相矛盾**。

## v1 / v2 在叙事上的分工

| | v1 详情面 | v2 演讲面 |
|---|---|---|
| 服务对象 | 老板 / 事后查阅 / 工作量证明 | 讲者 / 现场 / 听众判断 |
| 页数 | 15 页 | 6 页 |
| 信息密度 | 全量 items / KR / 任务名 | 每页 1 观点 + ≤3 支撑 |
| title 强度 | Action Title(结论判断) | Action Title + 行动化加强(允许更尖锐) |
| 来源 | 用户原始数据 | v1 详情面的精炼摘要 |

## 演讲面 6 页 schema

输出文件必须严格遵循以下 6 个 dict(顺序固定),命名一字不差:

```python
COVER = {
    "tag": str,           # 同 v1 COVER.tag
    "title": str,         # 同 v1 COVER.title(汇报主题,不重写)
    "subtitle": str,      # 同 v1 COVER.subtitle(三段式判断,与详情面对齐)
    "byline": str,        # 同 v1 COVER.byline
}

PRODUCT_KEYPOINT = {
    "section": "PART 01 · 产品",
    "title": str,                        # 大字 Action Title · 产品现状一句结论
    "subtitle": str,                     # 一行延伸/时间锚,通常复用 v1 PRODUCT_PROBLEMS.title
    "points": [                          # 恰好 3 个 · 来自 v1 PRODUCT_PROBLEMS.items
        {"num": "01", "head": str, "desc": str},
        {"num": "02", "head": str, "desc": str},
        {"num": "03", "head": str, "desc": str},
    ],
}

PRODUCT_MILESTONE = {
    "section": "PART 01 · 产品",
    "title": str,                        # 大字 Action Title · Q2 节奏一句结论
    "subtitle": str,                     # 5/6/7 月时间锚,通常同 v1 PRODUCT_Q2.subtitle
    "lanes": [                           # 3 个 lane(若 v1 有 5 group,合并到 3 lane)
        {"name": str, "task": str, "outcome": str},  # outcome 用 "→" 串联三段产出
        ...
    ],
}

BRAND_KEYPOINT = { ... }     # 同 PRODUCT_KEYPOINT 结构,section = "PART 02 · 品牌"
BRAND_MILESTONE = { ... }    # 同 PRODUCT_MILESTONE 结构,section = "PART 02 · 品牌"

CLOSING = { ... }            # 同 v1 CLOSING(全部字段直接复用)
```

## 摘要规则(核心)

### 规则 1 · KEYPOINT title 怎么写

**输入源**:v1 的 `*_MATRIX.title` + `*_MATRIX.subtitle`(总判断)+ `*_PROBLEMS.title`(卡点判断)

**输出**:一句话融合"现状判断 + Q3/下阶段行动指向"

**允许的强度加成**:演讲面 title 比 v1 详情面更强、更行动化。但**事实不变**。

| v1 详情面(描述层) | v2 演讲面(行动层) | 是否允许 |
|---|---|---|
| "增长压在标准版上,两端缺路径" | "增长压在标准版上,Q3 必须破两端" | ✅ 加行动指向 |
| "传播没方法论 · 新品冷启动靠运气" | 直接复用 | ✅ 已经够强 |
| "标准版增速进入平台期" | "Q3 看不到下一曲线" | ❌ 改写了具体卡点的事实(MAU 平台期 vs 看不到曲线 不等价) |

**红线**:title 改写**只允许加行动指向词**(必须 / 决定 / 关键 / 主战场),**不允许改任何具体事实**(数字 / 百分比 / 卡点命名)。

### 规则 2 · KEYPOINT subtitle + points 怎么写

**输入源**:v1 的 `*_PROBLEMS`

- `subtitle` ← v1 `PROBLEMS.title`(完整复用)
- `points[i].head` ← v1 `PROBLEMS.items[i].head`(**完整复用,一字不改**)
- `points[i].desc` ← v1 `PROBLEMS.items[i].desc`(**完整复用,一字不改**)
- `points[i].num` ← `"01"` / `"02"` / `"03"`

**红线**:`points` 是事实层,**不允许重写**。如果用户觉得 v1 的 PROBLEMS items 不对,应该回到 v1 的 `/rewrite-action-title` 修详情面,而不是在演讲面层做修补。两面不一致 = v2 失败。

### 规则 3 · MILESTONE title 怎么写

**输入源**:v1 的 `*_Q2.title`

绝大多数情况**直接复用**(v1 的 Q2 title 已经是 Action Title 形态)。如果觉得 v1 的 Q2 title 不够"叙事高潮",可以加冒号子句给三件事/三链路命名:
- v1 "Q2 三件事打透:Onboarding · V7 · AI 辅助" → 演讲面直接复用
- 若 v1 是 "Q2 计划" → 演讲面要改成 "Q2 跑通 X · Y · Z" 形态

### 规则 4 · MILESTONE lanes 怎么写

**输入源**:v1 的 `*_Q2.groups`

**关键操作 · group 合并**:演讲面 lane 数 = 3。若 v1 有 5 个 group(产品 Q2 的入门/标准·产品/标准·工具/企业·沙龙/企业·周边),按层级合并:

| v1 group(5 个) | v2 lane(3 个) | 合并方式 |
|---|---|---|
| 入门层 · Onboarding | 入门层 | 单个 group 直接成 lane |
| 标准层 · 产品 V7 + 标准层 · AI 工具 | 标准层 | task 写"V7 + AI 辅助上线",outcome 取两个 group 各自的关键产出合并 |
| 企业层 · 沙龙 + 企业层 · 周边 | 企业层 | task 写"沙龙 + 周边",outcome 取两个的代表产出合并 |

**lane.task 来源**:v1 `group.task` 原文。若是合并出来的 lane,用 "X + Y" 串联两个 task。

**字数硬约束**(版式装不下会换行,影响演讲面观感):
- `lane.task` ≤ **14 中文字**(英文/数字/标点不计入,但要尊重视觉总长)
  - 合并 lane 时,若 v1 两个 group.task 原文串联超 14 字,必须**改写为统一动作**:不取原文,提炼共同动词
  - 例:`"核心功能 V7 迭代" + "AI 辅助能力部署"` 串联 = "核心功能 V7 迭代 + AI 辅助能力部署"(15 字,溢出)→ 改写 `"核心功能 V7 + AI 辅助上线"`(11 字,统一为"上线")
  - 例:`"线下行业沙龙" + "首款周边商业化"` 串联 = "线下行业沙龙 + 首款周边商业化"(13 字,边界)→ 可改写 `"首场行业沙龙 + 首款周边商业化"`(13 字,选用一致量词"首场/首款")

**lane.outcome 来源**:v1 `group.phases` 的极简化合并。规则:
- 三个 phase 用 ` → ` 串联(中文箭头),保留每个 phase 最关键的动作
- 删掉 phase 内的 ` · ` 子细节,只留一句
- 例:v1 phases `["上线 · 种子用户招募", "转化测试 · 二期推广", "数据复盘 · SOP 沉淀"]` → outcome `"种子招募 → 转化测试 → SOP 沉淀"`

**字数硬约束**:
- `lane.outcome` 单段 ≤ **7 中文字**,三段总长 ≤ **22 字**(箭头不计)
  - **全角标点(《》【】等)和空格视觉上额外占位**,所以 7 字限制对纯中文宽松,对含全角标点的更紧
  - 合并 lane(两个 group)时 outcome 仍然只输出 3 段,**不是 6 段**:从两个 group 的同 phase 取最关键的合并
  - 例:标准·产品 phase 2 "V7 正式发布 · 用户教育" + 标准·工具 phase 2 "AI 助手正式上线 · 接管 70% 答疑"
    - 合并 = "V7 发布 + AI 接管 70% 答疑"? 太长,溢出
    - 必须再裁:取主语并各保留一个最关键成果 → "AI 接管 70% 答疑"(7 字,边界);通常拆分到两段更安全
  - 若实在压不进,**优先保留有数字的那段**(数字是事实层的锚,删了等于失准)
  - **专有产物名简化**:v1 原文若是产物简称(《IP 内容生产 SOP》《流量账号转化实操手册》)且含全角《》超限,**允许在演讲面省略形容词或说明性修饰**(如"生产"/"实操"),保留核心标识 → "沉淀 IP SOP"(5 字)。这不算事实层失准。
  - **三段总长视觉单行容纳为准**:即使每段 ≤ 7 字,三段加起来含数字、英文、` → ` 间隔,也可能视觉超单行。
    例:v1 IP 引流层 phases 完整提取 = "内容模型测试 → 公域→私域加粉 3,000 → 沉淀 IP SOP"(总长视觉超),必须再裁。
    每段保留最关键标识 → "模型测试 → 加粉 3,000 → 沉淀 IP SOP"(各 4/5/5 字)。优先保留有数字的中段。

**KEYPOINT.title / MILESTONE.title 字数约束**(在 40pt 大字版式下):
- 中文部分(冒号前)的核心判断 ≤ **5 中文字** if 后接长冒号子句(":Onboarding · V7 · AI 辅助" 这种 14+ 字符)
- 中文部分 ≤ **15 中文字** if 没有冒号子句(如 BRAND_KEYPOINT.title "传播没方法论 · 新品冷启动靠运气" 14 字)
- 例:
  - ✅ "Q2 三件事打透:Onboarding · V7 · AI 辅助"(5 字 + 长冒号子句)
  - ✅ "Q2 三事并进:Onboarding · V7 · AI 辅助"(4 字 + 长冒号子句)
  - ❌ "Q2 三大主线推进:Onboarding · V7 · AI 辅助"(6 字 + 长冒号子句,溢出换行)→ 改为 "Q2 推进三主线:Onboarding · V7 · AI 辅助"(5 字)
  - ❌ "Q2 三件事必须打透:Onboarding · V7 · AI 辅助"(7 字 + 长冒号子句,溢出)→ 改为 "Q2 三件事打透:Onboarding · V7 · AI 辅助"(5 字,删"必须"或换 "Q2 必打三件事")

### 规则 5 · COVER / CLOSING 直接复用

不重写。逐字段从 v1 拷贝。

## tone 三档

完整 tone 词典见 [`rewrite_action_title.md`](rewrite_action_title.md) "tone 力度档位" 一节。本文件不重复。

**演讲面 tone 适用规则**:

- `internal` / `balanced` / `external` 的修辞特征同 v1
- tone 只滑 KEYPOINT title 和 MILESTONE title 的修辞,**不滑** points / lane.task / lane.outcome(那些是事实层)
- 演讲面 tone 应该和详情面 tone **一致**(否则讲者临场 internal 说"营收全压标准版",听众翻详情面看到 external "标准版稳步领跑"会精神分裂)

**强约束**:开始重写前,**先检查 `content_action_<tone>.py` 是否存在**:
- 存在 → 用它作为输入,演讲面 title 的 tone 与详情面对齐
- 不存在 → 用 `content.py` 作为输入,但在审计里 warn "未发现匹配 tone 的详情面,两面 tone 一致性需要用户手动校验"

## 两面叙事一致 · 硬约束清单

输出文件**必须**通过以下检查(写完后自我核对一遍):

- [ ] COVER 全部字段与 v1 一字不差
- [ ] CLOSING 全部字段与 v1 一字不差
- [ ] PRODUCT_KEYPOINT.points 三条 head/desc 与 v1 PRODUCT_PROBLEMS.items 一字不差
- [ ] BRAND_KEYPOINT.points 三条 head/desc 与 v1 BRAND_PROBLEMS.items 一字不差
- [ ] PRODUCT_MILESTONE.title 与 v1 PRODUCT_Q2.title 一致(或加了行动指向但事实不变)
- [ ] PRODUCT_MILESTONE.lanes 每个 task 来源于 v1 PRODUCT_Q2 的 group.task(允许合并 X + Y)
- [ ] BRAND_MILESTONE 同上
- [ ] 演讲面页数 = 6(若超过 7 页,说明摘要失败,重新合并)

## 输出与审计

### 写出文件

Write 完整 Python 文件到 `content_presentation_<tone>.py`(保持 schema、可被 `redesign_presentation.py` 跑通)。

文件头 docstring:
```
"""演讲面数据 · v2 · tone={tone} · 自动生成

由 /rewrite-presentation 命令产出。
渲染:.venv/bin/python -c "import content_presentation_<tone> as c; ... " 或先 cp 覆盖 content_presentation.py 再跑 redesign_presentation.py
"""
```

### 追加审计

在 `docs/audit.md` 末尾追加:

```markdown

---

## v2 演讲面重写 · {YYYY-MM-DD} · tone={tone}

- 输入: content_action_<tone>.py(若存在) / content.py(若不存在)
- 输出: content_presentation_<tone>.py
- 演讲面 6 页骨架:
  - PRODUCT_KEYPOINT.title: <写入的判断>
  - PRODUCT_MILESTONE.title: <写入的判断>
  - BRAND_KEYPOINT.title: <写入的判断>
  - BRAND_MILESTONE.title: <写入的判断>
- group 合并方式: <若 v1 有 5 group,说明合并到 3 lane 的映射>
- 两面 tone 一致性: <"已对齐" / "未发现匹配 tone 的详情面 · 需手动校验">
```

## 不要做的事

- ❌ 不要重写 `content.py` / `content_action_*.py`(那些是输入)
- ❌ 不要修改 `redesign.py` / `redesign_presentation.py`
- ❌ 不要重写 PROBLEMS items 的 head/desc(事实层禁区)
- ❌ 不要重写 Q2 group 的 task 名(事实层禁区,只允许合并)
- ❌ 不要为了 tone 修辞改任何数字 / 产品名 / 账号名 / KR
- ❌ 不要超过 6 页
- ❌ 不要用 speaker notes / 不要把详情面塞进演讲面 — v2 形态是双独立 pptx
