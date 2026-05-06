# v1 设计哲学 · Action Title + Tone

> v1 解决的是 PPT 的「叙事层」: 让每页有明确观点 · 让信息层级互补不复述 · 让同一份事实可以适配不同场景。
>
> v1 没有解决的是「信息密度」: 演讲面 vs 工作量面的根本张力,留给 [v2](v2-roadmap.md)。

## 起源

调研 GitHub 上做 PPT 的 AI 项目时,识别出主流 PPT agent "像假发"的三大原因:

1. **结构同构** — 组件库化的版式让审美塌缩到一个均值
2. **保留偏置** — LLM 默认尊重用户输入,没人敢替用户砍内容
3. **不懂叙事意图** — 只在做 layout,不在做 storytelling

v0 的 redesign.py 已经解决了"装饰层"的问题(沉稳商务风版式)。v1 解决的是"叙事层"。

## v1 三个核心机制

### 1. Action Title — 标题是结论而非标签

**原则**: 每页的 title 应该是"如果只能记住一句话",而不是"我们这页要讲 X"。

| ❌ 描述性标题(像假发) | ✅ Action Title(有判断) |
|---|---|
| 产品矩阵 | 增长压在标准版上,两端缺路径 |
| 产品 · 当前问题 | 三个卡点决定 Q3 增速 |
| 产品 · Q1 进度 | Q1 节奏在轨:2 项交付 · 3 项进行中 |
| 品牌 · 当前问题 | 传播没方法论 · 新品冷启动靠运气 |

让动词、判断、数字进入标题。不要只堆名词。

### 2. B 修复 — 三层信息互补不复述

PROBLEMS 类页面尤其要小心。结构是:

| 层 | 职责 |
|---|---|
| `title` | 这页凭什么重要(结论 / 行动方向) |
| `subtitle` | 三个问题怎么命名(结构层) |
| `items[].head` | 每个问题的具体卡点表现 |
| `items[].desc` | 卡点的 root cause 或数据 |

**严禁** items.head 复述 subtitle 已经讲过的命名:

| 反例(v0) | 正例(v1) |
|---|---|
| subtitle: "增长引擎 · 转化路径 · 差异化护城河" | 同 |
| items.head: "需要新增长引擎" / "免费转付费薄弱" / "缺少差异化护城河" | "标准版增速进入平台期" / "试用用户付费转化缺路径" / "专业版与竞品高度同质" |

items.head 应该是"具体卡点表现",不是"问题名称的同义改写"。

### 3. Tone 三档 — 同一份事实的三种叙事语气

**问题**: "营收压在爆品上,其他三层未独立跑通"对内是诚实,对外是踩雷。同一份事实需要不同力度的标题。

**解法**:

| 档 | 适用场景 | 修辞特征 |
|---|---|---|
| `internal` | 部门内部 / 一号位 / 复盘会 | 尖锐 · 容许行业黑话 · 容许自嘲 · 数据可负面 |
| `balanced`(默认) | 跨部门 / 对上级 / 合作伙伴 | 中性 · 事实判断 · 不带情绪 · 留余地 |
| `external` | 投资人 / 客户 / 媒体 / 市场发布 | 建设性 · 把问题包装成机会 · 用建设词汇 |

三档同步滑动三个语义维度:

1. **判断词尖锐度**: 硬伤 / 卡点 / 抓手 · 困局 / 问题 / 挑战 · 没 / 待 / 在
2. **时态选择**: 完成时(已发生) / 进行时(正在发生) / 将来时(即将解决)
3. **归因方向**: 自我归因("我们没做好") / 中性事实 / 机会归因("市场正在变化")

**力度只滑修辞,不动事实** — 三档共享同一份 items / KR / 数据,变形的是"语气",不是"内容"。

完整的力度词典 + 红线在 [`prompts/rewrite_action_title.md`](../prompts/rewrite_action_title.md)。

## 三档实例对比(基于 demo 数据)

| 字段 | external | balanced | internal |
|---|---|---|---|
| COVER subtitle | 标准版稳步领跑 · 两端持续布局 · 品牌升级方法论 | 标准版守营收 · 两端待破局 · 品牌求方法论 | 标准版一条腿扛营收 · 两端没跑通 · 品牌靠运气 |
| PRODUCT_MATRIX title | 标准版稳步领跑,两端持续布局 | 增长压在标准版上,两端缺路径 | 营收全压标准版,其他三层都没跑出来 |
| PRODUCT_PROBLEMS title | 三大引擎驱动 Q3 增长 | 三个卡点决定 Q3 增速 | 三个硬伤决定 Q3 能不能涨 |
| BRAND_PROBLEMS title | 传播方法论建设中 · 新品冷启动机制升级 | 传播待沉淀方法论 · 新品冷启动待破局 | 传播完全没方法论 · 新品冷启动全靠运气 |
| BRAND_Q1 title | 9 个账号矩阵:5 个跑通模型 · 4 个进入优化阶段 | 9 个账号在跑:5 个跑通 · 4 个待破 | 9 个账号 · 5 个真在跑 · 4 个躺着 |

数字相同(9 / 5 / 4),修辞滑动。

## 三档红线

prompt 模板已经把三档失守的边界显式列出:

- **balanced 不是平均值,是独立档位** — 不要让 balanced 输出"两端模糊"的中庸句子,它有自己的中性事实判断特征
- **external 不能退化成"信息墙"** — 必须保留主谓宾判断结构,不能退化成"四层级产品组合"这种纯名词列表
- **internal 不能滑成"内部黑话"** — 容许尖锐("吃完红利 / 拉跨"),不容许只有内部人懂的缩写("办会破壁"是反面教材)
- **力度只滑修辞,不动事实** — 三档共享同一份 items / KR / 任务名 / 数据

## 工程形态

v1 以 **Claude Code Skill** 形态交付,不是 Python 脚本:

- [`prompts/rewrite_action_title.md`](../prompts/rewrite_action_title.md) — 单一真相源 prompt 模板(规则、词典、红线)
- [`.claude/commands/rewrite-action-title.md`](../.claude/commands/rewrite-action-title.md) — slash command 入口
- 用户输入 `/rewrite-action-title balanced`,Claude Code 加载这两份文件,读 `content.py`,按 prompt 重写,写入 `content_action_<tone>.py`,追加 `rewrite_audit.md`

为什么不写 Python 脚本调 API?

- 重写本质是对话式的(每页都要做语义判断),Claude Code skill 比脚本更契合
- 不需要 API key,门槛低
- prompt 模板可单一真相源化(未来 API 版 `rewrite.py` 复用同一份)
- 项目调研里"中文工作汇报场景空缺"的差异化生态位 = Claude Code skill

## v1 已完成的产物

```
content_action.py              v1 手写 master(balanced + B 修复)
content_action_balanced.py     skill mock 自动版(修了 v0 数字 bug)
content_action_external.py     skill mock 三档之一
content_action_internal.py     skill mock 三档之一
prompts/rewrite_action_title.md   prompt 模板
.claude/commands/rewrite-action-title.md   slash command
rewrite_audit.md               每次重写的审计日志
docs/v1-design-philosophy.md   本文件
```

## 用法

```bash
# 跑默认 balanced 重写
/rewrite-action-title balanced

# 切换为当前数据生成 pptx
cp content_action_balanced.py content.py
.venv/bin/python redesign.py
```

试不同档位看视觉对比:

```bash
/rewrite-action-title external   # 投资人版
/rewrite-action-title internal   # 内部复盘版
```

## v1 已知不解决的

- 演讲面 vs 工作量面的张力(items / KR 还是全量保留) → [v2](v2-roadmap.md)
- 输入端是手写 content.py(不是从原始 pptx 自动解析)
- 版式层多样性(redesign.py 还是固定 12 种页型)
- 跨语言/跨场景(只针对中文工作汇报)

这些都是已知边界,不是 bug。
