# [2026-06-01](https://github.com/imjuya/juya-ai-daily/issues/108)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260601/20260601083337906158289d_cover_8c11.png)

# AI 早报 2026-06-01

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1TwVR6qEd9) ｜ [YouTube](https://www.youtube.com/watch?v=XgVZ6VspHZI)

## 概览
### 要闻
- MiniMax 上线 MiniMax M3 模型，支持多模态和 1M 上下文 [↗](https://www.minimaxi.com/news/minimax-m3-zh) `#1`
### 模型发布
- SpaceXAI 上线 Grok-Imagine-Video-1.5-Preview API [↗](https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview) `#2`
- Qwen-VLA 发布，统一视觉-语言-动作建模 [↗](https://qwen.ai/blog?id=qwenvla) `#3`
### 开发生态
- OpenAI 宣布 Codex 用户破 500 万并重置付费用户使用额度 [↗](https://x.com/sama/status/2061097558819356732) `#4`
- 英特尔联合魔搭社区上线AI PC专区 [↗](https://modelscope.cn/brand/view/AI_PC?branch=0&tree=1) `#5`
- OpenClaw推出auto模式：LLM辅助的主机命令自动审批 [↗](https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals) `#6`
### 行业动态
- SpaceXAI 招聘中文 AI Tutor 远程岗位 [↗](http://job-boards.greenhouse.io/xai/jobs/5090180007) `#7`
- OpenAI 官宣成立 OpenAI Robotics 并启动招聘 [↗](https://x.com/sama/status/2061117302528188712) `#8`

---

## [MiniMax 上线 MiniMax M3 模型，支持多模态和 1M 上下文](https://www.minimaxi.com/news/minimax-m3-zh) `#1`
> MiniMax 上线了其新一代旗舰模型 `MiniMax M3`。该模型支持原生多模态与 **1M** token 上下文，专为 `Agent` 推理及代码等场景优化，现已上线 `API` 和 `Token Plan`，并在 `OpenCode` 中提供限时免费使用。更多细节有待官方的正式发布公告披露。

**MiniMax** 官方上线其新一代旗舰模型 `MiniMax-M3`，现已通过 **API** 和 **Token Plan** 开放使用，并在 **OpenCode** 中提供限时免费使用。

该模型主打原生多模态输入与最高 `1M token` 的长上下文能力，主要针对 `Agent` 推理、工具调用、代码和长文档等复杂任务场景进行了优化。

计费方面，输入 `512k tokens` 以内享 **7 天** 限时五折优惠，折后价格为输入 **2.10** 元、输出 **8.40** 元每百万 `tokens`。

而超过 `512k tokens` 的长文本处理能力目前为限时限量供应，需联系销售获取，官方预计 **数日后** 全量开放。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601083407_79259d41a8.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601083328_835dd0740e.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601083440_9eacb468dd.png)

相关链接：
- [https://www.minimaxi.com/news/minimax-m3-zh](https://www.minimaxi.com/news/minimax-m3-zh)

---

## [SpaceXAI 上线 Grok-Imagine-Video-1.5-Preview API](https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview) `#2`
> **SpaceXAI**发布视频生成模型`Grok-Imagine-Video-1.5-Preview`，现已上线API。该模型支持文本和图像输入，**480p**与**720p**分辨率分别按每秒**0.08**和**0.14**美元计费。据**Arena.ai**平台数据，其**720p**版本在`Image-to-Video Arena`排行榜上位居第一。

**SpaceXAI**发布了全新的视频生成模型`Grok-Imagine-Video-1.5-Preview`，目前已通过API向开发者开放。

该模型支持文本与图像输入生成视频，提供`480p`与`720p`两种分辨率选项，按生成的视频秒数计费。

**480p**分辨率的价格为每秒**0.08美元**，**720p**分辨率的价格为每秒**0.14美元**。

据`Arena.ai`平台数据显示，该`720p`版本在**Image-to-Video Arena排行榜**上位居第一。

相比前代同分辨率版本，其分数提升了**52分**，并超越了`Seedance-2.0`等模型。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/8c11e66e-0c7f-4591-8edd-bc34cd67ac4d/d6090a41-7880-4e3f-b12d-1188809abcd5/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601080439_e322445e2f.png)

相关链接：
- [https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview](https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview)
- [https://x.com/arena/status/2060874057130934376](https://x.com/arena/status/2060874057130934376)

---

## [Qwen-VLA 发布，统一视觉-语言-动作建模](https://qwen.ai/blog?id=qwenvla) `#3`
> **Qwen** 团队近期发布了 `Qwen-VLA` 视觉-语言-动作通用模型。该模型基于 `Qwen3.5-4B` 构建，能统一处理机器人操作、导航和轨迹预测，官方称其在多项模拟和真实评测中表现超过专项微调模型。

**Qwen**团队近期发布了统一视觉-语言-动作模型 `Qwen-VLA` 的技术报告及 **GitHub** 仓库。

该模型基于 `Qwen3.5-4B` 骨干网络与 **1.15B** 的 `DiT` 动作解码器构建。

通过统一的动作与轨迹预测框架，它实现了对机器人操作、视觉语言导航和轨迹预测的联合处理。

官方测试数据显示，作为一个统一的通用模型，`Qwen-VLA-Instruct` 在 `LIBERO`、`Simpler-WidowX`、真实 `ALOHA` 双臂机器人等多个评测中，匹配或超越了专门针对特定任务微调的专家模型。

模型采用了四阶段渐进式训练。

并通过形态感知的提示词条件机制，使得一套权重无需添加平台专属输出头即可适配多种机器人平台。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/8c11e66e-0c7f-4591-8edd-bc34cd67ac4d/643fcd0f-3267-4358-9a71-5fee5cb432be/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/8c11e66e-0c7f-4591-8edd-bc34cd67ac4d/643fcd0f-3267-4358-9a71-5fee5cb432be/m002.gif)

相关链接：
- [https://qwen.ai/blog?id=qwenvla](https://qwen.ai/blog?id=qwenvla)
- [https://github.com/QwenLM/Qwen-VLA](https://github.com/QwenLM/Qwen-VLA)

---

## [OpenAI 宣布 Codex 用户破 500 万并重置付费用户使用额度](https://x.com/sama/status/2061097558819356732) `#4`
> **Codex** 负责人 **Tibo** 宣布 **Codex** 用户数突破 **500** 万。为庆祝此里程碑，官方于**北京时间5月31日晚约11点半**面向所有 `ChatGPT` 付费订阅用户，重置了 `Codex` 的使用额度。

**OpenAI Codex** 负责人 **Tibo** 透露，`Codex` 的用户群体已经达到 **500 万** 规模。

为了庆祝这一里程碑，**Tibo** 于北京时间 **5月31日** 晚约 **11点半** 宣布已将所有 `ChatGPT` 付费订阅的 `Codex` 使用额度清零重置。

用户的每周和每小时限额均已恢复至 **100%**。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601080038_6d12131509.png)

相关链接：
- [https://x.com/sama/status/2061097558819356732](https://x.com/sama/status/2061097558819356732)

---

## [英特尔联合魔搭社区上线AI PC专区](https://modelscope.cn/brand/view/AI_PC?branch=0&tree=1) `#5`
> **英特尔**近期联合**魔搭**社区上线“**英特尔**AI PC专区”，集成针对`酷睿Ultra`优化的模型库、智能体部署指南及异构计算工具，为开发者提供端侧`AI`开发实战支持。

日前，**英特尔**联合**魔搭社区**推出了“**英特尔AI PC专区**”，定位为一个经过验证且持续更新的实战工具箱。

专区内的 `OpenVINO Model Center` 提供了大量已针对 `酷睿 Ultra` 的 `CPU`、`GPU` 和 `NPU` 转换及量化的热门模型。

同时，平台设有“**Claw智能体板块**”，提供 `OpenClaw`、`TRAE` 及 `樱桃AI语音助手`等框架的部署指南与现成技能集合。

该专区已在**魔搭社区**上线，还包含本地部署指南、实测数据、技术博客以及在线讨论区。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/8c11e66e-0c7f-4591-8edd-bc34cd67ac4d/91a00e00-1ff3-400c-ba89-6289a002a9a2/m001.png)

相关链接：
- [https://modelscope.cn/brand/view/AI_PC?branch=0&tree=1](https://modelscope.cn/brand/view/AI_PC?branch=0&tree=1)
- [https://mp.weixin.qq.com/s/tcEiMVEcsPZB-exj1WbnzQ](https://mp.weixin.qq.com/s/tcEiMVEcsPZB-exj1WbnzQ)

---

## [OpenClaw推出auto模式：LLM辅助的主机命令自动审批](https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals) `#6`
> **OpenClaw** 正公开测试名为 `auto` 的主机命令审批模式。该模式借助独立 `LLM` 审查器自动放行低风险命令，高风险或模糊情况则退回人工，兼顾了执行效率与安全。

OpenClaw正公开测试一种名为 **“auto”** 的主机命令审批模式，为 **YOLO** 的激进免审与 **Ask** 的频繁打断提供企业级的折中方案。

该模式在命令匹配允许列表时直接放行，未匹配时则由独立 `LLM` 审查器分析后仅允许一次低风险执行，其余高风险或模糊情况自动退回人工审批。

用户通过 `tools.exec.mode: auto` 配置 `opt-in` 启用，并能将审批请求推送至 **Slack**、**Telegram** 等渠道；审查器模型可与主代理分离，以支持更强的模型。

官方强调 **auto** 模式严格遵守主机本地安全设置，未来可能在测试顺利后成为更安全的默认选项。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601081905_ef374d822f.png)

相关链接：
- [https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals](https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals)

---

## [SpaceXAI 招聘中文 AI Tutor 远程岗位](http://job-boards.greenhouse.io/xai/jobs/5090180007) `#7`
> **SpaceXAI** 开放“`AI Tutor - Chinese`”远程职位，负责多语言音频标注以训练 **Grok** 语音交互能力，需中文母语及英语 **B2** 水平，时薪为 **35** 至 **45** 美元。

**SpaceXAI** 官方发布 **“AI Tutor - Chinese”** 招聘信息，提供**全球远程办公**机会。

该职位主要负责多语言音频数据的标注、注释与录制。目标在于训练并提升 `Grok` 模型在`语音交互`、`口音变化`及`跨文化语境`下的处理能力。

应聘者需具备**中文母语水平**，熟悉方言及口音差异。同时需要**英语 B2** 水平，并拥有出色的**跨口音高精度语音转录**能力。

职位形式涵盖**全职**、**兼职**或**承包商**。**美国地区时薪**为 **35 至 45 美元**，且不提供签证赞助。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601081759_092e87b54e.png)

相关链接：
- [http://job-boards.greenhouse.io/xai/jobs/5090180007](http://job-boards.greenhouse.io/xai/jobs/5090180007)

---

## [OpenAI 官宣成立 OpenAI Robotics 并启动招聘](https://x.com/sama/status/2061117302528188712) `#8`
> **OpenAI** 首席执行官 **Sam Altman** 宣布其世界模拟研究项目已演变为 `OpenAI Robotics` 并启动招聘。该团队将招募全栈硬件、系统及 `ML` 工程师，旨在研发能在物理世界协助人类的机器人，短期内聚焦于支持熟练工人建设基础设施。

**OpenAI** 首席执行官 **Sam Altman** 宣布，其世界模拟研究项目在过去一年中已演变为 `OpenAI Robotics`，目前正在招募顶尖的全栈硬件、运维、系统和 `ML` 工程师。

该团队由 **Aditya Ramesh** 领导，以机器人硬件和 `ML` 研究的协同设计为基础，旨在编程和制造对社会有用的机器人。

短期内，该团队专注于开发支持熟练工人建设未来基础设施的机器人。

而长期愿景是让每个人都拥有能执行任何任务的个人机器人。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260601/20260601080904_fb53f3aaa3.png)

相关链接：
- [https://x.com/sama/status/2061117302528188712](https://x.com/sama/status/2061117302528188712)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。