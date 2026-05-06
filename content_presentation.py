# -*- coding: utf-8 -*-
"""演讲面（presentation）数据 · v2

设计哲学（详见 docs/v2-roadmap.md）：
- 6 页骨架：封面 + 产品现状 + 产品节奏 + 品牌现状 + 品牌节奏 + 结尾
- 每页一个观点 + 不超过 3 个支撑
- 砍掉 v1 的目录/章节分隔/矩阵/OKR/甘特/账号矩阵 — 这些归详情面
- 判断与 v1 详情面对齐（balanced 档），不允许两面矛盾
"""

COVER = {
    "tag": "DEMO · Q2 · 2026",
    "title": "示例公司 Q2 工作汇报",
    "subtitle": "标准版守城 · 两端开荒 · 品牌求方法论",
    "byline": "DEMO · 工具示例数据",
}

PRODUCT_KEYPOINT = {
    "section": "PART 01 · 产品",
    "title": "增长压在标准版上,Q3 必须破两端",
    "subtitle": "三个卡点决定 Q3 增速",
    "points": [
        {"num": "01", "head": "标准版增速进入平台期", "desc": "MAU 增长曲线见顶 · 没有下一曲线接棒"},
        {"num": "02", "head": "试用用户走丢在第 3 步", "desc": "激活后无付费引导动作 · 自然转化路径断点"},
        {"num": "03", "head": "和竞品长得一样", "desc": "专业版核心功能高度重合 · 缺乏杀手级特性"},
    ],
}

PRODUCT_MILESTONE = {
    "section": "PART 01 · 产品",
    "title": "Q2 三件事打透:Onboarding · V7 · AI 辅助",
    "subtitle": "5 月启动 · 6 月交付 · 7 月复盘",
    "lanes": [
        {
            "name": "入门层",
            "task": "Onboarding v2 全流程跑通",
            "outcome": "种子招募 → 转化测试 → SOP 沉淀",
        },
        {
            "name": "标准层",
            "task": "核心功能 V7 + AI 辅助上线",
            "outcome": "正式发布 → AI 接管 70% 答疑 → 效果验收",
        },
        {
            "name": "企业层",
            "task": "首场行业沙龙 + 首款周边商业化",
            "outcome": "策划落地 → 全渠道发售 → 复盘归档",
        },
    ],
}

BRAND_KEYPOINT = {
    "section": "PART 02 · 品牌",
    "title": "传播没方法论 · 新品冷启动靠运气",
    "subtitle": "三个问题决定品牌能否撑起 Q3 增长",
    "points": [
        {"num": "01", "head": "选题靠拍脑袋", "desc": "数据没回流到选题决策 · 爆款不可复用"},
        {"num": "02", "head": "0 种子启动", "desc": "新品发布无可调用私域池 · 全靠付费投放"},
        {"num": "03", "head": "等需求 · 不造需求", "desc": "被动响应业务部门 · 缺主动议题设置"},
    ],
}

BRAND_MILESTONE = {
    "section": "PART 02 · 品牌",
    "title": "Q2 跑通三链路:双 IP · 高客单 · 运营闭环",
    "subtitle": "5 月测试 · 6 月放量 · 7 月沉淀 SOP",
    "lanes": [
        {
            "name": "IP 引流层",
            "task": "双 IP 账号引流跑通",
            "outcome": "模型测试 → 加粉 3,000 → 沉淀 IP SOP",
        },
        {
            "name": "高客单转化",
            "task": "高客单产品转化跑通",
            "outcome": "全链路验证 → ≥ 30 单 → 销售 SOP",
        },
        {
            "name": "运营全链路",
            "task": "新增运营全链路跑通",
            "outcome": "店铺上架 → 闭环跑通 ROI 正 → 卡点分析",
        },
    ],
}

CLOSING = {
    "tag": "Q2 · 2026",
    "title": "把每一件事做到位",
    "subtitle": "产品 · 品牌 · 协同",
    "footer": "THANKS",
}
