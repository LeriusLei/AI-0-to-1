"""Short bilingual site-level pages and shared presentation."""
CSS='''/* Material documentation layout, with accessible colors and targets. */
[data-md-color-primary="light-blue"]{--md-primary-fg-color:#0077a4;--md-typeset-a-color:#006fa1}
[data-md-color-scheme="slate"]{--md-primary-fg-color:#00646f;--md-typeset-a-color:#87d5ee}
body{font-family:Arial,"Microsoft YaHei",sans-serif}
.md-nav__link{min-height:24px;align-items:center}
.md-copyright{color:#aaa}
.md-typeset table:not([class]){font-size:.74rem;line-height:1.65}
.md-typeset a{text-underline-offset:3px}
.md-typeset p a,.md-typeset li a{text-decoration:underline}
.md-typeset td a{text-decoration:underline}
.ai-language{display:inline-flex;align-items:center;gap:.25rem;min-height:36px;width:auto;font-size:.7rem;font-weight:600;padding:.3rem}
.ai-language svg{width:1rem;height:1rem;fill:currentColor}
.ai-github{display:inline-flex;align-items:center;gap:.3rem;min-height:36px;font-size:.7rem;font-weight:600;white-space:nowrap}
.ai-github svg{width:1rem;height:1rem;fill:currentColor}
@media(max-width:480px){.ai-github span{display:none}}
.resource-table td:first-child{font-weight:600}
@media(max-width:640px){
 .resource-table .md-typeset__table{display:block!important;padding:0!important;margin:0!important}
 .md-typeset .resource-table table:not([class]){display:block;width:100%;min-width:0;box-shadow:none;border:0;font-size:.77rem}
 .resource-table thead{display:none}
 .resource-table tbody,.resource-table tr,.resource-table td{display:block!important;width:100%!important;min-width:0!important;max-width:100%}
 .resource-table tr{border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;margin:0 0 16px;overflow:hidden}
 .md-typeset .resource-table td{border:0!important;padding:9px 14px!important;overflow-wrap:anywhere}
 .resource-table td:first-child{padding-top:14px!important;font-size:.86rem}
 .resource-table td:last-child{padding-bottom:14px!important;color:var(--md-default-fg-color--light)}
 .resource-table td:nth-child(3):before{content:'能做什么：';font-weight:600;color:var(--md-default-fg-color)}
 html[lang=en] .resource-table td:nth-child(3):before{content:'Outcome: '}
 .resource-table.course td:nth-child(2):before{content:'适合：';font-weight:600}
 html[lang=en] .resource-table.course td:nth-child(2):before{content:'For: '}
 .resource-table.course td:nth-child(3):before{content:'学到什么：'}
 html[lang=en] .resource-table.course td:nth-child(3):before{content:'Covers: '}
}
'''

def write_tools(write,T):
    write('tools/index.md',T('''# 必学工具

工具让课程代码能运行，让一次实验可以重新做出来。先掌握Python环境、Notebook、Git和调试，再按项目选择GPU、模型端点或Agent辅助工具。

- [如何使用](reading.md)：难度、重复课程和项目选择。
- [环境与运行](environment.md)：本地与在线Notebook、模型端点和代码辅助工具。
- [信息检索](search.md)：从官网、文档和代码查找可靠答案。
''','''# Essential Tools

Tools make course code executable and experiments reproducible. Learn Python environments, notebooks, Git and debugging first; select GPUs, model endpoints or coding assistants when a project needs them.

- [How to use this guide](reading.md): difficulty, overlap and project selection.
- [Environment and execution](environment.md): local and online notebooks, endpoints and coding tools.
- [Finding information](search.md): reliable answers in official sites, docs and code.
'''))
    write('tools/reading.md',T('''# 如何使用

先看学习路线，再进入一个方向的概览。概览直接比较课程或项目，名称进入介绍，官网和GitHub链接直接到原站。

## 难度

1 / 5：入门；2 / 5：基础；3 / 5：需要机器学习或PyTorch基础；4 / 5：进阶；5 / 5：系统或研究工程。评级是本指南的学习判断。

## 避免重复

- 鱼书、Zero to Hero、LeeDL选一种主要解释；3Blue1Brown补视觉直觉。
- Happy-LLM建立全貌，CS336深入实现。
- All-in-RAG与LLM Universe的基础知识库不必重复做。
- MiniMind练SFT/LoRA，TRL再进入偏好与RL训练。
- nano-vLLM与mini-SGLang、verl与OpenRLHF分别先选一个。
- CSAPP与CMU 15-213是同一组课程资料。

## 语言

中文和英文页面内容对应，切换会保留当前条目。课程原站、教材和视频的教学语言由原作者决定。
''','''# How to Use This Guide

Read the roadmap, then one track overview. Overviews compare resources directly; titles open an introduction, while Website and GitHub links go straight to the source.

## Difficulty

1 / 5: introductory; 2 / 5: foundational; 3 / 5: ML or PyTorch background; 4 / 5: advanced; 5 / 5: systems or research engineering. Ratings are this guide's learning estimates.

## Avoiding duplicate work

- Choose one main explanation from Deep Learning from Scratch, Zero to Hero or LeeDL; use 3Blue1Brown for intuition.
- Happy-LLM provides a conceptual map; CS336 develops implementation.
- Do not repeat the same introductory knowledge base in both RAG courses.
- Use MiniMind for SFT/LoRA, then TRL for preference and RL training.
- Initially choose one small inference engine and one distributed post-training framework.
- CSAPP and CMU 15-213 share one entry.

## Languages

Chinese and English pages correspond, and the switch preserves the current article. External resources retain their authors' teaching languages.
'''))
    write('tools/environment.md',T('''# 环境与运行

## 读代码与写Notebook

- [VS Code Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) / [JupyterLab](https://jupyter.org/)：逐单元运行、看张量形状和中间结果。
- [Python](https://www.python.org/) / [NumPy](https://numpy.org/) / [PyTorch](https://pytorch.org/learn/)：语言、数组与模型训练。
- [Git](https://git-scm.com/book/zh/v2)：保存代码、配置和实验版本。

先按数据→模型→loss→optimizer→checkpoint→推理的顺序追一条调用链，再修改一个小模块观察变化。

## 在线运行

- [Colab](https://colab.research.google.com/)：打开课程Notebook或GitHub中的.ipynb。
- [Kaggle Code](https://www.kaggle.com/code)：Notebook与公开数据。
- [Jupyter Try](https://jupyter.org/try)：无需本地安装的小型体验。

免费资源的可用时长和硬件以平台当时显示为准。CPU先跑小样本；训练和推理项目再按模型要求使用GPU。

## 模型与代码辅助

NeMo Data Designer和Agent项目通常需要模型端点；开源框架不代表模型调用免费。可以使用项目支持的云端服务或兼容的自托管模型。

- [OpenCode](https://opencode.ai/en/docs) / [Pi](https://pi.dev/)：辅助读代码、定位错误与审查修改，按需要选一种。
''','''# Environment and Execution

## Reading code and using notebooks

- [VS Code notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) / [JupyterLab](https://jupyter.org/): run cells and inspect shapes and intermediate values.
- [Python](https://www.python.org/) / [NumPy](https://numpy.org/) / [PyTorch](https://pytorch.org/learn/): language, arrays and model training.
- [Git](https://git-scm.com/book/en/v2): version code, configurations and experiments.

Trace one path through data, model, loss, optimizer, checkpoint and inference. Then change one component and inspect the result.

## Online execution

- [Colab](https://colab.research.google.com/): open a course notebook or a GitHub .ipynb.
- [Kaggle Code](https://www.kaggle.com/code): notebooks and public datasets.
- [Jupyter Try](https://jupyter.org/try): small examples without a local installation.

Free hardware and usage limits depend on current platform availability. Start with small CPU examples, then use the hardware required by the chosen model.

## Model endpoints and coding tools

Data Designer and agent projects often require a model endpoint. An open-source framework does not make model inference free. Use a supported provider or a compatible self-hosted model.

- [OpenCode](https://opencode.ai/en/docs) / [Pi](https://pi.dev/): optional help for code reading, debugging and reviewing changes.
'''))
    write('tools/search.md',T('''# 信息检索

优先查课程官网、官方文档、项目README和作者页面，先确定版本，再查具体问题。

- 课程：先修、课表、作业、公开录像。
- 项目：Quickstart、示例、硬件与维护说明。
- 论文：[arXiv](https://arxiv.org/) / [OpenReview](https://openreview.net/) / 作者主页。
- 数学：[3Blue1Brown](https://www.3blue1brown.com/)建立图像，再用教材或正式课程核对推导。

用课程名或项目名加具体概念检索，例如“CS336 tokenizer”或“FSDP2 sharding”，更容易找到对应的一手解释。
''','''# Finding Information

Start with course sites, official docs, READMEs and author pages. Establish the version before investigating a specific question.

- Courses: prerequisites, schedules, assignments and public recordings.
- Projects: quickstarts, examples, hardware and maintenance guidance.
- Papers: [arXiv](https://arxiv.org/), [OpenReview](https://openreview.net/) and author pages.
- Mathematics: use [3Blue1Brown](https://www.3blue1brown.com/) for intuition, then check derivations in a text or formal course.

Search with a resource name and a concept, such as “CS336 tokenizer” or “FSDP2 sharding”, to reach the relevant primary explanation.
'''))

def write_coverage(write,T,R,D,changes,link):
    counts={k:sum(r['kind']==k for r in R.values()) for k in ['course','project','book']}
    text='# '+T('收录与来源','Sources and Selection')+'\n\n'
    text+=T(f"{counts['course']}个课程条目、{counts['project']}个项目、{counts['book']}本书。",f"{counts['course']} course entries, {counts['project']} projects and {counts['book']} books.")+'\n\n'
    text+='## '+T('取舍','Selection')+'\n\n'
    text+=T('按教学完整性、官方维护与项目分工筛选。删除了部分重复的小实现；数学直觉、小模型和JEPA等有明确学习用途的项目继续保留。','Resources are selected for teaching value, official maintenance and distinct roles. Several duplicate implementations were removed; small-model and research implementations remain when they serve a clear learning purpose.')+'\n\n'
    for x in changes:text+='- '+x['title'].split(' · ')[0]+' → '+link(x['replacement'])+'：'+x['reason_zh' if T(True,False) else 'reason_en']+'\n'
    text+='\n## '+T('编排方式','Organization')+'\n\n'
    text+=T('公共代码主线为PyTorch→自动微分→tiny GPT→CS336 A1，再按模型训练、应用、系统或机器人方向展开。课程和项目按依赖关系衔接，相近材料提供选择建议。','The shared implementation path runs from PyTorch through autodiff and tiny GPT to CS336 A1, followed by model training, applications, systems or robotics. Prerequisites connect courses and projects; overviews help choose between overlapping resources.')+'\n\n'
    text+=T('MiniMind、MedicalGPT、Hermes、DeepSeek-V3、MCP、DeepSpeed、FSDP与Diffusion Course已对应到相关分类。OpenCode/Pi放在工具页；Gemini Robotics作为研究参考。','MiniMind, MedicalGPT, Hermes, DeepSeek-V3, MCP, DeepSpeed, FSDP and the Diffusion Course are placed in their relevant tracks. OpenCode/Pi appear under tools; Gemini Robotics is a research reference.')+'\n\n'
    text+='## '+T('版本与来源','Versions and attribution')+'\n\n'
    text+=T('2026-11-05：撤下“评测、部署与MLOps”课程分类。FSDL 2022退出当前推荐，LLM Bootcamp保留为2023年AI应用概览；未定位的CS239A退出课程目录。评测工具按模型基准、应用测试和实验记录分别介绍。','2026-11-05: removed the Evaluation, Deployment and MLOps course category. FSDL 2022 is no longer recommended; LLM Bootcamp remains a 2023 application overview. The unidentified CS239A entry is removed. Evaluation tools are distinguished by benchmarks, application tests and experiment tracking.')+'\n\n'
    text+='['+T('B站视频汇总与字幕说明','Bilibili videos and subtitle notes')+'](courses/bilibili.md)\n\n'
    text+=T('GitHub数字为2026-11-01的接口快照，不自动更新。部分Datawhale章节状态沿用2026-10-24记录，最新发布见原站。I-JEPA归档状态已标注。','GitHub counts are a snapshot from 2026-11-01 and do not update automatically. Some Datawhale publication notes retain the 2026-10-24 check; follow the source for subsequent releases. I-JEPA is marked as archived.')+'\n\n'
    text+=T('结构参考','Structure reference: ')+' [CSStudyGuide](https://github.com/ZH1995/CSStudyGuide/); '+T('采用MkDocs Material，介绍、比较与双语内容独立编写。','built with MkDocs Material. Descriptions, comparisons and bilingual content are independently written.')+'\n'
    write('coverage.md',text)
