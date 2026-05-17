# [2026-05-17](https://github.com/imjuya/juya-ai-daily/issues/93)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260517/2026051708463064671837b1_cover_9e23.png)

# AI 早报 2026-05-17

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1VpL76LEwA) ｜ [YouTube](https://www.youtube.com/watch?v=Xl2offmOHZM)

## 概览
### 开发生态
- Codex发布更新：自定义快捷键、Git优化与大幅性能提升 [↗](https://x.com/OpenAIDevs/status/2055717793841221796) `#1`
- Codex 修复 GPT-5.5 性能下降问题并重置付费用户额度 [↗](https://x.com/thsottiaux/status/2055707616605835333) `#2`
- Vercel Labs 推出面向 Agent 的实验性编程语言 Zero [↗](https://github.com/vercel-labs/zero) `#3`
### 产品应用
- 微信读书推出 AI 助手 Skill [↗](https://weread.qq.com/r/weread-skills) `#4`
### 行业动态
- OpenAI 与马耳他政府合作向完成培训的公民提供一年免费 ChatGPT Plus [↗](https://openai.com/index/malta-chatgpt-plus-partnership/) `#5`
- 上海电信上线Token算力服务及免费体验活动 [↗](https://mp.weixin.qq.com/s/H8D6ClBheNj3a_Au-4LKQg) `#6`

---

## [Codex发布更新：自定义快捷键、Git优化与大幅性能提升](https://x.com/OpenAIDevs/status/2055717793841221796) `#1`
> `Codex` 发布多项功能与性能改进，现已支持自定义键盘快捷键、优化 `Git` 操作并提升线程面板和本地服务器列表体验，官方称大型仓库下 `Git` 操作提速约 **10** 至 **50** 倍，线程切换重渲染减少约 **75%**。

**OpenAI**通过其开发者社交账号宣布，根据用户反馈已为`Codex`推出一系列更新。

功能方面，键盘快捷键现可在设置中自定义，让工具适配个人工作流。**Git**关键操作（提交、推送、分支、PR 创建与状态）被移回审查流程更易触及。线程面板头像、本地服务器列表获得更整洁的加载与过滤优化。

性能上，官方称切换线程时重渲染降低约 **75%**，部分流路径实现零无谓重渲染。大型仓库中**Git**操作加速约 **10** 至 **50** 倍，UI 卡顿减少，启动与首次交互更快。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/9e230ae1-2eeb-47c1-bef2-3bf0b4b26314/bc036756-e225-48fd-8e1b-8f7e2ee489fe/m002.gif)

相关链接：
- [https://x.com/OpenAIDevs/status/2055717793841221796](https://x.com/OpenAIDevs/status/2055717793841221796)

---

## [Codex 修复 GPT-5.5 性能下降问题并重置付费用户额度](https://x.com/thsottiaux/status/2055707616605835333) `#2`
> 针对用户反馈，**Codex** 团队确认已修复导致 **`GPT-5.5`** 能力下降的两个问题，并于北京时间**17日**凌晨宣布已重置所有付费计划的使用额度。

**Codex** 团队成员 **Tibo** 发布声明称，已找到并修复了导致 `GPT-5.5` 模型在过去约 **48** 小时内对部分用户表现变差的两个问题。

作为补偿，官方已重置所有付费计划的 `Codex` 使用额度限制。

不过，**Tibo** 随后承认部分账户的重置存在传播延迟问题，团队正在就此进行排查。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260517/20260517083109_652f4cc5eb.png)

相关链接：
- [https://x.com/thsottiaux/status/2055707616605835333](https://x.com/thsottiaux/status/2055707616605835333)

---

## [Vercel Labs 推出面向 Agent 的实验性编程语言 Zero](https://github.com/vercel-labs/zero) `#3`
> **Vercel Labs** 宣布推出一款专为 **AI Agent** 打造的实验性编程语言 **Zero**，提供显式能力与 `JSON` 诊断。官方强调尚未稳定，主要供开发者试用和反馈。

**Vercel Labs** 团队在 **GitHub** 推出了一款名为 **Zero** 的新型编程语言，专门面向 **AI Agent** 的开发与运行需求设计。

官方将其定位为一种系统级语言，主打构建更小、更快的原生工具。该语言具备显式能力、可预测内存以及结构化的编译器输出。

该项目目前仍处于实验且频繁变动的阶段。虽然已在 **GitHub** 开源并提供安装脚本和 `VSCode` 插件支持，但官方强调其语言本身尚未稳定。

主要供开发者试用和反馈。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/9e230ae1-2eeb-47c1-bef2-3bf0b4b26314/39d941da-c09d-4bac-8f66-6ae713dc3316/m001.png)

相关链接：
- [https://github.com/vercel-labs/zero](https://github.com/vercel-labs/zero)
- [https://x.com/ctatedev/status/2055434061322039377](https://x.com/ctatedev/status/2055434061322039377)

---

## [微信读书推出 AI 助手 Skill](https://weread.qq.com/r/weread-skills) `#4`
> 微信读书新增 **AI** 助手 `Skill`，用户连接账号后可用 `AI` 搜书、导出笔记及分析阅读数据。

**微信读书**官方推出全新的“**微信读书 AI 助手**”`Skill`。

该功能允许用户连接个人账号，让 AI 助手随时查阅书架、分析阅读时长与偏好等数据、搜索书籍详情，并支持查看和导出个人的划线与读书笔记。

用户需下载指定的 `skill` 安装包发送给 AI 助手，并获取仅限个人可见的 `API Key` 完成配置。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/9e230ae1-2eeb-47c1-bef2-3bf0b4b26314/6b6bdcf6-34ab-4b6f-99be-d47e3cb935b6/m001.png)

相关链接：
- [https://weread.qq.com/r/weread-skills](https://weread.qq.com/r/weread-skills)

---

## [OpenAI 与马耳他政府合作向完成培训的公民提供一年免费 ChatGPT Plus](https://openai.com/index/malta-chatgpt-plus-partnership/) `#5`
> **OpenAI** 与 **马耳他政府**宣布达成合作。**马耳他**公民在完成当地大学开发的 `AI` 培训课程后，可获得为期一年的 `ChatGPT Plus` 免费使用权。

**OpenAI**与**马耳他政府**宣布建立合作伙伴关系，计划向该国全体公民推广 `ChatGPT Plus`。

根据这项官方称为“全球首创”的计划，**马耳他**公民需要先完成由**马耳他大学**开发的 **AI** 素养课程。

在完成该课程后，符合条件的参与者将由**马耳他数字创新局**分发账号，获得为期一年的 `ChatGPT Plus` 免费访问权限。

该项目第一阶段预计于 **5 月**启动，并计划随着更多本地居民及海外侨民完成课程而逐步扩大规模。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260516/20260516192901_0782256b37.png)

相关链接：
- [https://openai.com/index/malta-chatgpt-plus-partnership/](https://openai.com/index/malta-chatgpt-plus-partnership/)

---

## [上海电信上线Token算力服务及免费体验活动](https://mp.weixin.qq.com/s/H8D6ClBheNj3a_Au-4LKQg) `#6`
> 据报道，**上海电信**发布多档大模型调用`Token`资费套餐，**1 元**可享**25 万**额度点，支持话费支付。同时，限量向**上海**手机号用户提供免费**2500 万**额度体验。

据媒体报道，在近期举行的**中国电信**第六届科技节上海站，**上海电信**宣布即日起正式推出`Token`算力服务。

即日起推出多档`Token`资费套餐，支持话费支付，用户可通过API调用**30余款**主流大模型。

同时限量向上海手机号用户提供有效期一个月的`2500万`额度免费体验。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260516/20260516191514_b7a97322ca.png)

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260516/20260516191756_f05b8f27ba.png)

相关链接：
- [https://mp.weixin.qq.com/s/H8D6ClBheNj3a_Au-4LKQg](https://mp.weixin.qq.com/s/H8D6ClBheNj3a_Au-4LKQg)
- [https://mp.weixin.qq.com/s/2QcaNLJoG27StyQ7uUCzcw](https://mp.weixin.qq.com/s/2QcaNLJoG27StyQ7uUCzcw)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。