# -*- coding: utf-8 -*-
"""演讲面数据 · v2 · tone=balanced · 自动生成

由 /rewrite-presentation 命令产出。
渲染:cp content_presentation_balanced.py content_presentation.py && .venv/bin/python redesign_presentation.py
"""

# 规则 5 · 直接复用 v1 COVER
COVER = {
    "tag": "DEMO · Q2 · 2026",
    "title": "示例公司 Q2 工作汇报",
    "subtitle": "标准版守营收 · 两端待破局 · 品牌求方法论",
    "byline": "DEMO · 工具示例数据",
}

# 规则 1 · title 来自 v1 PRODUCT_MATRIX.title + 行动化加强
# 规则 2 · subtitle ← v1 PRODUCT_PROBLEMS.title;points ← v1 PRODUCT_PROBLEMS.items 一字不改
PRODUCT_KEYPOINT = {
    "section": "PART 01 · 产品",
    "title": "增长压在标准版上,Q3 必须破两端",
    "subtitle": "三个卡点决定 Q3 增速",
    "points": [
        {"num": "01", "head": "标准版增长进入平台期", "desc": "MAU 同比增速放缓 · 缺下一曲线接棒"},
        {"num": "02", "head": "试用用户付费转化缺路径", "desc": "激活后无引导动作 · 自然转化率偏低"},
        {"num": "03", "head": "专业版与竞品高度同质", "desc": "核心功能重合度高 · 缺乏关键特性"},
    ],
}

# 规则 3 · title 直接复用 v1 PRODUCT_Q2.title
# 规则 4 · v1 5 group → 3 lane:入门层 / 标准层(产品+工具合并) / 企业层(沙龙+周边合并)
PRODUCT_MILESTONE = {
    "section": "PART 01 · 产品",
    "title": "Q2 三事并进:Onboarding · V7 · AI 辅助",
    "subtitle": "5 月启动 · 6 月交付 · 7 月复盘",
    "lanes": [
        {
            "name": "入门层",
            "task": "Onboarding v2 全流程跑通",
            "outcome": "种子用户招募 → 转化测试 → SOP 沉淀",
        },
        {
            "name": "标准层",
            "task": "核心功能 V7 + AI 辅助上线",
            "outcome": "正式发布 → AI 接管 70% 答疑 → 效果验收",
        },
        {
            "name": "企业层",
            "task": "线下行业沙龙 + 首款周边商业化",
            "outcome": "策划落地 → 全渠道发售 → 复盘归档",
        },
    ],
}

# 规则 1 · BRAND_MATRIX 是职能描述非判断,KEYPOINT.title 直接取 v1 BRAND_PROBLEMS.title
# 规则 2 · subtitle ← v1 BRAND_PROBLEMS.subtitle(题外:title 已被占用,subtitle 用 PROBLEMS.subtitle 避免重复)
BRAND_KEYPOINT = {
    "section": "PART 02 · 品牌",
    "title": "传播待沉淀方法论 · 新品冷启动待破局",
    "subtitle": "三件事决定品牌能否撑起 Q3 增长",
    "points": [
        {"num": "01", "head": "选题决策缺数据支撑", "desc": "依赖经验判断 · 爆款逻辑不可复制"},
        {"num": "02", "head": "新品发布缺种子流量", "desc": "无私域流量池可调用 · 依赖付费投放"},
        {"num": "03", "head": "品牌响应业务节奏", "desc": "缺乏前置议题设置 · 主动出击意识不足"},
    ],
}

# 规则 3 · title 直接复用 v1 BRAND_Q2.title
# 规则 4 · v1 3 group 直接对应 3 lane,不需合并
BRAND_MILESTONE = {
    "section": "PART 02 · 品牌",
    "title": "Q2 三链路并进:双 IP · 高客单 · 运营闭环",
    "subtitle": "5 月测试 · 6 月放量 · 7 月沉淀 SOP",
    "lanes": [
        {
            "name": "IP 引流层",
            "task": "双 IP 账号引流跑通",
            "outcome": "内容模型测试 → 公域→私域加粉 3,000 → 沉淀《IP 内容生产 SOP》",
        },
        {
            "name": "高客单转化",
            "task": "高客单产品转化跑通",
            "outcome": "全链路成交 1 单 → 成交 ≥ 30 单 → 优化销售 SOP",
        },
        {
            "name": "运营全链路",
            "task": "新增运营全链路跑通",
            "outcome": "店铺上架 → 闭环跑通 ROI 正 → 卡点分析定 Q3",
        },
    ],
}

# 规则 5 · 直接复用 v1 CLOSING
CLOSING = {
    "tag": "Q2 · 2026",
    "title": "把每一件事做到位",
    "subtitle": "产品 · 品牌 · 协同",
    "footer": "THANKS",
}
