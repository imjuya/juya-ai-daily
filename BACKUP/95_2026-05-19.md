# [2026-05-19](https://github.com/imjuya/juya-ai-daily/issues/95)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260519/20260519090243818278329c_cover_fb7c.png)

# AI 早报 2026-05-19

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1LoLK6pEXE) ｜ [YouTube](https://www.youtube.com/watch?v=FzRTrUbr4cw)

## 概览
### 要闻
- 千问上线 Qwen3.7 Max Preview 和 Qwen3.7 Plus Preview [↗](https://x.com/Alibaba_Qwen/status/2056403591464984753) `#1`
### 模型发布
- Cursor 发布 Composer 2.5 并携手 SpaceXAI 合训新模型 [↗](https://cursor.com/blog/composer-2-5) `#2`
### 开发生态
- Anthropic 宣布将 Claude Design 各计划 token limits 翻倍 [↗](https://x.com/claudeai/status/2056460045756309820) `#3`
- Claude Code 上线基于 Opus 4.7 的 /fast 模式 [↗](https://x.com/ClaudeDevs/status/2056454359685476491) `#4`
- GitHub 发布多项 Copilot 更新 一键修复 Actions 上线 [↗](https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent) `#5`
- OpenRouter 发布长周期 Agent 构建原语与 SDK [↗](https://openrouter.ai/long-horizon) `#6`
- Browserbase 推出 Browse.sh 技能目录 [↗](http://Browse.sh) `#7`
### 技术与洞察
- 腾讯混元等机构发布古文字评测基准 Chronicles-OCR [↗](https://github.com/VirtualLUOUCAS/Chronicles-OCR) `#8`
### 行业动态
- Anthropic 收编 SDK 供应商 Stainless，将关停其托管产品 [↗](https://www.anthropic.com/news/anthropic-acquires-stainless) `#9`
- 消息称 Musk 诉 OpenAI 案败诉，陪审团认定起诉超时 [↗](https://the-decoder.com/elon-musk-loses-his-134-billion-lawsuit-against-openai-after-jury-deliberates-for-just-two-hours) `#10`
### 前瞻与传闻
- DeepSeek 调研 DeepSeek-V4 角色扮演及情感陪伴体验 [↗](https://www.xiaohongshu.com/explore/6a0ac4ce000000003601e8f6?xsec_source=pc_feed&note_flow_source=wechat) `#11`
- SpaceXAI 将提高 Grok Imagine 速率限制并改进生成准确度 [↗](https://x.com/elonmusk/status/2056282453556240552) `#12`

---

## [千问上线 Qwen3.7 Max Preview 和 Qwen3.7 Plus Preview](https://x.com/Alibaba_Qwen/status/2056403591464984753) `#1`
> **千问团队**在 **Qwen Studio** 上线了 `Qwen3.7 Max` 及 `Qwen3.7 Plus` 两款模型的 **Preview** 版。同步公开了 **Arena** 分数和排名，该系列模型或于近期的**阿里云峰会**正式发布。

**阿里通义千问**团队日前在 **Qwen Studio** 及评测平台 **Arena** 上线了 `Qwen3.7` 的预览版模型，包含 `Qwen3.7-Max-Preview` 与 `Qwen3.7-Plus-Preview` 两个版本。

根据 **Arena** 公布的数据，**Max** 版在 **Text** 赛道总排名第 **13**，且在数学、编程等分项均跻身前十。**Plus** 版在 **Vision** 赛道总排名第 **16**。

其正式发布活动预计在即将到来的**阿里云峰会**上进行。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260519/20260519083604_d682e09e32.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/274224ce-15ef-43ec-8263-5aa043388bee/m002.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/274224ce-15ef-43ec-8263-5aa043388bee/m003.png)

相关链接：
- [https://x.com/Alibaba_Qwen/status/2056403591464984753](https://x.com/Alibaba_Qwen/status/2056403591464984753)
- [https://mp.weixin.qq.com/s/MrimtAw2GECk7Gycgh6hCw?scene=1](https://mp.weixin.qq.com/s/MrimtAw2GECk7Gycgh6hCw?scene=1)

---

## [Cursor 发布 Composer 2.5 并携手 SpaceXAI 合训新模型](https://cursor.com/blog/composer-2-5) `#2`
> **Cursor** 宣布推出 **`Composer 2.5`**，官方称其复杂指令跟随能力更强，效率最高可比同类提升**十倍**，首周额度翻倍。同时，其宣布将与 **SpaceXAI** 联手，使用**十倍**算力从零训练一个更大模型。

**Cursor** 发布了最新的编程模型 `Composer 2.5`，该模型基于 **Moonshot** 的 `Kimi K2.5` 训练。

`Composer 2.5` 强化了长时间运行任务中的持续工作能力和复杂指令遵循表现。**Cursor** 官方称其效率最高可比同等能力模型提升**十倍**。

模型现已上线，提供标准版和更快的快速版本，后者为默认选项。首周将提供**双倍**使用额度。

训练中引入了基于文本反馈的强化学习等方法，有效解决了长轨迹中的信用分配难题。

同时，**Cursor** 同步宣布正与 **SpaceXAI** 合作，使用**十倍**总计算资源在**百万** `H100` 等效的 `Colossus 2` 集群上从零训练一个更大模型。

预计将带来重大能力飞跃。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/7cf42979-c620-4eac-a432-fd78581fa2a7/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/7cf42979-c620-4eac-a432-fd78581fa2a7/m002.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260519/20260519090446_d73ab25434.png)

相关链接：
- [https://cursor.com/blog/composer-2-5](https://cursor.com/blog/composer-2-5)
- [https://cursor.com/docs/models/cursor-composer-2-5](https://cursor.com/docs/models/cursor-composer-2-5)

---

## [Anthropic 宣布将 Claude Design 各计划 token limits 翻倍](https://x.com/claudeai/status/2056460045756309820) `#3`
> **Anthropic** 官方宣布已将 **Claude Design** 在所有订阅计划中的 `token limits` 翻倍。

**Anthropic** 通过其官方社交账号宣布，已将 **Claude Design** 在所有订阅计划中的 `token limits` 翻倍。

此次扩容主要针对此前用户极易触及输出上限的痛点。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/d4e3c78d-abe2-4a13-9ddd-a4bc71f96f21/m001.png)

相关链接：
- [https://x.com/claudeai/status/2056460045756309820](https://x.com/claudeai/status/2056460045756309820)

---

## [Claude Code 上线基于 Opus 4.7 的 /fast 模式](https://x.com/ClaudeDevs/status/2056454359685476491) `#4`
> **Claude Code** 官方宣布 **Fast** 模式已默认切换为 `Opus 4.7`，官方称其响应速度约为标准模式的 **2.5** 倍，但按更高 token 费率计费。

**ClaudeDevs** 官方社交账号宣布，`Claude Code` 的 Fast 模式现已默认使用 `Opus 4.7` 模型。

官方称该模式提供与标准 `Opus` 相同的质量，响应速度约为标准模式的 **2.5 倍**。但该功能按更高的 token 费率计费，适用于快速迭代、实时调试等对延迟敏感的场景。

用户可通过 `/fast` 命令启用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/4dddca10-6173-45bd-92a5-64885b7c5bd2/m001.gif)

相关链接：
- [https://x.com/ClaudeDevs/status/2056454359685476491](https://x.com/ClaudeDevs/status/2056454359685476491)

---

## [GitHub 发布多项 Copilot 更新 一键修复 Actions 上线](https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent) `#5`
> **GitHub**发布多项 **Copilot**更新，推出可一键修复 `Actions` 的云 Agent，并将 `Spaces API` 与 `CLI` 远程控制正式开放。

**GitHub** 官方近日针对 **Business** 和 **Enterprise** 用户推出多项 **Copilot** 更新。

核心全新能力是云 Agent 现可一键修复失败的 **GitHub Actions**，自动完成代码调查、修复推送并标记审查，同时新增用于审计该 Agent 配置的 `REST API`。

此前处于测试阶段的 Spaces 编程管理 API，以及 `Copilot CLI` 和 `VS Code` 会话的远程控制功能均已在本次正式全面可用。

此外 **Copilot Chat** 也通过同页面面板和上下文自动附加改善了交互体验。

相关链接：
- [https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent](https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent)
- [https://github.blog/changelog/2026-05-18-copilot-cloud-agent-fast-cost-efficient-models-for-simple-tasks](https://github.blog/changelog/2026-05-18-copilot-cloud-agent-fast-cost-efficient-models-for-simple-tasks)
- [https://github.blog/changelog/2026-05-18-ask-questions-in-context-with-copilot-on-web](https://github.blog/changelog/2026-05-18-ask-questions-in-context-with-copilot-on-web)

---

## [OpenRouter 发布长周期 Agent 构建原语与 SDK](https://openrouter.ai/long-horizon) `#6`
> **OpenRouter** 推出用于构建长程 `AI Agent` 的 `SDK` 与开发原语。该工具包支持运行多小时的复杂任务循环，内置成本上限控制、状态可恢复等功能。

**OpenRouter** 官方宣布发布用于构建长程、持久运行 **AI Agent** 的开发工具包与原语。

通过该 **Agent SDK**，开发者可以运行高步骤数、长超时的多步任务循环，并利用 `maxCost` 和 `stepCountIs` 等条件组合来限制最高成本与执行步数。

该工具支持持久化对话消息、工具结果和共享上下文，允许在系统崩溃、重新部署或人工审查后重放或恢复长程任务。

此外，SDK 原生集成了 `/api/v1/audio/transcriptions` 等端点以支持语音输入与输出，开发者目前可通过获取 API 密钥直接部署相关智能体。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/e7652021-6208-47b5-93cd-fec0a9353531/m001.png)

相关链接：
- [https://openrouter.ai/long-horizon](https://openrouter.ai/long-horizon)
- [https://x.com/OpenRouter/status/2056404687461519479](https://x.com/OpenRouter/status/2056404687461519479)

---

## [Browserbase 推出 Browse.sh 技能目录](http://Browse.sh) `#7`
> **Browserbase** 推出并开源名为 **Browse.sh** 的 `Agent` 技能生态系统，为 `Agent` 提供数百家网站预设指南。仅特定功能需 `API` 密钥。

**Browserbase** 官宣推出并开源名为 `Browse.sh` 的 Agent 技能生态系统，旨在帮助其可靠执行复杂的端到端浏览器任务。

官方称该生态为最大的开源技能集合，已研究数百家网站并提供了预设指南，同时与 **Ramp**、**Lovable** 等平台合作创建了认证技能。

该目录及其配套 CLI 工具对所有人免费开放，支持社区提交技能或由系统按需生成，但官方澄清，涉及调用 **Browserbase** 平台特定底层功能的技能仍需使用带有免费额度的 API 密钥。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/1d91ea5a-2674-45b2-8c73-419d3f675c00/m001.gif)

相关链接：
- [http://Browse.sh](http://Browse.sh)

---

## [腾讯混元等机构发布古文字评测基准 Chronicles-OCR](https://github.com/VirtualLUOUCAS/Chronicles-OCR) `#8`
> **腾讯混元**等机构发布古文字评测基准 `Chronicles-OCR`。官方称其能覆盖汉字“七体之变”，测试显示当前主流多模态大模型对古文字的识别与转写能力近乎失效。

**腾讯混元**、**SSV 数字文化实验室**等团队联合多家高校与**中科院**正式推出中国古文字感知评测基准 **Chronicles-OCR**。官方称该基准是业界首个覆盖甲骨、金文、篆、隶、楷、行、草“七体之变”的评测数据集，包含 `2800` 张专家标注图像，目前已公开于 **GitHub**。

研究团队对 `28` 个主流多模态大模型进行的测试显示，**GPT-5**、**Gemini 2.5 Pro** 等模型在跨时代字符检测任务上的得分接近零。且开启思维链推理模式反而会导致识别表现下降。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/6f791a39-c5b8-4f62-9998-717b41792e94/m001.png)

相关链接：
- [https://github.com/VirtualLUOUCAS/Chronicles-OCR](https://github.com/VirtualLUOUCAS/Chronicles-OCR)
- [https://mp.weixin.qq.com/s/RmzRuZcmYCDIhp_VI2G5Ig](https://mp.weixin.qq.com/s/RmzRuZcmYCDIhp_VI2G5Ig)

---

## [Anthropic 收编 SDK 供应商 Stainless，将关停其托管产品](https://www.anthropic.com/news/anthropic-acquires-stainless) `#9`
> **Anthropic** 收购 `SDK` 及 `MCP` 工具平台 **Stainless** 以提升 `Agent` 连接能力，后续将关停该公司所有托管版产品。

**Anthropic**宣布收购 SDK 和 MCP 服务器工具平台 **Stainless**。后者自 API 早期起，便为 **Anthropic** 生成所有官方 SDK。

官方虽未披露交易金额，但据媒体报道，此次收购作价超过 **3 亿美元**。

收购完成后，**Anthropic** 将逐步关停所有托管版 **Stainless** 产品，但现有客户仍可保留并修改已生成的 SDK。

官方称此举旨在进一步推进 `Claude` 平台的开发者体验及 Agent 外部连接能力。

相关链接：
- [https://www.anthropic.com/news/anthropic-acquires-stainless](https://www.anthropic.com/news/anthropic-acquires-stainless)
- [https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare](https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare)

---

## [消息称 Musk 诉 OpenAI 案败诉，陪审团认定起诉超时](https://the-decoder.com/elon-musk-loses-his-134-billion-lawsuit-against-openai-after-jury-deliberates-for-just-two-hours) `#10`
> 据媒体报道，**Elon Musk** 在针对 **OpenAI** 的诉讼中败诉，九人陪审团经过仅**两小时**的审议后一致认定其起诉过晚，**Musk** 的律师表示计划提起上诉。

据媒体报道，**Elon Musk** 近日在针对 **OpenAI** 和 **Sam Altman** 的诉讼中败诉。

奥克兰的九人陪审团在经过三周庭审和仅两小时的审议后，一致认定其主张已超过法定诉讼时效。该诉讼寻求高达 **1340 亿美元** 的赔偿。

法官 **Yvonne Gonzalez** 表示支持陪审团决定。而据媒体及 **Musk** 律师透露，**Musk** 方面保留了上诉权并计划继续上诉。

相关链接：
- [https://the-decoder.com/elon-musk-loses-his-134-billion-lawsuit-against-openai-after-jury-deliberates-for-just-two-hours](https://the-decoder.com/elon-musk-loses-his-134-billion-lawsuit-against-openai-after-jury-deliberates-for-just-two-hours)

---

## [DeepSeek 调研 DeepSeek-V4 角色扮演及情感陪伴体验](https://www.xiaohongshu.com/explore/6a0ac4ce000000003601e8f6?xsec_source=pc_feed&note_flow_source=wechat) `#11`
> **DeepSeek** 官方工作人员发帖向用户收集 `DeepSeek-V4` 模型使用反馈，调研角色扮演与情感陪伴体验，相关意见将用于指导下一次更新。

**DeepSeek** 工作人员在小红书平台发布调研贴，向用户收集关于 **DeepSeek-V4** 模型的使用反馈。

该模型上线已大半个月，此次调研重点聚焦于角色扮演与情感陪伴场景的体验。

同时也接受关于小说、公文、幻觉、搜索和代码等其他领域的反馈。

用户可以通过小红书评论区、私信进行提交。

如需提交长篇资料，可发送至指定邮箱。

这些收集到的意见将被用于指导模型的下次更新。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/fb7c583c-2c0f-4da4-9571-965532ee8ce4/4a04a1d3-3611-41f4-9bda-5ee9f69ee5d5/m001.png)

相关链接：
- [https://www.xiaohongshu.com/explore/6a0ac4ce000000003601e8f6?xsec_source=pc_feed&note_flow_source=wechat](https://www.xiaohongshu.com/explore/6a0ac4ce000000003601e8f6?xsec_source=pc_feed&note_flow_source=wechat)

---

## [SpaceXAI 将提高 Grok Imagine 速率限制并改进生成准确度](https://x.com/elonmusk/status/2056282453556240552) `#12`
> **Elon Musk** 称，`Grok`的图像与视频生成准确度即将大幅提升，并承诺将放宽 `Grok Imagine` 的使用频率限制。

**Elon Musk** 近期在社交平台上针对 **SpaceXAI** 的相关功能做出了两项明确表态。

他首先确认 `Grok` 在图像与视频生成的准确度方面即将迎来重大改进。

同时，针对用户反馈的 `Grok Imagine` 频率限制过严问题，他承诺将会提高使用额度。

但目前官方尚未公布具体的生效时间与详细额度。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260518/20260518180749_56c250221c.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260518/20260518180841_76e8477114.png)

相关链接：
- [https://x.com/elonmusk/status/2056282453556240552](https://x.com/elonmusk/status/2056282453556240552)
- [https://x.com/elonmusk/status/2056202821771403505](https://x.com/elonmusk/status/2056202821771403505)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。