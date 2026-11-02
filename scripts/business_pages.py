"""A concise bilingual reading shelf for AI, products and long-term change."""


def write_business(write, T):
    write('business/index.md', T('''# AI 商业认知

理解 AI 如何改变软件、产品和工作。这里从技术趋势读到应用落地，再用研究报告观察实际变化。

**先读：** [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) → [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) → [One Useful Thing](https://www.oneusefulthing.org/) → [AI Engineering](https://huyenchip.com/books/)。长期视角看《5000天后的世界》，行业变化看 OpenAI 与 Anthropic 的报告。

## 技术与长期方向

| 资料 | 看什么 |
| --- | --- |
| **[Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35)** · Andrej Karpathy<br>2017 · 文章<br>[官方博客](https://karpathy.github.io/) | 用数据与训练得到模型，如何改变传统的软件开发。关注数据、模型与工程师职责的变化，是理解 AI 产品形态的起点。 |
| **[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)** · Richard Sutton<br>2019 · 文章<br>[大学课程 PDF 备份](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf) | 从棋类、语音与视觉的历史讨论：能持续利用更多计算的搜索与学习方法，为什么有长期优势。适合理解规模化路线与方法选择。 |
| **《5000天后的世界》** · Kevin Kelly<br>书籍 · [原版出版社](https://www.php.co.jp/books/detail.php?isbn=978-4-569-85050-4) | 以“镜像世界”、AI 与数字空间讨论长期技术生活图景。用于拓宽时间尺度、寻找可能的产品场景；它呈现的是作者的未来观点。 |

## 产品与组织

| 资料 | 看什么 |
| --- | --- |
| **[One Useful Thing](https://www.oneusefulthing.org/)** · Ethan Mollick<br>博客 / 通讯 · [文章归档](https://www.oneusefulthing.org/archive) | 从研究与使用经验讨论 AI 对工作、教育和组织的影响。适合持续了解人机协作、工作方式与管理问题。 |
| **[AI Engineering](https://huyenchip.com/books/)** · Chip Huyen<br>2025 · 书籍 | 基于基础模型构建应用的完整过程：模型选择、评测、数据、部署与成本。适合把“能演示”推进到“能交付”的开发者与产品人员。 |
| **[Building effective agents](https://www.anthropic.com/research/building-effective-agents)** · Anthropic<br>2024 · 工程文章 | 区分固定工作流与自主 Agent，比较常见架构的用途。重点看任务表现、延迟与成本的取舍，帮助判断产品需要多大程度的自主性。 |

## 官方研究报告

| 报告 | 看什么 |
| --- | --- |
| **[GPT-4 Technical Report](https://openai.com/index/gpt-4-research/)** · OpenAI<br>2023 · [论文 PDF](https://cdn.openai.com/papers/gpt-4.pdf) | 了解模型能力、评测方式、局限与安全评估。重点读任务表现和失败案例，建立判断模型适用范围的依据。 |
| **[Claude 模型报告与系统卡](https://www.anthropic.com/transparency)** · Anthropic<br>官方报告入口 | 按模型查看能力与安全评估，再进入完整系统卡。比较结果时留意模型版本、工具配置和评测条件。 |
| **[The State of Enterprise AI](https://openai.com/index/the-state-of-enterprise-ai-2025-report/)** · OpenAI<br>2025 · [报告 PDF](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf) | 基于企业客户使用数据和员工调查，观察 AI 怎样进入业务流程，以及组织如何衡量收益。读数据来源、采用方式和实施条件。 |
| **[Anthropic Economic Index](https://www.anthropic.com/economic-index)** · Anthropic<br>系列报告 · [经济测量框架](https://www.anthropic.com/research/economic-index-primitives) | 通过 Claude 的使用样本研究任务、自动化与人机协作。按任务看工作变化，同时留意平台样本、成功率与测量口径。 |
| **[GPTs are GPTs](https://openai.com/index/gpts-are-gpts/)** · OpenAI / 学术合作者<br>2023 · 研究论文 | 分析美国职业中的任务与大模型能力如何对应。关注“任务受影响的潜力”这一口径，区分技术可做什么与实际采用进度。 |
''', '''# AI & Business

Understand how AI changes software, products and work. Start with technical shifts, move to building useful applications, then look at evidence of adoption.

**Start with:** [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) → [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) → [One Useful Thing](https://www.oneusefulthing.org/) → [AI Engineering](https://huyenchip.com/books/). Read Kevin Kelly for a longer horizon, and OpenAI and Anthropic reports for industry observations.

## Technology and the Long View

| Resource | What to look for |
| --- | --- |
| **[Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35)** · Andrej Karpathy<br>2017 · Essay<br>[Official blog](https://karpathy.github.io/) | How models learned from data change software development. Follow the changing roles of data, models and engineers as a starting point for understanding AI products. |
| **[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)** · Richard Sutton<br>2019 · Essay<br>[University course PDF copy](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf) | Historical examples from games, speech and vision explain the long-term strength of search and learning methods that can use increasing computation. Read it to understand scaling and research choices. |
| **The World 5,000 Days from Now** · Kevin Kelly<br>Book · [Original Japanese publisher](https://www.php.co.jp/books/detail.php?isbn=978-4-569-85050-4) | Kelly's vision of a mirror world, AI and digital environments. Use it to explore longer time horizons and possible product contexts. |

## Products and Organizations

| Resource | What to look for |
| --- | --- |
| **[One Useful Thing](https://www.oneusefulthing.org/)** · Ethan Mollick<br>Blog / newsletter · [Archive](https://www.oneusefulthing.org/archive) | Research and practical experience on AI in work, education and organizations. Follow it for human-AI collaboration, changes in work and management questions. |
| **[AI Engineering](https://huyenchip.com/books/)** · Chip Huyen<br>2025 · Book | Building applications with foundation models: model selection, evaluation, data, deployment and cost. Useful for developers and product teams moving from a demo to a usable service. |
| **[Building effective agents](https://www.anthropic.com/research/building-effective-agents)** · Anthropic<br>2024 · Engineering article | Distinguish predefined workflows from autonomous agents and compare common patterns. Focus on performance, latency and cost when deciding how much autonomy a product needs. |

## Official Research and Reports

| Report | What to look for |
| --- | --- |
| **[GPT-4 Technical Report](https://openai.com/index/gpt-4-research/)** · OpenAI<br>2023 · [Paper PDF](https://cdn.openai.com/papers/gpt-4.pdf) | Capabilities, evaluation methods, limitations and safety assessments. Read task results and failure cases to understand where a model can be useful. |
| **[Claude model reports and system cards](https://www.anthropic.com/transparency)** · Anthropic<br>Official report hub | Select a model to review capabilities and safety evaluations, then open its full system card. Compare model versions, tool configurations and evaluation conditions. |
| **[The State of Enterprise AI](https://openai.com/index/the-state-of-enterprise-ai-2025-report/)** · OpenAI<br>2025 · [Report PDF](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf) | Enterprise customer usage and worker surveys show how AI enters business workflows and how organizations assess value. Look at data sources, adoption patterns and implementation conditions. |
| **[Anthropic Economic Index](https://www.anthropic.com/economic-index)** · Anthropic<br>Report series · [Measurement framework](https://www.anthropic.com/research/economic-index-primitives) | Claude usage samples inform research on tasks, automation and human-AI collaboration. Look at task-level changes, platform sampling, success rates and measurement definitions. |
| **[GPTs are GPTs](https://openai.com/index/gpts-are-gpts/)** · OpenAI / academic collaborators<br>2023 · Research paper | Examines how tasks in US occupations align with language-model capabilities. Distinguish potential task exposure from actual adoption and measured employment changes. |
'''))
