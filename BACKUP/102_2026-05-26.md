# [2026-05-26](https://github.com/imjuya/juya-ai-daily/issues/102)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260526/20260526083058289091331f_cover_2165.png)

# AI 早报 2026-05-26

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1e8VF6fEX4) ｜ [YouTube](https://www.youtube.com/watch?v=PArEvWUAjgE)

## 概览
### 模型发布
- SpaceXAI 完成 Grok V9-Medium 模型训练并预告开源计划 [↗](https://x.com/elonmusk/status/2058787384364265734) `#1`
- OpenBMB 发布 MiniCPM5-1B 开源模型 [↗](https://huggingface.co/openbmb/MiniCPM5-1B) `#2`
### 开发生态
- Grok Build 面向 SuperGrok 和 X Premium+ 用户开放 [↗](https://x.com/xai/status/2058973760708091907) `#3`
- Google Antigravity 新增 Gemini 3.5 Flash (Low) [↗](https://x.com/antigravity/status/2058741814237241812) `#4`
### 产品应用
- ima 宣布全面开放 copilot 并上线 Skill 发布功能 [↗](https://mp.weixin.qq.com/s/R22ySmNraCJ4W4o2nbJu1w) `#5`
### 技术与洞察
- 华为发布韬(τ)定律：麒麟芯片将首发逻辑折叠技术 [↗](https://mp.weixin.qq.com/s/txF-C8pXnmGwqNLFEDep8A) `#6`
### 前瞻与传闻
- 社区反馈 Claude 注册疑似取消手机验证并重开申诉 [↗](https://linux.do/t/topic/2245547) `#7`

---

## [SpaceXAI 完成 Grok V9-Medium 模型训练并预告开源计划](https://x.com/elonmusk/status/2058787384364265734) `#1`
> **Elon Musk** 宣布，`1.5T` 参数的 `Grok` 基础模型 `V9-Medium` 已完成训练并进入微调阶段，几天后启动强化学习，预计在 **2 到 3 周**内公开发布，同时他还回应网友评论称，将在 **今年年底**开源 `0.5T` 参数的模型。

**SpaceXAI** 创始人 **Elon Musk** 确认，参数量为 `1.5T` 的 `Grok` 基础模型 `V9-Medium` 已经完成训练。

官方评估结果良好，且在补充训练中加入大量 `Cursor` 数据。该模型目前正处于微调阶段。

预计几天后启动强化学习，并计划在 `2 到 3 周` 内公开发布。官方称，`V9-Medium` 将比目前承载所有 `Grok` 生产流量的 `0.5T` `v8-Small` 模型带来重大改进。

尤其针对复杂编程任务。此外，**Elon Musk** 回应网友评论时称，将在今年年底开源 `0.5T` 模型。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260525/20260525193713_90a117b166.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260525/20260525193733_3dfd2ec3e3.png)

相关链接：
- [https://x.com/elonmusk/status/2058787384364265734](https://x.com/elonmusk/status/2058787384364265734)
- [https://x.com/elonmusk/status/2058796067592736866](https://x.com/elonmusk/status/2058796067592736866)

---

## [OpenBMB 发布 MiniCPM5-1B 开源模型](https://huggingface.co/openbmb/MiniCPM5-1B) `#2`
> **OpenBMB** 开源了 `MiniCPM5-1B` 模型。该模型具备混合推理能力，登顶了 **Artificial Analysis** 小模型榜单，成为 **2B** 以下最强模型。

**OpenBMB** 正式发布并开源 `MiniCPM5` 系列的首个模型 `MiniCPM5-1B`，开放了权重、训练数据及部署代码。

该模型拥有 **10.8 亿** 参数，官方宣称其在 **Artificial Analysis** 小模型榜单中以 **17.9 分** 排名第一，成为 `2B` 以下最强开源基础模型。

模型具备混合推理能力，`INT4` 量化后体积约 **0.5GB**，可在手机、浏览器及 CPU 环境下本地运行。

据官方介绍，其预训练采用了完全由 AI 编写的 `ForgeTrain` 框架，并在后训练阶段结合了强化学习（`RL`）与在线策略蒸馏（`OPD`）技术。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/21651354-1bad-4bcc-a58f-6c8a77fd8a07/379ab54f-f736-46c1-a71d-6ef965704cbd/m001.png)

相关链接：
- [https://huggingface.co/openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)

---

## [Grok Build 面向 SuperGrok 和 X Premium+ 用户开放](https://x.com/xai/status/2058973760708091907) `#3`
> **SpaceXAI** 宣布 `Grok Build` 现已开启 `Beta` 测试，并面向所有 `SuperGrok` 和 **X Premium+** 用户开放，支持 `Plan Mode`、`Imagine` 媒体生成及通过 `CLI` 构建自动化任务。

**SpaceXAI** 宣布其 **Grok Build** 现已进入 `Beta` 阶段。

并正式向所有 `SuperGrok` 和 `X Premium+` 用户开放使用。

该平台集成了多项能力，允许用户使用 `Plan Mode` 规划任务。

利用 `Imagine` 创建图像与视频。

以及通过 `CLI` 构建自动化任务或编排器。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260526/20260526081203_e8e9be59b0.png)

相关链接：
- [https://x.com/xai/status/2058973760708091907](https://x.com/xai/status/2058973760708091907)

---

## [Google Antigravity 新增 Gemini 3.5 Flash (Low)](https://x.com/antigravity/status/2058741814237241812) `#4`
> **Antigravity** 宣布引入 `Gemini 3.5 Flash (Low)` 选项，官方称其生成 `token` 数较 `Medium` 版减少约 **45%** 以优化简单任务，同时已重置所有付费用户的配额。

**Google** 旗下 **Antigravity** 官方宣布引入 `Gemini 3.5 Flash (Low)` 模型选项，以回应用户关于简单任务消耗过多 token 的反馈。

根据官方内部测试，该模型生成的 token 数量比 `Gemini 3.5 Flash (Medium)` 减少约 **45%**，且在 `SWE` 任务上表现通常优于 `Gemini 3 Flash (High)`。

非官方消息称该模型已支持在 `IDE`、`CLI` 和桌面端应用中使用。此外，官方已重置所有付费计划的 `Gemini` 配额。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/21651354-1bad-4bcc-a58f-6c8a77fd8a07/f0212a77-262d-4889-9833-88ee09356ded/m001.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260525/20260525191641_1b9b925956.png)

相关链接：
- [https://x.com/antigravity/status/2058741814237241812](https://x.com/antigravity/status/2058741814237241812)

---

## [ima 宣布全面开放 copilot 并上线 Skill 发布功能](https://mp.weixin.qq.com/s/R22ySmNraCJ4W4o2nbJu1w) `#5`
> `ima` 宣布取消排队限制，全面开放具备记忆与知识库的 `Agent` **“copilot”**，同时知识号同步上线发布 `Skill` 功能，用户需将应用更新至最新版即可体验。

**ima** 官方宣布其 **copilot** 功能现已全面开放，取消此前的**超十万人**排队限制。

该 **copilot** 是一个拥有记忆系统与知识库的 `Agent`，具备全场景感知能力，支持在不离开当前页面的情况下读取、总结和调用知识库。

并允许用户自行接入各大模型 `API KEY`。

同时，**ima** 知识号新增了发布 **Skill** 功能，官方首批上线了 `微信读书` 与 `腾讯招聘` **Skill**。

用户可在知识广场发现或发布 **Skill**，其中 **Skill** 发布入口目前仅限 `PC` 端。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/21651354-1bad-4bcc-a58f-6c8a77fd8a07/79bd9e0d-cd80-4084-9e4c-0d654d00fa43/m001.png)

相关链接：
- [https://mp.weixin.qq.com/s/R22ySmNraCJ4W4o2nbJu1w](https://mp.weixin.qq.com/s/R22ySmNraCJ4W4o2nbJu1w)

---

## [华为发布韬(τ)定律：麒麟芯片将首发逻辑折叠技术](https://mp.weixin.qq.com/s/txF-C8pXnmGwqNLFEDep8A) `#6`
> **华为**近日提出半导体发展新原则——`韬定律`。该定律主张以“时间缩微”替代传统的“几何缩微”，通过“逻辑折叠”等创新技术压缩信号传播时延，从而持续提升晶体管密度与系统性能。

在**电气电子工程师学会**（**IEEE**）举办的国际电路系统研讨会 `ISCAS 2026`上，**华为****何庭波**发表主旨演讲，正式提出指导半导体产业发展的新原则“韬(`τ`) 定律”。

该定律主张以“时间(`τ`) 缩微”替代传统的“几何缩微”，通过"`逻辑折叠`"等创新技术压缩信号传播时延，从而持续提升晶体管密度与系统性能。

**华为**在过去六年中基于该定律已成功设计并量产`381`款芯片，即将面世的麒麟芯片将率先采用逻辑折叠技术。官方预计到`2031`年其高端芯片晶体管密度将达到`1.4`纳米制程的同等水平。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/21651354-1bad-4bcc-a58f-6c8a77fd8a07/19b08849-9d97-4a0d-8086-586cb9d53eff/m001.png)

相关链接：
- [https://mp.weixin.qq.com/s/txF-C8pXnmGwqNLFEDep8A](https://mp.weixin.qq.com/s/txF-C8pXnmGwqNLFEDep8A)

---

## [社区反馈 Claude 注册疑似取消手机验证并重开申诉](https://linux.do/t/topic/2245547) `#7`
> 据**社区**用户反馈，近期 `Claude` 账号注册疑似取消了手机号验证，同时还开放了此前被封禁账号的申诉入口。

近日有社区用户发帖表示，**Claude** 普通账号的注册门槛有所降低，使用邮箱注册时已不再强制要求验证手机号。

与此同时，部分此前被封禁的用户发现，**Claude** 官网的账号申诉入口发生了变化，原本提示错误的页面现已允许用户重新提交一次解封申请。

目前上述信息均属于社区用户的个人测试与发现，并非官方公告。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/21651354-1bad-4bcc-a58f-6c8a77fd8a07/c25701ca-5300-4024-a57e-24587ae0579b/m001.png)

相关链接：
- [https://linux.do/t/topic/2245547](https://linux.do/t/topic/2245547)
- [https://linux.do/t/topic/2243139](https://linux.do/t/topic/2243139)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。