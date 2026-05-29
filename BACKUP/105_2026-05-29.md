# [2026-05-29](https://github.com/imjuya/juya-ai-daily/issues/105)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260529/202605290907446043745c78_cover_4ed6.png)

# AI 早报 2026-05-29

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1h1V46eEfL) ｜ [YouTube](https://www.youtube.com/watch?v=w5Ke-YatkTE)

## 概览
### 要闻
- Anthropic 发布 Claude Opus 4.8 模型 [↗](https://www.anthropic.com/news/claude-opus-4-8) `#1`
- Claude Code 推出 dynamic workflows 研究预览，支持数百 subagent 并行编排 [↗](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) `#2`
- Anthropic 完成 650 亿美元 H 轮融资，投后估值达 9650 亿美元 [↗](https://www.anthropic.com/news/series-h) `#3`
- 阶跃星辰开源 Step 3.7 Flash 多模态推理模型 [↗](https://static.stepfun.com/blog/step-3.7-flash/) `#4`
### 模型发布
- PaddlePaddle 推出 PaddleOCR-VL 1.6 升级文档解析能力 [↗](https://x.com/PaddlePaddle/status/2059990434827661769) `#5`
- 商汤开源 SenseNova-U1-8B-MoT-Infographic 模型 [↗](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-Infographic) `#6`
- Liquid AI 发布 LFM2.5-8B-A1B 设备端模型 [↗](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF) `#7`
- Bagel Labs 发布 Paris 2.0 去中心化视频生成模型 [↗](https://huggingface.co/bageldotcom/paris2) `#8`
- ElevenLabs 推出支持 90 多种语言的 Dubbing v2 [↗](https://elevenlabs.io/dubbing-studio) `#9`
- ElevenLabs 发布 Music v2 模型，支持跨流派无缝转换与局部重绘 [↗](https://elevenlabs.io/blog/introducing-music-v2) `#10`
- Nano Banana 系列模型 GA，可通过 Gemini API 投入生产使用 [↗](https://x.com/googleaidevs/status/2060068093485895978) `#11`
### 开发生态
- Antigravity CLI 1.0.3 发布：支持配额耗尽后使用 Google AI credits [↗](https://x.com/shengzheyao/status/2059814938609332726) `#12`
- 腾讯混元发布 Hy-Memory 插件提升 Agent 长期记忆能力 [↗](https://memory.hunyuan.tencent.com/) `#13`
- Firecrawl 发布 Monitoring 网页变更监控功能 [↗](https://x.com/firecrawl/status/2060042535003701523) `#14`
- Nous Research 发布 Hermes Agent v0.15.0 版本 [↗](https://x.com/Teknium/status/2060088572049559893) `#15`
- OpenClaw 更新 v2026.5.27：官方称包体积缩小 59%，强化安全边界 [↗](https://openclaw.ai/blog/lighter-core-sharper-claws/) `#16`
### 产品应用
- Mistral AI 将 Le Chat 更名为 Vibe 并推出 Work 与 Code 模式 `#17`
- Perplexity AI 助手 Computer 上线插件接入 Microsoft 365 [↗](https://www.perplexity.ai/hub/products/integrations/microsoft) `#18`
- 微软重构 Microsoft 365 Copilot 并提升加载速度 [↗](https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/) `#19`
### 技术与洞察
- Qwen 团队发布文生图评测基准 Qwen-Image-Bench [↗](https://github.com/QwenLM/Qwen-Image-Bench) `#20`
- Sakana AI 提出 DiffusionBlocks 训练框架 [↗](https://x.com/SakanaAILabs/status/2059648778051924281) `#21`
- NVIDIA发布Dynamo Snapshot：K8s推理冷启动降至5秒内 [↗](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/) `#22`
- 小米分享 AI Coding 工程化实践：VAF、VKF 与 eight-claw [↗](https://mp.weixin.qq.com/s/l5qeFWtXtaStweOqLP7RKA) `#23`
### 行业动态
- 豆包澄清“听信AI致婴儿喂养不足”传闻 [↗](https://weibo.com/7778831349/R1vRkEqCY) `#24`
- Linux Foundation 发布 OpenMDW-1.1，NVIDIA 宣布采用该模型许可证 [↗](https://openmdw.ai/) `#25`

---

## [Anthropic 发布 Claude Opus 4.8 模型](https://www.anthropic.com/news/claude-opus-4-8) `#1`
> **Anthropic**发布`Claude Opus 4.8`模型，强化了编码、Agent任务及长时运行工作的一致性方面的能力。该模型现已在官方全平台和各类第三方平台上线，官方`API`**定价不变**，`Fast`模式**降价三分之二**且**提速约2.5倍**。同步面向 `claude.ai` 和 `Cowork` 的所有用户推出`推理努力程度控制`功能。**Anthropic**还表示正开发更低成本同等能力模型，同时预计**数周内**将`Mythos`级别模型推向所有客户。

**Anthropic** 正式发布 `Claude Opus 4.8` 模型，现已全平台上线。

该模型基于 `Opus 4.7` 构建，具备 **100 万** `Token` 上下文窗口。

官方称其在编码、`Agent` 任务及长时运行工作的一致性上均有增强，更倾向于标记工作中的不确定性，官方评测显示其让代码缺陷未被注意地通过的概率约为前代的四分之一。

在定价方面，`API` 常规定价不变。

同步上线的 `Fast` 模式使用同一模型以约 **2.5** 倍速度运行，定价降至输入 **$10**、输出 **$50**，降幅达三分之二。

据第三方机构 **Artificial Analysis** 数据，`Opus 4.8` 以 **61.4** 分登顶 `Intelligence Index`，领先 `GPT-5.5（xhigh）` **1.2** 分。

在 `GDPval-AA` 评测中以 **1890** `Elo` 重夺第一，隐含对 `GPT-5.5` 约 **67%** 胜率。

该机构指出其 `Token` 效率因任务而异。

此外，其在 `Humanity's Last Exam` 超过 **OpenAI** 和 **Google** 模型，幻觉率显著低于同类。

据 **Databricks** 反馈，该模型在其平台的 `Token` 成本比前代低 **61%**。

本次同步推出多项新功能：`努力程度控制`面向全平台开放，提供 `Low` 到 `Max` 五个档位，`Opus 4.8` 默认使用 `High` 档位。

`动态工作流`以研究预览形式面向 **Enterprise** 等特定计划，支持运行数百个并行子 `Agent`。

`Messages API` 新增支持在任务中途更新指令而不破坏 `prompt cache`。

安全方面，**Anthropic** 称其不对齐行为发生率显著低于前代。

未来，**Anthropic** 计划开发更低成本及更高智能的模型，并预计在未来数周内将正由少数组织进行网络安全测试的 `Mythos` 级别模型推向所有客户。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/c6c55aa1-d4ba-4a5c-8490-da4b7be7c4c9/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/c6c55aa1-d4ba-4a5c-8490-da4b7be7c4c9/m002.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260529/20260529084047_8df02574cf.png)

相关链接：
- [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)
- [https://www.anthropic.com/claude-opus-4-8-system-card](https://www.anthropic.com/claude-opus-4-8-system-card)

---

## [Claude Code 推出 dynamic workflows 研究预览，支持数百 subagent 并行编排](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) `#2`
> **Anthropic**发布`Claude Code`更新，上线**dynamic workflows**功能与**Opus 4.8**模型。`workflows`可调度**上千个**`subagent`并行处理**大规模任务**，同时`Opus 4.8`的**fast mode**能以**两倍价格**换取约**2.5倍**速度。

**Anthropic** 发布 `Claude Code v2.1.154`，核心更新包括 `Opus 4.8` 模型上线和名为 `dynamic workflows` 的新功能。

`Dynamic workflows` 允许 `Claude` 根据用户描述自动生成 `JavaScript` 编排脚本，在后台调度最多 **16** 个并发 `subagent`、单次运行上限 **1000** 个 `agent`。

中间结果保存在脚本变量中而非占用上下文窗口，运行中断后可在同一会话内恢复。

该功能目前处于研究预览阶段，面向 **Max**、**Team** 套餐及 **Anthropic API**、`Amazon Bedrock`、`Google Cloud Vertex AI`、`Microsoft Foundry` 用户默认开启。

**Enterprise** 套餐默认关闭需管理员手动启用，**Pro** 套餐用户需在 `/config` 中手动开启。

官方提示单次运行 `token` 消耗远高于普通会话，建议从小范围任务开始。

`Opus 4.8` 的 `fast mode` 以标准费率的两倍提供约 **2.5** 倍速度。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/056ef1e8-f4f4-4d48-9fd3-915f9d60e502/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/056ef1e8-f4f4-4d48-9fd3-915f9d60e502/m002.png)

相关链接：
- [https://claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [https://code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows)
- [https://github.com/anthropics/claude-code/releases/tag/v2.1.154](https://github.com/anthropics/claude-code/releases/tag/v2.1.154)

---

## [Anthropic 完成 650 亿美元 H 轮融资，投后估值达 9650 亿美元](https://www.anthropic.com/news/series-h) `#3`
> **Anthropic** 宣布完成 **650 亿美元**`H 轮`融资，投后估值达 **9650 亿美元**。这笔资金预计将用于推进`安全`与`可解释性`研究，并扩展`算力`满足对 `Claude` 的需求。

**Anthropic** 宣布完成 **650亿美元** `H轮` 融资，投后估值达 **9650亿美元**。

本轮融资由 **Altimeter Capital** 等领投，包含超大规模计算厂商 **150亿美元** 先前承诺投资。

该公司本月早些时候经常性收入已突破 **47亿美元**。

官方预计，资金将用于推进 `安全和可解释性` 研究、扩展算力规模并深化产品开发。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260529/20260529084702_233c9493ac.png)

相关链接：
- [https://www.anthropic.com/news/series-h](https://www.anthropic.com/news/series-h)

---

## [阶跃星辰开源 Step 3.7 Flash 多模态推理模型](https://static.stepfun.com/blog/step-3.7-flash/) `#4`
> **阶跃星辰**发布 **`Step 3.7 Flash`** 多模态推理模型，采用 **`198B`** 稀疏 **`MoE`** 架构且仅激活约 **`11B`** 参数，支持多档推理努力程度，已开放 **`API`** 调用并以 **`Apache 2.0`** 协议开源全部权重。

**Step 3.7 Flash** 是**阶跃星辰**推出的旗舰多模态推理模型，由 `196B` 参数语言骨干与 `1.8B` 参数视觉编码器组成。

每 `token` 激活约 `11B` 参数，最高吞吐达 **400 TPS**，支持 `256K` 上下文窗口与低、中、高三档可选推理强度。

官方称该模型在 `ClawEval-1.1` 上得分 `67.1`、`SimpleVQA (Search)` 得分 `79.2` 均为同期第一。

`SWE-Bench Pro` 得分 `56.3` 为同期第二，并新增 `Advisor Mode` 可在约九分之一成本下达到 `Claude Opus 4.6` 约 **97%** 的编码性能。

模型已上线 `StepFun` 国内外 `API` 平台、`OpenRouter` 及 `NVIDIA NIM`，兼容 `OpenAI` 与 `Anthropic` 协议。

权重以 **Apache 2.0** 开源并提供 `BF16`、`FP8`、`NVFP4`、`GGUF` 等多种格式。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/03cd671e-fa02-403a-8947-9274217f54d0/m001.png)

相关链接：
- [https://static.stepfun.com/blog/step-3.7-flash/](https://static.stepfun.com/blog/step-3.7-flash/)
- [https://github.com/stepfun-ai/Step-3.7-Flash](https://github.com/stepfun-ai/Step-3.7-Flash)
- [https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)

---

## [PaddlePaddle 推出 PaddleOCR-VL 1.6 升级文档解析能力](https://x.com/PaddlePaddle/status/2059990434827661769) `#5`
> **PaddlePaddle** 正式发布 `PaddleOCR-VL 1.6` 模型。官方称其在 `OmniDocBench v1.6` 基准达到 **96.33%** ，且架构兼容前代，支持即插即用。

**PaddlePaddle** 团队正式发布了文档解析模型 `PaddleOCR-VL 1.6`。

官方数据显示，该模型在 `OmniDocBench v1.6` 基准测试中取得了 **96.33%** 的新 `SOTA` 成绩，并在文本、公式和表格识别上超越了现有的开源与闭源方案。

新版本引入了区域感知数据优化框架和渐进式后训练方案，显著提升了表格、中文古籍、生僻字及印章等复杂场景的识别能力。

其模型架构与 `PaddleOCR-VL 1.5` 完全兼容，支持零成本即插即用迁移。

目前已通过 **Hugging Face** 等渠道开源。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/4e96f143-846f-4bb0-a7b2-1b6c5304bd1d/m001.png)

相关链接：
- [https://x.com/PaddlePaddle/status/2059990434827661769](https://x.com/PaddlePaddle/status/2059990434827661769)
- [https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)

---

## [商汤开源 SenseNova-U1-8B-MoT-Infographic 模型](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-Infographic) `#6`
> **商汤**发布并开源了 `SenseNova-U1-8B-MoT-Infographic` 模型。官方称该模型提升了高密度信息图的文字准确率与排版稳定性，在相关基准测试中达到开源 **SOTA** 水平。

**商汤**官方正式发布升级版信息图生成模型 `SenseNova-U1-8B-MoT-Infographic`，重点强化了高密度视觉信息的生成能力。

官方表示，该模型在文字准确率、排版合理性、图表质量及学术页面渲染方面均有所增强，能够支持 **100** 种以上风格与布局的复杂内容生成。

根据官方公布的评测数据，其在 `BizGenEval` 和 `IGenBench` 等基准测试中达到开源模型中的最先进水平。

目前，该模型已在 `Hugging Face` 平台开源。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/efb71f1f-be17-4657-821b-9cd22e707ef2/m001.png)

相关链接：
- [https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-Infographic](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-Infographic)

---

## [Liquid AI 发布 LFM2.5-8B-A1B 设备端模型](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF) `#7`
> **Liquid AI** 发布 `LFM2.5-8B-A1B` 模型。该模型具有**128K** 上下文，官方称其性能可媲美参数量大 **4** 倍的同类 `MoE` 模型。

**Liquid AI** 正式发布 **LFM2.5-8B-A1B** 模型，这是一款专为手机、笔记本、PC 和机器人等设备优化的混合专家模型。

该模型总参数量为 **8B**，活跃参数量为 **1.5B**，支持 `128K 上下文`，并在 **38T tokens** 上进行了训练。

官方称其可在单台机器上实现完整的 `Agent` 循环，具备快速的工具调用能力，且性能可媲美参数量大 **4** 倍的其他 `MoE 模型`。

目前模型权重已在 **Hugging Face** 开放，采用 `LFM2 开放权重许可证`，并实现了对 **AMD**、**Intel**、**Apple** 等多家硬件平台的 `Day 0 推理`支持。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/15204c44-1960-428d-a170-bdb30533dbf7/m001.png)

相关链接：
- [https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF)

---

## [Bagel Labs 发布 Paris 2.0 去中心化视频生成模型](https://huggingface.co/bageldotcom/paris2) `#8`
> **Bagel Labs** 团队发布了 `Paris 2.0` 视频生成模型。官方称这是首个去中心化训练视频生成模型。该模型权重已在 **Hugging Face** 上有限度开放。

**Bagel Labs** 团队正式发布了 **Paris 2.0** 去中心化扩散模型，旨在解决地理分布式异构 `GPU` 上的视频生成训练难题。

该模型包含 **3** 个独立的 `11B` `Flux MM-DiT` 专家模型。训练时各模型独立处理数据切片且不交换任何梯度或参数，仅在推理阶段通过轻量级路由器进行专家选择。

官方数据显示，在匹配总算力的条件下，**Paris 2.0** 的 `FVD` 指标降至 **279.01**，表现优于同等条件下训练的单体模型，且 `CLIP` 对齐度与美学评分均有所提升。

模型权重目前已上线 **Hugging Face** 平台，仅限研究与评估使用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/78bd2b45-7399-4f22-b5ee-46655f7d71b0/m001.png)

相关链接：
- [https://huggingface.co/bageldotcom/paris2](https://huggingface.co/bageldotcom/paris2)
- [https://arxiv.org/abs/2605.26064](https://arxiv.org/abs/2605.26064)

---

## [ElevenLabs 推出支持 90 多种语言的 Dubbing v2](https://elevenlabs.io/dubbing-studio) `#9`
> **ElevenLabs** 发布了 `Dubbing v2`配音模型。该模型直接处理原始音频，能在**90**多种语言的翻译中保留原说话人的情感、语气和声音特征，并通过`同步感知逻辑`实现配音精准对齐。

**ElevenLabs** 正式发布 `Dubbing v2` 语音配音模型。

官方表示，该模型直接基于原始声音表现进行音频到音频处理，从而在翻译时保留原说话人的情感、语气、节奏及声音克隆特征。

该模型支持 **90 多种**语言及口音，内置具备同步感知能力的`翻译逻辑`以实现声音对齐。

`Dubbing v2` 现已在 **ElevenCreative** 和 **ElevenProductions** 平台上线，并在**未来 7 天**内为不同订阅计划的用户提供 **1 到 30 分钟**不等的免费使用额度。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/3359f49f-4faf-490b-9873-7f19e7bc5156/m001.png)

相关链接：
- [https://elevenlabs.io/dubbing-studio](https://elevenlabs.io/dubbing-studio)

---

## [ElevenLabs 发布 Music v2 模型，支持跨流派无缝转换与局部重绘](https://elevenlabs.io/blog/introducing-music-v2) `#10`
> **ElevenLabs** 近期发布了 `Music v2` 音乐模型，支持在同一首歌内无缝融合歌剧与重金属风格，并新增局部重绘功能，现已正式上线。

**ElevenLabs** 近期发布了全新升级的 AI 音乐生成模型 `Music v2`，提升了全流派的人声、器乐和编曲质量。

该模型能够在同一首歌曲中实现从歌剧到重金属、快节奏说唱的无缝过渡，甚至可嵌入非音乐类音效，同时保持音乐的连贯性。

新版本引入了改进的局部重绘功能，允许用户逐段重新生成特定部分而不影响其余内容，且多语言支持得到显著增强。

`Music v2` 现已在 `ElevenMusic` 和 `ElevenCreative` 平台全面上线，即将登陆 `ElevenAPI`。

官方同步下调了相关服务的**收费标准**，并确认所有生成的音轨均可用于商业用途。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/82c79641-c86c-4a31-b148-84a20ffd92dc/m001.png)

相关链接：
- [https://elevenlabs.io/blog/introducing-music-v2](https://elevenlabs.io/blog/introducing-music-v2)

---

## [Nano Banana 系列模型 GA，可通过 Gemini API 投入生产使用](https://x.com/googleaidevs/status/2060068093485895978) `#11`
> **Google** 宣布将 `Nano Banana Pro` 和 `Nano Banana 2` 两款图像生成模型正式转为GA，现可通过 `Gemini API` 投入生产环境使用。

**Nano Banana Pro**（对应 `Gemini 3 Pro Image`）与 **Nano Banana 2**（对应 `Gemini 3.1 Flash Image`）现已作为正式版发布。

其中 **Nano Banana 2** 的定价为每张图片 **0.045 美元**，并支持视频输入，能够分析视频片段以生成具有上下文感知能力的图片、缩略图和信息图。

**Nano Banana Pro** 的定价为每张 **0.134 美元**。

两款模型均通过 `Gemini API` 提供，开发者可立即用于生产环境。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/c968f8a5-1a2c-4b64-9fec-34eda697c138/m001.png)

相关链接：
- [https://x.com/googleaidevs/status/2060068093485895978](https://x.com/googleaidevs/status/2060068093485895978)

---

## [Antigravity CLI 1.0.3 发布：支持配额耗尽后使用 Google AI credits](https://x.com/shengzheyao/status/2059814938609332726) `#12`
> **Antigravity CLI** 发布 `1.0.3`版。该版本新增配额耗尽时启用 **Google AI credits** 的功能，同时改进了 `/diff` 体验并修复多项关键问题。

**Shengzhe** 宣布推出 `Antigravity CLI 1.0.3`。

新版本允许用户在原有配额耗尽时使用 **Google AI credits**，可通过 `/config -> UseF1Credits` 开启该功能，并使用 `/credits` 查询余额。

此外，此次更新还增强了 `Apple Terminal` 的 logo 显示效果与色彩方案预览面板。

同时，改善了 `/diff` 使用体验，并修复了多项关键问题。

相关链接：
- [https://x.com/shengzheyao/status/2059814938609332726](https://x.com/shengzheyao/status/2059814938609332726)

---

## [腾讯混元发布 Hy-Memory 插件提升 Agent 长期记忆能力](https://memory.hunyuan.tencent.com/) `#13`
> **腾讯混元**正式发布专为 `Openclaw` 等长期协作型 `Agent` 打造的 **`Hy-Memory`** 记忆插件，官方称其通过**6层记忆框架**与**演化链技术**解决记忆碎片化问题。

**腾讯混元**正式发布 **`Hy-Memory`** 记忆插件，专门为 **`Openclaw`** 这类长期协作型 `Agent` 设计，旨在解决长期任务中的记忆漂移和降级使用问题。

该插件采用 **6层记忆框架**、`System1`/`System2` 双系统以及演化链结构，通过 `supersedes` 指针串联新旧记忆，确保 `Agent` 在更新判断时不会丢失历史因果。

用户目前可通过单行命令将其安装至 **`Openclaw`**，默认使用 **`Chroma`** 本地嵌入式向量库，无需额外部署外部服务，并提供 **`Lite`**、**`Pro`** 和 **`Ultra`** 三种配置模式。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260529/20260529082051_4eec39d67a.png)

相关链接：
- [https://memory.hunyuan.tencent.com/](https://memory.hunyuan.tencent.com/)

---

## [Firecrawl 发布 Monitoring 网页变更监控功能](https://x.com/firecrawl/status/2060042535003701523) `#14`
> **Firecrawl** 发布 **Monitoring** 功能，系统在网页变动时仅提取变化并通知 `Agent`，官方称最高减少 **90%** 的 `LLM token` 消耗。

**Firecrawl** 正式发布 `Monitoring` 功能，允许用户通过输入 `URL` 并使用自然语言描述需求来设定网页追踪目标。

该功能支持追踪特定页面元素或整页内容。

用户可自定义内容过滤器、抓取行为以及监控频率，且系统仅在目标页面发生实际变化时才会触发通知。

触发后，系统会通过 `webhook` 或邮件发送包含详细差异对比及永久链接的通知。

官方表示，由于仅摄取变动内容，此举最高可减少 **90%** 的 `LLM token` 消耗。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/32455386-366b-4f54-88ee-831c6e6c0896/m001.png)

相关链接：
- [https://x.com/firecrawl/status/2060042535003701523](https://x.com/firecrawl/status/2060042535003701523)

---

## [Nous Research 发布 Hermes Agent v0.15.0 版本](https://x.com/Teknium/status/2060088572049559893) `#15`
> **Nous Research** 官方发布 `Hermes Agent` v0.15.0 版本，新增对 `Opus 4.8` 等模型的支持及 **SpaceXAI** 集成，官方称其会话搜索速度提升达 **750** 倍。

**Nous Research** 官方正式发布 `Hermes Agent v0.15.0` 版本。

该版本合并了来自 **321** 名贡献者的 **747** 个 PR。

此次更新新增了对 `Krea 2`、`Opus 4.8`、`Qwen 3.7` 等模型的支持以及深度的 `SpaceXAI` 集成，并引入了 `Skill Bundles` 与 `MCP Catalog`。

官方称此次性能优化使加载时间缩短 **50%**、会话搜索速度大幅提升 **750** 倍。

同时在安全层面加入了 `Bitwarden` 原生集成等防护机制。

用户现可通过运行 `hermes update` 命令获取更新。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/e708c704-aa5a-4780-a8bf-a637ee62e156/m001.png)

相关链接：
- [https://x.com/Teknium/status/2060088572049559893](https://x.com/Teknium/status/2060088572049559893)

---

## [OpenClaw 更新 v2026.5.27：官方称包体积缩小 59%，强化安全边界](https://openclaw.ai/blog/lighter-core-sharper-claws/) `#16`
> **OpenClaw** 发布 **2026.5.27** 版本，官方称其稳定冷启动 `Agent` 轮次提速 **2.9** 倍，发布包体积缩小 **59%**，同时收紧运行时安全边界。

**OpenClaw** 正式发布 **2026.5.27** 版本。

官方数据显示其稳定冷启动 `Agent` 轮次提速 **2.9** 倍至 **3.4** 秒，发布包体积缩小 **59%** 至 **17.8 MB**。

新版本收紧了运行时安全边界，提前拦截不安全的 `Node` 环境覆盖等输入，提升了 `Codex`内存稳定性与 `hook relay` 的重启恢复能力，并将 `Pixverse` 视频生成、`OpenAI` 兼容嵌入等功能引入核心或插件。

同时，官方公开了包含完整测试证据的发布仓库。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260529/20260529080815_82ebb3e301.png)

相关链接：
- [https://openclaw.ai/blog/lighter-core-sharper-claws/](https://openclaw.ai/blog/lighter-core-sharper-claws/)
- [https://github.com/openclaw/releases/blob/main/evidence/2026.5.27/release-evidence.md#mock-provider](https://github.com/openclaw/releases/blob/main/evidence/2026.5.27/release-evidence.md#mock-provider)

---

## Mistral AI 将 Le Chat 更名为 Vibe 并推出 Work 与 Code 模式 `#17`
> **Mistral AI** 宣布将 `Le Chat` 更名为 `Vibe`，升级为面向长周期生产力与编码的统一 **Agent**，同步上线 **Work 模式**、**Code 模式**及全新 `VS Code` 扩展。

**Mistral AI** 正式将其对话产品 `Le Chat` 更名为 **Vibe**，定位为执行长周期、多步骤复杂任务的统一 `Agent`。

全新上线的 `Work` 模式支持接入 `Google Workspace` 等办公工具执行计划与搜索。

`Code` 模式则在网页端提供隔离沙盒以实现并行编码和自动提交 `PR`，同时推出了配合该模式的 `VS Code` 扩展。

据媒体报道，此举旨在与 **OpenAI** 等公司的同类 `Agent` 展开竞争，且 `Pro` 订阅价格已下调至每月 **14.99 美元**。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/e93271c1-bd15-41ae-84b8-b14ab16a574e/m001.png)

---

## [Perplexity AI 助手 Computer 上线插件接入 Microsoft 365](https://www.perplexity.ai/hub/products/integrations/microsoft) `#18`
> Perplexity AI 宣布其产品 **Computer** 集成至 **Microsoft 365**。用户可在 **Word**、**Excel** 等应用内直接起草、分析与联网搜索，插件已上架 **微软应用商店**。

**Perplexity AI** 宣布，其 AI 助手 `Computer` 现已正式集成 `Microsoft 365` 办公套件。

该助手能够根据不同任务自动分配合适的模型，并在 `Word`、`Excel`、`PowerPoint`、`Outlook` 和 `Teams` 等应用中提取上下文。

这让用户无需切换标签页或复制粘贴即可完成起草、分析和研究工作。

目前，`Computer` 支持连接企业内部 `SharePoint` 及其他第三方工具。

相关集成插件已上线 **Microsoft Marketplace** 供用户安装使用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/34cc8cca-5f6e-4fb0-b988-21c79d3257e3/m001.png)

相关链接：
- [https://www.perplexity.ai/hub/products/integrations/microsoft](https://www.perplexity.ai/hub/products/integrations/microsoft)
- [https://marketplace.microsoft.com/en-us/product/WA200010847?tab=Overview](https://marketplace.microsoft.com/en-us/product/WA200010847?tab=Overview)

---

## [微软重构 Microsoft 365 Copilot 并提升加载速度](https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/) `#19`
> **微软**近日重构 `Microsoft 365 Copilot`。官方称新版应用加载速度提升超 **50%**，并引入统一的跨应用入口，将静态提示框升级为任务感知系统。

**微软**近日正式推出 **Microsoft 365 Copilot** 的全新设计方案，对独立应用及其在 `Word`、`Excel` 等办公软件中的交互界面进行了全面重构。

新设计将原本的静态提示框转变为任务感知工作区，并引入了统一的跨应用悬浮入口，支持在侧边栏直接操作或在画布内即时调用。

根据官方公布的测试数据，`Copilot` 应用的加载时间减少了 **50%** 以上，复杂提示词的响应时间也缩短了约 **10%**。

此外，官方数据显示在推出该体验后，`Copilot` 在 `Word`、`Excel`、`PowerPoint` 和 `Outlook` 中的使用量均出现了 **27%** 至 **43%** 不等的增长。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/334b3a06-6289-4645-8712-b686fe4af1dc/m001.png)

相关链接：
- [https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/](https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/)

---

## [Qwen 团队发布文生图评测基准 Qwen-Image-Bench](https://github.com/QwenLM/Qwen-Image-Bench) `#20`
> **Qwen** 团队推出文生图评测基准 **Qwen-Image-Bench** 及开源模型 **Q-Judger**。官方称该基准含 **56** 个专业创作考点，其自动评分结果与人类专家评估高度相关。

**Qwen** 团队正式发布文生图评测基准 **Qwen-Image-Bench** 以及配套的自动化评估模型 **Q-Judger**，相关数据集与代码均已开源。

该基准由专业艺术家团队参与开发，将评测维度划分为`质量`、`美学`、`对齐`、`真实世界保真度`和`创意生成` **5** 大核心支柱，并进一步细化为 **56** 个考点。

配套包含 **1000** 条中英文分层提示词。

评估模型 **Q-Judger** 基于 `Qwen3.6-27B` 微调，根据官方公布的测试数据，其自动评分结果与人类专家的专业评估具有显著相关性。

整体 **Spearman** 相关系数达到 **0.92**。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260528/20260528194955_7f0a819d48.png)

相关链接：
- [https://github.com/QwenLM/Qwen-Image-Bench](https://github.com/QwenLM/Qwen-Image-Bench)
- [https://huggingface.co/Qwen/Qwen-Image-Bench](https://huggingface.co/Qwen/Qwen-Image-Bench)

---

## [Sakana AI 提出 DiffusionBlocks 训练框架](https://x.com/SakanaAILabs/status/2059648778051924281) `#21`
> **Sakana AI** 提出 `DiffusionBlocks` 训练框架，该框架将 `Transformer` 划分为多个独立块进行训练，且性能与端到端训练相当。代码已开源。

**Sakana AI** 团队提出了名为 `DiffusionBlocks` 的框架，通过扩散解释将 `Transformer` 网络划分为多个独立可训练的块。

该方法在每次训练迭代中仅需计算**单个块**的梯度，从而将内存需求降至原先的约 **1/B**（`B` 为块数），且性能与端到端训练相匹配。

该团队在**视觉**、**图像生成**和**文本生成**等五种架构上验证了此方法，并指出其对**循环深度模型**可用单次前向传播替代昂贵的 `BPTT` 训练。

相关代码已开源，该论文被 **ICLR 2026** 接收，但目前方法仅在从零开始训练的网络上得到验证。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/884bba03-6cc1-421a-82da-732d6f9484a6/m001.png)

相关链接：
- [https://x.com/SakanaAILabs/status/2059648778051924281](https://x.com/SakanaAILabs/status/2059648778051924281)

---

## [NVIDIA发布Dynamo Snapshot：K8s推理冷启动降至5秒内](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/) `#22`
> **NVIDIA**推出`Dynamo Snapshot`，结合`CRIU`与`cuda-checkpoint`技术，将`K8s`推理冷启动降至**5秒**内，目前该实验版仅限单`GPU`的`vLLM`与`SGLang`使用。

**NVIDIA** 发布 `NVIDIA Dynamo Snapshot`，这是一种针对 `Kubernetes` 上 **AI** 推理工作负载的检查点与恢复方案。

其旨在将冷启动时间从 **数分钟** 减少至 **5秒以内**。

该方案利用 `CRIU` 恢复主机端进程状态，结合 `cuda-checkpoint` 恢复设备端 `GPU` 状态，并引入 `GPU Memory Service（GMS）` 将模型权重解耦以实现并行恢复。

目前，该功能的实验性版本已支持单 `GPU` 环境下的 `vLLM` 和 `SGLang` 工作负载。

但多 `GPU` 支持及部分性能优化仍在开发中。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/ad0c587b-3b63-44ad-a0ae-d680edede50b/m001.png)

相关链接：
- [https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/)

---

## [小米分享 AI Coding 工程化实践：VAF、VKF 与 eight-claw](https://mp.weixin.qq.com/s/l5qeFWtXtaStweOqLP7RKA) `#23`
> **小米**发文分享了**小米**零售研发团队 AI Coding 工程化实践，通过构建统一工作流 `VAF`、代码知识索引工具 `VKF` 及基于**飞书**的协作工作台 `eight-claw`，解决 `AI` 提效仅局限于个体的问题，实现组织级提效与知识沉淀。

**小米**发文分享了**小米零售研发团队**将 **AI Coding** 从个人提速推向团队提效的工程化实践，重点介绍了三个核心内部系统。

该团队指出，虽然 **AI** 提升了个体编码效率，但需求转述损耗与上下文散落导致组织整体未变快，因此必须降低工具使用门槛。

该实践通过带菜单的低门槛工作流 `VAF` 规范了开发流程，支持多服务汇聚协调并覆盖前后端及测试环节。

针对 **AI** 理解业务偏差的问题，团队构建了代码知识库 `VKF`，其 `2.0` 版本放弃了将代码转化为自然语言文档的尝试，转而作为代码的直接索引辅助 **AI** 检索。

此外，团队开发了集成于**飞书**的协作机器人 `eight-claw`，底层接入了 `Codex CLI`、`Claude Code` 等多种引擎，以“话题”为最小并行单元解决过程透明与多任务并行协作问题。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/3980e3b0-35ac-48cd-a11c-b28f8629140d/m001.png)

相关链接：
- [https://mp.weixin.qq.com/s/l5qeFWtXtaStweOqLP7RKA](https://mp.weixin.qq.com/s/l5qeFWtXtaStweOqLP7RKA)

---

## [豆包澄清“听信AI致婴儿喂养不足”传闻](https://weibo.com/7778831349/R1vRkEqCY) `#24`
> **豆包**回应婴儿喂养争议，指自媒体将“每顿”造谣为“每天”，且家长未提供完整对话背景。**豆包**同时强调`AI`内容仅供参考，不替代医嘱。

**豆包**官方针对“家长听信AI建议导致婴儿喂养不足”的媒体报道以及“每顿60ml”与“每天60ml”的争议发布澄清说明。

官方表示，经多轮测试，`豆包`会给出每日总奶量及就医建议。且涉事家长就诊时，并未提供完整的 `AI` 对话上下文。

**豆包**指出，部分自媒体将“每顿”扭曲为“每天”属于造谣。
**豆包**并重申，`AI` 内容仅供参考，不能替代专业医疗诊断。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260528/20260528195229_abed117a84.png)

相关链接：
- [https://weibo.com/7778831349/R1vRkEqCY](https://weibo.com/7778831349/R1vRkEqCY)

---

## [Linux Foundation 发布 OpenMDW-1.1，NVIDIA 宣布采用该模型许可证](https://openmdw.ai/) `#25`
> **Linux Foundation** 发布专为 **AI** 模型打造的宽松许可证 **OpenMDW**，**NVIDIA** 宣布在 `Cosmos`、`Nemotron` 等多个开源模型系列中采用该框架以简化许可。

**Linux Foundation** 发布了专为 AI 模型设计的宽松统一许可证 **OpenMDW-1.1**，该框架覆盖模型权重、代码、数据和文档。

**NVIDIA** 宣布正在其开源模型系列中采用该框架，旨在通过单一法律体系减少开发者和企业的法律摩擦。

此举将具体应用于 `Cosmos`、`Isaac GR00T`、`Ising` 和 `Nemotron` 等模型家族。

开发者只需将许可证文件复制到代码库根目录即可完成应用，且该许可证不强制要求发布特定的模型组件。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/4ed6b4e2-6ca0-4bc3-adb2-6bd1f80013e2/c144e498-0e4a-452c-bcc5-480f28dcaafd/m001.png)

相关链接：
- [https://openmdw.ai/](https://openmdw.ai/)
- [https://x.com/NVIDIAAI/status/2060035668655677804](https://x.com/NVIDIAAI/status/2060035668655677804)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。