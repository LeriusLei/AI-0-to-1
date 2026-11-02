"""Human-authored bilingual descriptions, audiences and resource comparisons."""

def rows(text, fields):
    result = {}
    for line in text.strip().splitlines():
        values = [v.strip() for v in line.split('|')]
        assert len(values) == len(fields) + 1, (len(values), line)
        result[values[0]] = dict(zip(fields, values[1:]))
    return result

# id | English title | Chinese audience | Chinese introduction | English audience | English introduction | English prerequisites
COURSES = rows('''
cs50 | CS50: Introduction to Computer Science | 零基础，想先建立计算机与编程全貌的人。 | 从Scratch和C讲到算法、内存、Python、SQL与Web，配套每周习题和最终项目。比CS50P覆盖更广，也需要更多时间。 | Beginners seeking a broad introduction to computer science. | Covers Scratch, C, algorithms, memory, Python, SQL and the web, with weekly problem sets and a final project. Broader than CS50P. | No prior programming required.
python_numpy | Python and NumPy | 会一点编程，需要补Python语法和数组运算的人。 | Python官方教程讲语法、函数、模块和异常；NumPy Quickstart讲数组、索引、广播与矩阵运算。适合查缺补漏。 | Learners moving into Python and numerical computing. | Python's tutorial covers language fundamentals; NumPy introduces arrays, indexing, broadcasting and matrix operations. Useful as a focused reference. | Basic computer use; some programming helps.
pytorch | PyTorch: Training Fundamentals | 会Python，准备第一次自己训练模型的人。 | 从Tensor和autograd进入数据加载、模型、损失、优化器与保存加载，串成完整训练流程。 | Python users writing their first training loop. | Connects tensors and autograd to data loading, models, losses, optimizers and checkpoints. | Python, NumPy and basic derivatives.
zero_to_hero | Neural Networks: Zero to Hero | 想把神经网络原理对应到每行代码的人。 | 依次构建micrograd、字符语言模型和GPT，讲解反向传播、训练调试与生成。与鱼书选择一套作为原理主课。 | Learners who want to connect neural-network concepts to code. | Builds micrograd, character language models and GPT while explaining backpropagation and training. Choose this or a comparable introductory book as the main implementation course. | Python and basic calculus.
cs229 | CS229: Machine Learning | 有线代、概率和微积分基础，想系统学习统计学习的人。 | 讲线性与逻辑回归、生成式方法、核方法、学习理论和无监督学习，侧重数学推导与习题。 | Learners seeking a mathematical foundation in machine learning. | Studies regression, classification, generative methods, kernels, learning theory and unsupervised learning through derivations and problem sets. | Linear algebra, probability, multivariable calculus and Python.
cs224n | CS224N: NLP with Deep Learning | 已学深度学习，想理解语言模型与NLP任务的人。 | 从词向量、序列建模和注意力进入Transformer、预训练与语言任务。偏表示和任务；CS336更偏完整训练工程。 | Deep-learning students interested in language and representation. | Connects word vectors, sequence models and attention to Transformers, pretraining and NLP tasks. Complements CS336's engineering focus. | Machine learning, neural networks and Python.
cs336 | CS336: Language Modeling from Scratch | 已会PyTorch和Transformer，愿意完成实现型作业的人。 | 围绕分词、模型、优化、资源核算、系统、数据和后训练构建语言模型。先做A1，再按方向进入系统或后训练作业。 | Learners ready for substantial language-model implementation work. | Covers tokenization, architectures, optimization, compute, systems, data and post-training. Start with Assignment 1; later assignments serve different specializations. | Confident Python/PyTorch, linear algebra, probability and Transformer basics.
hf_llm | Hugging Face LLM Course | 想熟悉Transformers生态并使用现有模型的人。 | 讲Tokenizer、模型输入输出、Datasets、训练与模型分享，适合连接理论和常用工具。 | Learners adopting the Transformers ecosystem. | Introduces tokenizers, model inputs and outputs, datasets, training and model sharing. A practical bridge from theory to established tools. | Python and introductory deep learning.
csapp | CSAPP / CMU 15-213: Computer Systems | 想转向AI性能、内存与系统工程的人。 | 用C和汇编理解程序执行、缓存、链接、虚拟内存、网络和并发，配套经典系统实验。CSAPP与15-213放在同一条目。 | Learners entering performance engineering or AI systems. | Explains execution, caches, linking, virtual memory, networking and concurrency through C, assembly and systems labs. CSAPP and 15-213 share this entry. | C programming and data structures.
cs140 | CS140: Operating Systems | 已有C和计算机系统基础，想深入操作系统的人。 | 通过Pintos学习线程、调度、用户程序、虚拟内存和文件系统。放在CSAPP之后。 | Learners ready to implement operating-system components. | Uses Pintos to study threads, scheduling, user programs, virtual memory and file systems. Take it after a systems introduction. | C, computer systems and debugging experience.
hf_agents | Hugging Face Agents Course | 想尽快构建第一个工具型Agent的人。 | 通过示例学习工具调用、Agent框架与实践任务。适合应用起步，之后再读更底层的Agent harness。 | Builders creating their first tool-using agent. | Introduces tools, agent frameworks and practical assignments. Follow it with a closer look at an agent harness. | Python, LLM APIs and basic prompting.
dlai_agentic | DeepLearning.AI: Agentic AI | 想先理清Agent设计模式，再动手实现的人。 | 讲反思、工具使用、规划、多Agent与评估，提供组织Agent工作流的视角。 | Learners seeking a compact introduction to agent design. | Explains reflection, tool use, planning, multi-agent systems and evaluation. Useful before choosing a framework. | Python and basic LLM application development.
cs329z | CS329Z: Agent Engineering | 已做过工具循环和评测，准备构建完整Agent系统的人。 | 围绕Agent harness、上下文、工具与评估组织课程和项目，适合从Demo走向可靠应用。 | Builders who have implemented basic agents and evaluations. | Studies agent harnesses, context, tools and evaluation through systems-oriented projects. | Python engineering, LLM fundamentals and an introductory agent project.
cs329a | CS329A: Self-Improving AI Agents | 同时具备Agent、后训练与评估基础的进阶学习者。 | 研究Agent如何利用反馈改进表现，涉及优化、学习与实验。应放在普通Agent工程之后。 | Advanced learners combining agents, post-training and evaluation. | Examines agents that improve through feedback, optimization and learning. Follow an introductory agent-engineering course first. | Agent systems, evaluation and post-training or RL fundamentals.
cs2680 | CS2680: Modern AI Systems | 关注现代LLM系统和Agent实践的学习者。 | 通过课程资料与作业拆解现代AI应用，连接模型能力、Agent循环与系统设计。 | Learners interested in modern LLM applications and systems. | Connects model capabilities, agent loops and system design through lectures and assignments. | Python, machine learning and LLM application basics.
fsdl | Full Stack: LLM Bootcamp | 已会调用模型，想理解LLM应用完整链路的人。 | 讲Prompt、检索、应用架构、部署和LLMOps。它侧重产品与系统，不替代模型训练课程。 | Builders moving from model calls to complete LLM applications. | Covers prompting, retrieval, application architecture, deployment and LLMOps. Focuses on applications rather than training a foundation model. | Python and basic LLM APIs.
cs285 | CS285: Deep Reinforcement Learning | 已有机器学习和PyTorch基础，想深入决策学习的人。 | 讲模仿学习、策略梯度、价值学习、离线RL与模型式RL，是后续世界模型和机器人策略的重要基础。 | Learners seeking a rigorous introduction to deep RL. | Covers imitation learning, policy gradients, value learning, offline RL and model-based RL. Supports later work on world models and robotics. | Probability, optimization, neural networks and PyTorch.
cs224r | CS224R: Deep Reinforcement Learning | 关注机器人、交互和强化学习研究的人。 | 从深度RL方法进入模仿学习、离线数据和机器人应用，与CS285有较多重合，可按方向选一门主课。 | Learners interested in RL for interaction and robotics. | Studies deep RL, imitation, offline data and robotics applications. Overlaps with CS285; choose one main course before adding selected topics. | Machine learning, probability and deep learning.
mit_diffusion | MIT 6.S184: Flow Matching and Diffusion | 熟悉深度学习，想理解连续生成模型的人。 | 用ODE/SDE、概率路径和速度场解释Diffusion与Flow Matching，并配套采样和条件生成实验。 | Deep-learning students interested in continuous generative models. | Develops diffusion and flow matching through ODEs, SDEs, probability paths and vector fields, with sampling and conditional-generation labs. | Calculus, probability, neural networks and Python.
cs258 | Berkeley CS258: Parallel Computer Architecture | 已有体系结构基础，研究并行系统的进阶学习者。 | 使用公开历史课程研究互连网络、共享内存、一致性、同步与事务内存，前置明显高于CSAPP。 | Advanced learners studying parallel architectures. | Uses an archived public course on interconnects, shared memory, coherence, synchronization and transactional memory. Requires more background than CSAPP. | Advanced computer architecture, caches, memory and concurrency.
dw-leedl | LeeDL Tutorial | 喜欢中文讲解，希望系统补深度学习的人。 | 整理李宏毅课程的文字、视频和代码，适合作为Zero to Hero或鱼书的另一种讲解。 | Learners who prefer Chinese explanations of deep learning. | Organizes Hung-yi Lee's lectures, notes and code. An alternative explanation alongside an implementation-focused course. | Python and basic mathematics.
dw-happy | Happy-LLM | 会Python与基础深度学习，想用中文理解LLM的人。 | 从语言模型基础讲到Transformer、预训练与微调。适合先建立全貌，再用CS336完成工程实现。 | Learners seeking a Chinese introduction to LLMs. | Introduces language models, Transformers, pretraining and fine-tuning. Build a conceptual map here, then use CS336 for deeper implementation. | Python, neural networks and basic PyTorch.
dw-scratch | LLMs From Scratch CN | 想用中文逐步阅读从零实现LLM代码的人。 | 围绕文本处理、注意力和GPT实现展开。与Happy-LLM和Raschka原书重叠，可作为配套解释。 | Learners reading an LLM implementation with Chinese explanations. | Covers text processing, attention and GPT construction. Overlaps with Happy-LLM and Raschka's book; use it as a companion. | Python, PyTorch and neural-network fundamentals.
dw-self | Self-LLM | 已懂微调原理，想查具体开源模型配置的人。 | 按模型整理部署、推理与微调实践。适合作为操作手册，不需要把全部模型逐个做完。 | Users deploying or fine-tuning a particular open model. | Provides model-specific deployment, inference and fine-tuning guides. Use the relevant model guide as a reference. | Python, a chosen model and basic fine-tuning knowledge.
dw-solarge | So-Large-LM | 已有LLM基础，想补论文和理论脉络的人。 | 按主题整理大模型架构、训练与相关研究，适合遇到问题时选读。 | Learners extending an existing LLM foundation. | Collects architecture, training and research topics. Best used for targeted reading after an introductory course. | Transformer, pretraining and post-training fundamentals.
dw-cookbook | LLM Cookbook | 想用中文做短小LLM应用练习的人。 | 汇集吴恩达相关短课的中文讲解与Notebook，覆盖提示、检索和应用工作流。 | Learners who prefer short, practical LLM exercises in Chinese. | Collects Chinese explanations and notebooks for short courses on prompting, retrieval and application workflows. | Python and access to the models required by each notebook.
dw-universe | LLM Universe | 想先做一个完整知识库应用的新手。 | 从环境、模型接入和向量知识库开始搭建LLM应用。基础部分与All-in-RAG重叠，先选一套完成。 | Beginners building a first knowledge-base application. | Builds an LLM application through setup, model integration and vector retrieval. Its introductory RAG work overlaps with All-in-RAG. | Python and basic LLM usage.
dw-rag | All-in-RAG | 已会Python和模型API，想系统学习RAG的人。 | 按数据处理、切块、检索、重排、生成与评估组织实践，适合做第二版知识库系统。 | Builders seeking a structured RAG curriculum. | Covers data preparation, chunking, retrieval, reranking, generation and evaluation. Useful for improving a first knowledge-base system. | Python and LLM API basics.
dw-agents | Hello-Agents | 想用中文理解并实现Agent的人。 | 从工具调用和Agent循环走向记忆、规划、框架与应用。适合作为Agent方向的中文主课。 | Learners building agents with Chinese explanations. | Moves from tool calls and the agent loop to memory, planning, frameworks and applications. A useful main course for the agent track. | Python, LLM APIs and basic software engineering.
dw-easyrl | Easy-RL | 想先用中文建立强化学习概念的人。 | 从MDP、价值函数和策略讲到常见RL算法。之后再用CleanRL读实现或学习CS285。 | Learners seeking an introductory RL text in Chinese. | Builds the concepts of MDPs, value functions, policies and common RL algorithms. Follow it with CleanRL or a university course. | Probability, calculus and Python.
dw-zerosglang | Zero-to-SGLang | 想从小型推理引擎理解LLM服务的人。 | 按请求、KV Cache、Prefill/Decode与调度解释推理系统。与nano-vLLM或mini-SGLang配合阅读。 | Learners studying how an LLM inference engine works. | Explains requests, KV caches, prefill/decode and scheduling through a small implementation. Pair with nano-vLLM or mini-SGLang. | Python, Transformers, GPU memory and basic systems concepts.
dw-easyvibe | Easy-Vibe | 想借助AI工具完成一个应用原型的人。 | 从需求和交互进入原型与产品实践，侧重做出应用；模型原理和训练另走基础路线。 | Learners using AI tools to build an application prototype. | Connects requirements, interactions, prototyping and product practice. Use a separate course for model theory and training. | Basic programming and an application idea.
cs50p | CS50P: Introduction to Programming with Python | 完全没有编程基础，或想重新打牢Python的人。 | 通过习题学习函数、条件、循环、异常、测试、文件和类。AI入门优先选它，CS50留作更广的计算机导论。 | Complete beginners who need a focused Python course. | Teaches functions, control flow, exceptions, testing, files and classes through exercises. More focused on Python than CS50. | No prior programming required.
missing_semester | The Missing Semester | 会写代码，但命令行、Git和调试还不顺手的人。 | 学Shell、编辑器、版本控制、调试与性能分析，帮助后续课程和实验更顺畅。 | Programmers who need stronger everyday development tools. | Covers the shell, editors, version control, debugging and profiling to support later coursework and experiments. | Basic programming.
mit1806 | MIT 18.06: Linear Algebra | 想系统掌握矩阵、子空间和分解的人。 | 讲线性方程组、向量空间、正交、特征值与矩阵分解。先看3Blue1Brown建立几何直觉，再用习题补扎实。 | Learners seeking a systematic linear-algebra foundation. | Studies systems of equations, vector spaces, orthogonality, eigenvalues and matrix decompositions. Pair visual intuition with exercises. | High-school algebra.
mit1801 | MIT 18.01SC: Single Variable Calculus | 对导数、积分和链式法则还不熟悉的人。 | 讲单变量微积分并提供练习。用于理解梯度的基础；多元微积分仍需后续课程补充。 | Learners strengthening derivatives, integrals and the chain rule. | Teaches single-variable calculus with exercises. Builds a foundation for gradients; multivariable calculus requires further study. | High-school algebra and trigonometry.
stat110 | Harvard Stat 110: Probability | 想理解随机变量、期望和概率模型的人。 | 讲条件概率、贝叶斯公式、常见分布、期望与极限定理，是机器学习与RL的重要基础。 | Learners building a probability foundation for ML and RL. | Covers conditional probability, Bayes' rule, distributions, expectation and limit theorems. | Calculus and basic algebra.
cs188 | Berkeley CS188: Artificial Intelligence | 想理解AI中搜索、规划和决策，而不只学神经网络的人。 | 讲搜索、约束、MDP、强化学习和概率推断，通过项目把经典AI方法落到代码。 | Learners interested in search, planning and decision making. | Covers search, constraints, MDPs, reinforcement learning and probabilistic inference through programming projects. | Python, data structures and probability.
cs228 | CS228: Probabilistic Graphical Models | 有概率基础，想深入结构化概率建模的人。 | 用图表达变量关系，研究表示、推断与参数学习。它不是图神经网络课程。 | Learners interested in structured probabilistic modeling. | Uses graphs to study probabilistic representation, inference and learning. Distinct from graph neural networks. | Probability, linear algebra and machine learning.
fastai | Practical Deep Learning for Coders | 会编程，希望先快速完成深度学习应用的人。 | 采用先实践后解释的方法完成图像、文本等任务，适合建立项目经验后再补数学原理。 | Programmers who prefer an application-first introduction. | Builds image, text and other applications before developing the underlying theory. | Python programming.
cs231n | CS231n: Deep Learning for Computer Vision | 已懂神经网络，想系统学习视觉方法的人。 | 从视觉识别和卷积网络进入深度视觉模型，配套实现作业。适合作为视觉方向主课。 | Neural-network students entering computer vision. | Develops visual recognition and deep vision models through lectures and implementation assignments. | Linear algebra, calculus, Python and introductory neural networks.
cs224w | CS224W: Machine Learning with Graphs | 对关系数据、网络和图神经网络感兴趣的人。 | 讲图表示、消息传递和图学习任务，适合社交、推荐、分子与知识图谱等关系数据问题。 | Learners modeling relational data with graphs. | Covers graph representations, message passing and graph-learning tasks for networked data. | Machine learning, probability and Python.
cs236 | CS236: Deep Generative Models | 想从概率建模角度比较不同生成方法的人。 | 系统介绍VAE、GAN、Flow等生成模型的目标与方法，为进一步学习Diffusion和Flow Matching建立背景。 | Learners seeking a probabilistic view of generative modeling. | Compares objectives and methods for VAEs, GANs, flows and other generative models. | Probability, calculus and deep learning.
dlsys | CMU 10-414/714: Deep Learning Systems | 想实现深度学习框架、理解训练效率的人。 | 从自动微分和算子实现进入加速、编译及系统问题，比只使用PyTorch更接近框架内部。 | Learners interested in building deep-learning frameworks. | Moves from automatic differentiation and operators to acceleration, compilation and systems design. | Python, C/C++, linear algebra and computer systems.
fsdl2022 | Full Stack Deep Learning 2022 | 能训练模型，想掌握实验、数据与部署流程的人。 | 连接数据管理、训练、测试、部署与监控，补上模型之外的工程环节。 | Learners moving from training models to maintaining ML systems. | Connects data management, experimentation, testing, deployment and monitoring. | Python, deep learning and a basic training project.
smol_course | Hugging Face Smol Course | 懂Transformer，准备做第一次小模型后训练的人。 | 用小型语言模型学习指令数据、SFT、PEFT和偏好训练，适合接TRL与LlamaFactory。 | Learners starting practical post-training on small language models. | Introduces instruction data, SFT, PEFT and preference training before deeper work with TRL or training tools. | Python, Transformers and basic training loops.
hf_deeprl | Hugging Face Deep RL Course | 喜欢边做环境边学习RL的人。 | 用实践任务连接RL概念、环境和算法实现，可与Easy-RL形成文字与实验搭配。 | Learners who prefer hands-on reinforcement learning. | Connects RL concepts to environments and practical implementations. Pair with a theory-oriented introduction. | Python, probability and basic deep learning.
cs239a_pending | CS239A: Identification Pending | 曾记录此编号，准备继续核对来源的人。 | 目前尚未唯一定位学校、课程名称和官网，暂不编排为学习任务。 | Readers checking the identity of this recorded course code. | The institution, title and official site have not been uniquely identified. It is not assigned a place in the learning sequence. | Not yet identified.
bbb_linear | 3Blue1Brown: Essence of Linear Algebra | 矩阵计算会做，但缺少几何直觉的人。 | 用动画理解向量、基、线性变换、行列式与特征向量，帮助读懂神经网络中的矩阵运算。搭配MIT 18.06补练习。 | Learners who can calculate with matrices but want geometric intuition. | Visualizes vectors, bases, linear maps, determinants and eigenvectors. Pair it with MIT 18.06 for exercises and a fuller course. | High-school algebra.
bbb_calculus | 3Blue1Brown: Essence of Calculus | 想看懂导数和链式法则为何成立的人。 | 通过图像解释变化率、导数、积分与链式法则。先建立直觉，再把链式法则接到反向传播。 | Learners seeking intuition for derivatives and the chain rule. | Visual explanations of rates of change, derivatives, integrals and the chain rule. Leads naturally into backpropagation. | High-school algebra; functions and graphs.
bbb_nn | 3Blue1Brown: Neural Networks and Backpropagation | 神经网络初学者，以及想补反传推导的人。 | 先看网络和梯度下降，再看反传直觉与Backpropagation calculus：从损失沿计算链求权重导数，最后接micrograd代码。 | Beginners in neural networks and learners revisiting backpropagation. | Start with networks and gradient descent, then connect backpropagation intuition to the chain-rule derivation and a micrograd implementation. | Basic derivatives; pair with Essence of Calculus if needed.
hf_diffusion | Hugging Face Diffusion Course | 会PyTorch，想从Notebook进入图像生成的人。 | 从加噪与去噪开始，实现小型扩散模型，再学习微调、条件控制与Diffusers管线。偏动手，MIT 6.S184补连续模型原理。 | PyTorch users who prefer notebook-based generative-model practice. | Implements diffusion models, fine-tuning, conditioning and Diffusers pipelines. Complements MIT 6.S184's mathematical treatment. | Python, PyTorch and introductory deep learning.
pytorch_distributed | PyTorch Distributed: DDP and FSDP2 | 已会单卡训练，想理解多卡通信与显存分片的人。 | 从DDP进入FSDP2，理解参数、梯度和优化器状态的分片及通信。先读官方小例子，再比较DeepSpeed。 | Learners moving from single-device training to distributed training. | Introduces DDP and FSDP2, including sharding and communication. Read the official examples before comparing DeepSpeed. | A working PyTorch training loop, GPU memory and process basics.
''', ['title_en','audience_zh','summary_zh','audience_en','summary_en','prereq_en'])

BOOKS = rows('''
d2l | Dive into Deep Learning | Interactive explanations of deep-learning mathematics and implementations, with executable notebooks. | Learners pairing a course with worked examples. | Free official online text and notebooks.
ai_agent_book | AI Agent Book | A companion reference for agent tools, memory, orchestration and evaluation. | Readers building a first agent system. | Public author-maintained website and code.
dw-pumpkin | Pumpkin Book | Derivations and explanations accompanying the Chinese Watermelon machine-learning textbook. | Readers who need the mathematical steps behind the textbook. | Public companion derivations; the main textbook is separate.
fish | Deep Learning from Scratch | Implements neural-network fundamentals with Python and NumPy, including backpropagation and CNNs. | Learners who prefer a compact, code-oriented introduction. | The book is commercially published; official code and notebooks are public.
mml | Mathematics for Machine Learning | Linear algebra, vector calculus, probability and optimization for machine learning. | Learners connecting mathematics to ML notation. | Author-provided online edition.
islp | An Introduction to Statistical Learning | An accessible introduction to statistical learning, with practical Python labs. | Learners starting applied machine learning. | Official online book and lab materials.
esl | The Elements of Statistical Learning | A more advanced treatment of statistical learning, model fitting and generalization. | Readers comfortable with probability, calculus and linear algebra. | Author-provided online edition.
dlbook | Deep Learning | Foundations of neural networks, optimization, regularization and representation learning. | Learners seeking a theoretical reference after introductory practice. | Official online edition; printed book sold separately.
pml | Probabilistic Machine Learning: An Introduction | Machine learning through probability, statistical modeling and decision making. | Readers with calculus, linear algebra and probability. | Author-provided online edition and companion code.
sutton | Reinforcement Learning: An Introduction | Foundations of value functions, dynamic programming, temporal-difference methods and policy learning. | Learners building a rigorous RL foundation. | Author-hosted edition; publisher link provided as an alternative.
aima | Artificial Intelligence: A Modern Approach | A broad reference on search, reasoning, planning, uncertainty and learning. | Readers who want AI beyond neural networks. | Commercial textbook with public companion resources.
rasbt_llm | Build a Large Language Model (From Scratch) | Builds tokenization, attention, GPT training and fine-tuning step by step. | Python users implementing their first language model. | Commercial book with public companion code and selected material.
dl_python | Deep Learning with Python, Third Edition | Introduces deep-learning concepts through the Keras ecosystem and practical examples. | Programmers who want a Keras-oriented companion to PyTorch-based courses. | Commercial book; see the publisher for edition and access details.
''', ['title_en','summary_en','audience_en','personal_en'])

# Each project gets an explicit distinction and a concrete place in the learning sequence.
PROJECTS = rows('''
micrograd | micrograd | 标量级自动微分，代码短，能看清计算图与梯度累加；不承担大模型训练。 | 看完3Blue1Brown反传推导后读它，再转PyTorch张量实现。 | A small scalar automatic-differentiation engine. | Makes the computation graph and gradient accumulation visible; not a large-model training framework. | Read after the backpropagation videos, then move to tensor-based PyTorch.
makemore | makemore | 用字符生成串起计数模型、MLP和更复杂网络，重点是理解训练实验。 | 接在micrograd之后；它与nanoGPT是由简单语言模型到Transformer的衔接。 | Character-level language-model experiments. | Starts with simple models and grows toward neural language modeling, making training experiments easy to inspect. | Follow micrograd; use it as the bridge to a Transformer project.
nanogpt | nanoGPT | 紧凑的GPT训练代码，便于追踪数据、模型、loss和生成；比nanochat范围小。 | 先训练字符级小模型，再对照自己的tiny GPT和CS336 A1。 | A compact GPT training implementation. | Easier to trace than a full chat-model pipeline; focuses on model training and generation. | Train a small character model, then compare it with your own tiny GPT and CS336 A1.
minimind | MiniMind | 中文小模型全流程，包含预训练、SFT和LoRA；适合看不同阶段如何共用模型。 | 用小数据做SFT/LoRA，偏好训练的深入实现交给TRL。 | A Chinese small-language-model training pipeline. | Connects pretraining, SFT and LoRA around a shared model implementation. | Start with small-data SFT or LoRA; use TRL for a deeper preference-training project.
medicalgpt | MedicalGPT | 把通用模型训练流程放到医疗领域；重点是数据、领域适配与评测，不是临床产品。 | 完成通用SFT后再读，先比较数据格式和领域评测设计。 | A domain-adaptation pipeline centered on medical language data. | Adds domain-specific data and evaluation concerns to a general training workflow. | Read after a general SFT project; compare data formats and domain evaluation.
learn_claudecode | learn-claude-code | 分步骤构建编码Agent，能看到工具循环、上下文与任务组织逐步增长。 | Agent代码入门优先读它，再去Hermes或OpenHands看完整系统。 | A step-by-step coding-agent implementation. | Exposes how tools, context and task management are added to a small agent loop. | Start here before reading a complete system such as Hermes or OpenHands.
tradingagents | TradingAgents | 金融分析场景的多Agent工作流，角色分工鲜明，但不代表策略有稳定收益。 | 作为Agent应用案例阅读；练习离线评测、信息时间边界和失败分析。 | A multi-agent workflow for financial analysis. | Makes role specialization visible, while predictive or trading performance still needs separate evidence. | Use it as an application case study with offline evaluation and careful time boundaries.
hermes | Hermes Agent | 带记忆、技能和工具的持久Agent，适合观察真实应用如何管理长期状态。 | 先掌握单Agent循环，再沿工具、记忆、技能和网关分模块阅读。 | A persistent agent with tools, memory and skills. | Focuses on a continuing assistant and its state, rather than a single isolated prompt. | Learn a basic agent loop first, then read tools, memory, skills and gateway components separately.
nano_vllm | nano-vLLM | 以精简实现说明批处理、KV Cache与LLM推理路径，比成熟服务框架容易读。 | 推理系统入门优先选它或mini-SGLang中的一个。 | A compact implementation of LLM inference. | Exposes batching, KV caches and execution paths with less infrastructure than a production server. | Choose this or mini-SGLang as the first inference-engine reading project.
mini_sglang | mini-SGLang | SGLang官方小型实现，适合对照调度、缓存和执行模块。 | 已读nano-vLLM时只比较设计差异，不必重新做一遍相同基础。 | A small inference-engine implementation from the SGLang organization. | Provides a compact route into scheduling, caching and execution design. | Use as an alternative to nano-vLLM, or compare selected design choices afterward.
vllm | vLLM | 成熟LLM服务引擎，关注吞吐、显存管理、批处理与接口集成。 | 先理解小引擎，再用固定请求测Prefill、Decode、吞吐和延迟。 | A production-oriented LLM serving engine. | Emphasizes throughput, memory management, batching and serving interfaces. | Study a small engine first, then benchmark fixed requests and separate prefill from decode.
sglang | SGLang | 面向LLM与多模态推理的服务系统，具备自己的运行时与调度设计。 | 与vLLM选择一个作为服务主项目，另一个用于同负载性能对照。 | A serving system for language and multimodal models. | Offers a distinct runtime and scheduling design from vLLM. | Choose one main serving engine; compare the other under the same workload.
faiss | FAISS | 向量相似度搜索库，提供索引和检索能力；不负责完整RAG工作流。 | 先用小型向量集比较精确检索与近似检索，再接应用框架。 | A library for vector similarity search. | Supplies indexing and retrieval primitives rather than a complete RAG application. | Compare exact and approximate search on a small dataset before adding a framework.
deepseek | DeepSeek-V3 | 官方模型实现和技术资料，用于理解MoE等架构与推理；不是个人低成本预训练教程。 | 先读结构和小段推理代码，再对照CS336的资源与并行章节。 | The official DeepSeek-V3 model and inference reference. | Useful for architecture and systems reading; full-scale pretraining is not a small personal exercise. | Study the architecture and selected inference code alongside CS336's resource-accounting topics.
ijepa | I-JEPA | 从图像上下文预测目标表征，研究自监督表示；官方仓库已归档。 | 作为JEPA起点读目标和数据流，不把它当作可交互的视频世界模型。 | The original image-based JEPA implementation. | Predicts target representations from image context; its repository is archived. | Read for the self-supervised objective, then distinguish it from video and action-conditioned models.
vjepa | V-JEPA | 把表征预测扩展到视频，关注时空表征，不以像素重建为核心。 | 与I-JEPA比较输入、掩码和目标，再进入V-JEPA 2。 | Video representation learning with JEPA. | Extends representation prediction to space and time rather than centering on pixel reconstruction. | Compare its inputs, masking and targets with I-JEPA before V-JEPA 2.
vjepa2 | V-JEPA 2 | 进一步连接视频表征与动作条件建模，适合研究感知到规划的关系。 | 先读公开模型和示例，区分纯视频预训练与动作条件训练。 | A video and action-conditioned JEPA research implementation. | Connects learned video representations with action-conditioned modeling. | Separate video pretraining from the action-conditioned stage when reading examples.
dreamerv3 | DreamerV3 | 学习潜在动力学，并在想象轨迹中优化策略；与JEPA表征预测的目标不同。 | 先学MDP、策略和模型式RL，再用简单环境读训练循环。 | A model-based RL agent that learns in imagined latent trajectories. | Learns dynamics and optimizes behavior, unlike a representation-only prediction objective. | Learn RL and model-based planning first; start with a simple environment.
openpi | OpenPI: pi0 and pi0.5 | 连续动作块与Flow Matching策略，适合研究视觉、语言和动作的结合。 | 先看数据接口与推理；有机器人数据或仿真任务后再微调。 | Open implementations of pi0-family robot policies. | Uses continuous action chunks and flow-based policies, providing a contrast to tokenized-action approaches. | Begin with data interfaces and inference before attempting task-specific fine-tuning.
openvla | OpenVLA | 将视觉语言模型连接到动作token预测，可与OpenPI的连续动作路线比较。 | 先读动作表示和数据处理；与OpenPI选一个做主要策略项目。 | An open vision-language-action model. | Connects a vision-language model to action-token prediction, contrasting with continuous-action policies. | Study action representation and preprocessing; choose one main VLA policy project.
lerobot | LeRobot | 覆盖机器人数据、训练、评估与设备接入的工具链，不只是一种模型。 | 机器人方向先从它理解数据格式与回放，再选具体策略。 | A robotics learning toolkit spanning data, training, evaluation and devices. | Provides the workflow around policies rather than a single policy architecture. | Use it to learn dataset formats and replay before choosing a policy.
dw-tiny | Tiny-Universe | 中文白盒小实现集合，便于对照不同组件；不适合作为全部通读的主线。 | 已有一个模型项目后，按当前组件查阅相应小实现。 | A collection of small, readable AI implementations in Chinese. | Useful for comparing components, but less focused than one continuous model-building course. | Consult the relevant implementation when a component becomes important.
trl | TRL | 提供SFT、DPO、GRPO和蒸馏训练器，便于比较数据、loss和rollout的变化。 | SFT/LoRA之后做DPO，再做GRPO；最后看在线蒸馏。 | Trainers for supervised fine-tuning, preference optimization, RL and distillation. | Makes changes in datasets, objectives and rollout pipelines explicit across methods. | Follow SFT with DPO, then GRPO; leave online distillation until later.
verl | verl | 将rollout、奖励和策略更新组织成分布式后训练流水线。 | 已理解TRL和单机训练后再读，用它研究资源调度与多进程协作。 | A distributed post-training framework. | Coordinates rollout, rewards and policy updates across distributed workers. | Read after a simpler trainer; focus on worker roles, scheduling and data movement.
openrlhf | OpenRLHF | 基于Ray等组件组织RLHF工程，适合与verl比较训练与推理协同。 | 与verl先选一个深入，避免同时配置两套分布式训练栈。 | A distributed RLHF framework. | Offers an alternative organization of training and inference components to verl. | Choose either verl or OpenRLHF as the first distributed post-training framework.
reasoning_scratch | Reasoning from Scratch | 以教学代码拆解推理评估、GRPO和蒸馏，比完整分布式框架更容易追算法。 | 和TRL形成原理与工具对照，先读小例子再追框架实现。 | Educational code for reasoning-model evaluation, GRPO and distillation. | Easier to trace algorithmically than a large distributed training stack. | Pair it with TRL: inspect the small algorithm before the framework abstraction.
nanochat | nanochat | 从Tokenizer到预训练、对话微调和评估的端到端项目，比nanoGPT更完整。 | 在tiny GPT和CS336 A1之后读，先缩小模型与数据看流程。 | An end-to-end small chat-model pipeline. | Extends beyond nanoGPT to tokenization, training, conversational adaptation and evaluation. | Read after a tiny GPT project; reduce model and data size to inspect the pipeline.
llmc | llm.c | 用C/CUDA实现语言模型训练，适合理解算子、内存与GPU性能。 | 先会PyTorch训练和C，再比较相同操作在低层实现中的数据流。 | Language-model training implemented in C and CUDA. | Exposes kernels and memory behavior hidden behind a high-level training library. | Learn PyTorch and C first, then trace equivalent operations at the lower level.
litgpt | LitGPT | 包含模型、训练和微调工作流的工具化实现，强调已有模型的使用与扩展。 | 在理解最小训练循环后选一个小模型，比较配置式工程和手写流程。 | A toolkit for training and adapting language models. | Offers a more configurable workflow than a minimal teaching implementation. | Use one small model after you understand the basic training loop.
smollm | SmolLM | 开放小模型及相关训练资料，适合研究模型大小、数据与能力之间的关系。 | 作为小模型配方参考，与MiniMind或nanochat比较数据和评估。 | A family of small language models and training resources. | Useful for studying relationships between scale, data and capability. | Compare its data and evaluation choices with MiniMind or nanochat.
olmo | OLMo | 强调开放的模型、数据与训练研究资料，便于研究可复现性。 | 读配方、日志和数据说明；个人实验使用缩小版本，不追完整规模。 | Open language-model research resources and training implementations. | Particularly useful for examining training recipes, data provenance and reproducibility. | Read the recipe and logs, then reduce the scale for personal experiments.
datatrove | DataTrove | 面向文本语料处理的流水线，重点是过滤、去重与数据准备，不负责凭空生成知识。 | 先处理一小批真实文本，记录每个过滤步骤对数量和质量的影响。 | A pipeline toolkit for text-corpus processing. | Focuses on preparing, filtering and deduplicating data rather than generating new examples. | Process a small real corpus and inspect the effect of every filtering stage.
distilabel | Distilabel | 用LLM构造指令、偏好与评估数据，适合连接数据生成和后训练。 | 数据合成入门先做一条生成—评分—过滤流水线，再接训练器。 | Pipelines for LLM-generated and labeled training data. | Closely connects synthetic instruction or preference data to model post-training. | Build one generation, scoring and filtering pipeline before feeding a trainer.
datasets | Hugging Face Datasets | 数据加载、映射、流式读取与分享的底层工具，不是模型也不是生成框架。 | 所有数据项目的先修工具；先熟悉map、拆分、缓存和数据模式。 | A toolkit for loading, transforming and sharing datasets. | Provides data infrastructure rather than a model or synthetic-data generator. | Learn mapping, splitting, caching, schemas and streaming before a larger data project.
nemo_designer | NeMo Data Designer | 按列、依赖关系和约束设计合成数据，强调多样性、字段关联与自动验证；与清洗语料的DataTrove分工不同。 | 数据合成重点项目：从官方preview例子做小表，再加入种子数据和验证器；模型端点另行配置。 | NVIDIA's framework for designing structured synthetic datasets. | Uses column-based configuration, dependencies and validation; complements corpus preparation tools rather than replacing them. | Start with the official preview example, then add seed data and validators. Configure a model endpoint separately.
llamafactory | LlamaFactory | 将多模型微调流程做成统一配置与界面，降低实验配置成本。 | 想先跑通SFT/LoRA可用它；想追训练算法时回到TRL或MiniMind。 | A unified interface for adapting many language models. | Reduces configuration effort through standardized workflows, rather than teaching every algorithm from first principles. | Use for a first SFT or LoRA run; return to TRL or MiniMind for the algorithm.
unsloth | Unsloth | 侧重高效微调与训练实现，提供便于起步的Notebook和模型适配。 | 资源有限时优先查看其支持模型和Notebook，再与常规训练器比较。 | Efficient model-adaptation tools and notebooks. | Focuses on practical training efficiency and supported model integrations. | Check supported models and notebooks, then compare with a standard trainer on the same task.
alignment_handbook | Alignment Handbook | 给出具体SFT与偏好对齐配方，适合学习实验配置和数据选择。 | 在TRL基础上读一个配方，理解数据和超参为何这样组合。 | Recipes for supervised and preference-based alignment. | Emphasizes complete experiment configurations and data choices around existing trainers. | Read one recipe after learning the trainer it relies on.
openr1 | Open R1 | 开放推理模型复现中的数据、训练与评估，连接合成数据和RL后训练。 | 完成GRPO小实验后再读，优先追一条数据到评估的链。 | An open effort around reasoning-model training and evaluation. | Connects synthetic data, post-training and evaluation in a research-oriented workflow. | Read after a small GRPO experiment; follow one data-to-evaluation path.
llamaindex | LlamaIndex | 面向数据接入、索引与检索应用的开发框架，比FAISS更接近应用组织。 | 需要组合文档处理、检索与模型时选它，仍保留独立检索评测。 | A framework for data-connected LLM applications. | Works at a higher application level than FAISS, organizing ingestion, indexing and retrieval. | Choose it for composable RAG applications while keeping retrieval evaluation explicit.
ragflow | RAGFlow | 集成式知识库与RAG应用，便于快速体验完整系统和文档处理。 | 想先看产品形态可选它；想理解算法与调用链先做All-in-RAG。 | An integrated RAG and knowledge-base application. | Offers a fuller product experience than a low-level retrieval library. | Use to explore an end-to-end product; build a smaller pipeline first for algorithmic understanding.
langgraph | LangGraph | 用显式状态和图组织Agent流程，适合分支、暂停、恢复和持久工作流。 | 单Agent工具循环跑通后再引入，让复杂状态成为采用框架的理由。 | A framework for stateful agent workflows. | Makes state transitions and control flow explicit, useful for branching and resumable execution. | Add it when a working agent needs structured state, not before a basic tool loop.
autogen | AutoGen | 以多Agent交互和协作为主要视角，与LangGraph的显式流程视角不同。 | 有明确角色分工需求时再读；同时参考项目当前维护与迁移说明。 | A framework centered on multi-agent interaction. | Emphasizes collaboration between agents rather than only an explicit workflow graph. | Study when role-based collaboration is necessary; consult current maintenance and migration guidance.
openhands | OpenHands | 完整的软件开发Agent系统，包含执行环境与应用层基础设施。 | 放在learn-claude-code之后，按沙箱、执行、上下文和评测分模块读。 | A complete software-development agent platform. | Includes execution environments and application infrastructure beyond a small coding-agent loop. | Follow a minimal agent implementation, then inspect execution, isolation, context and evaluation.
mcp_sdk | MCP Python SDK | 连接模型应用与工具、资源的协议SDK；本身不负责规划、记忆或自主决策。 | 先做一个小工具服务和客户端，再把它接入已有Agent。 | The official Python SDK for Model Context Protocol. | Implements tool and resource connectivity; it is not an agent planner or memory system. | Build a small server and client, then integrate them with an existing agent.
diffusers | Diffusers | 多种扩散与生成模型的通用实现库，支持训练、推理和管线组合。 | 从HF Diffusion Course的小模型开始，再读一种scheduler和pipeline。 | A library of diffusion and generative-model implementations. | Supplies models, schedulers and pipelines rather than one isolated architecture. | Start with the diffusion course, then inspect one scheduler and one pipeline.
sam | Segment Anything | 提示式图像分割模型，用点、框等提示产生掩码；不是目标检测器。 | 与YOLO比较输出任务，先运行单张图像的提示分割。 | A promptable image-segmentation model. | Produces masks from prompts such as points or boxes, unlike an object detector. | Compare with detection and begin with prompted segmentation on one image.
yolo | Ultralytics YOLO | 成熟视觉任务工具链，适合检测等任务的训练和部署实践。 | 想练数据标注、指标和部署可先做它，再深入模型结构。 | A practical toolkit for vision tasks such as object detection. | Useful for a complete data-to-deployment workflow, rather than only architecture reading. | Start with a small labeled dataset, metrics and inference before changing architectures.
pyg | PyTorch Geometric | 图神经网络工具库，以节点、边和消息传递为核心；与概率图模型不同。 | 配合CS224W做节点或图分类，重点检查图批处理和信息泄漏。 | A library for graph neural networks. | Centers on nodes, edges and message passing, distinct from probabilistic graphical-model inference. | Pair with CS224W and inspect batching and leakage in a small graph task.
llava | LLaVA | 将视觉编码器连接到语言模型，适合理解多模态对齐与指令数据。 | 在语言模型基础后读，先追图像特征如何进入语言模型。 | A vision-language model implementation. | Connects visual features to a language model and multimodal instruction training. | Trace how image features enter the language model before attempting fine-tuning.
cleanrl | CleanRL | 以便于阅读的单文件算法实现为特色，适合追loss与交互循环。 | RL代码入门优先读它，再用Stable-Baselines3组织更多实验。 | Readable, compact implementations of RL algorithms. | Makes the interaction loop and optimization objective easy to trace. | Use for algorithm study before moving to a more abstract experiment library.
sb3 | Stable-Baselines3 | 稳定、统一接口的RL算法库，更适合搭建基线和重复实验。 | 做同一环境的算法比较时选它；读原理时参考CleanRL。 | A library of established reinforcement-learning implementations. | Provides consistent interfaces for baselines and repeated experiments. | Use for controlled comparisons; consult CleanRL for a more direct algorithm walkthrough.
gymnasium | Gymnasium | 强化学习环境接口与基础环境集合，不是训练算法库。 | 先理解reset、step、终止与截断，再接CleanRL或SB3。 | Standard environment interfaces and environments for RL. | Defines interaction with an environment rather than implementing the learning algorithm. | Understand reset, step, termination and truncation before connecting a trainer.
diffusion_policy | Diffusion Policy | 用扩散过程预测动作序列，是模仿学习策略；不等同于完整通用VLA。 | 已会扩散和行为克隆后读，适合连接生成模型与机器人动作。 | An imitation-learning policy based on action-sequence diffusion. | A bridge from generative modeling to robot control, rather than a general-purpose VLA system. | Read after diffusion fundamentals and behavior cloning.
gr00t | Isaac GR00T | 面向机器人基础模型的官方实现与工具，适合研究多模态与动作接口。 | 先看公开示例和数据要求，再与OpenPI/OpenVLA比较策略接口。 | NVIDIA's robot foundation-model implementation and tooling. | Offers another multimodal-to-action design alongside OpenPI and OpenVLA. | Inspect examples and data requirements before selecting it as a policy project.
libero | LIBERO | 机器人操作任务和评测环境，主要提供实验场景，不是策略模型。 | 用固定任务和成功率比较策略，先跑环境再接模型。 | A benchmark and environment suite for robot manipulation. | Supplies tasks and evaluation settings rather than a learned policy. | Run an environment first, then compare policies under fixed tasks and metrics.
mujoco | MuJoCo | 多体动力学仿真器，负责物理环境，不负责自动学习控制策略。 | 从一个简单场景理解状态、动作和时间步，再接RL或模仿学习。 | A physics simulator for articulated systems. | Supplies simulated dynamics, not a learning algorithm or policy. | Explore state, actions and simulation steps before adding RL or imitation learning.
lmeval | LM Evaluation Harness | 标准化语言模型任务评测，侧重固定数据、评分和可比结果。 | 微调前后使用同一任务配置，先建立可重复的基线。 | A harness for language-model benchmark evaluation. | Focuses on fixed tasks and comparable scoring rather than application tracing. | Evaluate before and after training with identical task settings.
mlflow | MLflow | 管理实验、参数、指标和模型生命周期，不替代具体任务评测。 | 项目出现多个实验版本时接入，先记录配置与结果再扩展部署。 | Experiment tracking and model-lifecycle tooling. | Organizes runs, parameters and artifacts rather than defining task-specific quality. | Add once you have multiple experiments to compare.
deepeval | DeepEval | 面向LLM应用的测试与评估工具，适合RAG和Agent输出质量检查。 | 从人工可审阅的小评测集开始，明确模型裁判的局限。 | Testing and evaluation tools for LLM applications. | Complements benchmark evaluation with application-focused checks. | Start with a small human-reviewable dataset and inspect judge-model limitations.
aima_python | AIMA Python | 配套AIMA教材的经典AI算法，覆盖搜索、推断与决策，拓宽神经网络之外的视角。 | 按CS188主题选择一两个算法实验，不必把教材所有实现都重写。 | Companion implementations of classical AI algorithms. | Adds search, reasoning and decision-making perspectives beyond neural networks. | Use selected algorithms alongside CS188 or the AIMA textbook.
deepspeed | DeepSpeed | 分布式训练与推理工具，ZeRO等机制帮助组织显存与通信，层次低于具体RLHF工作流。 | 单卡训练之后先学DDP/FSDP，再读一个ZeRO配置并比较显存分工。 | Distributed training and inference infrastructure. | Mechanisms such as ZeRO address memory and communication below a task-specific RLHF workflow. | Learn DDP/FSDP first, then inspect one ZeRO configuration and its memory layout.
''', ['title_en','difference_zh','recommendation_zh','summary_en','difference_en','recommendation_en'])

COURSE_GUIDES = rows('''
programming | Programming | Python把数学想法变成数据处理和实验；命令行与Git让代码可以运行、调试和保存。 | 零基础从CS50P开始，已有编程基础直接补Python/NumPy，再学Missing Semester。CS50是更广的计算机导论。 | Python turns mathematical ideas into data pipelines and experiments; the shell and Git support reliable development. | Start with CS50P if new to coding. Otherwise use Python/NumPy to fill gaps, then learn development tools. CS50 offers broader CS coverage.
math | Mathematics | 线代描述表示和变换，微积分描述模型怎样更新，概率帮助理解数据、预测和不确定性。 | 先用3Blue1Brown建立图像，再用MIT 18.06、18.01SC和Stat 110补系统知识与习题。反传推导在深度学习分类。 | Linear algebra describes representations, calculus explains updates, and probability describes data and uncertainty. | Begin with 3Blue1Brown's visual explanations, then use MIT and Stat 110 for systematic study and exercises. Backpropagation is in Deep Learning.
ml | AI and Machine Learning | 机器学习解释模型怎样从数据得到规律，经典AI补上搜索、推断与决策，是理解现代系统取舍的基础。 | CS229作为统计学习主课；CS188拓宽经典AI；需要结构化概率模型时再进入CS228。 | Machine learning studies learning from data; classical AI adds search, inference and decisions. Together they explain many choices in modern systems. | Use CS229 for statistical learning, CS188 for classical AI, and CS228 when structured probabilistic modeling becomes relevant.
deep | Deep Learning | 深度学习把表示和预测一起训练，反向传播把损失对参数的影响高效传回网络，是后续模型训练的公共基础。 | 3Blue1Brown补直觉和反传公式，PyTorch练训练流程；Zero to Hero、鱼书、LeeDL选一套主要解释。fast.ai适合先应用后原理。 | Deep learning trains representations and predictors together. Backpropagation efficiently computes parameter gradients and underpins later model training. | Use 3Blue1Brown for intuition and derivation, PyTorch for training, and one main explanatory course or book. fast.ai offers an application-first route.
vision | Vision, Graphs and Multimodality | 图像、关系图和文本图像配对具有不同数据结构，决定模型如何表示输入与利用结构。 | 视觉主课选CS231n；关系数据选CS224W。两者不要求连续学完，再按项目进入视觉语言模型。 | Images, relational graphs and image-text pairs impose different structures on models and data. | Choose CS231n for vision or CS224W for relational data. These are different branches, not consecutive prerequisites.
llm | Language Models and Pretraining | 语言模型通过序列预测学习表示；预训练涉及模型、数据、优化与计算资源的整体配合。 | Happy-LLM先建立中文全貌，CS336深入实现；CS224N补NLP任务。其余资料用于对照，不重复从零实现同一模型。 | Language models learn through sequence prediction. Pretraining combines model design, data, optimization and compute. | Use Happy-LLM for an overview and CS336 for implementation. CS224N adds NLP tasks; use other texts as companions rather than duplicating projects.
post | Fine-tuning and Post-training | 后训练把通用模型适配到指令、偏好与任务反馈，效果同时依赖数据质量、目标函数和评测。 | 先Smol Course或HF LLM Course，再做SFT/LoRA→DPO→GRPO。Self-LLM是按模型查配置的手册。 | Post-training adapts a model to instructions, preferences and task feedback through data, objectives and evaluation. | Begin with the Smol or LLM course, then progress from SFT/LoRA to DPO and GRPO. Use Self-LLM for model-specific setup.
rag | RAG and Applications | RAG把可更新的外部信息接到生成模型上；检索质量、引用和评测决定系统能否可靠回答。 | 第一个知识库选LLM Universe或All-in-RAG；想系统优化检索优先All-in-RAG。LLM Bootcamp补应用架构，Cookbook补小练习。 | RAG connects external information to a generative model. Retrieval quality, attribution and evaluation determine its usefulness. | Choose one introductory RAG course. Use All-in-RAG for deeper retrieval work, LLM Bootcamp for architecture and Cookbook for short exercises.
agents | Agents | Agent让模型调用工具并根据结果继续行动；状态、失败处理和评测比增加角色数量更关键。 | Hello-Agents或HF Agents作为起点；DLAI梳理模式。做过基础项目后学CS329Z，更后面再看自改进Agent。 | Agents use tools and continue acting on their results. State, error handling and evaluation matter more than simply adding roles. | Start with Hello-Agents or the HF course; use DLAI for design patterns. Move to CS329Z after a basic project, then study self-improvement.
rl | Reinforcement Learning | 强化学习研究怎样通过交互与奖励学习决策，连接机器人、世界模型与部分LLM后训练方法。 | Easy-RL或HF课程入门，CS285或CS224R选一门主课。先理解MDP和策略，再连接LLM中的奖励与rollout。 | RL learns decisions from interaction and rewards, connecting robotics, world models and some LLM post-training methods. | Start with Easy-RL or the HF course, then choose CS285 or CS224R. Understand MDPs and policies before LLM-specific rewards and rollouts.
generative | Generative Models | 生成模型学习数据分布并采样新内容；不同目标决定训练过程、可控性和采样成本。 | HF Diffusion Course先动手，MIT 6.S184补Diffusion和Flow Matching数学，CS236比较更广的生成模型。 | Generative models learn distributions and sample new data. Their objectives shape training, control and sampling cost. | Use the HF course for practice, MIT 6.S184 for continuous-model mathematics, and CS236 for a wider comparison.
systems | Computer and AI Systems | 训练与推理效率受内存、计算、调度和通信共同限制，系统基础让性能分析有依据。 | CSAPP打底，再按目标选推理引擎或DDP/FSDP。CMU DL Systems研究框架内部；CS140、CS258是更深的系统方向。 | Memory, compute, scheduling and communication jointly limit training and inference. Systems foundations make performance work explainable. | Start with CSAPP, then specialize in inference or DDP/FSDP. Use CMU's course for framework internals; OS and parallel architecture are deeper branches.
engineering | Evaluation, Deployment and MLOps | 模型上线需要数据版本、实验记录、固定评测、服务与监控，才能知道一次改动是否真的更好。 | 用FSDL把已有模型项目变成可维护系统；与项目中的MLflow和评测工具结合。 | Deployed models need data versions, experiments, evaluations, serving and monitoring to make changes measurable. | Use FSDL to extend an existing model project, alongside experiment-tracking and evaluation tools.
''', ['name_en','intro_zh','guide_zh','intro_en','guide_en'])

PROJECT_GUIDES = rows('''
basics | Implement from Scratch | 小实现让数据、计算图、loss和更新过程可见，避免直接进入大框架后只会修改配置。 | 先micrograd→makemore，再写tiny GPT。Tiny-Universe和AIMA按主题查阅，不作为额外通读任务。 | Small implementations expose data flow, graphs, objectives and updates before large frameworks hide them. | Follow micrograd with makemore and a tiny GPT. Use the other collections as targeted references.
pretrain | Pretraining | 预训练项目连接Tokenizer、数据、模型、优化与checkpoint，是理解大模型成本和行为的基础。 | 入门nanoGPT，完整流程nanochat；LitGPT偏工具，SmolLM/OLMo偏开放配方，llm.c偏低层性能。 | Pretraining joins tokenization, data, models, optimization and checkpoints into one process. | Start with nanoGPT, use nanochat for a complete pipeline, then choose tooling, open recipes or lower-level performance work.
data | Data Processing and Synthesis | 数据质量决定模型能学到什么。真实数据清洗与合成数据生成是两种工作，生成后仍要验证、去重和评估。 | Datasets学数据操作，DataTrove清洗语料；NeMo Data Designer设计关联字段与验证，Distilabel适合指令与偏好数据流水线。 | Data quality controls what a model can learn. Preparing real corpora and synthesizing examples are different jobs; generated data still needs validation and evaluation. | Learn Datasets first. Use DataTrove for corpus preparation, NeMo Data Designer for structured generation, and Distilabel for training-data pipelines.
post | Fine-tuning and Post-training | 这一类把模型适配到指令和偏好。小模型能练完整数据与评测流程，大规模rollout则需要分布式工程。 | MiniMind入门，TRL追算法；LlamaFactory/Unsloth简化运行；verl/OpenRLHF先选一个；MedicalGPT是后置领域案例。 | These projects adapt models to instructions and preferences. Small models expose the workflow; large rollouts introduce distributed systems. | Start with MiniMind, inspect algorithms in TRL, use convenience tools as needed, and choose only one distributed framework initially.
rag | RAG and Vector Search | 从文档到答案至少经过解析、切块、索引、检索和生成。各项目所在层次不同，不能只按界面完整程度比较。 | FAISS练检索原语，LlamaIndex组合应用，RAGFlow看集成产品。先做检索基线，再增加框架与界面。 | RAG spans parsing, chunking, indexing, retrieval and generation. The projects operate at different layers. | Use FAISS for retrieval primitives, LlamaIndex for composition and RAGFlow for a fuller product. Establish a retrieval baseline first.
agents | Agents | Agent工程关注工具、状态、记忆、执行环境与评估。协议SDK、编排框架和完整应用承担不同职责。 | learn-claude-code读小循环，LangGraph组织状态，MCP接工具；Hermes看长期助手，OpenHands看软件执行，TradingAgents看领域协作。 | Agent engineering spans tools, state, memory, execution and evaluation. SDKs, orchestration frameworks and applications serve different roles. | Learn a small loop first, then select explicit state, tool connectivity, persistent assistance or a domain application according to the problem.
inference | Inference and Serving | 推理把权重变成可用服务，需要同时处理KV Cache、请求调度、显存、延迟与吞吐。 | nano-vLLM或mini-SGLang先选一个；之后vLLM/SGLang选主引擎。DeepSeek-V3作为模型架构与推理参考。 | Inference turns weights into a service while managing caches, requests, memory, latency and throughput. | Start with one small engine, then one production server. Use DeepSeek-V3 as a model and architecture reference.
vision | Vision and Graph Learning | 检测输出位置与类别，分割输出掩码，视觉语言模型输出语言；图学习则处理节点和关系。 | 根据任务选YOLO、SAM、LLaVA或PyG，不把这四个当成先后必须完成的同一种项目。 | Detection predicts objects, segmentation predicts masks, vision-language models produce language, and graph models process relations. | Choose by output and data structure rather than treating these projects as consecutive versions of one task.
generative | Diffusion and Generative Models | 扩散工具把去噪模型、采样器、条件控制与推理流程拆开，适合比较采样质量、速度和可控性。 | 用Diffusers完成一个小模型，再比较一个scheduler或条件输入；原理配MIT或HF课程。 | Diffusion libraries separate models, schedulers, conditioning and pipelines, enabling controlled quality and speed comparisons. | Build one small model in Diffusers, then vary a scheduler or conditioning input alongside the course material.
rl | Reinforcement Learning | 环境给出状态与反馈，算法决定如何学习策略。区分接口和算法有助于定位训练问题。 | Gymnasium懂交互，CleanRL读算法，Stable-Baselines3跑基线和比较实验。三者可以配合使用。 | Environments supply observations and feedback; algorithms learn policies. Separating them makes training failures easier to diagnose. | Learn the Gymnasium interaction contract, inspect an algorithm in CleanRL, then use SB3 for repeated experiments.
world | JEPA and World Models | JEPA偏重预测表征；模型式RL还需要动力学、奖励和决策。两者相关，但训练目标并不相同。 | I-JEPA→V-JEPA→V-JEPA 2比较图像、视频和动作条件；DreamerV3单独走RL与想象轨迹路线。 | JEPA emphasizes representation prediction, while model-based RL also learns dynamics and behavior. Their objectives differ. | Compare the image, video and action-conditioned JEPAs. Study DreamerV3 as a separate model-based RL route.
robotics | VLA and Robotics | 机器人学习由数据、仿真、任务和策略共同组成，VLA只是其中一种策略接口，硬件条件也会影响选型。 | LeRobot学流程，MuJoCo/LIBERO提供环境；Diffusion Policy、OpenVLA、OpenPI和GR00T按动作表示与设备条件选择。 | Robotics combines data, simulation, tasks and policies. VLA is one policy interface, and hardware affects what can be reproduced. | Learn the workflow and environment first, then choose a policy based on action representation, data and available devices.
engineering | Evaluation and MLOps | 固定评测回答模型有没有变好，实验记录解释为什么变化，分布式基础设施决定训练怎样运行。 | LM Evaluation Harness做模型任务，DeepEval做应用测试，MLflow管实验；DeepSpeed用于更深的训练系统实践。 | Evaluations measure change, experiment records explain it, and distributed infrastructure controls how training runs. | Use a benchmark harness for models, application tests for products, tracking for experiments and DeepSpeed for training infrastructure.
''', ['name_en','intro_zh','guide_zh','intro_en','guide_en'])

LINK_LABELS = {k:v['en'] for k,v in rows('''
课程官网 | Course website
课程网站与配套资源 | Course website and materials
官方网站 / 仓库 | Official website / repository
项目源码（GitHub） | Source code on GitHub
GitHub与官方说明 | GitHub and project guide
课程安排 | Schedule
课程表与课件 | Schedule and slides
课程与作业表 | Schedule and assignments
2015 完整课程表 | Complete 2015 schedule
2018 课程与作业表 | 2018 schedule and assignments
课程官网与作业 | Website and assignments
课程与视频表 | Schedule and videos
课程目录 | Course contents
课程与代码目录 | Course and code contents
课程与书籍说明 | Course and book guide
课程 Notebook 与示例 | Course notebooks and examples
官方文档 | Official documentation
官方教程 | Official tutorials
官方快速开始 | Official quickstart
视频课程 | Video lectures
官方视频课程 | Official video lectures
扩展视频 | Additional video
视频 · Spring 2024 | Video lectures: Spring 2024
配套视频 | Companion videos
配套作业与参考代码 | Assignments and reference code
作业代码 | Assignment code
作业列表 | Assignments
代码 | Code
公开实验 | Public labs
学期项目 | Term project
阅读任务 | Readings
项目官网 | Project website
项目仓库 | Project repository
项目总目录 | Project contents
示例项目 | Example projects
作者 / 官方入口 | Author / official website
作者发布版本入口 | Author's published edition
作者学习路径 | Author's learning paths
出版社入口（作者站超时时备用） | Publisher (alternative to the author's site)
在线阅读 | Read online
国内在线阅读 | Alternative online edition
中文在线课程 | Online course in Chinese
中文课程目录 | Course contents in Chinese
中文教程与文档 | Tutorials and documentation in Chinese
中文学习地图 | Learning map in Chinese
中文说明 | Chinese guide
英文原课目录 | Original course contents in English
完整目录 | Contents
仓库与内容说明 | Repository and contents
Datawhale 内容目录 | Datawhale contents
勘误 | Errata
功能与参数 | Features and configuration
Python 官网教程 | Official Python tutorial
NumPy 官网教程 | Official NumPy quickstart
按章节阅读与运行 Notebook | Read and run chapter notebooks
李宏毅原课：视频 / 课件 / 作业 | Hung-yi Lee's lectures, slides and homework
参考课程 CS324 | Companion course: CS324
全部模型教程 | All model guides
按模型选择教程 | Choose a guide by model
AMD 教程 | AMD guide
Apple MLX 教程 | Apple MLX guide
训练流程与高效微调 | Training workflow and efficient fine-tuning
训练脚本 | Training scripts
架构、数据与训练章节 | Architecture, data and training
架构与数据流 | Architecture and data flow
文本数据与 Tokenizer | Text data and tokenizers
注意力实现 | Attention implementation
GPT 模型实现 | GPT model implementation
Transformer 架构 | Transformer architecture
LLaMA2、Tokenizer 与预训练 | Llama 2, tokenization and pretraining
第6章：RLVR / GRPO | Chapter 6: RLVR / GRPO
第7章：改进GRPO | Chapter 7: Improving GRPO
第8章：蒸馏 | Chapter 8: Distillation
SFT：指令微调 | SFT: instruction fine-tuning
DPO：偏好训练 | DPO: preference training
GRPO：规则奖励 | GRPO: rule-based rewards
OPD：在线策略蒸馏 | OPD: on-policy distillation
GRPO示例 | GRPO examples
OPD示例 | OPD examples
推理基础：prefill / decode | Inference fundamentals: prefill / decode
KV Cache 与显存账本 | KV cache and memory accounting
请求生命周期：代码走读 | Request lifecycle: code walkthrough
离线性能测试入口 | Offline benchmark
ReAct、规划与反思 | ReAct, planning and reflection
从零构建 Agent 框架 | Build an agent framework from scratch
记忆与检索 | Memory and retrieval
全栈应用 | Full-stack application
四步构建 RAG | Build RAG in four steps
文档切块 | Document chunking
混合检索 | Hybrid retrieval
需求到原型 | Requirements to prototype
文案生成器项目 | Copywriting generator project
强化学习基础教程 | RL fundamentals
策略梯度 | Policy gradients
Q-learning 悬崖寻路项目 | Q-learning cliff-walking project
Pintos 项目手册 | Pintos project manual
实验 · Attack Lab | Attack Lab
实验 · Bomb Lab | Bomb Lab
实验 · Cache Lab | Cache Lab
实验 · Data Lab | Data Lab
项目习题课 1 · Threads | Project section 1: Threads
项目习题课 2 · User Programs | Project section 2: User programs
项目习题课 3 · Virtual Memory | Project section 3: Virtual memory
项目习题课 4 · File Systems | Project section 4: File systems
习题 0 · 线性代数与多元微积分 | Problem set 0: Linear algebra and multivariable calculus
习题 1 · 监督学习 | Problem set 1: Supervised learning
习题 2 · 监督学习进阶 | Problem set 2: Advanced supervised learning
习题 3 · 深度学习与无监督学习 | Problem set 3: Deep and unsupervised learning
习题 4 · EM、深度学习与 RL | Problem set 4: EM, deep learning and RL
作业 1 · 从零构建 Transformer 语言模型 | Assignment 1: Build a Transformer language model
作业 1 · 构建 Agentic Harness | Assignment 1: Build an agent harness
作业 1 · 模仿学习 | Assignment 1: Imitation learning
作业 1 · 起始代码 ZIP | Assignment 1: Starter code ZIP
作业 2 · Word2Vec 与依存句法分析 | Assignment 2: Word2Vec and dependency parsing
作业 2 · 在线强化学习 | Assignment 2: Online RL
作业 2 · 策略梯度 | Assignment 2: Policy gradients
作业 2 · 系统与并行 | Assignment 2: Systems and parallelism
作业 2 · 起始代码 ZIP | Assignment 2: Starter code ZIP
作业 3 · MadsOpt Harness Competition | Assignment 3: MadsOpt harness competition
作业 3 · Q-learning 与 Actor-Critic | Assignment 3: Q-learning and actor-critic
作业 3 · Self-Attention 与 Transformer | Assignment 3: Self-attention and Transformers
作业 3 · 离线强化学习 | Assignment 3: Offline RL
作业 3 · 缩放规律 | Assignment 3: Scaling laws
作业 3 · 起始代码 ZIP | Assignment 3: Starter code ZIP
Assignment 1 · Harness 起始代码说明 | Assignment 1: Harness starter guide
Assignment 1 · 起始代码 | Assignment 1: Starter code
Assignment 2 · 起始代码 | Assignment 2: Starter code
Assignment 2 · 起始代码 TAR.GZ | Assignment 2: Starter code TAR.GZ
Assignment 3 · 任务说明 | Assignment 3: Instructions
Assignment 1：Exploring Word Vectors（代码） | Assignment 1: Exploring word vectors (code)
Assignment 1：MadsLens，观察并分析 Agent 执行过程 | Assignment 1: MadsLens agent tracing
Assignment 2：MadsLoop，搭建 Agent 循环 | Assignment 2: MadsLoop agent loop
Homework 1 · 起始代码 | Homework 1: Starter code
Homework 2 · 起始代码 | Homework 2: Starter code
Lab 1：ODE / SDE 与采样 | Lab 1: ODEs, SDEs and sampling
Lab 1：ODE / SDE 与采样 · 在线练习 | Lab 1: ODEs, SDEs and sampling (online)
Lab 2：Flow Matching / Diffusion | Lab 2: Flow matching and diffusion
Lab 2：Flow Matching / Diffusion · 在线练习 | Lab 2: Flow matching and diffusion (online)
Lab 3：条件生成 · 在线练习 | Lab 3: Conditional generation (online)
线性代数专题 | Linear algebra collection
线性变换与矩阵：视频与图文 | Linear transformations: video and illustrated lesson
微积分专题 | Calculus collection
微积分总览：视频与图文 | Essence of calculus: video and illustrated lesson
链式法则与乘积法则 | Chain rule and product rule
官方微积分视频系列 | Official calculus video playlist
神经网络专题 | Neural networks collection
反向传播直觉：视频与图文 | Backpropagation intuition: video and illustrated lesson
反向传播公式推导：视频与图文 | Backpropagation calculus: video and illustrated derivation
反向传播推导：官方视频 | Backpropagation calculus: official video
FSDP2官方教程 | Official FSDP2 tutorial
DDP官方教程 | Official DDP tutorial
分布式训练总览 | Distributed training overview
MCP官方文档 | Official MCP documentation
Karpathy microgpt：纯Python完整算法 | Karpathy microgpt: a complete algorithm in pure Python
''', ['en']).items()}
