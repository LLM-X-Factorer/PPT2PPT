# -*- coding: utf-8 -*-
"""演讲面数据 · v2 · tone=external · 自动生成

由 /rewrite-presentation 命令产出。
渲染:cp content_presentation_external.py content_presentation.py && .venv/bin/python redesign_presentation.py

external 档:建设性 · 把问题包装成机会 · 用建设词汇,适合投资人 / 客户 / 媒体 / 市场发布。
红线:不能退化成"信息墙"(纯名词列表),必须保留主谓宾判断结构。
"""

# 规则 5 · 直接复用 v1 COVER
COVER = {
    "tag": "DEMO · Q2 · 2026",
    "title": "示例公司 Q2 工作汇报",
    "subtitle": "标准版稳步领跑 · 两端持续布局 · 品牌升级方法论",
    "byline": "DEMO · 工具示例数据",
}

# 规则 1 · title 直接复用 v1 PRODUCT_MATRIX.title(已是 external 建设性判断,主谓宾结构完整)
# 规则 2 · subtitle ← v1 PRODUCT_PROBLEMS.title;points ← v1 PRODUCT_PROBLEMS.items 一字不改
PRODUCT_KEYPOINT = {
    "section": "PART 01 · 产品",
    "title": "标准版稳步领跑,两端持续布局",
    "subtitle": "三大引擎驱动 Q3 增长",
    "points": [
        {"num": "01", "head": "标准版进入新增长曲线探索", "desc": "MAU 进入稳定平台期 · 启动下一曲线规划"},
        {"num": "02", "head": "试用付费链路持续优化", "desc": "完善激活后的引导路径 · 提升自然转化"},
        {"num": "03", "head": "专业版差异化升级中", "desc": "强化核心功能差异 · 打造关键特性"},
    ],
}

# 规则 3 · title 直接复用 v1 PRODUCT_Q2.title
# 规则 4 · v1 5 group → 3 lane
PRODUCT_MILESTONE = {
    "section": "PART 01 · 产品",
    "title": "Q2 推进三主线:Onboarding · V7 · AI 辅助",
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
    "title": "传播方法论建设中 · 新品冷启动机制升级",
    "subtitle": "三大举措支撑 Q3 品牌增长",
    "points": [
        {"num": "01", "head": "选题数据机制建设中", "desc": "建立数据驱动的选题决策体系"},
        {"num": "02", "head": "新品种子流量体系完善中", "desc": "搭建私域流量池 · 优化新品冷启动路径"},
        {"num": "03", "head": "品牌主动议题机制建设中", "desc": "建立前置议题设置能力 · 强化主动出击"},
    ],
}

# 规则 3 · title 直接复用 v1 BRAND_Q2.title
# 规则 4 · v1 3 group 直接对应 3 lane,不需合并
BRAND_MILESTONE = {
    "section": "PART 02 · 品牌",
    "title": "Q2 三链路升级:双 IP · 高客单 · 运营闭环",
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
