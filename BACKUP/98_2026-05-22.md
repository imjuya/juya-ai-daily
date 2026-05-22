# [2026-05-22](https://github.com/imjuya/juya-ai-daily/issues/98)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260522/20260522091114161812cefe_cover_b939.png)

# AI 早报 2026-05-22

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV14WLe6UEAS) ｜ [YouTube](https://www.youtube.com/watch?v=_6JILpKOFnE)

## 概览
### 要闻
- DeepSeek 引入 API 并发限制和 user_id 隔离 [↗](https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit) `#1`
- OpenAI 发布 Codex 多项更新，上线 Appshots 与锁屏控制控制功能 [↗](https://developers.openai.com/codex/remote-connections) `#2`
- Qwen3.7-Max 上线 API 和 Qwen Studio [↗](https://bailian.console.aliyun.com/cnbeijing?tab=model&#/modelmarket/detail/qwen3.7-max?serviceSite=asiapacific-china) `#3`
- Antigravity 永久提升 Gemini 模型速率限制并重置周配额 `#4`
### 模型发布
- SpaceXAI 发布编码模型 Grok Build 0.1 [↗](https://docs.x.ai/developers/models/grok-build-0.1) `#5`
- 腾讯混元开源多语言翻译模型家族 Hy-MT2 [↗](https://aistudio.tencent.com/llm/zh?tabIndex=0) `#6`
- 网易有道开源多模态数学推理模型 Confucius4 [↗](https://huggingface.co/netease-youdao/Confucius4) `#7`
- 美团开源 LongCat-Video-Avatar-1.5 框架 [↗](https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/) `#8`
- Runway 发布 Aleph 2.0 及 Edit Studio [↗](https://runwayml.com/news/introducing-aleph-2-and-edit-studio) `#9`
### 开发生态
- SpaceXAI宣布OpenCode支持接入Grok订阅 [↗](https://x.ai/news/grok-opencode) `#10`
- Google 发布 ADK for Kotlin 与ADK for Android 0.1.0 版本 [↗](https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/) `#11`
- Anthropic 公布 Claude Opus 网络安全应用成果并发布 Compliance API [↗](https://claude.com/blog/compliance-api-security-partners) `#12`
- OpenClaw 发布 2026.5.20 版本更新 [↗](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20) `#13`
- Claude Code 预告升级 /usage 命令支持分类查看 Token 明细 [↗](https://x.com/bcherny/status/2057476878110261587) `#14`
### 产品应用
- OpenAI推出ChatGPT for PowerPoint测试版 [↗](https://chatgpt.com/apps/powerpoint/) `#15`
- MiniMax Agent 集成 Perplexity Search [↗](https://x.com/MiniMaxAgent/status/2057491132133904739) `#16`
- CapCut 宣布与 Gemini App 达成集成合作 [↗](https://x.com/capcutapp/status/2057340757896216641) `#17`
### 行业动态
- Modal 完成 3.55 亿美元 C 轮融资，投后估值达 46.5 亿美元 [↗](https://modal.com/blog/modal-series-c) `#18`
### 前瞻与传闻
- 消息称月之暗面启动拆除VIE架构 冲刺赴港IPO `#19`
- Anthropic被曝正与Microsoft洽谈租用Maia 200芯片 [↗](https://www.theverge.com/ai-artificial-intelligence/935688/anthropic-is-in-talks-to-use-microsofts-ai-chips-too) `#20`

---

## [DeepSeek 引入 API 并发限制和 user_id 隔离](https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit) `#1`
> **DeepSeek**更新`API`文档，明确`deepseek-v4-pro`与`deepseek-v4-flash`并发上限为**500**和**2500**，超限报错可免费扩容。新增`user_id`隔离，实现内容安全与`KVCache`调度隔离，扩容账号按此独立限速。此外，还增加了请求保活机制。

**DeepSeek** 官方 `API` 文档新增限速与隔离细则，规定了不同模型的并发限制与保活机制。

在账号粒度上，`deepseek-v4-pro` 并发限制为 **500**，`deepseek-v4-flash` 为 **2500**。超出限制会返回 `HTTP 429` 错误码，用户可提交工单免费申请扩容。

`API` 同时引入了 `user_id` 隔离功能，用于实现不同终端用户的内容安全、`KVCache` 及调度隔离。且对扩容账号会按 `user_id` 维度进行独立并发限速。

此外，请求在等待期间会通过特定格式保活，若 **10 分钟** 仍未开始推理服务器将关闭连接。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260522/20260522083214_abd4b324eb.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260522/20260522083259_2664b604d6.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260522/20260522083326_2594ab0603.png)

相关链接：
- [https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit](https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit)

---

## [OpenAI 发布 Codex 多项更新，上线 Appshots 与锁屏控制控制功能](https://developers.openai.com/codex/remote-connections) `#2`
> **OpenAI**发布`Codex`应用多项更新。`Appshots`功能支持一键截取窗口画面与文本。`/goal`指令正式上线。`Computer Use`新增锁定模式，允许用手机远程操控已锁屏的**Mac**，`Business`版新增支持共享自定义插件。

**OpenAI** 集中发布了针对编程工具 `Codex` 应用的多项功能更新。

官方正式推出 `Appshots` 功能，允许用户在 **Mac** 上通过双击 `Command` 键一键提取当前应用窗口的截图及完整文本上下文。

同时 `/goal` 指令结束实验阶段，支持 `Codex` 持续**数小时**甚至**数天**处理长任务，目前部分用户可能需手动运行命令来激活该功能。

此外，`Computer Use` 新增锁定使用能力，允许用户通过手机等设备远程操控已锁屏的 **Mac** 主机，**Business** 版用户也已获准在团队内共享自定义插件。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/f3cfb096-7241-4a6a-8932-2fd09e4257bd/m001.png)

相关链接：
- [https://developers.openai.com/codex/remote-connections](https://developers.openai.com/codex/remote-connections)
- [https://developers.openai.com/codex/app/computer-use](https://developers.openai.com/codex/app/computer-use)

---

## [Qwen3.7-Max 上线 API 和 Qwen Studio](https://bailian.console.aliyun.com/cnbeijing?tab=model&#/modelmarket/detail/qwen3.7-max?serviceSite=asiapacific-china) `#3`
> `Qwen3.7-Max` 正式上线 `API` 和 `Qwen Studio`。该模型标准输入和输出价格分别为每百万 **tokens** **12 元** 和 **36 元**。根据 **Artificial Analysis** 数据，其智能指数得分达 **56.6 分**，幻觉率显著降低。

**阿里云百炼平台**现已上线 `Qwen3.7-Max` 模型，当前开放纯文本输入与输出能力。官方强调其在长周期自主执行、编程及办公生产力等 `Agent` 能力上有所提升。

在定价与规格方面，该模型上下文窗口为 `1M tokens`；其标准输入和输出价格分别为每百万 `tokens` 12 元和 36 元。据 **Artificial Analysis** 测试数据，`Qwen3.7-Max` 在 `智能指数` 中得分 56.6，较 `Qwen3.6-Max-Preview` 提升 4.8 分。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260522/20260522090500_9048c1e713.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/a91eab1d-a581-47f1-8c1e-c34a5304a553/m002.png)

相关链接：
- [https://bailian.console.aliyun.com/cnbeijing?tab=model&#/modelmarket/detail/qwen3.7-max?serviceSite=asiapacific-china](https://bailian.console.aliyun.com/cnbeijing?tab=model&#/modelmarket/detail/qwen3.7-max?serviceSite=asiapacific-china)
- [https://x.com/ArtificialAnlys/status/2057374452883788196](https://x.com/ArtificialAnlys/status/2057374452883788196)

---

## Antigravity 永久提升 Gemini 模型速率限制并重置周配额 `#4`
> **Google**宣布，`Antigravity` 已将所有付费层级中 `Gemini` 模型的`速率限制`永久提升 **3 倍**，并重置了所有用户本周的 `Gemini` `配额`，以回应用户快速触及限制的反馈。

**Google** 宣布，**Antigravity** 已将所有付费层级中 ``Gemini 模型`` 的速率限制永久提升 **3 倍**，并重置了所有用户**本周**的配额。

官方表示此举旨在回应用户过快达到限制的反馈，以便用户进一步测试 ``3.5 Flash 模型``。

针对 ``Antigravity 2.0`` 更新导致 ``IDE`` 消失、丢失配置的问题，工作人员承认发布不够顺利，将发布更新进行修复。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260521/20260521184951_e875d2b535.png)

---

## [SpaceXAI 发布编码模型 Grok Build 0.1](https://docs.x.ai/developers/models/grok-build-0.1) `#5`
> **SpaceXAI** 近期上线了专为 `agentic coding` 打造的 `Grok Build 0.1` 模型，现已上线官方及部分第三方 API 平台。

**SpaceXAI** 发布了专为 `agentic software engineering workflows` 训练的快速模型 `Grok Build 0.1`。

该模型目前处于早期访问和 `Beta` 测试阶段。新模型支持 `256K` 上下文窗口、`函数调用` 及推理功能。

且推理算力不可配置、不支持非推理模式，官方 `API` 输入和输出定价分别为每百万 `token` **1 美元** 和 **2 美元**。

除官方 `API` 外，该模型现已集成至 `Grok Build CLI`，并登陆 **Vercel** `AI Gateway` 和 **Nous Research** 的 `Hermes Agent` 等第三方平台。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260521/20260521185706_5c71d3e0b9.png)

相关链接：
- [https://docs.x.ai/developers/models/grok-build-0.1](https://docs.x.ai/developers/models/grok-build-0.1)

---

## [腾讯混元开源多语言翻译模型家族 Hy-MT2](https://aistudio.tencent.com/llm/zh?tabIndex=0) `#6`
> **腾讯混元**正式开源多语言翻译模型系列 `Hy-MT2`，并上线“**腾讯 Hy 翻译**”小程序。官方称该系列包含 **三款** 支持 **33 种** 语言的模型，性能在多项任务中击败多家头部闭源模型。

腾讯**混元**发布了全新多语言翻译模型 `Hy-MT2`，并已同步推出支持离线端侧推理的“腾讯 Hy 翻译”小程序。

该系列涵盖 `1.8B`、`7B` 及 `30B-A3B` 三种参数规模，均支持 **33** 种语言互译与 **5** 种中国方言。

官方表示，`7B` 和 `30B-A3B` 模型在各类任务中达到开源最佳，在真实场景评测中甚至超越了 `DeepSeek-V4-Pro` 和 `Gemini 3.1 Pro` 等头部闭源模型。

而 `1.8B` 模型也击败了**微软**等主流商业翻译 API。得益于自研的 `1.25-bit` 极端量化技术，`1.8B` 模型仅需约 **440MB** 存储空间即可在主流手机芯片上部署。

且推理速度较上代提升 **1.5** 倍。目前模型与配套的翻译指令遵循测试集已在 **Github** 等多个平台开源，iOS 和安卓独立 APP 正在上架中。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/992e991d-97c5-4abe-96dc-d3b3686a0609/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/992e991d-97c5-4abe-96dc-d3b3686a0609/m002.png)

相关链接：
- [https://aistudio.tencent.com/llm/zh?tabIndex=0](https://aistudio.tencent.com/llm/zh?tabIndex=0)
- [https://mp.weixin.qq.com/s/a_GPa-brAIB5aqXyd8W4-Q](https://mp.weixin.qq.com/s/a_GPa-brAIB5aqXyd8W4-Q)
- [https://huggingface.co/collections/tencent/hy-mt2](https://huggingface.co/collections/tencent/hy-mt2)

---

## [网易有道开源多模态数学推理模型 Confucius4](https://huggingface.co/netease-youdao/Confucius4) `#7`
> **网易有道**开源多模态数学推理模型“`子曰4`”。该模型基于 `Qwen3.5-27B`，官方称其在 `视觉数理基准测试` 中达到同规模 `SOTA` 水平，并将 `思维链` 长度减少约 **43.2%**。

**网易有道** **AI 团队**已正式开源专为数学推理设计的 `多模态大模型` “`子曰4`”，该项目基于 `Qwen3.5-27B` 进行二次开发并遵循 `Apache 2.0` 协议。

该模型采用“`监督微调（SFT）+强化学习（RL）`”的迭代训练框架，官方数据显示其在多个视觉数理基准上达到同尺寸模型的最佳水平，并在内部闭源数据集 `Math-Hard-500` 上实现了 `23.2%` 的性能提升。

为解决推理过度思考的问题，团队通过引入 `长度感知强化学习` 等机制，使整体思维链减少了 `43.2%`，从而降低了解题成本与响应时间。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/cf521b61-c4f0-4ac3-a55a-ab03aad10630/m001.png)

相关链接：
- [https://huggingface.co/netease-youdao/Confucius4](https://huggingface.co/netease-youdao/Confucius4)
- [https://modelscope.cn/models/netease-youdao/Confucius4](https://modelscope.cn/models/netease-youdao/Confucius4)

---

## [美团开源 LongCat-Video-Avatar-1.5 框架](https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/) `#8`
> **美团** **LongCat** 团队开源了音频驱动数字人视频生成框架 `LongCat-Video-Avatar-1.5`。新版本将音频编码器升级为 `Whisper-large-v3`，并通过步数蒸馏技术将推理加速至 **8** 步。

**美团** **LongCat** 团队正式发布了 `LongCat-Video-Avatar-1.5` 框架及对应权重。

该版本采用 `Whisper-large-v3` 替代原有的 `Wav2Vec2` 音频编码器，以提升唇形同步的准确度与自然度。原生支持音频文本到视频、音频图像到视频及视频续写任务，并能够泛化至动漫、动物及多人交互等复杂场景。

官方通过基于 `508` 对测试数据和 `770` 名评估者的人类评估基准宣称，该模型在写实度、稳定性和自然度上表现优异。

模型默认强制开启基于 `DMD2` 的 `8` 步蒸馏推理，并提供 `INT8` 量化选项以降低显存占用。虽然模型权重遵循 `MIT` 协议开源，但官方明确要求其生成的演示内容仅限学术使用，不得用于商业用途。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/496c7beb-b246-48b1-b667-5ecc357e3414/m001.png)

相关链接：
- [https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/](https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/)
- [https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)
- [https://github.com/meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video)

---

## [Runway 发布 Aleph 2.0 及 Edit Studio](https://runwayml.com/news/introducing-aleph-2-and-edit-studio) `#9`
> **Runway** 官方发布旗舰视频编辑模型升级版 `Aleph 2.0` 及新产品 `Edit Studio`。该模型支持最长 **30 秒** `1080p` 视频处理，具备局部精准修改及跨镜头编辑等能力，目前已在桌面网页端向所有付费用户开放。

**Runway** 官方宣布推出其旗舰视频编辑模型的升级版 `Aleph 2.0`，并同步上线专为该模型打造的新产品体验 `Edit Studio`。

`Aleph 2.0` 现已支持处理时长上限为 **30 秒**的 `1080p` 视频素材，并在编辑过程中能精准保留原视频未修改的细节，避免多余的画面变动。

同时，新模型引入了图像级别的控制能力，用户可通过修改单帧画面来指导视频的最终呈现效果，且支持在包含多次场景切换的视频中跨多个镜头一次性应用编辑。

`Edit Studio` 允许用户在正式生成前将修改效果作为图像进行预览，从而减少试错成本并加快迭代速度。

目前，上述功能已面向所有 **Runway** 付费计划的用户开放，可通过桌面网页端使用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/51752d33-a3ff-4173-b23a-6df71f66400d/m001.png)

相关链接：
- [https://runwayml.com/news/introducing-aleph-2-and-edit-studio](https://runwayml.com/news/introducing-aleph-2-and-edit-studio)

---

## [SpaceXAI宣布OpenCode支持接入Grok订阅](https://x.ai/news/grok-opencode) `#10`
> **SpaceXAI** 宣布用户现已能在 `OpenCode` 中使用 `SuperGrok` 或 **X Premium** 订阅。接入后可直接使用 `Grok Build` 模型进行编码。

**SpaceXAI** 宣布用户现已能在 **OpenCode** 中使用其 **SuperGrok** 或 **X Premium** 订阅。

接入后，用户可使用驱动 **Grok Build** 的底层模型进行编码，该模型与 **SpaceXAI** 基于终端的 **Agent** 采用同一模型，旨在提供高速度和代码库智能支持。

用户只需在 **OpenCode** 中执行 `/connect` 命令并选择“**xAI**”，即可根据设备环境选择通过浏览器或无头模式完成身份验证。

**SpaceXAI** 同时预告，未来将推出更多开源 **Agent** 和集成功能。

相关链接：
- [https://x.ai/news/grok-opencode](https://x.ai/news/grok-opencode)

---

## [Google 发布 ADK for Kotlin 与ADK for Android 0.1.0 版本](https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/) `#11`
> **Google** 官方宣布推出 `ADK` for `Kotlin` 和 `ADK` for `Android` 的 **0.1.0** 版本，开发者可利用该开源框架在后端或 `Android` 应用内构建 `AI Agent`。

**Google** 官方宣布推出用于开发和运行 `AI Agent` 的开源框架 `ADK for Kotlin` 与 `ADK for Android` 的 `0.1.0` 版本。

其中，`ADK for Kotlin` 面向后端项目，而 `ADK for Android` 提供专门的端侧优化。

允许开发者利用本地大语言模型在设备上直接运行 `Agent`，在保护隐私的同时保持与云端模型交互的灵活性。

此次发布的首个实验性版本包含了完整的构建基础。

支持混合编排、`MCP Tools`、`A2A` 以及多种 `Agent` 类型与运行时管理功能。

相关链接：
- [https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/](https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/)

---

## [Anthropic 公布 Claude Opus 网络安全应用成果并发布 Compliance API](https://claude.com/blog/compliance-api-security-partners) `#12`
> **Anthropic** 发布了多家安全厂商将 `Claude Opus` 模型应用于网络安全防御的早期测试数据，并面向 `Claude Enterprise` 正式推出 `Claude Compliance API`。

**Anthropic** 官方公布了 **Wiz**、**Palo Alto Networks** 和 **Accenture** 等合作伙伴利用 `Claude Opus` 进行漏洞挖掘与修复的早期成果。

根据官方提供的数据，**Accenture** 内部的安全测试覆盖率已从约 `10%` 提升至 `80%` 以上，扫描周转时间从 `3` 到 `5` 天缩短至不到 `1` 小时。

同时，**Anthropic** 发布了 `Claude Compliance API`，提供对 `Claude Enterprise` 对话内容及平台活动日志的编程访问接口。

目前，包含 **CrowdStrike** 和 **Microsoft Purview** 在内的 `28` 款外部安全与合规工具已完成集成并向企业客户开放。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/24c5ee51-52a3-415c-b167-24bf6171fd2e/m001.png)

相关链接：
- [https://claude.com/blog/compliance-api-security-partners](https://claude.com/blog/compliance-api-security-partners)
- [https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity)

---

## [OpenClaw 发布 2026.5.20 版本更新](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20) `#13`
> **OpenClaw** 官方发布 **2026.5.20** 版本更新，该版本新增了 `Discord` 语音跨频道跟随用户、敏感明文密钥警告提示，并修复了 `Windows` 安装界面冻结及无头设备 `SpaceXAI` 登录验证等问题。

**OpenClaw** 官方正式发布 **2026.5.20** 版本更新，本次主要聚焦于底层体验与安全性的修复。

更新后，`Discord` 语音会话支持自动跟随配置用户跨频道移动并进行多人切换，`Doctor` 工具会在配置文件包含明文密钥时发出警告，且模型固定状态提示变得更加清晰。

此外，此次更新解决了 `Windows` 环境安装时卡顿的问题，并引入了设备代码 `OAuth` 来简化无头设备上的 **SpaceXAI** 登录验证。

相关链接：
- [https://github.com/openclaw/openclaw/releases/tag/v2026.5.20](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20)

---

## [Claude Code 预告升级 /usage 命令支持分类查看 Token 明细](https://x.com/bcherny/status/2057476878110261587) `#14`
> **Anthropic** 预告 `Claude Code` 下一版本将升级 `/usage` 命令，支持按 `Skills`、`Agents`、`MCPs` 和 `Plugins` 分类查看 `Token` 消耗明细，同时将登陆 `Desktop` 端。

**Anthropic** 工程师 **Boris Cherny** 预告 **Claude Code** 下一版本将升级 `/usage` 命令，支持按 `Skills`、`Agents`、`MCPs` 和 `Plugins` 分类展示 `Token` 消耗明细，并已新增 `MCP` 支持。

该功能聚合所有会话数据，可按天或按周筛选，统计方式会将下游 `tokens` 归因到对应的 `skill`、`plugin` 或 `MCP`。目前该功能已在 `CLI` 端可用，即将上线 `Desktop` 端，数据暂未通过 `API` 向第三方工具开放。

同期，`Claude Code v2.1.147` 已发布，引入默认关闭的 `Workflow` 工具用于确定性多智能体编排，并将 `/simplify` 命令重命名为 `/code-review`。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/b25b5df7-992b-4d82-9162-97d0d81c25b9/m001.png)

相关链接：
- [https://x.com/bcherny/status/2057476878110261587](https://x.com/bcherny/status/2057476878110261587)
- [https://github.com/anthropics/claude-code/releases/tag/v2.1.147](https://github.com/anthropics/claude-code/releases/tag/v2.1.147)

---

## [OpenAI推出ChatGPT for PowerPoint测试版](https://chatgpt.com/apps/powerpoint/) `#15`
> **OpenAI**推出`ChatGPT` for **PowerPoint**测试版插件，支持在**PPT**内直接创建、编辑幻灯片及生成图像，现已面向全球多数用户开放。

**OpenAI**官方宣布推出“`ChatGPT for PowerPoint`”加载项测试版，用户可直接在 **PowerPoint** 中调用 `ChatGPT` 创建、编辑演示文稿及生成图像。

该工具不仅能基于文档或提示词生成新幻灯片，还能分析现有内容结构、提取关键信息并保持幻灯片可编辑状态。

目前该功能已面向全球的 `ChatGPT Free`、`Plus`、`Pro`、`Business`、`Enterprise` 及 `Edu` 等各级别用户开放，用户需通过 **Office** 加载项商店安装并登录 **OpenAI** 账号使用。

相关链接：
- [https://chatgpt.com/apps/powerpoint/](https://chatgpt.com/apps/powerpoint/)

---

## [MiniMax Agent 集成 Perplexity Search](https://x.com/MiniMaxAgent/status/2057491132133904739) `#16`
> **MiniMax Agent** 官方宣布已集成并上线 `Perplexity AI Search`。官方数据显示，该搜索方案较原默认服务总成本降低 **27%**，且通过率提升 **2%**。

**MiniMax Agent** 现已集成并上线 **Perplexity AI Search**。

官方称在 **700 多个** `Agent` 任务的基准测试中，**Perplexity** 提供了最佳的答案质量与片段密度。

与之前的默认服务 **Serper** 相比，新集成使总成本降低 **27%**，工具调用次数减少 **45%**，`Token` 使用量下降 **42%**，且通过率提升 **2%**。

官方指出，高质量的搜索片段能提供更好的基础，从而有效减少 `Agent` 工作流中的循环搜索次数。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/6b57109e-32fb-4755-98b0-96828d64219a/m001.png)

相关链接：
- [https://x.com/MiniMaxAgent/status/2057491132133904739](https://x.com/MiniMaxAgent/status/2057491132133904739)

---

## [CapCut 宣布与 Gemini App 达成集成合作](https://x.com/capcutapp/status/2057340757896216641) `#17`
> **剪映国际版** **CapCut** 官方宣布正与 **Gemini App** 建立合作，用户不久后将能在 **Gemini** 应用内直接使用 **CapCut** 的高级功能编辑图片和视频。

**剪映国际版** **CapCut** 官方发文确认与 **Gemini App** 达成合作。

集成完成后，用户不久后将能够直接在 `Gemini` 应用内调用 **CapCut** 的高级创作与编辑能力来处理图片和视频。

**CapCut** 表示，随着工作流变得更加无缝，未来的创作将更具对话性、直观性且实现跨工具智能整合。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/12cc53cb-3789-4f9f-9390-bc74490c0096/m001.png)

相关链接：
- [https://x.com/capcutapp/status/2057340757896216641](https://x.com/capcutapp/status/2057340757896216641)

---

## [Modal 完成 3.55 亿美元 C 轮融资，投后估值达 46.5 亿美元](https://modal.com/blog/modal-series-c) `#18`
> 云平台 `Modal` 宣布完成 **3.55 亿美元** `C 轮`融资，投后估值达 **46.5 亿美元**。官方称其年化收入已超 **3 亿美元**，未来将重点扩展 `大规模低延迟推理`与 `Agent 计算层`。

官方宣布，为 **AI** 工作负载构建云平台的 **Modal** 完成 **3.55 亿美元** C 轮融资，投后估值达 **46.5 亿美元**。

本轮融资由 `General Catalyst` 和 `Redpoint` 领投。

官方称，自去年九月以来其业务增长五倍，年化收入已超过 **3 亿美元**。且平台已累计启动超 **10 亿个** 用于运行 `AI` 代码的隔离环境。

该公司计划利用新资金推进大规模低延迟推理、强化学习循环整合以及构建 `Agent` 计算层。并将通过推出细粒度 `RBAC` 来安全赋能 `Agent` 开发。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/b939e2f7-928f-4459-9fb5-6f73ab5cccd1/778900f0-a12b-4535-8e4f-cef24a0dafa9/m001.png)

相关链接：
- [https://modal.com/blog/modal-series-c](https://modal.com/blog/modal-series-c)

---

## 消息称月之暗面启动拆除VIE架构 冲刺赴港IPO `#19`
> 据报道，**月之暗面**完成**20亿美元**新一轮融资后，已正式通知股东启动拆除 `VIE` 及 `红筹架构`，旨在为赴港 `IPO` 扫清障碍，其投后估值已突破**200亿美元**。

据媒体报道，**月之暗面**在完成**20亿美元**新融资后，已正式向股东发出通知启动架构重组。核心动作是拆除现有的`VIE`及`红筹架构`，以期为赴**香港证券交易所**IPO 扫清监管障碍。

据知情人士透露，该公司计划解散相关离岸实体并建立合资企业结构，从而在合规的同时保留外资投资者权益。

在资本层面，**月之暗面**过去**6个月**累计融资约**39亿美元**，投后估值突破**200亿美元**。而在业务端其年度经常性收入也已突破**2亿美元**。

---

## [Anthropic被曝正与Microsoft洽谈租用Maia 200芯片](https://www.theverge.com/ai-artificial-intelligence/935688/anthropic-is-in-talks-to-use-microsofts-ai-chips-too) `#20`
> 据报道，**Anthropic**正在与**Microsoft**进行早期洽谈，拟租用**Microsoft**尚未向外部客户开放的定制`AI芯片``Maia 200`，但双方目前尚未签署最终协议。

据 **The Information** 等媒体报道，**Anthropic** 正与 **Microsoft** 进行早期洽谈。

拟在 `Azure` 上部署 **Microsoft** 的自研 `AI 芯片` `Maia 200`。该芯片旨在高效运行如 `Claude` 等已有模型。

但 **Microsoft** 至今未将其开放给 `Azure` 客户，仅用于自有数据中心。

若最终敲定租用，这将是 **Microsoft** 自研芯片在外部云客户中的一次重要突破。

目前谈判仍处早期阶段，知情人士称尚未达成任何承诺。

相关链接：
- [https://www.theverge.com/ai-artificial-intelligence/935688/anthropic-is-in-talks-to-use-microsofts-ai-chips-too](https://www.theverge.com/ai-artificial-intelligence/935688/anthropic-is-in-talks-to-use-microsofts-ai-chips-too)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。