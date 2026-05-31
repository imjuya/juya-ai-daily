# [2026-05-31](https://github.com/imjuya/juya-ai-daily/issues/107)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260531/20260531075840013178bc0b_cover_748a.png)

# AI 早报 2026-05-31

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1mvVj68Es1) ｜ [YouTube](https://www.youtube.com/watch?v=ysd4v7xE-4Q)

## 概览
### 模型发布
- 阶跃星辰为 Hermes Agent 用户提供 Step 3.7 Flash 模型限时免费服务 [↗](https://x.com/StepFun_ai/status/2060726184712052849) `#1`
### 开发生态
- OpenClaw 发布 2026.5.28 版本 [↗](https://x.com/openclaw/status/2060843306100183541) `#2`
### 技术与洞察
- 小米详解 MiMo-V2.5 推理优化 [↗](https://mp.weixin.qq.com/s/3e8ms4m00NbRVicLry1oAQ) `#3`
### 行业动态
- MiniMax 启动 A 股 IPO 进程 [↗](https://zhidx.com/p/561711.html) `#4`
- 软银宣布在法国投资最高 750 亿欧元建设 AI 数据中心 [↗](https://group.softbank/en/news/press/20260531_0) `#5`
### 前瞻与传闻
- 爆料称 ChatGPT 正在开发 "Translation Block" [↗](https://x.com/btibor91/status/2060811897495294445) `#6`

---

## [阶跃星辰为 Hermes Agent 用户提供 Step 3.7 Flash 模型限时免费服务](https://x.com/StepFun_ai/status/2060726184712052849) `#1`
> 阶跃星辰的新模型 `Step 3.7 Flash` 目前正通过 **Nous Portal** ，面向 **Hermes Agent** 用户开展为期 **30 天** 的免费开放活动。

**StepFun** 联合 **Nous Research** 面向 `Hermes Agent` 用户推出了全新的 `Step 3.7 Flash` 模型限时免费活动。

官方表示，`Step 3.7 Flash` 是一款 `MoE` 视觉-语言模型，重点针对 `Agent` 效率、编码、搜索以及多模态工作流进行了优化。

用户需在 **Nous Portal** 注册免费账号方可获取 **30 天** 的访问权限。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260531/20260531074421_02033a4328.png)

相关链接：
- [https://x.com/StepFun_ai/status/2060726184712052849](https://x.com/StepFun_ai/status/2060726184712052849)

---

## [OpenClaw 发布 2026.5.28 版本](https://x.com/openclaw/status/2060843306100183541) `#2`
> **OpenClaw** 发布 **2026.5.28** 版本，新增支持 `Claude Opus 4.8` 模型及通过 `fal` 接入的 `Krea` 图像模型，官方称该版本冷启动快 **14.5%**、热启动快 **16.0%**、新安装体积缩小 **52.8%**。

**OpenClaw** 正式发布 **2026.5.28** 版本，将 `Claude Opus 4.8` 纳入模型目录，使用常规 **Anthropic** 认证与运行时路由。

该版本同时通过 `fal` 接入 `Krea` 图像模型，可接入现有 `image_generate` 工作流。

根据官方测量数据，相比前版 .27，冷启动快 **14.5%**、热启动快 **16.0%**、新安装体积缩小 **52.8%**，`Package roots` 从 **371** 减至 **300**。

此外 `Gateway`、插件与会话热路径减少了重复的元数据、配置及 `session-store` 开销。

`Discord` 进度草稿可在工具长时间运行时显示清理后的助手评论而不改变最终回复。

`/subagents` 命令新增展示活跃子运行的标签、会话、时间戳与工具日志，便于调试委托链路。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260531/20260531073802_ab80eab5ae.png)

相关链接：
- [https://x.com/openclaw/status/2060843306100183541](https://x.com/openclaw/status/2060843306100183541)

---

## [小米详解 MiMo-V2.5 推理优化](https://mp.weixin.qq.com/s/3e8ms4m00NbRVicLry1oAQ) `#3`
> **小米MIMO团队**发布了 `MiMo-V2.5` 系列模型推理优化技术报告，通过重构 **KVCache** 系统和引入自研分布式缓存 **GCache**，官方称成功兑现了 `Hybrid SWA` 架构的效率潜力，使线上服务端 **KV Cache** 命中率平均达 **93%**，并将由此节省的成本通过 **API** 降价回馈用户。

**小米**大模型团队发文详细介绍了 `MiMo-V2.5` 系列模型的推理全链路工程化实践，旨在解决 `Hybrid SWA`、`MoE` 及多模态 `Encoder` 在真实线上系统中的效率转化问题。

通过重构双池 `KV Cache` 管理、引入自研分布式缓存 `GCache` 以及优化 `Prefill` 与 `Decode` 执行链路，官方称将 `EP` 缩减至原先的 **1/2**，实现了约 **40%** 的端到端性能提升，多模态 `Encoder` 吞吐也提升至 **2 倍**。

官方表示，目前服务端 `KV Cache` 命中率平均可达 **93%**，部分优化成果已回馈 `SGLang` 开源社区，且已通过 `API` 降价将节省的成本回馈用户。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/748a2e98-87ab-4ee9-a26d-8e3100e9e163/d26c6930-c4c1-486a-838d-187967db1773/m001.png)

相关链接：
- [https://mp.weixin.qq.com/s/3e8ms4m00NbRVicLry1oAQ](https://mp.weixin.qq.com/s/3e8ms4m00NbRVicLry1oAQ)

---

## [MiniMax 启动 A 股 IPO 进程](https://zhidx.com/p/561711.html) `#4`
> 据媒体报道，**MiniMax** 已于 **5 月 29 日** 同 **中信证券** 签署辅导协议，正式启动 `A 股 IPO` 进程，此前该公司已于今年 **1 月** 在 `港交所` 上市。

媒体报道显示，**证监会**官网披露 **MiniMax** 已提交上市辅导备案报告，由 **中信证券** 担任辅导机构，正式开启 **A 股** 上市进程。

在资本表现方面，该公司自今年 **1 月** 登陆 **港交所** 以来股价大幅上涨，并将于 **6 月 8 日** 被纳入 `恒生科技指数`。

业务数据方面，官方称其过去两个月 `ARR` 实现超 **100%** 增长，目前 `ARR` 已超过 **3 亿美元**，全球企业及开发者客户数超 **百万**。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/748a2e98-87ab-4ee9-a26d-8e3100e9e163/25c91425-2074-4afd-86bc-d1cdaf722cbc/m001.png)

相关链接：
- [https://zhidx.com/p/561711.html](https://zhidx.com/p/561711.html)

---

## [软银宣布在法国投资最高 750 亿欧元建设 AI 数据中心](https://group.softbank/en/news/press/20260531_0) `#5`
> **软银**宣布计划在**法国**投资最高 **750 亿欧元**，开发并运营总容量 `5 GW` 的 **AI 数据中心**，其中第一阶段将投入 **450 亿欧元**建设 `3.1 GW` 产能。

**SoftBank Group** 宣布计划在法国开发和运营 `5 GW` 的 **AI** 数据中心，总投资额最高可达 **750 亿欧元**。

该项目第一阶段将向 **Hauts-de-France** 地区投入 **450 亿欧元**，计划于 **2031 年**前在 **Dunkirk**、**Bosquel** 和 **Bouchain** 等地交付 `3.1 GW` 的数据中心容量。

此外，**SoftBank Group** 将与 **Schneider Electric** 合作，在 **Dunkirk** 港建立涵盖两家工厂的先进制造集群。

预计该整体项目将为当地创造数千个高技能工作岗位。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260531/20260531075712_8ec04c1232.png)

相关链接：
- [https://group.softbank/en/news/press/20260531_0](https://group.softbank/en/news/press/20260531_0)

---

## [爆料称 ChatGPT 正在开发 "Translation Block"](https://x.com/btibor91/status/2060811897495294445) `#6`
> 据爆料博主称，**OpenAI** 正在为 `ChatGPT` 开发 "Translation Block" 翻译组件，其支持的语言中罕见地包含了《权力的游戏》虚构语言 **"High Valyrian"**。

据爆料博主 **Tibor Blaho** 发文，**OpenAI** 目前正在为 **ChatGPT** 开发一款名为 `"Translation Block"` 的全新翻译小组件。

该组件被测试的语言列表中不仅包含现实中的常用语种，还特别加入了一种为 **《权力的游戏》** 专门创造的虚构语言 `"High Valyrian"`。

该功能仍处于内部开发阶段，尚未正式上线。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/748a2e98-87ab-4ee9-a26d-8e3100e9e163/6aa3dadb-334a-49ee-bc85-68e0ea088a20/m001.png)

相关链接：
- [https://x.com/btibor91/status/2060811897495294445](https://x.com/btibor91/status/2060811897495294445)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。