# [test2](https://github.com/imjuya/juya-ai-daily/issues/1)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260216/202602160815074762543e8c_cover_2212.jpg)

# AI 早报 2026-02-16

## 概览
### 精选
- OpenClaw 创始人 Peter Steinberger 加入 OpenAI `#1`
### 模型发布
- 京东开源JoyAI-LLM-Flash模型 `#2`
- MiniMax上线 M2.5-HighSpeed 高速版API `#3`
### 产品应用
- 月之暗面推出 AI 助手 Kimi Claw `#4`
- MiniMax 宣布即将上线 OpenRoom `#5`
### 行业动态
- 马斯克宣布Grok 4.20下周发布 `#6`
- 谷歌发布报告披露Gemini遭滥用 `#7`

---

## OpenClaw 创始人 Peter Steinberger 加入 OpenAI `#1`
> 开源 AI 项目 **OpenClaw** 创始人 **Peter Steinberger** 加入 **OpenAI**，将推动下一代 `个人 Agent` 发展。**OpenClaw** 将转为基金会运营的独立开源项目，并获得 **OpenAI** 支持。**Steinberger** 表示，目标是打造人人可用的 `智能体`，而与 **OpenAI** 合作是实现这一愿景的最快路径。

开源 AI 智能体项目 **OpenClaw** 创始人 **Peter Steinberger** 已加入 **OpenAI**，旨在推动下一代个人 `Agent` 的开发。**Steinberger** 在其个人博客中表示，其目标是构建一个普通用户也能便捷使用的 `Agent`，并认为与 **OpenAI** 合作是将此能力带给所有人的最快方式。

**OpenAI** CEO **Sam Altman** 在社交媒体上确认了此消息，称 **Steinberger** 是一位天才，其关于智能体协同工作的想法将迅速成为 **OpenAI** 产品的核心。**Steinberger** 将在 **OpenAI** 负责驱动下一代个人 `Agent` 的发展。

至于 **OpenClaw** 项目的未来，将移转至一个基金会，作为独立开源项目持续运营，并获得 **OpenAI** 支持。**Altman** 强调，未来是“`极度多智能体`”的时代，支持开源是 **OpenAI** 愿景的重要组成部分。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/221286a1-616c-4976-8913-e8c39c44799d/fa2660ce-5694-4af4-aedc-34264b54760e/m001.png)

```
https://steipete.me/posts/2026/openclaw
https://x.com/sama/status/2023150230905159801
```

---

## 京东开源JoyAI-LLM-Flash模型 `#2`
> **京东**开源了基于 `MoE` 架构的语言模型 `JoyAI-LLM Flash`，总参数量达**48B**， 激活参数**3B**，该模型在知识、推理、编程与智能体任务上表现优异，已发布于 **Hugging Face**。

**京东集团探索研究院**推出并开源了全新模型`JoyAI-LLM-Flash`。该模型是基于`混合专家系统架构`的中型指令语言模型，拥有**480亿总参数**和**30亿激活参数**，专为`工具使用`、`推理`和`自主问题解决`设计。

性能评估显示，该模型在**19**个权威基准测试中综合表现领先。数学能力上，`MATH 500`得分**97.10**；编程能力上，`HumanEval`得分**96.34**；`Agentic`能力上，`SWE-bench Verified`得分**60.60**。但在与`GLM-4.7-Flash`的对比中，其`Tau2-Telecom`基准得分**79.83**，略低于后者的**88.60**。模型在长上下文处理上表现稳定，`RULER`基准得分**95.60**。

该模型在**20万亿**`token`上`预训练`，并融合了三项关键技术：其一为`Fiber Bundle RL`，引入`FiberPO`优化框架以提升`训练稳定性`；其二是`Training-Inference Collaboration`，通过带`dense MTP`的`Muon优化器`，实现了**1.3**至**1.7**倍的`吞吐量`提升；其三为`Agentic Intelligence`，以强化核心的`推理`与`工具调用`能力。

模型权重与代码采用`Modified MIT License`在**Hugging Face**开源，同步提供了官方`API`及与**OpenAI**、**Anthropic**兼容的`API`接口，方便用户`部署`与`集成`。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/221286a1-616c-4976-8913-e8c39c44799d/2ccda77a-5436-4e2e-9cad-a7452b3fd332/m001.png)

```
https://huggingface.co/jdopensource/JoyAI-LLM-Flash
```

---

## MiniMax上线 M2.5-HighSpeed 高速版API `#3`
> **MiniMax**上线`M2.5-HighSpeed`，速度达**100TPS**。模型已在`API`中上线，同时上线了极速版`Coding Plan`，提供 `Plus`、`Max`、`Ultra`三档。

**MiniMax**上线了专为Agent应用场景设计的新型号`MiniMax-M2.5-HighSpeed`。据官方称，该模型支持**100 TPS**的极速推理，速度为同类产品的**3**倍。其对应极速版`Coding Plan`与`API`接口已同步上线，`Plus`、`Max`与`Ultra`三档规格套餐均可用。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/221286a1-616c-4976-8913-e8c39c44799d/c7d48d38-c487-4cbe-b8dc-92e3900ee656/m001.png)

```
https://mp.weixin.qq.com/s/xOjcMFjA46QdidYJOhK9gw
```

---

## 月之暗面推出 AI 助手 Kimi Claw `#4`
> **月之暗面**推出 `Kimi Claw`，一个集成于 **kimi.com** 中的 `OpenClaw 框架` 实现。支持 **7*24** 小时运行。目前已上线 **Beta** 测试，支持 **Allegretto** 及以上套餐用户。

**Moonshot AI** 推出集成于 **kimi.com** 的 **Kimi Claw**（`OpenClaw` 框架实现），提供 **7×24 小时**云端 AI Agent 环境。该功能目前处于 `Beta` 测试阶段，面向 **Allegretto** 及以上套餐用户（据称需 **199 元/月**及以上）。

核心功能包括：`ClawHub` 技能库（**5000+** 社区技能）支持无代码集成；**40GB** 云存储优化 `RAG` 流程；**Pro-Grade Search** 提供 **Yahoo Finance** 等实时结构化数据；`BYOC` 模式允许接入自托管实例。

技术层面，**Kimi Claw** 运行在基于 `KVM/QEMU` 的 `Ubuntu 24.04 LTS` 虚拟化环境中，配置为 **2** vCPU（`Intel Xeon Platinum 8582C`）、**3.8GB** 内存、**40GB** 存储，默认使用 `Kimi K2.5 Thinking` 模型并支持定时任务。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/221286a1-616c-4976-8913-e8c39c44799d/b554ffc7-e448-4870-a6f7-5333f374d6a7/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/221286a1-616c-4976-8913-e8c39c44799d/b554ffc7-e448-4870-a6f7-5333f374d6a7/m002.png)

```
https://www.kimi.com/bot
```

---

## MiniMax 宣布即将上线 OpenRoom `#5`
> **MiniMax** 推出名为 **OpenRoom** 的首个 `agent-native` playground，支持用户探索由 `agent` 构建的 `多模态` 动态世界，并与 `agent` 互动。平台目前处于“即将上线”阶段，可通过加入官方社区获取访问。

**MiniMax** 推出 **OpenRoom**，定位为 **首个** `agent-native` `playground`。该平台允许用户探索由 `agent` 构建的动态多模态世界，并体验 `agent` 与人类之间的互动。用户可与不同 `agent` 建立连接，并让其在环境中主导运行。

产品目前状态为“Coming soon”，正根据真实用户的反馈进行快速迭代和演化。早期访问权限可通过加入其社区获取。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/221286a1-616c-4976-8913-e8c39c44799d/eb972b87-f05c-42c7-b0c3-82e6ee7fa0a3/m001.png)

```
https://www.openroom.ai/
https://x.com/MiniMax_AI/status/2023059842542485683
```

---

## 马斯克宣布Grok 4.20下周发布 `#6`
> **Elon Musk** 宣布 `Grok 4.20` 将于下周发布，相比 `4.1` 版本有显著升级。

**马斯克**称`Grok 4.20`下周发布，较`4.1`显著改进。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/221286a1-616c-4976-8913-e8c39c44799d/c094f103-37e3-48f8-aca6-a31757901161/m001.png)

```
https://x.com/elonmusk/status/2022921927791382896
```

---

## 谷歌发布报告披露Gemini遭滥用 `#7`
> **Google**威胁情报团队报告称，**2025年第四季度**，黑客加速利用`AI`实施攻击，包括`模型提取`、`AI钓鱼`及`恶意软件开发`。**Google**已禁用违规账户，强化安全控制，并推出`SAIF框架`与防御工具应对`AI`滥用风险。

**Google Threat Intelligence Group** (**GTIG**) 发布了一份报告，详细说明了威胁行为者对人工智能的滥用情况，包括 `模型提取攻击`、`AI增强的钓鱼活动` 以及新型 `AI集成恶意软件` 的开发。报告指出，在 **2025年第四季度** 观察到威胁行为者日益整合AI以加速攻击生命周期，但目前尚未发现政府背景的 `APT` 组织对前沿模型或生成式AI产品发起直接攻击。**Google** 已采取行动，包括禁用相关账户，并加强了安全控制与 `Gemini模型` 以防止滥用。

```
https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gtig-report-ai-cyber-attacks-feb-2026/
https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use
```

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。

作者`橘鸦Juya`，视频版在同名**哔哩哔哩**。欢迎**点赞、关注、分享**。