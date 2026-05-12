# [2026-05-12](https://github.com/imjuya/juya-ai-daily/issues/87)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260512/20260512084025312668546c_cover_d84f.png)

# AI 早报 2026-05-12

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1qn5P6LEXS) ｜ [YouTube](https://www.youtube.com/watch?v=QlCIM_GQzJo)

## 概览
### 要闻
- Claude Code 上线 Agent view 功能并新增 /goal 指令 [↗](https://claude.com/blog/agent-view-in-claude-code) `#1`
### 模型发布
- Thinking Machines Lab 发布实时多模态“交互模型” TML-Interaction-Small [↗](https://thinkingmachines.ai/blog/interaction-models/) `#2`
- OpenBMB 发布开源多模态模型 MiniCPM-V 4.6 [↗](https://huggingface.co/openbmb/MiniCPM-V-4.6) `#3`
### 开发生态
- Anthropic 推出 Claude Platform on AWS [↗](https://claude.com/blog/claude-platform-on-aws) `#4`
- OpenAI 为 Codex 推出 OpenAI Developers 插件 [↗](https://x.com/OpenAIDevs/status/2053925962287583379) `#5`
- OpenCode 宣布 DeepSeek V4 Flash 开启限时免费 [↗](https://x.com/opencode/status/2053887208688431179) `#6`
- Nous Portal 宣布限时免费提供 Qwen 3.6 Plus 模型 [↗](https://x.com/NousResearch/status/2053876496045920601) `#7`
- Windsurf 面向付费用户将 Kimi K2.6 免费期再延长一个月 [↗](https://x.com/windsurf/status/2053895578946531518) `#8`
### 产品应用
- 千问与淘宝全面打通，开启AI购物体验 [↗](https://mp.weixin.qq.com/s/10VoJmPCkk4yOm2fJLk0EQ) `#9`
- QClaw 发布「文件空间」功能，打通腾讯文档与 ima 知识库 [↗](https://mp.weixin.qq.com/s/AgmVAhSl7BNSGxE0FBqa1g) `#10`
### 技术与洞察
- Artificial Analysis 发布 Coding Agent Index 评测模型与工具组合 [↗](https://artificialanalysis.ai/agents/coding-agents) `#11`
- Google 发布报告称首次发现攻击者利用 AI 开发零日漏洞 [↗](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) `#12`
### 行业动态
- OpenAI 推出 Daybreak 网络安全愿景 [↗](https://openai.com/daybreak/) `#13`
- OpenAI 成立 OpenAI Deployment Company [↗](https://openai.com/index/openai-launches-the-deployment-company/) `#14`
- MiniMax 发起 10x Team 计划招募行业专家 [↗](https://mp.weixin.qq.com/s/G3m2xksI2jHAROhNdP7x2Q) `#15`
- Qwen 官宣全球 Ambassador 计划并招募开发者与活动大使 [↗](https://qwen.ai/ambassador) `#16`
- Unsloth 宣布正式加入 PyTorch 生态 [↗](https://unsloth.ai/blog/pytorch) `#17`
### 前瞻与传闻
- 消息称快手计划分拆可灵AI，寻求200亿美元估值IPO [↗](https://zhidx.com/p/557037.html) `#18`

---

## [Claude Code 上线 Agent view 功能并新增 /goal 指令](https://claude.com/blog/agent-view-in-claude-code) `#1`
> **Claude** 宣布在 **Claude Code** 中推出 `Agent view` 研究预览版，用户可通过运行 `claude agents` 命令，在单一界面集中调度和查看多个并行会话。伴随发布的新版本还引入了 `/goal` 等新指令。

**Claude** 宣布推出 **Claude Code** 的新功能 **Agent view**。

该功能目前处于研究预览版状态，旨在解决开发者运行并行 **Agent** 时需频繁管理多个终端标签或 `tmux` 窗格的痛点。

用户可通过运行 `claude agents` 命令，在单一列表中直观查看所有正在运行、等待输入或已完成的会话。

系统并支持直接内联回复或使用 `/bg` 命令将任务置于后台。

此功能现已面向所有付费套餐开放。伴随发布的 `v2.1.139` 版本还引入了 `/goal` 等新指令。

同时，该版本修复了多项终端 **UI** 兼容问题。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/f36a3579-90d0-41e0-8594-002bb8c41087/m001.gif)

相关链接：
- [https://claude.com/blog/agent-view-in-claude-code](https://claude.com/blog/agent-view-in-claude-code)
- [https://code.claude.com/docs/en/agent-view](https://code.claude.com/docs/en/agent-view)
- [https://github.com/anthropics/claude-code/releases/tag/v2.1.139](https://github.com/anthropics/claude-code/releases/tag/v2.1.139)

---

## [Thinking Machines Lab 发布实时多模态“交互模型” TML-Interaction-Small](https://thinkingmachines.ai/blog/interaction-models/) `#2`
> **Thinking Machines Lab** 发布 **Interaction Models** 研究预览，公布了一种原生支持实时多模态人机协作的模型 `TML-Interaction-Small`，并称其在智能与交互性上达到当前最优水平，未来数月将开放有限研究预览。

**Thinking Machines Lab** 在其官方博客上发布了交互模型（`Interaction Models`）的研究预览及详细技术报告。

这是一种被设计为原生支持实时、多模态人机协作的模型，旨在解决当前大语言模型因“回合制”交互而导致的协作带宽瓶颈。其核心理念是让交互能力随智能一同扩展，而非作为事后添加的“外挂”。

该研究预览中的模型命名为 `TML-Interaction-Small`，是一个包含 **2760 亿** 参数的混合专家（`MoE`）模型，每次推理活跃参数为 **120 亿**。

其架构核心是“时间对齐的微轮转（`Time-Aligned Micro-Turns`）”，能够持续接收并理解音频、视频和文本流，并实现近乎实时的响应与思考。

官方称，该模型在智能性与交互响应性上取得了当前最优的综合表现；未来数月将开放有限研究预览供收集反馈，更广泛的发布和更大规模的模型计划于今年晚些时候推出。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260512/20260512083039_7722e16101.png)

相关链接：
- [https://thinkingmachines.ai/blog/interaction-models/](https://thinkingmachines.ai/blog/interaction-models/)

---

## [OpenBMB 发布开源多模态模型 MiniCPM-V 4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6) `#3`
> **OpenBMB** 发布并开源了 **1.3B** 参数量的端侧多模态大模型 `MiniCPM-V 4.6`。官方称该模型在多项基准测试中击败了 `Qwen3.5-0.8B`，原生支持在 iOS、Android 和 HarmonyOS 手机端运行。

**OpenBMB** 正式发布并开源了 **1.3B** 参数量的边缘多模态大模型 `MiniCPM-V 4.6`，模型权重基于 `Apache 2.0` 协议开放。

官方表示，该模型基于 `SigLIP2-400M` 与 `Qwen3.5-0.8B` 构建，采用最新的 `LLaVA-UHD v4` 架构，将视觉编码计算量降低了 **55.8%**。

根据官方提供的数据，该模型在多项基准测试中，以极低的 token 消耗超越了 `Qwen3.5-0.8B`。

该模型专为消费级硬件和移动设备优化，原生支持在 **iOS**、**Android** 和 **HarmonyOS** 平台端侧部署。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/10024a21-7447-46a4-b0d4-8794e9ee9290/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/10024a21-7447-46a4-b0d4-8794e9ee9290/m002.gif)

相关链接：
- [https://huggingface.co/openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)
- [https://github.com/OpenBMB/MiniCPM-V-edge-demo](https://github.com/OpenBMB/MiniCPM-V-edge-demo)

---

## [Anthropic 推出 Claude Platform on AWS](https://claude.com/blog/claude-platform-on-aws) `#4`
> **Anthropic** 宣布 **Claude Platform on AWS** 现已正式上线。**AWS** 客户可通过现有凭证和统一账单直接访问全套原生 `Claude API`，该服务由 **Anthropic** 运营。

**Anthropic**宣布 **Claude Platform on AWS** 正式全面可用，允许 **AWS**客户通过原有的 **IAM**身份验证和统一账单访问完整的原生 **Claude**平台功能。

该服务目前支持 `Claude Opus 4.7`、`Sonnet 4.6`与`Haiku 4.5`模型，并提供 `Claude Managed Agents`、代码执行以及 `MCP connector` 等全套工具，所有更新均与原生 API 同步发布。

不同于由 **AWS** 处理数据的 **Amazon Bedrock**，此平台由 **Anthropic**负责运营且数据在 **AWS**边界外处理，其计费能直接抵扣现有的 **AWS**承诺。

拥有现有 **Bedrock**私有优惠的用户需在迁移前联系客户经理，否则折扣无法追溯适用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260512/20260512073839_78a79f5d6b.png)

相关链接：
- [https://claude.com/blog/claude-platform-on-aws](https://claude.com/blog/claude-platform-on-aws)
- [https://aws.amazon.com/claude-platform/](https://aws.amazon.com/claude-platform/)

---

## [OpenAI 为 Codex 推出 OpenAI Developers 插件](https://x.com/OpenAIDevs/status/2053925962287583379) `#5`
> **OpenAI Developers** 宣布，`Codex` 现可通过 **OpenAI Developers** 插件，协助开发者使用 `OpenAI APIs` 更快地构建 `AI` 应用与 Agent。

**OpenAI Developers** 宣布 **Codex** 已上线 **OpenAI Developers** 插件，旨在通过快捷调用 **OpenAI APIs** 来加速 `AI` 应用和 Agent 的构建流程。

不过，有社区开发者指出，官方展示的用例中存在以明文形式生成并存储 `API` 密钥的操作，担忧这可能引发账单失控等安全隐患。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/d6d29116-d938-4b6d-b223-3ee15d46ec2e/m001.gif)

相关链接：
- [https://x.com/OpenAIDevs/status/2053925962287583379](https://x.com/OpenAIDevs/status/2053925962287583379)

---

## [OpenCode 宣布 DeepSeek V4 Flash 开启限时免费](https://x.com/opencode/status/2053887208688431179) `#6`
> **OpenCode** 宣布 **DeepSeek V4 Flash** 开启限时免费活动，用户现可免费调用体验。

**OpenCode** 官方宣布，`DeepSeek V4 Flash` 模型即日起开启限时免费。

作为 **OpenCode Go** 订阅目前最受欢迎的模型，它因卓越的性能和极低的使用成本受到开发者青睐。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260512/20260512081630_2dd65b0df8.png)

相关链接：
- [https://x.com/opencode/status/2053887208688431179](https://x.com/opencode/status/2053887208688431179)

---

## [Nous Portal 宣布限时免费提供 Qwen 3.6 Plus 模型](https://x.com/NousResearch/status/2053876496045920601) `#7`
> Nous Research 宣布，由**阿里**推出的 `Qwen 3.6 Plus` 现已在 **Nous Portal** 平台限时免费开放。

**Nous Research**宣布，阿里旗下模型 `Qwen 3.6 Plus` 现已在 **Nous Portal** 平台限时免费提供。该模型受到社区欢迎，用户目前通过 **Nous Portal** 的免费或付费订阅均可对其进行体验。

**Nous Portal** 是一项整合型订阅服务，提供超过 300 个模型的访问权限、独家折扣，并将 Token 与付费工具捆绑计费。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260512/20260512080832_a05faacfea.png)

相关链接：
- [https://x.com/NousResearch/status/2053876496045920601](https://x.com/NousResearch/status/2053876496045920601)
- [https://portal.nousresearch.com](https://portal.nousresearch.com)

---

## [Windsurf 面向付费用户将 Kimi K2.6 免费期再延长一个月](https://x.com/windsurf/status/2053895578946531518) `#8`
> **Windsurf** 宣布，因推广期间反响热烈，将 **Kimi K2.6** 对付费用户的免费使用期再延长一个月。

**Windsurf** 于 **4 月下旬** 宣布 **Kimi K2.6** 模型上线其平台，面向 Pro、Teams 和 Max 用户免费开放**两周**。

因该模型在推广期间反响热烈，**Windsurf** 随后宣布将免费期再延长**一个月**，上述用户目前可继续免费使用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260512/20260512081258_c230c2d424.png)

相关链接：
- [https://x.com/windsurf/status/2053895578946531518](https://x.com/windsurf/status/2053895578946531518)

---

## [千问与淘宝全面打通，开启AI购物体验](https://mp.weixin.qq.com/s/10VoJmPCkk4yOm2fJLk0EQ) `#9`
> **阿里**宣布，淘宝“`AI`低价帮抢”功能接入了支付宝“`AI`付”能力，同时千问 App 也与淘宝全面打通，用户可在千问内完成商品挑选、比价并下单。

即日起，在淘宝 App 中体验"**AI 低价帮抢**"功能时，可使用支付宝"**AI 付**"完成安全便捷的支付验证。

同时，**千问 App**也于今日与**淘宝**全面打通。将 App 更新至 `6.9.1` 及以上版本后，用户可直接在千问内进行**淘宝**商品挑选、对比及下单购买。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/56033e32-5262-4a98-9da6-078effd6c56f/m001.gif)

相关链接：
- [https://mp.weixin.qq.com/s/10VoJmPCkk4yOm2fJLk0EQ](https://mp.weixin.qq.com/s/10VoJmPCkk4yOm2fJLk0EQ)
- [https://mp.weixin.qq.com/s/-2Il_yefQVnmdM0ZHC0nUg](https://mp.weixin.qq.com/s/-2Il_yefQVnmdM0ZHC0nUg)

---

## [QClaw 发布「文件空间」功能，打通腾讯文档与 ima 知识库](https://mp.weixin.qq.com/s/AgmVAhSl7BNSGxE0FBqa1g) `#10`
> **QClaw** 宣布上线「文件空间」功能，通过与 **腾讯文档** 和 `ima` 知识库的深度打通，实现文件的一站式管理与 `AI` 协作。

**QClaw** 宣布上线「文件空间」功能。该功能通过底层账号与权限的深度集成，一次性打通了用户的本地文件、**腾讯文档**和 `ima` 知识库。

用户授权后，可直接在 **QClaw** 内访问并操作 **腾讯文档**里的文档、表格、思维导图等文件，并对多份文件下达指令。

此集成支持 AI 生成的文档以协作链接形式直接发送，同事可点开链接在网页端或用自己的 **QClaw** 协同编辑。

此外，**QClaw** 还接入了 `ima` 知识库，用户可调取知识库内收藏的公众号文章、研报等内容，也能将 AI 产出一键保存回 `ima`，实现知识的双向沉淀。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/97fc8805-180b-4bdc-8e34-b5743ddac1c0/m001.png)

相关链接：
- [https://mp.weixin.qq.com/s/AgmVAhSl7BNSGxE0FBqa1g](https://mp.weixin.qq.com/s/AgmVAhSl7BNSGxE0FBqa1g)

---

## [Artificial Analysis 发布 Coding Agent Index 评测模型与工具组合](https://artificialanalysis.ai/agents/coding-agents) `#11`
> **Artificial Analysis** 发布 **Coding Agent Index**，评测“模型 + 编程工具”组合。官方数据显示，**Opus 4.7** 搭配 `Cursor CLI` 以**61 分**取得最高分。

**Artificial Analysis** 正式发布 **Coding Agent Index**，该基准通过测试模型与编程工具组合在 `SWE-Bench-Pro-Hard-AA`、`Terminal-Bench v2` 和 `SWE-Atlas-QnA` 三项任务中的表现，评估其在真实软件工程中的综合能力。

官方公布的评测数据显示，**Opus 4.7** 搭配 `Cursor CLI` 以 **61分** 位居第一。紧随其后的是 **GPT-5.5** 搭配 `Codex` 以及 **Opus 4.7** 搭配 `Claude Code`，两者得分均为 **60分**。

在开源模型方面，**GLM-5.1** 搭配 `Claude Code` 以 **53分** 成为得分最高的开源权重组合。

此外，官方指出各组合在经济性和效率上差异显著。单任务 API 成本差异超过 **30倍**，执行时间差异超过 **7倍**。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/36f8976b-a660-4742-9f52-0f65fbec79f0/m001.png)

相关链接：
- [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- [https://x.com/ArtificialAnlys/status/2053865095076438427](https://x.com/ArtificialAnlys/status/2053865095076438427)

---

## [Google 发布报告称首次发现攻击者利用 AI 开发零日漏洞](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) `#12`
> **Google** 威胁情报小组发布报告称，首次发现攻击者利用据信由 `AI` 开发的零日漏洞策划大规模攻击，其主动防御措施可能已成功阻止该计划。

**Google** 威胁情报小组（**GTIG**）发布了关于 **AI** 驱动威胁及最新防御措施的报告。

报告指出，**GTIG** 首次观察到攻击者试图使用一个被认为是利用 **AI** 开发的零日漏洞策划大规模攻击。**Google** 的主动反制发现可能已阻止该事件发生。

为了应对威胁，**Google** 通过分类器和禁用恶意账户等方式缓解 **Gemini** 的模型滥用，并利用 `Big Sleep` 和 `CodeMender` 等 AI Agent 进行漏洞检测与自动修复。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260512/20260512075723_1dee98c71c.png)

相关链接：
- [https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)

---

## [OpenAI 推出 Daybreak 网络安全愿景](https://openai.com/daybreak/) `#13`
> **OpenAI** 发布 **Daybreak** 网络安全愿景，整合 `GPT-5.5` 与 `Codex Security`，通过威胁建模加速漏洞的发现与修复，并面向防御分析、红队测试等场景提供分级模型访问。

**OpenAI** 推出 **Daybreak** 网络安全愿景，旨在改变软件的构建与防御方式，使安全能力更早融入软件生命周期。

**Daybreak** 将 `GPT-5.5` 的推理能力与 `Codex Security` 的智能体工作流结合，基于连接的代码仓库和系统上下文构建可编辑的威胁模型，帮助团队发现、验证和修复漏洞，并生成可审查的补丁建议与修复验证证据。

为适应不同安全场景，**OpenAI** 划分了三种访问级别：通用默认的 `GPT-5.5`、面向经验证防御工作的 `GPT-5.5 with Trusted Access for Cyber`，以及面向授权红队、渗透测试和受控验证等专业场景的 `GPT-5.5-Cyber` 预览访问。

目前，企业可通过 **OpenAI** 官方渠道请求漏洞扫描或联系销售了解接入方式。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/5828ee02-3408-43a9-afab-a45ffd59debd/m001.gif)

相关链接：
- [https://openai.com/daybreak/](https://openai.com/daybreak/)
- [https://x.com/OpenAI/status/2053939702110269822](https://x.com/OpenAI/status/2053939702110269822)

---

## [OpenAI 成立 OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/) `#14`
> **OpenAI** 宣布成立由其控股的 **OpenAI Deployment Company**。该公司获超 **40 亿美元** 初始投资，将通过外派工程师模式，协助企业将前沿 `AI` 模型转化为实际生产力。目前已达成收购 **Tomoro** 的协议，首批将引入约 **150 名** 资深部署专家。

**OpenAI** 正式启动由其控股的独立业务单元 `OpenAI Deployment Company`，旨在解决企业将 **AI** 投入生产时的工程、合规与传统系统集成等难题。

该公司获得由 **TPG** 领投、**贝恩资本** 等机构参与的超 **40** 亿美元初始注资。

并宣布收购 AI 咨询公司 **Tomoro**，从而在成立初期即获得约 **150** 名资深工程师支持。

通过 `Forward Deployed Engineering` 模式，团队将深入企业一线构建定制化可靠系统。

目前已在 **BBVA** 和 **John Deere** 等客户中实现业务流程的 **AI** 原生化改造。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260512/20260512080250_1ecd79e283.png)

相关链接：
- [https://openai.com/index/openai-launches-the-deployment-company/](https://openai.com/index/openai-launches-the-deployment-company/)
- [https://openai.com/business/the-openai-deployment-company/](https://openai.com/business/the-openai-deployment-company/)

---

## [MiniMax 发起 10x Team 计划招募行业专家](https://mp.weixin.qq.com/s/G3m2xksI2jHAROhNdP7x2Q) `#15`
> **MiniMax** 发起 "**10x Team**" 计划招募行业专家，合作构建 **AI** 评测与工作流。官方提供多模态模型及无限 `Token`，支持全职或至少 `4` 个月的线下协作。

**MiniMax** 官方宣布发起 **`10x Team`** 计划，期望与各领域专家合作推动行业实现十倍增长。

官方透露过去几个月已在工业软件、游戏引擎及金融等领域展开合作，成果将体现在后续模型中。此次招募要求合作者有行业积累，并共同定义问题、构建评测与工作流。

官方将提供多模态模型能力、研发环境及无限 Token，且评测会开源。该项目支持全职或至少四个月的线下 Fellowship，工作地可选北京、上海、香港、旧金山或伦敦，并提供具有竞争力的薪酬及股票激励。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/6aa072ea-b411-47a5-8b2a-e6d812eea984/m001.png)

相关链接：
- [https://mp.weixin.qq.com/s/G3m2xksI2jHAROhNdP7x2Q](https://mp.weixin.qq.com/s/G3m2xksI2jHAROhNdP7x2Q)

---

## [Qwen 官宣全球 Ambassador 计划并招募开发者与活动大使](https://qwen.ai/ambassador) `#16`
> **Qwen** 官方宣布招募全球开发者与活动大使。入选者可获模型内测资格与每月最高 **100 美元** `API` 额度，需完成对应的月度考核任务。

**Qwen** 官方正式启动"**Qwen Ambassador Program**"，面向全球招募开发者与活动两类大使以拓展其开源生态。

开发者大使需每月产出至少 `4` 篇内容，活动大使则需每月举办至少 `1` 场活动并发布 `2` 篇社交帖子。

作为回报，入选者将获得专属徽章、与官方团队的私密交流权限、`Qwen` 模型内测资格、每月 `50` 至 `100` 美元的 API 额度以及年度周边礼包等活动资金支持。

申请结果将在提交后 `15` 个工作日内通过邮件通知，若连续 `2` 个月未履行考核要求将被视为自动退出。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/bbe97968-e937-43d4-bdb7-6196723459c5/m001.png)

相关链接：
- [https://qwen.ai/ambassador](https://qwen.ai/ambassador)
- [https://x.com/Alibaba_Qwen/status/2053835267061301316](https://x.com/Alibaba_Qwen/status/2053835267061301316)

---

## [Unsloth 宣布正式加入 PyTorch 生态](https://unsloth.ai/blog/pytorch) `#17`
> **Unsloth** 宣布正式加入 **PyTorch** 生态。该团队表示，加入生态后项目路线保持不变，将继续维持开源并按计划推出桌面端应用。

开源项目 **Unsloth** 宣布已正式加入 **PyTorch Ecosystem**。

该项目利用定制化的 `Triton` 内核，在无精度损失的情况下将模型训练速度提升约两倍，并降低约 **70%** 的显存占用。

其最新发布的开源界面 `Unsloth Studio` 支持在 **Windows**、**Mac** 和 **Linux** 环境中训练和运行超过 **500** 种模型，并与 **PyTorch** 联合推出了多项底层优化技术。

团队表示，加入生态后项目路线保持不变，将继续维持开源并按计划推出桌面端应用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/d84f21fa-c3f2-4fbe-acbe-50dbc2e7ed6d/7167c90d-f109-4840-a085-c0f6fbdabd2f/m001.png)

相关链接：
- [https://unsloth.ai/blog/pytorch](https://unsloth.ai/blog/pytorch)

---

## [消息称快手计划分拆可灵AI，寻求200亿美元估值IPO](https://zhidx.com/p/557037.html) `#18`
> 据报道，**快手**计划分拆视频生成业务"**可灵AI**"为明年的潜在**IPO**做准备，目前正寻求估值高达**200亿美元**的上市前融资。

据媒体报道引述知情人士消息，**快手**正计划将旗下视频生成业务"**可灵AI**"分拆，并寻求高达 **200亿美元** 估值的IPO前融资，为**明年一季度**潜在的IPO做准备。

报道指出，**可灵AI**今年**第一季度**收入达 **7500万美元**，大部分来自海外市场，并预计在启动上市时其年化收入将达到约 **13亿美元**。

**快手**近期已注册并更名成立两家**可灵AI**相关子公司。**快手**方面目前对此IPO消息不予置评。

相关链接：
- [https://zhidx.com/p/557037.html](https://zhidx.com/p/557037.html)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。