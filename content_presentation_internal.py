# -*- coding: utf-8 -*-
"""演讲面数据 · v2 · tone=internal · 自动生成

由 /rewrite-presentation 命令产出。
渲染:cp content_presentation_internal.py content_presentation.py && .venv/bin/python redesign_presentation.py

internal 档:尖锐 · 容许行业黑话 · 容许自嘲,适合部门内部 / 一号位 / 复盘会。
"""

# 规则 5 · 直接复用 v1 COVER
COVER = {
    "tag": "DEMO · Q2 · 2026",
    "title": "示例公司 Q2 工作汇报",
    "subtitle": "标准版一条腿扛营收 · 两端没跑通 · 品牌靠运气",
    "byline": "DEMO · 工具示例数据",
}

# 规则 1 · title 来自 v1 PRODUCT_MATRIX.title + 行动加强
# 规则 2 · subtitle ← v1 PRODUCT_PROBLEMS.title;points ← v1 PRODUCT_PROBLEMS.items 一字不改
PRODUCT_KEYPOINT = {
    "section": "PART 01 · 产品",
    "title": "营收全压标准版,Q3 必须破两端",
    "subtitle": "三个硬伤决定 Q3 能不能涨",
    "points": [
        {"num": "01", "head": "标准版增速吃完红利", "desc": "MAU 见顶 · 没有下一曲线"},
        {"num": "02", "head": "试用用户全走丢", "desc": "激活后没引导动作 · 自然转化率拉跨"},
        {"num": "03", "head": "和竞品长得一模一样", "desc": "核心功能高度重合 · 没有杀手特性"},
    ],
}

# 规则 3 · title 直接复用 v1 PRODUCT_Q2.title
# 规则 4 · v1 5 group → 3 lane
PRODUCT_MILESTONE = {
    "section": "PART 01 · 产品",
    "title": "Q2 必打三件事:Onboarding · V7 · AI 辅助",
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
            "task": "线下行业沙龙 + 首款周边商业化",
            "outcome": "策划落地 → 全渠道发售 → 复盘归档",
        },
    ],
}

# 规则 1 · BRAND_MATRIX 是职能描述非判断,KEYPOINT.title 直接取 v1 BRAND_PROBLEMS.title
# 规则 2 · subtitle ← v1 BRAND_PROBLEMS.subtitle 避免重复
BRAND_KEYPOINT = {
    "section": "PART 02 · 品牌",
    "title": "传播完全没方法论 · 新品冷启动全靠运气",
    "subtitle": "三件事不解决,Q3 品牌涨不动",
    "points": [
        {"num": "01", "head": "选题靠拍脑袋", "desc": "数据没回流到选题 · 爆款不可复用"},
        {"num": "02", "head": "0 种子启动", "desc": "新品发布没私域池 · 全靠付费投放"},
        {"num": "03", "head": "等需求 · 不造需求", "desc": "被动响应业务部门 · 没主动议题"},
    ],
}

# 规则 3 · title 直接复用 v1 BRAND_Q2.title
# 规则 4 · v1 3 group 直接对应 3 lane,不需合并
BRAND_MILESTONE = {
    "section": "PART 02 · 品牌",
    "title": "Q2 必跑三链路:双 IP · 高客单 · 运营闭环",
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

# 规则 5 · 直接复用 v1 CLOSING
CLOSING = {
    "tag": "Q2 · 2026",
    "title": "把每一件事做到位",
    "subtitle": "产品 · 品牌 · 协同",
    "footer": "THANKS",
}
