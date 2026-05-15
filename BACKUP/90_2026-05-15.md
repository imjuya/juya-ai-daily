# [2026-05-15](https://github.com/imjuya/juya-ai-daily/issues/90)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260515/202605150841510351081fb4_cover_90e8.png)

# AI 早报 2026-05-15

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV11X5h6MEfm) ｜ [YouTube](https://www.youtube.com/watch?v=hvhQ_T-7r1A)

## 概览
### 要闻
- ChatGPT 移动应用上线 Codex 远程控制功能 [↗](https://openai.com/index/work-with-codex-from-anywhere/) `#1`
### 模型发布
- 蚂蚁百灵正式开源 Ring-2.6-1T [↗](https://huggingface.co/inclusionAI/Ring-2.6-1T) `#2`
### 开发生态
- Cline 开源 Cline SDK 并重构底层架构，推出 Cline 2.0 [↗](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime) `#3`
- GitHub 推出原生桌面应用 GitHub Copilot app 技术预览版 [↗](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/) `#4`
- SpaceXAI推出编程Agent工具Grok Build早期测试版 [↗](https://x.ai/cli) `#5`
- Kimi 发布 WebBridge 扩展，支持第三方 Agent [↗](https://www.kimi.com/features/webbridge) `#6`
- OpenClaw 更新 2026.5.12 版 [↗](https://github.com/openclaw/openclaw/releases/tag/v2026.5.12) `#7`
- Hermes Agent 集成 Codex App-Server Runtime [↗](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime) `#8`
- Nous Portal 携手 Novita Labs 限时提供免费 DeepSeek V4 Flash [↗](https://x.com/Teknium/status/2055051368055046617) `#9`
- OpenCode 宣布 Qwen 3.6 Plus 再次免费开放 [↗](https://x.com/opencode/status/2055068702538612784) `#10`
### 行业动态
- Anthropic 联手盖茨基金会投入 2 亿美元推进 AI 公益 [↗](https://www.anthropic.com/news/gates-foundation-partnership) `#11`
- Cerebras以每股185美元完成IPO并正式挂牌交易 [↗](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering) `#12`
- 初创公司 Recursive 完成 6.5 亿美元融资 [↗](https://www.nytimes.com/2026/05/13/technology/recursive-superintelligence-funding-ai.html) `#13`
### 前瞻与传闻
- 据报道Apple批评欧盟协助AI对手访问Google服务的措施 [↗](https://www.reuters.com/sustainability/boards-policy-regulation/apple-criticises-eu-measures-help-ai-rivals-access-google-services-2026-05-13/) `#14`
- 消息称 OpenAI 拟因合作未达预期起诉 Apple [↗](https://techcrunch.com/2026/05/14/openai-is-reportedly-preparing-legal-action-against-apple-it-wouldnt-be-the-first-partner-to-feel-burned) `#15`
- 消息称 Microsoft 要求内部团队停用 Claude Code 转向 Copilot CLI [↗](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) `#16`
- 报道称美国批准向10家中国企业出售英伟达H200芯片但尚未交付 [↗](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/) `#17`

---

## [ChatGPT 移动应用上线 Codex 远程控制功能](https://openai.com/index/work-with-codex-from-anywhere/) `#1`
> **OpenAI** 宣布在 **ChatGPT** 移动应用中推出 `Codex` 预览版。该功能现已面向 **iOS** 和 **Android** 平台的所有用户开放，允许其通过手机远程监控和管理运行在本地计算机或开发机上的 `Codex` 任务，不过目前仅支持连接 **macOS** 端 `Codex` 应用。此外，官方还宣布正式上线 `Remote SSH` 和 `Hooks` 等功能。

**OpenAI** 宣布将编程工具 `Codex` 引入 **ChatGPT** 移动应用，目前该功能已处于预览状态并面向所有套餐（含免费版与 Go 套餐）的 **iOS** 和 **Android** 用户开放。

用户可通过手机端实时查看跨线程的工作状态、审查代码差异与测试结果、批准指令或更改模型，而真实的开发环境、文件与凭证仍保留在本地或远程计算机上。

底层通信通过安全中继层跨设备同步状态，但目前手机端仅支持连接 **macOS** 上的 `Codex` 应用，**Windows** 平台的支持即将推出。

此外，官方还宣布 **Remote SSH** 和 `Hooks` 功能正式可用，并推出了面向企业团队的编程访问令牌及本地环境的 **HIPAA** 合规支持。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/760fb3eb-5fe3-4f51-8da3-6bab6f357b0e/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/760fb3eb-5fe3-4f51-8da3-6bab6f357b0e/m002.gif)

相关链接：
- [https://openai.com/index/work-with-codex-from-anywhere/](https://openai.com/index/work-with-codex-from-anywhere/)
- [https://x.com/OpenAI/status/2055016850849993072](https://x.com/OpenAI/status/2055016850849993072)

---

## [蚂蚁百灵正式开源 Ring-2.6-1T](https://huggingface.co/inclusionAI/Ring-2.6-1T) `#2`
> **蚂蚁百灵团队**宣布正式开源其此前发布的万亿参数旗舰思考模型 `Ring-2.6-1T`。该模型已在 **Hugging Face** 及 **ModelScope** 提供下载。

**蚂蚁集团** **百灵团队**宣布正式开源其此前发布的万亿参数旗舰思考模型 `Ring-2.6-1T`，现已面向开发者等群体在 **Hugging Face** 和 **ModelScope** 上线。

该模型专为真实复杂任务场景设计，核心从“回答”升级为“执行”，重点增强了多步骤任务与工具协作等 **Agent** 执行能力。

并引入了支持 high 与 xhigh 两个档位的 `Reasoning Effort` 机制。**蚂蚁集团**称该模型在 **PinchBench** 等多个基准测试中达到 **SOTA** 水平。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/b701c5b4-e828-4c9b-88c9-912521bb174a/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/b701c5b4-e828-4c9b-88c9-912521bb174a/m002.png)

相关链接：
- [https://huggingface.co/inclusionAI/Ring-2.6-1T](https://huggingface.co/inclusionAI/Ring-2.6-1T)
- [https://modelscope.cn/models/inclusionAI/Ring-2.6-1T](https://modelscope.cn/models/inclusionAI/Ring-2.6-1T)

---

## [Cline 开源 Cline SDK 并重构底层架构，推出 Cline 2.0](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime) `#3`
> **Cline** 宣布推出并开源 **`Cline SDK`**，将核心 **Agent** 运行时抽象为独立的可插拔框架，并基于此推出 **Cline 2.0**。目前其 **CLI** 和看板应用已迁移至该 **`SDK`**，IDE 扩展正处于迁移过程中。

**Cline** 官方宣布推出并开源 `Cline SDK`，将原本内置于 `VS Code` 扩展中的核心 `Agent` 运行时剥离，重塑为分层、模块化的独立架构。

基于该 SDK 构建的 **Cline 2.0** 改变了运行时的设计逻辑，使得长时间运行的任务不再因 UI 重启而中断，且具备更好的持久性与跨平台移植能力。

该框架在运行时层原生支持插件系统、多种 `LLM` 提供商接入、定时任务以及无需额外编排层的 `Agent Teams` 多智能体协作，同时内置了对 `MCP` 连接器的支持。

目前，**Cline CLI** 和看板应用已基于该 SDK 完成重构，`VS Code` 和 `JetBrains` 扩展正在迁移中。

此外，升级后的 **Cline CLI** 引入了实验性的连接器通道，用户可通过交互式向导将 `Agent` 接入 `WhatsApp` 和 `Slack` 等平台。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/8fe015f5-ee38-442d-b7a2-203f14a380d3/m001.png)

相关链接：
- [https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime)

---

## [GitHub 推出原生桌面应用 GitHub Copilot app 技术预览版](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/) `#4`
> **GitHub** 宣布推出原生桌面应用 **`GitHub Copilot app`** 技术预览版，目前 **Copilot Pro** 和 **Pro+** 订阅用户可注册抢先体验。

**GitHub** 官方宣布其原生桌面应用 `GitHub Copilot app` 进入技术预览阶段。

该工具允许开发者基于 **GitHub** 上的 issue、pull request 等上下文直接启动 `Agentic` 开发，并在拥有专属分支、文件和对话的独立空间内进行隔离工作。

开发者能够在应用内审查代码变更、通过集成终端验证结果，并直接发起 pull request，还能利用 `Agent Merge` 自动处理后续审查与检查。

目前 `Copilot Pro` 和 `Pro+` 订阅用户可以注册参与抢先体验；`Copilot Business` 和 `Enterprise` 订阅用户将在**本周内**逐步获得访问权限。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/66256d42-6c18-4e8b-ad1a-c5615c6fb9e6/m001.png)

相关链接：
- [https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/)

---

## [SpaceXAI推出编程Agent工具Grok Build早期测试版](https://x.ai/cli) `#5`
> **SpaceXAI**宣布推出 CLI 编程工具 **Grok Build** 早期测试版，集成原生 `subagent` 视图、全屏终端 UI 及 `ACP` 集成等功能，目前仅面向 **SuperGrok Heavy** 订阅用户开放。

**SpaceXAI** 官方发布了名为 **Grok Build** 的 `Agentic` 命令行工具早期测试版，用于编写代码、构建应用及自动化工作流。

该工具提供支持鼠标交互的全屏终端 UI、用于并行处理任务的 `subagent` 视图、无头模式以及 `Agent Client Protocol` 集成。并且零配置完全兼容 `Claude Code` 的插件与配置。

目前该工具仅限 **SuperGrok Heavy** 订阅用户使用，**SpaceXAI** 官方表示将通过此次测试收集反馈以改进模型与产品。

部分社区用户在社交媒体上对高达 **300 美元** 每月的订阅门槛表达了不满，希望能向更低级别的订阅者或 API 用户开放测试权限。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260515/20260515075629_4f667e436a.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/73aa104e-9061-4fd5-b231-d7aa7ee0e51b/m002.png)

相关链接：
- [https://x.ai/cli](https://x.ai/cli)
- [https://docs.x.ai/build/overview](https://docs.x.ai/build/overview)

---

## [Kimi 发布 WebBridge 扩展，支持第三方 Agent](https://www.kimi.com/features/webbridge) `#6`
> **Kimi** 正式宣布推出名为"**Kimi WebBridge**"的浏览器扩展，使 `AI Agent` 能接管浏览器自动执行点击与填写等任务。该工具支持 `Kimi Claw Desktop`，也兼容 `Claude Code` 等第三方 Agent。

**Kimi** 正式发布浏览器扩展 **`Kimi WebBridge`**，允许 AI Agent 在用户的浏览器中自动执行点击、导航、输入和提取等繁琐任务。

该扩展通过本地服务与 **`Chrome DevTools Protocol`** 结合运行，确保登录会话和页面内容等数据完全留在本地设备。

目前，用户可通过 **Kimi** 官网或 Chrome Web Store 下载该工具，它不仅支持 **`Kimi Claw Desktop`**，还兼容 **`Claude Code`**、**`Cursor`**、**`Codex`** 和 **`Hermes`** 等多种第三方 Agent。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/b1b262d4-9cce-4f0b-92f5-42903e81bd14/m001.gif)

相关链接：
- [https://www.kimi.com/features/webbridge](https://www.kimi.com/features/webbridge)

---

## [OpenClaw 更新 2026.5.12 版](https://github.com/openclaw/openclaw/releases/tag/v2026.5.12) `#7`
> `OpenClaw` 发布 **2026.5.12** 版本，重点优化了安装体积、运行时容错以及与 `OpenAI` 的集成体验。

**OpenClaw** 正式发布 **2026.5.12** 版本，重点优化了安装体积、运行时容错以及与 **OpenAI** 的集成体验。

该版本将 **OpenAI** 设置默认为 `ChatGPT/Codex` 登录，引入 `ACP` 备用运行时回退机制以应对停滞的流式响应。

为了支持更精简的安装，**WhatsApp**、**Slack** 及 **Amazon Bedrock** 等依赖已移出核心运行时。

此外，**Tg** 渠道获得了隔离轮询和 **HTML** 格式支持。系统安全性也通过沙箱绑定和凭据管理的强化而显著提升。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260515/20260515073444_714598f140.png)

相关链接：
- [https://github.com/openclaw/openclaw/releases/tag/v2026.5.12](https://github.com/openclaw/openclaw/releases/tag/v2026.5.12)

---

## [Hermes Agent 集成 Codex App-Server Runtime](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime) `#8`
> **Hermes Agent** 推出可选的 `Codex App-Server Runtime` 测试功能。该功能允许 **Hermes** 在处理 `openai/*` 和 `openai-codex/*` 模型轮次时，将其交给 `Codex CLI app-server` 执行。

Nous Research 旗下 **Hermes Agent** 新增可选的 `Codex App-Server Runtime` 集成。

开启该功能后，**Hermes** 会将 **OpenAI** 模型的轮次交由 `Codex CLI app-server` 处理。用户无需 API 密钥即可使用 **ChatGPT** 订阅额度，并直接调用 `Codex` 内置的终端命令、文件编辑、沙盒隔离及原生插件。

**Hermes** 自身的浏览器自动化、视觉分析等高级工具通过 MCP 回调机制保持可用。但 `delegate_task`、`memory` 等依赖内部上下文的工具在此运行时下暂不可用。

该功能目前为 **Opt-in Beta** 状态，需安装 **0.130.0** 或更高版本的 `Codex CLI` 并完成单独授权。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/90e81afc-6728-453d-a197-6f07d1106de1/1e920e9c-1735-4323-8385-5b5ebc636b60/m001.png)

相关链接：
- [https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime)
- [https://x.com/NousResearch/status/2054958564951912714](https://x.com/NousResearch/status/2054958564951912714)

---

## [Nous Portal 携手 Novita Labs 限时提供免费 DeepSeek V4 Flash](https://x.com/Teknium/status/2055051368055046617) `#9`
> Nous Research 宣布，得益于 Novita Labs 支持，`DeepSeek V4 Flash` 现已在 **Nous Portal** 限时免费提供。

**Nous Research**宣布，`DeepSeek V4 Flash` 模型现已登陆 **Nous Portal** 平台。

得益于 **Novita Labs** 的支持，该模型目前正通过 **Nous Portal** 的免费层级向用户限时免费开放。

用户只需注册相关免费层级，即可直接在 `Hermes Agent` 中调用该模型。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260515/20260515072602_63a6646eca.png)

相关链接：
- [https://x.com/Teknium/status/2055051368055046617](https://x.com/Teknium/status/2055051368055046617)

---

## [OpenCode 宣布 Qwen 3.6 Plus 再次免费开放](https://x.com/opencode/status/2055068702538612784) `#10`
> **OpenCode** 官方宣布 **Qwen 3.6 Plus** 模型再次面向用户免费开放。

**OpenCode** 官方宣布 **`Qwen 3.6 Plus`** 模型在其平台上再次免费提供。

此前，由于用户大量消耗平台算力，该模型的免费服务曾受到限制。

目前，**OpenCode** 团队已找到并扩充了更多的 GPU 资源，以支持本次的“第二轮”免费活动。

用户现可继续在平台上免费使用该模型。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260515/20260515082737_8e01242122.png)

相关链接：
- [https://x.com/opencode/status/2055068702538612784](https://x.com/opencode/status/2055068702538612784)

---

## [Anthropic 联手盖茨基金会投入 2 亿美元推进 AI 公益](https://www.anthropic.com/news/gates-foundation-partnership) `#11`
> **Anthropic** 宣布与**盖茨基金会**合作，未来四年将投入 **2 亿美元**资金、`Claude`额度及技术支持，以推进全球健康、生命科学、教育及经济流动性项目。

**Anthropic** 官方宣布与**盖茨基金会**建立合作伙伴关系，承诺在未来四年内共同投入 **2 亿美元**的赠款、`Claude` 使用额度以及技术支持。

该合作由 **Anthropic** 的 `Beneficial Deployments` 团队牵头，重点聚焦全球健康与生命科学、教育以及经济流动性三大领域。项目将在美国及全球范围内与多方合作实施。

作为合作的一部分，**Anthropic** 将开发相关的连接器、基准测试和公共数据集，并把针对农业等特定领域的改进工具作为公共产品公开发布。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260515/20260515074436_398cd706f5.png)

相关链接：
- [https://www.anthropic.com/news/gates-foundation-partnership](https://www.anthropic.com/news/gates-foundation-partnership)
- [https://www.gatesfoundation.org/ideas/media-center/press-releases/2026/05/ai-anthropic-partnership](https://www.gatesfoundation.org/ideas/media-center/press-releases/2026/05/ai-anthropic-partnership)

---

## [Cerebras以每股185美元完成IPO并正式挂牌交易](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering) `#12`
> 芯片公司 **Cerebras Systems** 以每股 **185 美元** 的价格完成首次公开募股并登陆纳斯达克。据媒体报道，该股首日开盘价飙升至 **350 美元**，较发行价大涨 **89%**。

**Cerebras Systems** 官方宣布以每股 **185** 美元的价格发行 **3000** 万股 `A 类普通股`，成功筹集 **55.5** 亿美元资金。

股票已在纳斯达克全球精选市场开始交易。据报道，受市场对人工智能概念股的狂热追捧，该股首日开盘价飙升至 **350** 美元，较发行价上涨 **89%**。

基于开盘价计算的彻底稀释后估值达到 **1067.5** 亿美元。

相关链接：
- [https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering)
- [https://www.reuters.com/legal/transactional/cerebras-set-debut-stock-market-gripped-by-ai-mania-2026-05-14/](https://www.reuters.com/legal/transactional/cerebras-set-debut-stock-market-gripped-by-ai-mania-2026-05-14/)
- [https://techcrunch.com/2026/05/14/cerebras-raises-5-5b-kicking-off-2026s-ipo-season-with-a-bang](https://techcrunch.com/2026/05/14/cerebras-raises-5-5b-kicking-off-2026s-ipo-season-with-a-bang)

---

## [初创公司 Recursive 完成 6.5 亿美元融资](https://www.nytimes.com/2026/05/13/technology/recursive-superintelligence-funding-ai.html) `#13`
> 由 **田渊栋** 与 **Richard Socher** 等人联合创办的 **Recursive Superintelligence** 宣布获 **6.5 亿美元** 融资，该公司致力于构建无需人类干预即可持续自我优化的递归式超级智能系统。

**Recursive Superintelligence** 正式亮相并宣布完成 **6.5 亿美元** 融资，估值据报达 **46.5 亿美元**。

该公司由 **8** 位来自 **Meta**、`OpenAI` 和 `DeepMind` 等机构的研究者联合创办。核心成员包括 **Richard Socher**、**田渊栋**、**施天麟** 及 **Tim Rocktäschel**。

团队计划利用“开放式演化”技术，构建能够自动发现弱点并持续优化自身的递归式超级智能系统。据联合创始人透露，其研发将首先聚焦“**AI** 改进 **AI**"，并预计在数季度内推出首批产品。

相关链接：
- [https://www.nytimes.com/2026/05/13/technology/recursive-superintelligence-funding-ai.html](https://www.nytimes.com/2026/05/13/technology/recursive-superintelligence-funding-ai.html)

---

## [据报道Apple批评欧盟协助AI对手访问Google服务的措施](https://www.reuters.com/sustainability/boards-policy-regulation/apple-criticises-eu-measures-help-ai-rivals-access-google-services-2026-05-13/) `#14`
> 据路透社报道，**Apple** 批评欧盟拟议的帮助 **AI** 竞争对手访问 **Google** 服务的措施，警告此举将引发严重的隐私与安全风险。

据**路透社**报道，**Apple**呼应了**Google**的立场，公开批评欧盟反垄断监管机构拟议的草案措施，反对其强制要求**Google**协助`AI`竞争对手访问其服务以遵守《数字市场法》。

**Apple**警告称，允许第三方`AI`服务与系统应用深度交互将对用户隐私、安全性及设备性能构成深远风险。该公司还强烈质疑欧盟委员会的技术专长，批评监管机构仅基于不到三个月的工作就试图取代**Google**工程师的判断，实质上是在重新设计操作系统。

由于自身同样面临欧盟要求开放生态系统的压力，**Apple**强调此案对其自身的操作系统具有广泛的指示性影响。

相关链接：
- [https://www.reuters.com/sustainability/boards-policy-regulation/apple-criticises-eu-measures-help-ai-rivals-access-google-services-2026-05-13/](https://www.reuters.com/sustainability/boards-policy-regulation/apple-criticises-eu-measures-help-ai-rivals-access-google-services-2026-05-13/)

---

## [消息称 OpenAI 拟因合作未达预期起诉 Apple](https://techcrunch.com/2026/05/14/openai-is-reportedly-preparing-legal-action-against-apple-it-wouldnt-be-the-first-partner-to-feel-burned) `#15`
> 据报道，**OpenAI** 因与 **Apple** 双方于 **2024 年 WWDC** 宣布的 `ChatGPT` 集成合作未达预期，正考虑对其采取法律行动。

据媒体报道，**OpenAI** 正考虑就双方于 **2024 年** **WWDC** 宣布的 **ChatGPT** 集成合作对 **Apple** 采取法律行动。

目前已聘请外部律师事务所研究包括发送正式违约通知在内的选项。报道引述未具名 **OpenAI** 高管称，公司“从产品角度已做了一切”。

但 **Apple** 未能履行协议义务，导致功能被埋没、难以找到。且收入远低于此前预期的 **数十亿美元** 级别。

该高管透露，**Apple** 曾让 **OpenAI** “盲目信任”，但结果并不理想。

相关链接：
- [https://techcrunch.com/2026/05/14/openai-is-reportedly-preparing-legal-action-against-apple-it-wouldnt-be-the-first-partner-to-feel-burned](https://techcrunch.com/2026/05/14/openai-is-reportedly-preparing-legal-action-against-apple-it-wouldnt-be-the-first-partner-to-feel-burned)
- [https://9to5mac.com/2026/05/14/openai-preparing-legal-action-against-apple-over-siri-partnership-report/](https://9to5mac.com/2026/05/14/openai-preparing-legal-action-against-apple-over-siri-partnership-report/)

---

## [消息称 Microsoft 要求内部团队停用 Claude Code 转向 Copilot CLI](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) `#16`
> 据媒体报道，**Microsoft** 要求内部团队在 **6 月底前** 停用 `Claude Code` 并转向 `GitHub Copilot CLI`。另有报道指出，**Microsoft** 构建了让逾百个 `AI Agent` 互相竞争以寻找 **Windows** 漏洞的系统。

据 **The Verge** 报道，**Microsoft** 正在取消内部大部分 `Claude Code` 许可证，要求开发者改用 `GitHub Copilot CLI`。

此次调整主要针对负责 Windows 和 **Microsoft 365** 等产品的体验与设备团队，工程师需在 **6 月**底前完成过渡。

官方内部备忘录称此举旨在整合命令行工具，但消息人士指其同样出于削减新财年运营开支的财务考量。

此外据媒体报道，**Microsoft** 建立了名为 `MDASH` 的系统，利用超过 **100** 个 `AI Agent` 互相竞争挖掘漏洞，近期发现了 **16** 个 Windows 安全漏洞。

相关链接：
- [https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)
- [https://the-decoder.com/microsoft-pits-more-than-100-ai-agents-against-each-other-to-find-windows-vulnerabilities/](https://the-decoder.com/microsoft-pits-more-than-100-ai-agents-against-each-other-to-find-windows-vulnerabilities/)

---

## [报道称美国批准向10家中国企业出售英伟达H200芯片但尚未交付](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/) `#17`
> 据**路透社**报道，**美国政府**已批准向约**10**家**中国公司**出售**英伟达**`H200`芯片，每家获准最高采购**7.5万**枚。但因双方的监管审查与附加条件，目前尚未有任何实际交付，该笔交易仍处于停滞状态。

据**路透社**报道，**美国**已批准包括**阿里巴巴**、**腾讯**、**字节跳动**和**京东**在内的约**10**家中国企业购买**英伟达**`H200`芯片，**联想**和**富士康**也获准成为该芯片的分销商。

根据**美国**许可条款，每位获批客户最高可采购**7.5万**枚芯片，买家可直接向**英伟达**或通过授权分销商购买。

尽管获得美方放行，但截至目前尚未有任何实际交付。交易因有关部门的供应链安全审查以及美方的多项苛刻附加条件而陷入停滞。

**美国**方面要求买家保证芯片不用于军事用途，且**特朗普政府**达成了一项**美国**获得**25%**销售收入的特殊协议，引发了中方对安全漏洞的担忧。

相关链接：
- [https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。