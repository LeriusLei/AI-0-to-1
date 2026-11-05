"""Goal-first choices and concrete outcomes for the resource overviews."""
from editorial_content import rows

PROJECT_GOALS=rows('''
micrograd | 弄懂反向传播与自动求导 | 跟踪标量计算图，训练一个小MLP。 | Understand backpropagation and autodiff | Trace a scalar graph and train a small MLP.
makemore | 自己训练第一个语言模型 | 用字符序列训练模型，生成新名字并比较loss。 | Train a first language model | Generate names with character models and compare losses.
dw-tiny | 按模块拆解模型代码 | 选择一个网络模块，运行并修改它的最小实现。 | Inspect model components | Run and change one minimal network component.
aima_python | 学搜索、规划和经典AI | 实现搜索或MDP，观察不同策略的决策。 | Learn search, planning and classical AI | Implement search or an MDP and compare decisions.
nanogpt | 看懂GPT的预训练循环 | 训练一个小GPT，保存checkpoint并采样文本。 | Understand GPT pretraining | Train a small GPT, save checkpoints and sample text.
nanochat | 串起一个聊天模型的流程 | 阅读数据、分词、训练、评测和聊天入口的连接。 | Follow a chat-model pipeline | Connect data, tokenization, training, evaluation and chat.
llmc | 学模型训练底层性能 | 对照C/CUDA训练实现，理解算子与显存开销。 | Study lower-level training performance | Inspect C/CUDA training, operators and memory use.
litgpt | 用现成配方训练或微调模型 | 运行一个支持的模型配置，理解训练参数。 | Use model-training recipes | Run a supported configuration and understand its parameters.
smollm | 学小模型的数据和训练配方 | 阅读开放配方，比较数据组成与模型表现。 | Study small-model recipes | Compare data composition and model behavior in open recipes.
olmo | 研究开放预训练流程 | 追踪公开数据、训练配置和模型检查点。 | Inspect open pretraining | Trace released data, configurations and checkpoints.
datasets | 整理手里的训练样本 | 做数据切分、map、过滤与流式加载。 | Prepare existing training examples | Split, map, filter and stream a dataset.
datatrove | 清洗和去重预训练语料 | 串起读取、过滤、去重与导出的语料流水线。 | Clean pretraining corpora | Build a reading, filtering, deduplication and export pipeline.
nemo_designer | 用大模型生成带约束的数据 | 从种子或schema生成关联字段，加规则验证与质量检查。 | Generate constrained data with LLMs | Generate dependent fields from seeds or a schema and validate them.
distilabel | 合成指令、回答和偏好样本 | 连接生成、评分与过滤，导出用于后训练的样本。 | Synthesize instructions and preferences | Generate, score and filter examples for post-training.
minimind | 用小模型练预训练和SFT | 跑通少量样本的训练、LoRA与生成流程。 | Practice training and SFT on small models | Run a small-data training, LoRA and generation workflow.
medicalgpt | 做领域模型适配 | 在通用微调之后，比较领域数据与评测方式。 | Adapt a model to a domain | Compare domain data and evaluations after general fine-tuning.
trl | 学SFT、DPO、GRPO与蒸馏 | 对照trainer追数据、loss、奖励和rollout流程。 | Learn SFT, DPO, GRPO and distillation | Trace data, losses, rewards and rollouts through trainers.
verl | 理解分布式强化学习后训练 | 追踪rollout、奖励、策略更新和worker协作。 | Inspect distributed RL post-training | Trace rollouts, rewards, policy updates and workers.
openrlhf | 比较另一套RLHF工程实现 | 对照Ray与训练/推理组件的协作方式。 | Compare an RLHF implementation | Inspect Ray and the interaction of training and inference components.
reasoning_scratch | 读小型推理训练算法 | 从短代码理解推理评估、GRPO和蒸馏。 | Read small reasoning-training algorithms | Understand evaluation, GRPO and distillation in compact code.
llamafactory | 快速做一次SFT或LoRA | 按配置训练一个支持的模型并比较输出。 | Run a first SFT or LoRA job | Train a supported model from configuration and compare outputs.
unsloth | 在有限显存下做模型适配 | 运行支持的Notebook，观察训练效率与显存。 | Fine-tune within a memory budget | Run a supported notebook and inspect speed and memory use.
alignment_handbook | 读完整的后训练实验配方 | 把模型、数据、训练参数和评估配置对应起来。 | Read post-training experiment recipes | Connect models, datasets, training parameters and evaluation settings.
openr1 | 理解开放推理模型复现流程 | 比较合成数据、奖励与后训练配置。 | Inspect open reasoning-model recipes | Compare synthetic data, rewards and post-training configurations.
deepspeed | 理解多卡训练的显存分工 | 在DDP/FSDP之后读ZeRO配置与状态切分。 | Understand distributed training memory | Inspect ZeRO configuration and state sharding after DDP/FSDP.
faiss | 学向量索引与近邻搜索 | 为自己的向量建立索引并测召回和查询耗时。 | Learn vector indexing and nearest neighbors | Index embeddings and measure retrieval quality and latency.
llamaindex | 做自己的文档问答应用 | 连接文档、切块、检索、重排与生成。 | Build a document question-answering app | Connect parsing, chunks, retrieval, reranking and generation.
ragflow | 研究完整知识库产品 | 跟踪文档解析、索引与问答界面之间的数据流。 | Inspect a complete knowledge-base product | Trace data across parsing, indexing and the question-answering interface.
learn_claudecode | 看懂Agent的工具调用循环 | 从最小循环逐步加入工具、记忆和执行状态。 | Understand an agent tool loop | Extend a minimal loop with tools, memory and execution state.
mcp_sdk | 给模型应用接自己的工具 | 编写一个本地MCP服务和客户端。 | Connect tools to model applications | Write a local MCP server and client.
langgraph | 管理多步骤Agent的状态 | 做一个可恢复、带明确分支的工具工作流。 | Manage state in multi-step agents | Build a resumable tool workflow with explicit branches.
autogen | 研究多个Agent如何协作 | 比较消息传递、角色与终止条件。 | Inspect multi-agent coordination | Compare messaging, roles and stopping conditions.
openhands | 研究能操作软件的代码Agent | 追踪任务、执行环境、文件修改和反馈。 | Inspect a software-operating coding agent | Trace tasks, execution environments, file changes and feedback.
hermes | 研究持久助手与长期记忆 | 看会话、工具、记忆与后台任务如何衔接。 | Study persistent assistants and memory | Connect sessions, tools, memory and background tasks.
tradingagents | 看领域多Agent工作流 | 理解信息收集、角色分工与汇总流程。 | Inspect a domain-specific multi-agent workflow | Trace collection, role separation and result synthesis.
nano_vllm | 读第一个精简推理引擎 | 跟踪一次请求的batch、KV Cache和模型执行。 | Read a first small inference engine | Trace batching, KV caches and model execution for a request.
mini_sglang | 学调度与前缀复用 | 从小实现理解请求调度、缓存与执行分工。 | Learn scheduling and prefix reuse | Inspect scheduling, caches and execution in a small implementation.
vllm | 运行和研究成熟推理系统 | 启动模型服务，在固定请求下比较延迟与吞吐。 | Run and study a production inference system | Serve a model and compare latency and throughput under fixed requests.
sglang | 比较推理系统的调度设计 | 跟踪前缀缓存、调度和结构化生成的执行路径。 | Compare inference scheduling designs | Trace prefix caching, scheduling and structured generation.
deepseek | 研究MoE架构及模型推理 | 阅读DeepSeek-V3结构和推理代码，核对资源开销。 | Study MoE architecture and inference | Inspect DeepSeek-V3 structure, inference code and resource costs.
yolo | 训练一个目标检测模型 | 从标注数据得到检测框，并比较准确率与推理速度。 | Train an object detector | Predict boxes from labeled data and compare quality and speed.
sam | 做提示驱动的图像分割 | 用点或框得到掩码，理解提示与分割结果。 | Build prompt-driven segmentation | Produce masks from points or boxes and inspect their behavior.
pyg | 在图数据上做预测 | 实现节点或图分类，学习消息传递与图批处理。 | Make predictions on graph data | Implement node or graph classification and message passing.
llava | 理解图像如何接入语言模型 | 追踪视觉编码器、连接器与语言输出。 | Understand vision-language connections | Trace a vision encoder, connector and language output.
diffusers | 运行和修改扩散生成管线 | 生成图像，替换scheduler或条件控制并比较结果。 | Run and modify a diffusion pipeline | Generate images and compare schedulers or conditioning.
gymnasium | 理解RL环境接口 | 编写环境交互循环，查看observation、action与reward。 | Understand the RL environment interface | Write an interaction loop using observations, actions and rewards.
cleanrl | 逐行读强化学习算法 | 追踪单文件PPO或DQN的数据与更新过程。 | Read RL algorithms line by line | Trace a single-file PPO or DQN implementation.
sb3 | 快速建立强化学习基线 | 在固定环境运行算法，比较奖励曲线和设置。 | Establish an RL baseline | Run an algorithm in a fixed environment and compare rewards.
ijepa | 学图像表征预测 | 区分预测潜在表示与重建图像像素。 | Study image representation prediction | Distinguish latent prediction from pixel reconstruction.
vjepa | 把表征预测扩展到视频 | 追踪视频编码、目标表示和预测目标。 | Extend representation prediction to video | Trace video encoding, target representations and prediction objectives.
vjepa2 | 研究视频与动作条件世界模型 | 看视频表征如何接到动作条件预测和规划。 | Study video and action-conditioned world models | Connect video representations to action-conditioned prediction and planning.
dreamerv3 | 用世界模型学习决策 | 跟踪潜在动力学、想象轨迹和actor-critic。 | Learn decisions through a world model | Trace latent dynamics, imagined trajectories and actor-critic learning.
lerobot | 跑通机器人学习数据与训练 | 读取轨迹、训练基线策略并查看推理接口。 | Connect robotics data and policy training | Read trajectories, train a baseline and inspect inference interfaces.
mujoco | 搭建可交互的物理仿真 | 加载机器人模型，控制关节并获取状态。 | Build an interactive physics simulation | Load a robot, control joints and inspect state.
libero | 比较机器人策略的任务表现 | 在固定操作任务中运行策略并查看成功率。 | Compare robot policies on tasks | Run policies on fixed manipulation tasks and inspect success rates.
openpi | 研究pi0系列VLA | 对照动作块、Flow Matching与数据接口，再做任务适配。 | Study pi0-family VLA policies | Inspect action chunks, flow matching and data interfaces before adaptation.
openvla | 研究token化动作的VLA | 追踪图像、语言到动作token的映射与适配。 | Study tokenized-action VLA | Trace image and language inputs to action tokens and adaptation.
diffusion_policy | 用扩散模型预测机器人动作 | 比较条件输入、动作序列与采样推理。 | Predict robot actions with diffusion | Compare conditioning, action sequences and sampling.
gr00t | 研究通用机器人基础模型 | 先读数据规范与策略推理，理解模型适配条件。 | Study a general robotics foundation model | Inspect data formats, policy inference and adaptation requirements.
lmeval | 比较语言模型的基准表现 | 固定任务、样本和生成设置，输出可比较的分数。 | Compare language-model benchmark results | Fix tasks, samples and generation settings to obtain comparable scores.
deepeval | 给LLM或RAG应用写评测 | 做小型问答评测集，区分规则检查与模型裁判。 | Evaluate an LLM or RAG application | Build a small QA evaluation set and distinguish rules from model judges.
mlflow | 管理自己的多次模型实验 | 记录参数、指标与产物，比较运行结果。 | Track repeated model experiments | Record parameters, metrics and artifacts and compare runs.
''',['goal_zh','outcome_zh','goal_en','outcome_en'])

# goal / introductory choices / outcome. The group name remains available
# beside the recommendation, so readers can compare alternatives in one step.
STARTS={
 'programming':('从零学Python','Learn Python from scratch',['cs50p'],'会写函数、处理文件并完成编程习题。','Write functions, process files and complete programming exercises.'),
 'math':('补齐模型需要的数学','Build mathematical foundations',['bbb_linear','bbb_calculus','mit1806'],'看懂矩阵、梯度和链式法则。','Understand matrices, gradients and the chain rule.'),
 'ml':('理解模型怎样学习','Understand learning from data',['cs229'],'理解损失、泛化和常用机器学习算法。','Understand objectives, generalization and common algorithms.'),
 'deep':('自己写一个训练循环','Write a training loop',['pytorch','zero_to_hero'],'用数据训练神经网络并保存模型。','Train and save a neural network.'),
 'vision':('学习视觉或图模型','Study vision or graph models',['cs231n','cs224w'],'按图像或图数据选择相应模型和任务。','Choose models for image or graph tasks.'),
 'llm':('实现语言模型与预训练','Implement language models',['dw-happy','cs336'],'从分词、Transformer进入训练与评估。','Connect tokenization, Transformers, training and evaluation.'),
 'post':('做SFT、LoRA和偏好训练','Fine-tune and align models',['smol_course','hf_llm'],'组织训练样本，运行并比较后训练方法。','Prepare examples and compare post-training methods.'),
 'rag':('做知识库或LLM应用','Build a knowledge base or LLM app',['dw-rag','dw-universe'],'完成从文档检索到引用回答的应用。','Build retrieval and source-grounded answers.'),
 'agents':('让模型调用工具做任务','Build tool-using agents',['dw-agents','hf_agents'],'串起工具调用、状态与任务执行。','Connect tools, state and task execution.'),
 'rl':('让策略从交互中学习','Learn policies from interaction',['dw-easyrl','cs285'],'理解环境、奖励和策略更新。','Understand environments, rewards and policy updates.'),
 'generative':('理解流匹配与扩散生成','Study flow matching and diffusion',['mit_diffusion','hf_diffusion'],'用Notebook实现采样和条件生成。','Implement sampling and conditional generation in notebooks.'),
 'systems':('理解训练和推理为什么慢','Understand training and inference performance',['csapp','dw-zerosglang','dlsys'],'解释缓存、调度、显存与通信开销。','Explain caches, scheduling, memory and communication costs.'),
}
PROJECT_STARTS={
 'basics':('看懂反传与小模型训练','Understand gradients and small-model training',['micrograd','makemore']),
 'classical':('学习搜索和经典AI','Learn search and classical AI',['aima_python']),
 'pretrain':('训练自己的小GPT','Train a small GPT',['nanogpt','nanochat']),
 'data':('清洗已有训练数据','Prepare existing training data',['datasets','datatrove']),
 'synthesis':('用大模型合成训练数据','Synthesize training data with LLMs',['nemo_designer','distilabel']),
 'post':('适配模型与强化学习后训练','Adapt and post-train models',['minimind','trl']),
 'rag':('做文档检索和问答','Build document retrieval and QA',['faiss','llamaindex']),
 'agents':('做一个能调用工具的Agent','Build a tool-using agent',['learn_claudecode','langgraph']),
 'inference':('研究推理引擎与性能','Study inference engines and performance',['nano_vllm','vllm']),
 'vision':('做检测、分割或图预测','Build detection, segmentation or graph prediction',['yolo','sam','pyg']),
 'generative':('做扩散图像生成','Build diffusion image generation',['diffusers']),
 'rl':('实现强化学习算法','Implement reinforcement learning',['gymnasium','cleanrl']),
 'world':('研究JEPA与世界模型','Study JEPA and world models',['ijepa','dreamerv3']),
 'robotics':('研究VLA与机器人策略','Study VLA and robot policies',['lerobot','openpi']),
 'engineering':('评测模型并记录实验','Evaluate models and track experiments',['lmeval','deepeval','mlflow']),
}
