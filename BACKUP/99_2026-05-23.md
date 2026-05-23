# [2026-05-23](https://github.com/imjuya/juya-ai-daily/issues/99)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260523/202605230859395236467639_cover_0d52.png)

# AI 早报 2026-05-23

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV11fGa6KE9y) ｜ [YouTube](https://www.youtube.com/watch?v=48MZ6aXyw2c)

## 概览
### 要闻
- DeepSeek 宣布将 DeepSeek-V4-Pro API 2.5 折优惠转为永久定价 [↗](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) `#1`
### 模型发布
- 智谱发布 GLM-5.1-HighSpeed，官方称速度达 400 tokens/s [↗](https://mp.weixin.qq.com/s/FJn5athj8G4y2narTzMSyA) `#2`
- Qwen3.7-Max 上线千问，阿里云百炼提供限时优惠 [↗](https://mp.weixin.qq.com/s/eBQwL51ahGU2OgSuaYPGmQ) `#3`
- OpenBMB 开源基于昇腾 910B 原生训练的 BitCPM-CANN 模型 [↗](https://x.com/OpenBMB/status/2057816337880355220) `#4`
- 网易有道推出Confucius4-TTS，14语言零样本语音克隆引擎即将全量开源 [↗](https://huggingface.co/netease-youdao/Confucius4) `#5`
### 开发生态
- Antigravity 修复 2.0 IDE 争议，翻倍上下文长度并提升配额至 9 倍 [↗](https://x.com/_mohansolo/status/2057969609480032313) `#6`
- Claude Code 的 auto mode 面向 Pro 订阅用户开放 [↗](https://x.com/ClaudeDevs/status/2057946803685974482) `#7`
- Warp 开放免费BYOK功能，支持自定义端点接入 [↗](https://docs.warp.dev/agent-platform/inference/bring-your-own-api-key/) `#8`
- TRAE 中国版上线 Kimi 原生视频理解能力 [↗](https://mp.weixin.qq.com/s/TCkMqQGRoTewiHo6RnfQTw) `#9`
- Perplexity 开源供应链扫描工具 Bumblebee [↗](https://github.com/perplexityai/bumblebee) `#10`
### 技术与洞察
- Anthropic 公布 Project Glasswing 进展，发现逾万高危漏洞 [↗](https://www.anthropic.com/research/glasswing-initial-update) `#11`
- Google DeepMind 发布 AlphaProof Nexus 数学证明框架 [↗](https://arxiv.org/html/2605.22763v1) `#12`
### 行业动态
- 有关部门推进国产大模型适配国产算力芯片 [↗](https://www.ndrc.gov.cn/xwdt/wszb/202605xwfbh/) `#13`
### 前瞻与传闻
- OpenAI 测试 ChatGPT 简化版模型选择器 [↗](https://x.com/adamhfry/status/2057808938024817109) `#14`

---

## [DeepSeek 宣布将 DeepSeek-V4-Pro API 2.5 折优惠转为永久定价](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) `#1`
> **DeepSeek** 宣布将 `` `DeepSeek-V4-Pro` `` 模型 API 现有的 **2.5 折** 优惠转为永久定价，此价格将于原定 **5 月 31 日** 优惠结束后正式生效。

**DeepSeek** 宣布将 `DeepSeek-V4-Pro` 模型 API 的限时 **2.5 折**优惠转为永久正式定价。

新价格定为原定价的 **1/4**，具体费率为每百万 tokens 缓存未命中输入 **3 元**、输出 **6 元**。

以及缓存命中输入 **0.025 元**。该价格将在原定于 **5 月 31 日**结束的优惠活动后正式执行。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260523/20260523083444_6bf00882ba.png)

相关链接：
- [https://api-docs.deepseek.com/zh-cn/quick_start/pricing](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)
- [https://x.com/deepseek_ai/status/2049312932014813344](https://x.com/deepseek_ai/status/2049312932014813344)

---

## [智谱发布 GLM-5.1-HighSpeed，官方称速度达 400 tokens/s](https://mp.weixin.qq.com/s/FJn5athj8G4y2narTzMSyA) `#2`
> **智谱**发布高速版旗舰模型 `GLM-5.1-HighSpeed`，官方称在保留原模型能力下速度达 **400** `tokens/s`，目前仅面向部分企业客户开放。

智谱发布了旗舰模型 `GLM-5.1` 的高速版本 API“**GLM-5.1-highspeed**”。

该版本并非轻量级模型，而是完整保留了原模型的综合能力与 Coding 能力。官方称其输出速度达到 **400 tokens/s**，刷新了当前全球大模型厂商 API 的速度上限。

技术层面，该高速版由**智谱** GLM 团队与**TileRT** 团队联合打造。采用了常驻 `Engine Kernel` 与异构 `Worker` 等系统级优化技术。

目前，该模型仅面向**智谱** **BigModel** 开放平台的部分企业客户定向开放。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/45166f99-6757-4c59-957e-4a3080a542ac/m001.gif)

相关链接：
- [https://mp.weixin.qq.com/s/FJn5athj8G4y2narTzMSyA](https://mp.weixin.qq.com/s/FJn5athj8G4y2narTzMSyA)
- [https://docs.bigmodel.cn/cn/guide/models/text/glm-5.1-highspeed](https://docs.bigmodel.cn/cn/guide/models/text/glm-5.1-highspeed)
- [https://www.tilert.ai/blog/speed-as-the-next-scaling-law.html](https://www.tilert.ai/blog/speed-as-the-next-scaling-law.html)

---

## [Qwen3.7-Max 上线千问，阿里云百炼提供限时优惠](https://mp.weixin.qq.com/s/eBQwL51ahGU2OgSuaYPGmQ) `#3`
> **阿里**宣布旗舰模型 `Qwen3.7-Max`，已接入`千问`多端供免费体验。同时有用户发现， **阿里云百炼**针对该模型提供限时**五折**优惠。

**阿里巴巴**近期发布了全新一代**千问**旗舰模型 `Qwen3.7-Max`。

目前，该模型已正式接入**千问** `APP`（需更新至 `6.9.7` 及以上版本）、`PC` 端以及网页端供用户免费体验。

此外，据用户发现，**阿里云百炼**平台也已上线 `Qwen3.7 Max`，并正处于限时 **5 折**的优惠活动中。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/05ad3a5d-2fb5-4941-b37b-016bd12a544f/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/05ad3a5d-2fb5-4941-b37b-016bd12a544f/m002.png)

相关链接：
- [https://mp.weixin.qq.com/s/eBQwL51ahGU2OgSuaYPGmQ](https://mp.weixin.qq.com/s/eBQwL51ahGU2OgSuaYPGmQ)

---

## [OpenBMB 开源基于昇腾 910B 原生训练的 BitCPM-CANN 模型](https://x.com/OpenBMB/status/2057816337880355220) `#4`
> **OpenBMB** 联合 **面壁智能** 与 **清华大学** 开源了 `BitCPM-CANN` 模型系列。官方称，这是首个在 `华为昇腾 910B` 上完成端到端原生训练的 `1.58-bit` 三值大模型，现已提供 `0.5B` 至 `8B` 规模版本。

**OpenBMB** 联合 **面壁智能** 与 **清华大学** 正式发布并开源了 `BitCPM-CANN` 模型家族，涵盖 `0.5B`、`1B`、`3B` 及 `8B` 多种参数规模。

官方表示，这是业界首个在 **华为** `昇腾 910B NPU` 上完成从量化算子到全栈框架端到端原生训练的 `1.58-bit` 三值模型。

该模型内存占用相比 `BF16` 降低约 **6 倍**，在 **11 项** 基准测试中，`1B` 到 `8B` 模型能保留全精度 `MiniCPM4` 约 **95%** 至 **97%** 的性能，目前已在 **Hugging Face** 和 **ModelScope** 同步上线。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/d2f15925-f4a6-4b44-8306-73a68706ecb3/m001.png)

相关链接：
- [https://x.com/OpenBMB/status/2057816337880355220](https://x.com/OpenBMB/status/2057816337880355220)
- [https://huggingface.co/collections/openbmb/bitcpm4-cann](https://huggingface.co/collections/openbmb/bitcpm4-cann)
- [https://www.modelscope.cn/collections/OpenBMB/BitCPM4-CANN](https://www.modelscope.cn/collections/OpenBMB/BitCPM4-CANN)

---

## [网易有道推出Confucius4-TTS，14语言零样本语音克隆引擎即将全量开源](https://huggingface.co/netease-youdao/Confucius4) `#5`
> **网易有道**近期推出了 `Confucius4-TTS`，能进行 **14** 种语言的 `零样本声音克隆`与`跨语言合成`，据称 **3** 秒复刻原声且准确度超**97%**。模型权重即将发布。

**网易有道**在**GitHub**上开放了`Confucius4-TTS`开源项目，这是一个基于“`语音编码器 `+` 大语言模型”`架构的零样本多语种文语转换系统。

该系统支持`14`种语言，无需参考文本即可进行声音克隆，并可实现不泄露口音的跨语言音色迁移，同时保留说话人情感。

官方表示，在多个公开基准测试中，其零样本能力和合成质量达到业内先进水平；据**官方微信公众号**信息，其声音克隆过程仅需`3`秒，克隆准确度高于`97%`，相似度超过`85%`。

目前，项目代码仓库已公开，但模型权重尚待完全释放，官方提供了在线演示页面供外界试用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/c69b2717-763f-4dba-811f-c317eca6c8df/m001.png)

相关链接：
- [https://huggingface.co/netease-youdao/Confucius4](https://huggingface.co/netease-youdao/Confucius4)
- [https://github.com/netease-youdao/Confucius4-TTS](https://github.com/netease-youdao/Confucius4-TTS)
- [https://confucius4-tts.youdao.com/gradio](https://confucius4-tts.youdao.com/gradio)

---

## [Antigravity 修复 2.0 IDE 争议，翻倍上下文长度并提升配额至 9 倍](https://x.com/_mohansolo/status/2057969609480032313) `#6`
> Antigravity 发布更新，将`Gemini 3.5 Flash`最大上下文长度翻倍，付费订阅每周 `Gemini` 配额提至**九倍**、并重置了额度。同时，新增 `IDE` 打开与安装按钮，修复了 `Windows` 故障，支持一键迁移旧设置。`CLI` 推送新版优化体验。

Antigravity 团队针对近期大量用户反馈进行了密集更新，重点解决了 `IDE` 连接不明与配额限制问题。

官方已将产品内 `Gemini 3.5 Flash` 的最大上下文长度翻倍，并将所有付费计划的每周 `Gemini` 配额在原有基础上两次提升 **3 倍**（累计达 **9 倍**），同时面向所有用户重置了本周配额。

在产品体验方面，`Antigravity 2.0` 澄清并未下线 `IDE` 支持，而是在项目级对话界面的右上角新增了明确的"Open IDE"与"Install IDE"按钮，修复了 `Windows` 端的打开故障，并支持一键迁移旧版设置与扩展。

此外，`Antigravity CLI` 发布了包含身份验证与 `Windows` 体验优化的 `v1.0.1` 版本，官方同时确认将采纳社区建议，后续上线模型思考层级选择器与配额进度条。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260522/20260522192039_edb9712d90.png)

相关链接：
- [https://x.com/_mohansolo/status/2057969609480032313](https://x.com/_mohansolo/status/2057969609480032313)
- [https://x.com/JackWoth98/status/2057924242222575684](https://x.com/JackWoth98/status/2057924242222575684)
- [https://x.com/_mohansolo/status/2057910616153882949](https://x.com/_mohansolo/status/2057910616153882949)

---

## [Claude Code 的 auto mode 面向 Pro 订阅用户开放](https://x.com/ClaudeDevs/status/2057946803685974482) `#7`
> `Claude Code` 的 `auto mode` 现已面向 **Pro** 订阅用户开放，并新增对 `` `Sonnet 4.6` `` 和 `` `Opus 4.7` `` 模型的支持。

**Claude** 开发者账号 **@ClaudeDevs** 宣布 `auto mode` 两项更新：该功能现已面向 `Pro` 计划用户开放。

同时新增对 `Sonnet 4.6` 模型的支持，与 `Opus 4.7` 一同可用。

用户通过 `Shift+tab` 快捷键即可启动 `auto mode`，需运行 `claude update` 或将 `Claude` 桌面应用更新至最新版本。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260523/20260523083103_3f20243fad.png)

相关链接：
- [https://x.com/ClaudeDevs/status/2057946803685974482](https://x.com/ClaudeDevs/status/2057946803685974482)

---

## [Warp 开放免费BYOK功能，支持自定义端点接入](https://docs.warp.dev/agent-platform/inference/bring-your-own-api-key/) `#8`
> 终端工具 **Warp** 宣布向免费计划用户开放自带 `模型密钥` 功能，并全面支持兼容 **OpenAI** `` Chat Completions API `` 的自定义推理端点。

**Warp** 团队宣布推出名为“Bring your own inference”的更新，将自带密钥（BYOK）功能扩展至免费计划用户，并新增对自定义推理端点的支持。

用户现可直接使用 **OpenAI**、**Anthropic** 或 **Google** 的 API key，或通过兼容 `OpenAI Chat Completions API` 的端点接入，以此驱动 **Warp Agent** 体验。

在定价方面，10 人及以下的团队或个人开发者在 **Free**、**Build** 或 **Max** 计划中使用自带推理功能时均不消耗 **Warp credits**；而 10 人以上的企业则需通过 **Business** 或 **Enterprise** 计划，并按 Agent 活跃工作时间消耗较低费率的平台 credits。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/9272e140-7aa5-4412-89f0-d9b23d89d1c3/m001.gif)

相关链接：
- [https://docs.warp.dev/agent-platform/inference/bring-your-own-api-key/](https://docs.warp.dev/agent-platform/inference/bring-your-own-api-key/)
- [https://docs.warp.dev/agent-platform/inference/custom-inference-endpoint/](https://docs.warp.dev/agent-platform/inference/custom-inference-endpoint/)

---

## [TRAE 中国版上线 Kimi 原生视频理解能力](https://mp.weixin.qq.com/s/TCkMqQGRoTewiHo6RnfQTw) `#9`
> **TRAE**中国版内置的 `Kimi-K2.6` 和 `Kimi-K2.5` 模型现已上线原生视频理解能力，可让 `Agent` 直接看懂并解析视频。

**TRAE** 中国版内置的 `Kimi-K2.6/2.5` 模型现已支持原生视频理解能力。

该功能允许用户向 **TRAE** 发送视频路径，由模型直接“看懂”并解析视频内容。进而支持视频动效转前端代码、Bug 视频转修复代码、流程视频转 `RPA` 脚本等应用场景。

目前该能力已面向 **TRAE SOLO** 和 **TRAE IDE** 中国版用户开放。官方同步在**小红书**发起了分享体验赢取 **Labubu** 的活动。

相关链接：
- [https://mp.weixin.qq.com/s/TCkMqQGRoTewiHo6RnfQTw](https://mp.weixin.qq.com/s/TCkMqQGRoTewiHo6RnfQTw)

---

## [Perplexity 开源供应链扫描工具 Bumblebee](https://github.com/perplexityai/bumblebee) `#10`
> **Perplexity** 宣布开源内部安全工具 `Bumblebee`，这是一款针对 `macOS` 和 `Linux` 开发终端的只读扫描器，已在 **GitHub** 发布，暂不支持 `Windows`。

**Perplexity** 官方宣布开源其内部安全工具 **Bumblebee**，这是一款专为 `macOS` 和 `Linux` 开发者终端设计的只读供应链扫描器。

该工具能直接读取锁文件和清单等磁盘元数据，在发生安全事件时精准匹配并排查存在风险的语言开发包、`MCP` 配置以及各类编辑器和浏览器扩展。

为避免触发恶意代码执行，**Bumblebee** 在扫描过程中不调用包管理器、不执行代码也不读取源文件，严格保持只读特性。

目前该工具已在 **GitHub** 以 `Go` 语言静态单文件形式发布，用户可结合自定义风险目录用于日常盘点或应急响应。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/807b1338-16d0-4d4d-9d47-a13af3adffe8/m001.png)

相关链接：
- [https://github.com/perplexityai/bumblebee](https://github.com/perplexityai/bumblebee)
- [https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee](https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee)

---

## [Anthropic 公布 Project Glasswing 进展，发现逾万高危漏洞](https://www.anthropic.com/research/glasswing-initial-update) `#11`
> **Anthropic** 公布 `Project Glasswing` 进展，宣称 `Claude Mythos Preview` 在关键软件及开源项目中已发现超一万个高危或严重漏洞。

Anthropic 发布了 AI 网络安全倡议 **Project Glasswing** 的初步更新，过去一个月与约 **50** 家合作伙伴利用未公开模型 `Claude Mythos Preview` 进行安全测试。

官方数据显示，该模型在关键软件中发现了超过 **一万个** 高危或严重级别的漏洞，并在一千多个开源项目中估计发现六千余个此类漏洞，其中经独立机构评估确认为真实漏洞的比例达 **90.6%**。

由于目前尚无足够强大的安全防护措施来防止此类高能力模型被滥用，Mythos 级模型暂不向公众发布。为应对行业修补漏洞的瓶颈，官方现已面向企业客户推出 `Claude Security` 公开测试版，并开始应要求向符合条件的客户提供内部漏洞扫描工具集。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/bffbc55d-df6d-4a01-b3b1-4a99049249ab/m001.png)

相关链接：
- [https://www.anthropic.com/research/glasswing-initial-update](https://www.anthropic.com/research/glasswing-initial-update)

---

## [Google DeepMind 发布 AlphaProof Nexus 数学证明框架](https://arxiv.org/html/2605.22763v1) `#12`
> **Google DeepMind** 推出 `AlphaProof Nexus` 框架，通过结合 `大型语言模型` 与 `Lean` 编译器进行数学形式化证明搜索。相关证明结果及代码已在 `GitHub` 公开。

**Google DeepMind** 开发了名为 **AlphaProof Nexus** 的数学证明框架，该框架结合 `大型语言模型` 与 `Lean` 形式化验证工具。

在测试中，其全功能 Agent 自主解决了 **9** 个 **Erdős** 开放问题，证明了 **44** 个 **OEIS** 猜想。并解决了优化论和代数几何等领域的多个开放性问题。

该系统通过 `LLM` 生成证明代码并由 `Lean` 编译器验证的循环机制运行。研究团队已将成功生成的证明发布在 `GitHub` 仓库中。

虽然基础的 `LLM Agent` 在事后分析中也解决了同样的 **Erdős** 问题，但全功能 Agent 在处理复杂难题时表现出更高的成本效益。

相关链接：
- [https://arxiv.org/html/2605.22763v1](https://arxiv.org/html/2605.22763v1)
- [https://github.com/google-deepmind/alphaproof-nexus-results](https://github.com/google-deepmind/alphaproof-nexus-results)

---

## [有关部门推进国产大模型适配国产算力芯片](https://www.ndrc.gov.cn/xwdt/wszb/202605xwfbh/) `#13`
> 据报道，**有关部门**表示，正指导`国产大模型`适配`国产算力芯片`，谋划出台加快“`人工智能+`”落地配套文件，并推动`央国企`开放高价值应用场景。

**有关部门**在近期新闻发布会上表示，将推动人工智能与各行业深度融合，指导国产大模型加大力度适配国产算力芯片以确保自主可控。

目前**有关部门**已出台制造、医疗等十多个行业的“人工智能+”政策，正在谋划进一步落地的配套文件，并将持续推动`央国企`开放高价值应用场景。

在基础设施和资金支持上，将加快`具身智能`训练设施建设，把科技再贷款额度扩大至**1.2万亿元**覆盖人工智能等领域，并启动集成电路企业税收优惠清单制定。

此外，**有关部门**明确否认网传“要求高科技企业不得接受美国资本投资”的消息，强调从未限制科技企业接受合法外商投资。

相关链接：
- [https://www.ndrc.gov.cn/xwdt/wszb/202605xwfbh/](https://www.ndrc.gov.cn/xwdt/wszb/202605xwfbh/)

---

## [OpenAI 测试 ChatGPT 简化版模型选择器](https://x.com/adamhfry/status/2057808938024817109) `#14`
> **OpenAI** 正在 **ChatGPT** 网页端测试名为 "Intelligence" 的简化版 `模型选择器`，将原有的 `模型` 与 `推理档位` 精简为 `四个选项`。**官方**确认会在全面推出前添加 `设置`，允许用户恢复指定常用的 **Pro** 选项。

**OpenAI** 正在 **ChatGPT** 网页端进行小规模 `A/B 测试`，推出名为 "**Intelligence Picker**" 的简化版模型选择界面。

该界面将原本包含 Instant、Thinking (Light, Standard, Extended, Heavy) 和 Pro (Standard, Extended) 的 **7** 个复杂档位，精简为 Instant、Medium、High 和 Pro 四个直接选项。

针对社区对失去手动选择能力的担忧，**OpenAI** 官方确认其意图并非移除模型指定功能，并承诺在全面推出该界面前添加设置项，让用户能够恢复设置最常用的 Pro 选项。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/0d522b2d-3341-4531-be03-d46e5a2cef2d/43f27d3f-a843-4fe9-b880-77370790c3fd/m001.png)

相关链接：
- [https://x.com/adamhfry/status/2057808938024817109](https://x.com/adamhfry/status/2057808938024817109)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。