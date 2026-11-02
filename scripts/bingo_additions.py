"""Focused additions and corrections: distinct concepts get distinct records."""
from bingo_english import EN,add
NEW=[]
def zh(text):
 for line in text.strip().splitlines():
  v=[x.strip() for x in line.split('|')];assert len(v)==8,line
  NEW.append(dict(id=v[0],category=v[1],title=v[2],en=v[3],summary=v[4],explain=[v[5]],example=v[6],pitfall=v[7]))
zh('''
rmsnorm | neural | RMSNorm | Root Mean Square Normalization | 按特征的均方根缩放向量，通常不减去均值。 | 与LayerNorm相比，省去中心化；具体实现仍有epsilon和可学习缩放。 | 将一个Token的隐藏向量除以其均方根，再乘缩放参数。 | RMSNorm和LayerNorm不是完全相同的归一化公式。
mqa | transformer | MQA | Multi-Query Attention | 多个查询头共享一组K和V。 | 相比每头各有K/V的MHA，MQA减少KV缓存；GQA则允许多个KV组。 | 8个查询头使用1个KV头。 | 减少KV头不等于把所有注意力头合并成一个。
temperature | transformer | 温度 | Temperature | 采样前用温度缩放logits，改变分布的集中程度。 | 对正温度T计算softmax(z/T)。降低温度通常更集中；T趋近0的极限与实际API的0值处理需区分。 | logits相同则调整正温度后仍是均匀分布。 | 温度影响随机性，不能单独保证事实正确。
topk | transformer | Top-k采样 | Top-k Sampling | 只在概率最高的k个候选中重新归一化并采样。 | k固定候选数量，不固定这些候选的总概率质量。 | k=1相当于选择最高分候选，平分时需处理并列。 | 检索中的top-k和解码中的Top-k使用场景不同。
topp | transformer | Top-p采样 | Nucleus Sampling | 保留累计概率达到阈值p的高概率候选集合，再采样。 | 先按概率排序，再取覆盖阈值的前缀；候选个数随分布而变。 | 概率[0.7,0.2,0.1]且p=0.8时，通常保留前两项。 | Top-p的p是概率阈值，不是候选数量。
cot | transformer | 思维链 | Chain of Thought | 通过中间步骤文本组织模型的求解过程。 | 可由提示示例、监督训练或推理过程产生；步骤是否有用应按最终任务和可靠性评估。 | 把多步算术分成若干中间计算。 | 可读的解释不一定忠实反映模型内部机制。
logits | neural | Logits | Logits | 模型输出的未归一化分数。 | 对分类可用Softmax转成分布；许多交叉熵接口直接接收logits以保证数值稳定。 | 二分类分数[2,0]还不是[2,0]的概率。 | logits可以为负；不要求总和等于1。
loss | neural | 损失函数 | Loss Function | 将模型预测与训练目标的差异变成可优化的量。 | 样本、Token和类别维度如何归约，会改变参数接收到的梯度权重。 | 交叉熵衡量目标类别的负对数概率。 | 训练loss和业务指标并不一定一致。
optimizer | neural | 优化器 | Optimizer | 根据梯度与内部状态更新参数的算法。 | 反向传播算梯度，优化器决定如何使用梯度；动量和自适应统计会跨步保存。 | SGD执行w←w−ηg，Adam还维护梯度统计。 | optimizer.step不替代梯度计算或正确的清梯度操作。
learningrate | neural | 学习率 | Learning Rate | 控制参数更新尺度的超参数。 | 它与梯度大小、优化器、批次和调度共同影响实际更新；不同参数组可以有不同学习率。 | 学习率太大可能让loss振荡或发散。 | 小学习率也不能修复错误的目标或数据。
adam | neural | Adam | Adaptive Moment Estimation | 利用梯度一阶与二阶矩估计调节更新的优化器。 | 通常维护梯度与平方梯度的指数移动平均，并作偏差修正。 | 在稀疏或不同尺度梯度上给参数不同更新幅度。 | Adam里的L2项与AdamW的解耦权重衰减一般不同。
gradientaccum | neural | 梯度累积 | Gradient Accumulation | 多个微批次累积梯度后再进行一次参数更新。 | 按目标归约梯度，并在正确的优化器步边界清梯度、更新调度器。 | 连续处理4个8样本微批次，再更新一次。 | 累积与真正大批次在BatchNorm等条件下未必等价。
earlystop | ml | 提前停止 | Early Stopping | 根据验证表现停止继续训练，限制过拟合与浪费。 | 预先选监控指标、改善阈值和等待窗口，保留合适的检查点。 | 验证loss若干轮无改善后停止。 | 不应反复用测试集决定停止时刻。
features | ml | 特征 | Feature | 输入中被模型使用的属性或表示分量。 | 特征可以来自人工构造，也可以通过神经网络学习；含义依赖任务和表示。 | 表格中的年龄列，或图像编码器的一维隐藏特征。 | 相关特征不自动具有因果作用。
labels | ml | 标签 | Label | 监督学习中指定的目标结果或标注。 | 标签的定义、时间边界、一致性和噪声会直接影响模型学到的行为。 | 把一封邮件标成垃圾邮件。 | 标签不是永远无误的真相，尤其是偏好与主观任务。
hyperparameters | ml | 超参数 | Hyperparameter | 训练过程或模型结构中由外部选择的设置。 | 区别于通过优化学到的参数；通常使用验证数据和实验预算选择。 | 学习率、层数、批次大小和LoRA秩。 | 反复查看测试结果来调超参数会污染最终评估。
selfsupervised | ml | 自监督学习 | Self-supervised Learning | 从数据本身构造预测目标的表示学习方法。 | 目标不必由人工逐条标注，但仍存在明确的训练信号和数据选择。 | 从前文预测下一个Token，或从图像上下文预测被遮部分。 | 无人工标签不等于没有监督目标，也不等于数据天然干净。
federated | evaluation | 联邦学习 | Federated Learning | 在多个参与方本地进行部分训练，并聚合更新。 | 数据可留在本地，但更新通信、设备差异和参与方可信度仍需设计。 | 多台设备协同改善一个模型。 | 数据不集中不自动保证隐私，需要另行分析泄露风险。
hessian | math | 海森矩阵 | Hessian | 标量函数的二阶偏导数组成的矩阵。 | 描述局部曲率，可用于分析优化，但大模型通常不会显式存完整海森矩阵。 | 对L=w²，二阶导数为2。 | Jacobian记录一阶输出敏感性，Hessian描述二阶曲率。
eigenvalue | math | 特征值与特征向量 | Eigenvalue and Eigenvector | 线性变换下方向保持不变、只改变尺度的特殊方向与倍数。 | 若Av=λv且v非零，则v为特征向量、λ为特征值。 | 对角矩阵沿坐标轴进行缩放。 | 特征值与奇异值通常不同；一般矩阵可能出现复特征值。
recall | evaluation | 召回率 | Recall | 实际正例中被模型找出的比例。 | Recall=TP/(TP+FN)，与精确率从不同分母看结果；需声明正例及平均方式。 | 10个实际目标找出8个，召回率为0.8。 | 只提高召回率可能引入很多误报。
f1 | evaluation | F1分数 | F1 Score | 精确率与召回率的调和平均。 | F1=2PR/(P+R)；多分类时micro、macro等平均方式含义不同。 | P=1、R=0.5时F1约为0.667。 | F1不直接反映真负例，也不代表概率校准。
gbdt | ml | 梯度提升树 | Gradient Boosted Decision Trees | 逐步加入树模型，改善当前整体目标的集成方法。 | 新树近似拟合损失的下降方向，学习率、深度和轮数一起控制复杂度。 | 用多棵浅树逐步改善表格预测。 | 与并行构建、再平均的随机森林训练方式不同。
ptq | inference | 训练后量化 | Post-training Quantization | 在已有模型上确定低比特表示与缩放等参数。 | 部分方法需要校准数据；权重、激活和KV缓存可使用不同策略。 | 对已有权重做分组INT4量化。 | PTQ不意味着完全没有校准或计算成本。
qat | inference | 量化感知训练 | Quantization-aware Training | 训练时模拟或纳入量化影响，使模型适应低精度部署。 | 常在训练图中引入伪量化等操作，具体反向规则与部署内核需匹配。 | 让模型在模拟INT8误差的条件下继续训练。 | QAT与直接保存低比特权重不是同一件事。
kto | posttrain | KTO | Kahneman-Tversky Optimization | 一种可利用好/坏反馈而非必须成对偏好的对齐方法。 | 目标以参考模型及相对价值的设计来学习期望行为，输入约定与DPO、ORPO不同。 | 给回答标注desirable或undesirable。 | 使用同一数据集时也要匹配各方法的输入语义。
sarsa | rl | SARSA | State-Action-Reward-State-Action | 使用实际下一动作来构造TD目标的动作价值学习方法。 | 与标准Q-learning的最大化下一动作目标不同，SARSA目标反映当前行为。 | 按实际采样的下一动作更新当前Q值。 | SARSA与Q-learning在探索期间可能学到不同策略。
zero | inference | ZeRO | Zero Redundancy Optimizer | 通过分片减少数据并行训练中的冗余状态。 | 不同阶段逐步分片优化器状态、梯度和参数；执行时仍需相应集合通信。 | 多设备分担原本每卡都有的优化器状态。 | ZeRO阶段、Offload和具体框架实现应分别核对。
allgather | inference | All-gather | All-gather | 将各进程持有的片段收集到每个进程。 | 输出由所有参与方的片段拼接组成，不像all-reduce那样做求和等归约。 | 每卡一段参数，计算前收集完整所需部分。 | 聚合片段和数值归约是不同操作。
reducescatter | inference | Reduce-scatter | Reduce-scatter | 先进行跨进程归约，再把结果分片分给进程。 | 每个参与方最终只得到归约结果的一部分，常用于分片训练。 | 求和梯度后，每卡保留相应分片。 | 其输出分布与all-reduce不同。
cudagraph | inference | CUDA Graph | CUDA Graph | 捕获并重复执行一组GPU操作，减少CPU侧启动开销。 | 适用性受形状、内存与控制流等约束影响，通常与计算图编译配合。 | 重放一段重复的推理执行序列。 | 图捕获不是自动把任意Python动态逻辑编译成高效内核。
sequenceparallelism | inference | 序列并行 | Sequence Parallelism | 沿序列维度拆分部分模型计算或激活的并行策略。 | 具体切分对象依框架而异；与上下文并行可有关联但不能直接互换术语。 | 将部分逐Token操作与激活分布到多个进程。 | 它不是有效Token吞吐指标，也不只是把长文本切成短样本。
''')

add('''
rmsnorm | Normalization using the root mean square of features. | Usually scale without subtracting the feature mean, with numerical stabilization and learned gain. | Normalize one token's hidden vector. | It differs mathematically from LayerNorm.
mqa | Attention with one shared key/value head for multiple query heads. | Reduces KV storage compared with separate KV heads. | Eight query heads share one KV head. | GQA permits more than one shared KV group.
temperature | A positive scale controlling sampling-distribution concentration. | Apply softmax to logits divided by T. | Equal logits stay equally probable. | Temperature does not establish answer correctness.
topk | Sampling after retaining the k highest-scoring candidates. | Renormalize probability inside the retained set. | k=1 selects a highest-score candidate. | Decoding top-k differs from retrieving k documents.
topp | Sampling from a probability-mass-based candidate set. | Keep a sorted prefix reaching threshold p and renormalize. | [0.7,0.2,0.1] with p=0.8 retains two candidates. | p is a probability threshold, not a count.
cot | Intermediate reasoning text used during problem solving. | Prompts or training can encourage stepwise responses. | Break arithmetic into intermediate calculations. | A readable explanation need not faithfully describe internal computation.
logits | Unnormalized scores produced by a model. | Softmax or another mapping converts them to the required output representation. | Scores [2,0] are not probabilities. | Logits can be negative and need not sum to one.
loss | A quantity expressing the training objective. | Reduction across examples or tokens affects gradient weighting. | Use negative log probability of the target class. | Lower training loss is not identical to better deployment quality.
optimizer | An algorithm updating parameters from gradients and state. | Backpropagation computes gradients; the optimizer chooses the update. | SGD subtracts learning rate times gradient. | A parameter update does not replace gradient calculation.
learningrate | A hyperparameter controlling update scale. | It interacts with the optimizer, gradients and schedule. | Excessive steps can make loss oscillate. | Tiny steps cannot repair a mistaken objective.
adam | Adaptive optimization using gradient moment estimates. | Maintain moving statistics and apply bias correction under the algorithm. | Adjust parameter-wise update scales. | Adam's L2 regularization differs from AdamW's decoupled decay.
gradientaccum | Combining several microbatch gradients before updating parameters. | Scale and clear gradients at the correct optimizer-step boundary. | Four microbatches of eight examples. | Batch-dependent operations can differ from a true batch of 32.
earlystop | Stopping training based on a validation criterion. | Define the metric, tolerance and patience beforehand. | Stop after validation loss stops improving. | Do not use the final test set as the stopping signal.
features | Attributes or representation components used by a model. | Features may be engineered or learned. | A table column or hidden activation. | Predictive association does not imply causality.
labels | Target annotations used in supervised learning. | Definitions, consistency and noise determine the training signal. | Mark an email as spam. | Labels can be mistaken or subjective.
hyperparameters | Externally selected model or training settings. | Choose them using a suitable validation process. | Learning rate, layer count or LoRA rank. | Repeated test-based tuning compromises final evaluation.
selfsupervised | Learning from targets constructed from the data itself. | No manual per-example label is required for the objective. | Predict the next token. | It still has supervision and can learn data errors.
federated | Training partly at multiple data-holding participants. | Aggregate local updates under a defined coordination protocol. | Improve a shared model across devices. | Local data storage alone does not guarantee privacy.
hessian | A matrix of second derivatives of a scalar function. | Describes local curvature rather than first-order sensitivity. | The second derivative of w² is two. | It is different from a Jacobian.
eigenvalue | A scale factor for a direction preserved by a linear map. | Av=λv for nonzero v defines the relationship. | A diagonal matrix scales coordinate directions. | Eigenvalues and singular values are not generally identical.
recall | The fraction of actual positives recovered. | Compute TP divided by TP+FN under a stated convention. | Recover eight of ten targets: 0.8. | High recall can coexist with many false positives.
f1 | The harmonic mean of precision and recall. | Compute 2PR/(P+R), with a stated averaging convention. | P=1 and R=0.5 gives about 0.667. | It does not directly measure true negatives or calibration.
gbdt | An ensemble adding trees to improve an objective sequentially. | New trees approximate an improvement direction under the loss. | Fit successive shallow trees to improve predictions. | Random forests build their ensemble differently.
ptq | Quantizing an already trained model. | Determine formats and scales, possibly using calibration data. | Convert weight groups to a low-bit representation. | Post-training does not mean zero calibration cost.
qat | Training with quantization effects represented in the computation. | Simulate lower-precision behavior with suitable gradient handling. | Continue learning with fake quantization. | Training representation and deployment kernels must agree.
kto | Alignment using desirability-style feedback. | Its objective and data assumptions differ from paired-preference methods. | Label answers desirable or undesirable. | Do not substitute another method's input format without checking semantics.
sarsa | TD action-value learning using the actual next action. | Its target follows the behavior policy instead of maximizing over next actions. | Update from a sampled state-action transition. | It can differ from Q-learning during exploration.
zero | Sharding redundant states in data-parallel training. | Stages progressively partition optimizer state, gradients and parameters. | Distribute optimizer-state storage across devices. | Stage choice and offload settings are separate decisions.
allgather | Gathering every participant's shard at every participant. | Collect the pieces without a numerical reduction. | Assemble needed parameter shards. | Gathering differs from summing tensors.
reducescatter | Reducing inputs and distributing result shards. | Each participant retains only a designated portion of the reduced result. | Sum gradients and keep local shards. | Output placement differs from all-reduce.
cudagraph | Capturing GPU operations for repeated execution. | Replay can reduce launch overhead under memory and execution constraints. | Replay a repeated inference sequence. | Graph capture is different from general graph compilation.
sequenceparallelism | Partitioning sequence-related computation or activations across workers. | The exact operations depend on the framework and parallel setup. | Distribute selected per-token operations. | It is not an effective-token throughput metric.
''')

zh('''
ai | ml | 人工智能 | Artificial Intelligence | 研究和构建感知、推理、学习与决策等能力的系统。 | 机器学习是其中一类方法，搜索、规划和符号推理等也属于AI研究范围。 | 一个系统可以用搜索规划路径，也可以用神经网络识别物体。 | AI不只指大语言模型或聊天机器人。
machinelearning | ml | 机器学习 | Machine Learning | 用数据或交互经验调整模型，使其在任务上获得规律与能力。 | 明确数据、目标、假设与评估，才能判断训练结果能否泛化。 | 从标注邮件学习垃圾邮件分类。 | 拟合已有样本不等于在新场景中可靠。
deeplearning | neural | 深度学习 | Deep Learning | 利用多层可学习表示完成预测、生成或决策的机器学习方法。 | 深层网络将输入逐步变换成任务表示，通常用梯度方法联合优化。 | 从像素到局部特征，再到图像类别。 | 深度并不自动带来更好效果，数据与优化同样重要。
neuralnetwork | neural | 神经网络 | Neural Network | 由参数化运算与非线性组成的可学习函数。 | 训练时根据目标计算损失，通过求导更新权重、偏置等参数。 | 两层MLP将一组特征映射成分类分数。 | 神经网络是数学计算模型，不能直接等同生物大脑。
transformer | transformer | Transformer | Transformer | 以注意力与逐位置前馈变换等模块组织序列表示的网络架构。 | 通过位置表示、注意力、FFN、残差和归一化形成模块；编码器、因果解码器有不同约束。 | 一个Token用注意力吸收前文信息，再预测下一Token。 | Transformer是架构家族，不只用于文本，也不只存在因果版本。
parameter | neural | 参数 | Parameter | 模型在训练中被学习或更新的数值。 | 权重、偏置和某些缩放项是参数；是否更新还取决于冻结设置及优化器配置。 | 一个线性层保存权重矩阵和可选偏置。 | 参数与外部选择的学习率等超参数不同。
weight | neural | 权重 | Weight | 控制输入分量如何组合或变换的模型参数。 | 在线性层z=Wx+b中，W的每个元素决定某输入对某输出的影响。 | 一个输入特征通过一列权重影响多个输出。 | 单个权重大小不总能直接说明特征的重要程度。
bias | neural | 偏置参数 | Bias Parameter | 在线性变换中添加的、与当前输入值无关的可学习项。 | z=Wx+b使输出可整体平移；并非每种层都需要独立偏置。 | 单个神经元输出wx+b。 | 偏置参数不同于统计偏差或社会公平中的偏见。
epoch | pretrain | 训练轮次 | Epoch | 对一个定义好的训练数据集合完成一遍遍历。 | 一个epoch含多少优化器步取决于批次、分布式划分、采样和梯度累积。 | 1000样本、每批100且无丢弃，通常有10个微批次。 | 流式数据或无限采样训练中，一轮的定义需要另行声明。
relu | neural | ReLU | Rectified Linear Unit | 把负输入映射为0、保留非负输入的激活函数。 | 计算max(0,x)，引入非线性；0处的反向规则按实现约定。 | [-2,0,3]变成[0,0,3]。 | 长期处于负区间的单元可能得不到有效梯度。
sigmoid | neural | Sigmoid | Sigmoid | 把实数平滑映射到0到1之间的函数。 | σ(x)=1/(1+exp(-x))，常用于二分类概率接口或门控。 | σ(0)=0.5。 | 输出在0到1之间不自动代表概率已校准。
gelu | neural | GELU | Gaussian Error Linear Unit | 利用高斯分布函数对输入进行平滑门控的激活函数。 | 常写成xΦ(x)，实现中也可使用近似公式。 | 与ReLU硬截断不同，部分负值仍能通过。 | GELU不是把所有负数直接设为0。
standardization | ml | 标准化 | Standardization | 用训练数据统计量调整特征的中心和尺度。 | 常见z-score为(x−均值)/标准差；推理使用训练时确定的统计量。 | 对不同单位的表格特征先做尺度处理。 | 不要用测试集统计量拟合预处理；它与LayerNorm不是同一操作。
''')
add('''
ai | Building systems with abilities such as perception, reasoning, learning and decision making. | AI includes machine learning as well as other methods. | Use search to plan a route. | AI is broader than language models.
machinelearning | Adapting a model from data or interaction experience. | Define the task, objective, assumptions and evaluation. | Learn a spam classifier from labeled emails. | Fitting old examples does not establish generalization.
deeplearning | Machine learning using multiple learned representation layers. | Optimize composed transformations for a task. | Map pixels through intermediate features to a class. | Greater depth is not automatically better.
neuralnetwork | A learnable function made from parameterized operations and nonlinearities. | Train parameters using an objective and suitable updates. | A two-layer classification network. | The mathematical model is not a literal biological brain.
transformer | An architecture family organizing attention and feed-forward transformations. | Position handling, residuals, normalization and attention constraints define a particular variant. | Predict a token using previous context. | Transformers support more than text or causal decoding.
parameter | A numerical value learned or updated within a model. | Training configuration determines which parameters change. | A linear layer's matrix. | Parameters differ from externally selected hyperparameters.
weight | A parameter controlling how input components are transformed or combined. | In z=Wx+b, W maps input features to outputs. | One feature contributes to several outputs. | Weight magnitude alone need not measure feature importance.
bias | An input-independent learnable offset in a transformation. | Add b to Wx in a linear layer. | Compute wx+b for one neuron. | This parameter differs from statistical bias or social bias.
epoch | One traversal of a defined training collection. | Step counts depend on batching, sampling and accumulation. | Ten batches cover 1,000 examples at batch size 100. | Streaming training needs an explicit epoch convention.
relu | An activation equal to max(0,x). | It introduces nonlinearity by suppressing negative inputs. | [-2,0,3] becomes [0,0,3]. | Persistently inactive units may receive no useful gradient.
sigmoid | A smooth mapping from real values into (0,1). | It is used in binary-output interfaces and gates. | Sigmoid of zero is 0.5. | Bounded output does not imply calibrated probability.
gelu | An activation using a smooth Gaussian-based gate. | A common definition is x times the normal CDF. | Some negative inputs remain nonzero. | GELU is not a hard zeroing of negative values.
standardization | Centering and scaling features using learned data statistics. | Fit preprocessing on training data and reuse it at evaluation. | Apply a z-score transform. | Test-set statistics can cause leakage.
''')

FIX={
 'layernorm':('LayerNorm','Layer Normalization','对每个样本或Token的指定特征维度进行中心化与缩放。','先减去特征均值，再除以标准差并作可学习变换；RMSNorm则不进行同样的中心化。','对一个Token的隐藏向量做归一化。','它不使用BatchNorm那样的批次统计；与RMSNorm公式不同。'),
 'privacy':('差分隐私','Differential Privacy','用输出分布对单条记录变化的敏感程度约束隐私泄露。','训练中常结合逐样本梯度裁剪、加噪与隐私预算核算；具体保证依赖机制与假设。','在给定隐私预算下训练并报告参数。','联邦学习只规定训练组织方式，不自动提供差分隐私保证。'),
 'metrics':('精确率','Precision','预测为正例的样本中，真正正确的比例。','Precision=TP/(TP+FP)，用于衡量正例预测的可信程度；需说明正类与平均方式。','预测10个目标，其中8个正确，精确率0.8。','精确率、召回率和总体准确率的分母不同。'),
 'ensemble':('随机森林','Random Forest','通过多棵有差异的决策树聚合预测的集成方法。','常结合样本重采样和随机特征选择，再进行投票或平均；与逐步提升的GBDT训练方式不同。','平均多棵树的回归预测。','随机森林和梯度提升树不是同一个算法。'),
 'unsupervised':('无监督学习','Unsupervised Learning','从没有外部目标标签的数据中学习结构或分布。','聚类、密度估计等任务各有自己的目标；自监督则显式从数据构造预测目标。','用K-means发现一组数据的分组结构。','无监督不意味着没有优化目标，也不意味着模型必然发现人类期望的类别。'),
 'collective':('All-reduce','All-reduce','在进程组内归约各方数据，并把结果交给每个参与方。','归约可以是求和等操作；all-gather收集片段、reduce-scatter分发归约分片，语义不同。','对各卡梯度求和，再让各卡得到同样结果。','数学上的求和与训练框架最终采用求和还是平均需分别核对。'),
}
