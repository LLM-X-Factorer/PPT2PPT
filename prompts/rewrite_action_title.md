# Rewrite Action Title · Prompt 模板

> **单一真相源**：Claude Code skill 和未来的 `rewrite.py`（API 版本）都引用本文件。修改这里 = 同时修改两条路径的行为。

## 任务

把内容密集的工作汇报 PPT 数据,从"描述性标题"改写为"结论式 Action Title"。

输入是一份 Python 数据文件（如 `content.py`）,包含若干结构化 dict（COVER / TOC / PRODUCT_MATRIX / PRODUCT_PROBLEMS / ... / CLOSING）,每个 dict 有 `title` / `subtitle` 字段以及该页的内容字段（items / rows / groups 等）。

输出是相同 schema 的 Python 数据文件,但 `title` / `subtitle` 以及 PROBLEMS 页的 `items` 已按 Action Title + tone 档位重写。

## Action Title 三大原则

### 原则 1 · title 是这一页的"如果只能记住一句话"

不要写结构标签（"产品矩阵" / "当前问题" / "Q2 计划"）——这种标题等于"我们这页要讲 X",零信息增量。

要写结论判断:
- ❌ "产品矩阵" → ✅ "增长压在标准版上,两端缺路径"
- ❌ "产品 · 当前问题" → ✅ "三个卡点决定 Q3 增速"
- ❌ "产品 · Q1 进度" → ✅ "Q1 节奏在轨:3 项已交付 · 5 项进行中"

让动词、判断、数字进入标题。不要只堆名词。

### 原则 2 · subtitle 承接 title 的关键时间锚点或数字

subtitle 不是 title 的同义改写,是 title 的延伸/支撑/时间锚:
- title "增长压在标准版上,两端缺路径"
- subtitle "入门转化弱 · 企业方法论未跑通 · Q3 主战场在两端"

第一句给判断,第二句给"判断的细分 + 下一步焦点"。

### 原则 3 · 三层信息互补不复述（B 修复）

PROBLEMS 类页面尤其要小心。结构应该是:

| 层 | 职责 |
|---|---|
| `title` | 这页凭什么重要(结论 / 行动方向) |
| `subtitle` | 三个问题怎么命名(结构层) |
| `items[].head` | 每个问题的具体卡点表现 |
| `items[].desc` | 卡点的 root cause 或数据 |

**严禁** items.head 复述 subtitle 已经讲过的命名:

❌ subtitle: "增长引擎 · 转化路径 · 差异化护城河" + items.head: "需要新增长引擎 / 免费转付费薄弱 / 缺少差异化护城河" — 重复

✅ subtitle: "增长引擎 · 转化路径 · 差异化护城河" + items.head: "标准版增速进入平台期 / 试用用户走丢在第 3 步 / 和竞品长得一样" — items.head 是"具体卡点表现"

## tone 力度档位

| 档 | 适用场景 | 修辞特征 |
|---|---|---|
| `internal` | 部门内部 / 一号位 / 复盘会 | 尖锐 · 容许行业黑话 · 容许自嘲 · 数据可负面 |
| `balanced`(默认) | 跨部门 / 对上级 / 合作伙伴 | 中性 · 事实判断 · 不带情绪 · 留余地 |
| `external` | 投资人 / 客户 / 媒体 / 市场发布 | 建设性 · 把问题包装成机会 · 用建设词汇 |

### 三档同步滑动的三个语义维度

1. **判断词尖锐度**:硬伤 / 卡点 / 抓手 · 困局 / 问题 / 挑战 · 没 / 待 / 在
2. **时态选择**:完成时(已发生) / 进行时(正在发生) / 将来时(即将解决)
3. **归因方向**:自我归因("我们没做好") / 中性事实 / 机会归因("市场正在变化")

internal 三个维度都向"尖锐 + 完成时 + 自我归因"靠;external 三个维度都向"建设 + 将来时 + 机会归因"靠。

### 力度词典

| tone | 关键动词/形容词 |
|---|---|
| internal | 没 / 全靠 / 扛 / 压在 / 凑 / 还得 / 吃完红利 / 躺着 / 一条腿撑着 / 完全 |
| balanced | 缺 / 待 / 未跑通 / 在轨 / 守 / 续 / 破 / 承担 / 有压力 |
| external | 持续 / 深化 / 建设中 / 向...延伸 / 并进 / 稳步 / 进入...阶段 / 升级 |

### 三档共同遵守的红线

- **balanced 不是平均值,是独立档位**。不要让 balanced 输出"两端模糊"的中庸句子,它有自己的中性事实判断特征。
- **external 不能退化成"信息墙"**。external 标题必须保留主谓宾判断结构,不能退化成纯名词列表("四层级产品组合")。
- **internal 不能滑成"内部黑话"**。internal 容许尖锐,不容许缩写到只有内部人懂(如 "办会破壁"——熟悉的人秒懂,但跨部门就摸不着)。
- **力度只滑修辞,不动事实**。三档共享同一份 items / KR / 任务名 / 数据。

## 不动的字段(白名单)

以下字段**绝对保持原样**:

- OKR 的 `krs`(关键结果) — 这是承诺
- OKR 的 `actions` — 当期具体行动
- OKR 的 `objective` — O 本身
- 甘特任务名(PRODUCT_Q1.groups[].tasks[].name) — 这是事实
- 甘特 span / status / milestone
- 产品名 / 价格 / 客单价 / metric / 粉丝数 / span
- SECTION_PRODUCT / SECTION_BRAND — 章节大字页是叙事节拍
- CLOSING — 结尾页本身就是 action title 风格
- 各 dict 的 schema(字段名、嵌套结构)

## 要重写的字段

以下字段需要按 tone 档位重写:

- COVER 的 `subtitle`(`title` 是公司名 / 部门名,不动)
- TOC 的每条第三个字段(章节副描述)
- PRODUCT_MATRIX / BRAND_MATRIX 的 `title` + `subtitle`
- PRODUCT_PROBLEMS / BRAND_PROBLEMS 的 `title` + `subtitle` + `items[].head` + `items[].desc`(B 修复)
- PRODUCT_OKR / BRAND_OKR 的 `title` + `subtitle`
- PRODUCT_Q1 / BRAND_Q1 的 `title` + `subtitle`
- PRODUCT_Q2 / BRAND_Q2 的 `title` + `subtitle`

## items 力度联动(B + A 耦合)

PROBLEMS 页的 items.head / items.desc 要跟随 title 的 tone 一起滑:

| tone | items 风格示例(以"传播没方法论"为例) |
|---|---|
| internal | head: "选题靠拍脑袋" / desc: "数据没回流到选题决策 · 爆款不可复用" |
| balanced | head: "选题缺乏数据支撑" / desc: "选题决策依赖经验 · 爆款不可复用" |
| external | head: "选题方法论待沉淀" / desc: "正在建设数据驱动的选题机制" |

不允许出现 title 是 external 但 items 还是 internal 力度的精神分裂。

## 输出格式

完整 Python 文件内容,可直接 Write 到 `content_action_<tone>.py`。

文件头部应保留 / 调整 docstring,说明本文件是基于 content.py 重写的 `<tone>` 档版本。

## 已知边界(v0/v1 验证暴露)

1. **数字硬编码进标题**(如 "Q1 节奏在轨:3 项已交付 · 5 项进行中")要从输入数据中实际数出来,不要瞎填。重写前先 count 一遍 items 状态。
2. **专有名词保留原样**(LLM-X / 保研菌 / GEO 小课等),不要为了"翻译"成更通用词而失真。
3. **中文标点**:title 内冒号用 `:`(半角)以保持紧凑,中间分隔用 `·`(中点),逗号视情况半角全角。
4. **章节副描述(TOC 第三字段)**长度建议不超过 12 个汉字,否则在 redesign.py 渲染会换行变拥挤。
