"""Curate the migrated glossary and emit self-contained bilingual Bingo assets."""
from pathlib import Path
import json,re,shutil
from bingo_additions import NEW,FIX,EN

CATS=[
 ('math','数学与张量','Math & Tensors','数据怎样表示，模型怎样求导。','Representations, probability and derivatives.'),
 ('ml','机器学习','Machine Learning','从特征和目标，理解模型如何拟合与泛化。','Features, learning objectives and generalization.'),
 ('neural','神经网络','Neural Networks','从分数与损失，走到反传和参数更新。','From scores and losses to gradients and updates.'),
 ('vision','视觉与多模态','Vision & Multimodal','图像、音频和跨模态表示各解决什么问题。','Images, audio and cross-modal representations.'),
 ('transformer','序列与Transformer','Sequences','从Token到注意力，再到生成。','From tokens and attention to generation.'),
 ('pretrain','预训练','Pretraining','模型的初始学习、继续训练与压缩。','Initial learning, continued training and compression.'),
 ('data','数据与合成','Data & Synthesis','准备真实数据，再设计和验证合成样本。','Prepare real data; generate and validate synthetic examples.'),
 ('posttrain','微调与后训练','Post-training','数据、反馈和目标函数怎样改变模型行为。','How data, feedback and objectives change behavior.'),
 ('retrieval','检索与RAG','Retrieval & RAG','从找得到信息，到用证据回答。','From finding information to evidence-based answers.'),
 ('agents','Agent工程','Agents','把工具、状态、执行和反馈连接起来。','Tools, state, execution and feedback.'),
 ('rl','强化学习','Reinforcement Learning','通过交互与奖励学习决策。','Learning decisions through interaction and rewards.'),
 ('generative','生成模型','Generative Models','表示数据分布并生成新样本。','Modeling distributions and generating examples.'),
 ('world','世界模型与JEPA','World Models & JEPA','区分表征预测、动力学和决策。','Distinguish representations, dynamics and decisions.'),
 ('robotics','具身与机器人','Robotics','让感知与策略接到真实动作上。','Connecting perception and policies to physical actions.'),
 ('inference','推理与系统','Inference & Systems','理解缓存、内存、并行与服务性能。','Caches, memory, parallelism and serving performance.'),
 ('evaluation','评测与可信AI','Evaluation & Trust','识别数据泄漏、指标偏差与部署风险。','Data leakage, metric interpretation and deployment risks.'),
]
SOURCE={
 'math':('D2L · 数学基础','D2L: mathematical foundations','https://d2l.ai/chapter_preliminaries/index.html'),
 'ml':('Google · 机器学习课程','Google: Machine Learning Crash Course','https://developers.google.com/machine-learning/crash-course'),
 'neural':('PyTorch · 网络层与损失','PyTorch: layers and losses','https://docs.pytorch.org/docs/stable/nn.html'),
 'vision':('CS231n · 课程','CS231n: course materials','https://cs231n.stanford.edu/'),
 'transformer':('Hugging Face · 术语与例子','Hugging Face: glossary and examples','https://huggingface.co/docs/transformers/glossary'),
 'pretrain':('CS336 · 模型、数据与训练','CS336: models, data and training','https://cs336.stanford.edu/'),
 'data':('Hugging Face · Datasets','Hugging Face: Datasets','https://huggingface.co/docs/datasets/'),
 'posttrain':('TRL · 训练方法','TRL: training methods','https://huggingface.co/docs/trl/'),
 'retrieval':('FAISS · 索引与搜索','FAISS: indexing and search','https://github.com/facebookresearch/faiss/wiki'),
 'agents':('Hello-Agents · 教程','Hello-Agents: tutorial','https://github.com/datawhalechina/hello-agents'),
 'rl':('CS285 · 强化学习','CS285: reinforcement learning','https://rail.eecs.berkeley.edu/deeprlcourse/'),
 'generative':('MIT · Flow Matching与扩散','MIT: flow matching and diffusion','https://diffusion.csail.mit.edu/2025/'),
 'world':('V-JEPA 2 · 官方实现','V-JEPA 2: official implementation','https://github.com/facebookresearch/vjepa2'),
 'robotics':('LeRobot · 机器人学习文档','LeRobot: robot learning documentation','https://huggingface.co/docs/lerobot/'),
 'inference':('PyTorch · 分布式训练','PyTorch: distributed training','https://docs.pytorch.org/tutorials/distributed/home.html'),
 'evaluation':('Google · 机器学习术语','Google: Machine Learning Glossary','https://developers.google.com/machine-learning/glossary'),
}
COURSES={'math':['bbb_linear','bbb_calculus','mit1806'],'ml':['cs229','cs188'],'neural':['bbb_nn','pytorch','zero_to_hero'],'vision':['cs231n','cs224w'],'transformer':['cs224n','cs336'],'pretrain':['dw-happy','cs336'],'data':['cs336','nemo_designer','datasets'],'posttrain':['smol_course','trl'],'retrieval':['dw-rag','llamaindex'],'agents':['dw-agents','learn_claudecode'],'rl':['dw-easyrl','cs285'],'generative':['hf_diffusion','mit_diffusion'],'world':['cs285','vjepa2'],'robotics':['lerobot','openpi'],'inference':['dw-zerosglang','pytorch_distributed'],'evaluation':['cs336','lmeval','deepeval']}
FAMILIES=[
 'ai machinelearning deeplearning neuralnetwork search supervised',
 'neuralnetwork mlp parameter weight bias activation relu sigmoid gelu',
 'standardization features layernorm batchnorm leakage',
 'transformer attention ffn residual embedding architectures',
 'epoch batch gradientaccum checkpoint scheduler pretraining',
 'cosine norm vector embeddingsearch contrastive',
 'gnn matrix mlp supervised graphretrieval',
 'keypoint grounding pose pixels frame',
 'mae selfsupervised patch vit jepa',
 'ocr chunking pixels grounding',
 'search planning mpc policy',
 'template unicode token instructiondata toolcall',
 'scalar vector matrix tensor shape broadcast matmul reshape rank svd eigenvalue',
 'probability bayes expectation gaussian montecarlo likelihood entropy kl',
 'gradient chainrule jacobian hessian backprop autograd stopgradient',
 'features labels supervised unsupervised selfsupervised transfer metalearning',
 'linearreg logistic svm knn tree ensemble gbdt',
 'kmeans pca svd contrastive',
 'split crossval overfit regularize earlystop hyperparameters leakage shift',
 'metrics recall f1 auc calibration retrievalmetrics iou benchmark',
 'loss logits softmax crossentropy mse numerical',
 'optimizer learningrate sgd adam adamw scheduler gradclip initialization',
 'mlp activation residual layernorm rmsnorm batchnorm dropout prenorm',
 'batch gradientaccum mixedprecision dtype checkpoint trainmode reproducibility',
 'cnn pooling convshape resnet pixels augmentation detection segmentation sam',
 'patch vit clip contrastive vlm connector crossattention multialign grounding',
 'asr whisper tts video videogen',
 'token bpe unicode embedding weighttying teachershift perplexity',
 'attention qkv mask mha mqa gqa mla sparseattention rope longcontext',
 'ffn moe expertparallel tensorparallel',
 'sampling temperature topk topp testtime rejectionsampling',
 'icl cot prompt architectures bertgpt',
 'rnn ssm bptt rssm',
 'pretraining scaling baseinstruct continual modelmerge pruning',
 'datapipeline dataquality synthetic curriculum instructiondata packing modelcard',
 'posttraining sft finetune peft lora qlora dora quantization ptq qat',
 'preference rewardmodel rlhf rlaif rlvr rewardhacking verifier',
 'ppo grpo dpo orpo kto rloo reference advantage lengthbias',
 'distillation opd offpolicykd onoffpolicy kl',
 'processreward alignmenttax onlineeval r1',
 'prefill kvcache pagedattention flashattention prefixcache continuousbatch specdecode latency',
 'gpu roofline fusion triton profiling compile cudagraph quantkernel offload memorybudget activationckpt effective_tokens',
 'ddp fsdp zero allgather reducescatter collective tensorparallel pipelineparallel contextparallel sequenceparallelism expertparallel',
 'systems serving idempotency sandbox',
 'rag embeddingsearch chunking vectordb bm25 hnsw ivfpq hybrid reranker grounded',
 'queryrewrite graphretrieval retrievalmetrics rag',
 'agent toolcall react planning memory mcp graphworkflow contextcompress agenteval injection sandbox',
 'mdp pomdp policy return value qvalue bellman advantage exploration',
 'mc-td qlearning sarsa dqn policygradient actorcritic gae onoffpolicy importancesampling',
 'offline modelbased mpc sac ddpgtd3 trpo hierarchical goalcondition',
 'autoencoder vae elbo vqvae normalizingflow gan modecollapse',
 'diffusion schedule ddim score cfg latentdiffusion unetdit flowmatching rectifiedflow',
 'worldmodel rssm dreamerv3 jepa ijepa vjepa vjepa2 wam',
 'embodied obsstate frame pose kinematics controller trajectory slam tactile affordance',
 'bc dagger teleop dataset sim2real domainrandom',
 'vla actiontoken actionchunk act diffusionpolicy pi0 openvla lerobot realtimechunk',
 'privacy federated causal modelcard hallucination grounded injection',
]
ORDER={
 'math':'scalar vector matrix tensor shape dtype reshape broadcast matmul norm rank svd eigenvalue gradient chainrule jacobian hessian probability bayes expectation gaussian entropy kl likelihood cosine montecarlo numerical',
 'ml':'ai machinelearning features labels standardization supervised unsupervised selfsupervised linearreg logistic tree ensemble gbdt svm knn kmeans pca overfit regularize earlystop hyperparameters transfer metalearning search gnn causal',
 'neural':'deeplearning neuralnetwork mlp parameter weight bias activation relu sigmoid gelu logits softmax loss crossentropy mse autograd backprop optimizer learningrate sgd adam adamw scheduler batch gradientaccum initialization residual layernorm rmsnorm batchnorm dropout gradclip bptt stopgradient',
 'transformer':'transformer unicode token bpe embedding architectures bertgpt teachershift attention qkv mask mha mqa gqa mla rope longcontext sparseattention ffn prenorm weighttying moe rnn ssm perplexity icl cot sampling temperature topk topp',
 'pretrain':'pretraining epoch baseinstruct continual scaling mixedprecision checkpoint trainmode reproducibility modelmerge pruning',
}

def build_data(root):
 seed=json.loads((root/'data/knowledge_seed.json').read_text(encoding='utf-8'))
 allterms=seed['terms']+json.loads(json.dumps(NEW,ensure_ascii=False));catalog=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
 resources={r['id']:r for r in catalog['entries']};anchors=json.loads((root/'data/glossary_anchors.json').read_text(encoding='utf-8'))['anchors']
 norm=lambda s:re.sub('[^a-z0-9]','',s.lower());anchor_map={norm(a):a for a in anchors}
 byid={t['id']:t for t in allterms}
 for id,(name,en,summary,explain,example,pitfall) in FIX.items():byid[id].update(title=name,en=en,summary=summary,explain=[explain],example=example,pitfall=pitfall)
 EN['metrics']=dict(summary='The fraction of predicted positives that are correct.',explain=['Compute TP/(TP+FP), with a stated positive class and averaging convention.'],example='Eight correct predictions out of ten: precision 0.8.',pitfall='Precision differs from recall and overall accuracy.')
 for id,name,en in [('gqa','GQA','Grouped-Query Attention'),('icl','上下文学习','In-context Learning'),('fsdp','FSDP','Fully Sharded Data Parallel'),('compile','计算图编译','Graph Compilation'),('orpo','ORPO','Odds Ratio Preference Optimization'),('svd','奇异值分解','Singular Value Decomposition'),('jacobian','雅可比矩阵','Jacobian')]:byid[id].update(title=name,en=en)
 for t in allterms:
  old=t['category'];id=t['id']
  if id in {'cnn','pooling','convshape'}:t['category']='vision'
  if id in {'datapipeline','packing','synthetic','curriculum','dataquality','instructiondata'}:t['category']='data'
  if id in {'finetune','peft','lora','qlora','dora'}:t['category']='posttrain'
  if id in {'quantization','memorybudget','activationckpt','sequenceparallel'}:t['category']='inference'
  if id in {'mixedprecision','checkpoint','trainmode','reproducibility'}:t['category']='pretrain'
  if id in {'metrics','auc','calibration','crossval','leakage','shift','privacy','benchmark','modelcard','onlineeval','hallucination'}:t['category']='evaluation'
  if id in {'rag','embeddingsearch','chunking','vectordb','bm25','hnsw','ivfpq','hybrid','reranker','grounded','queryrewrite','graphretrieval','retrievalmetrics'}:t['category']='retrieval'
  if id in {'worldmodel','rssm','dreamerv3','jepa','ijepa','vjepa','vjepa2','wam'}:t['category']='world'
  if id=='sequenceparallel':t.update(id='effective_tokens',title='有效Token吞吐',en='Effective Token Throughput')
  if id=='opd':t['courses']=['trl','reasoning_scratch']
  if id=='grpo':t['courses']=['trl','reasoning_scratch','cs336']
 source_overrides={
 'tensor':('PyTorch · Tensor','PyTorch: Tensor','https://docs.pytorch.org/docs/stable/tensors.html'),
 'rmsnorm':('PyTorch · RMSNorm','PyTorch: RMSNorm','https://docs.pytorch.org/docs/stable/generated/torch.nn.RMSNorm.html'),
 'softmax':('PyTorch · Softmax','PyTorch: Softmax','https://docs.pytorch.org/docs/stable/generated/torch.nn.Softmax.html'),
 'pooling':('PyTorch · MaxPool2d','PyTorch: MaxPool2d','https://docs.pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html'),
 'grpo':('TRL · GRPO与实现差异','TRL: GRPO and implementation variants','https://huggingface.co/docs/trl/grpo_trainer'),
 'opd':('TRL · 同策略蒸馏','TRL: on-policy distillation','https://huggingface.co/docs/trl/distillation_trainer'),
 'dpo':('TRL · DPO','TRL: DPO','https://huggingface.co/docs/trl/dpo_trainer'),
 'kto':('TRL · KTO','TRL: KTO','https://huggingface.co/docs/trl/kto_trainer'),
 'lora':('PEFT · LoRA','PEFT: LoRA','https://huggingface.co/docs/peft/developer_guides/lora'),
 'synthetic':('NeMo Data Designer · 配置、预览与验证','NeMo Data Designer: configuration, preview and validation','https://docs.nvidia.com/nemo/datadesigner/getting-started/welcome'),
 'moe':('Switch Transformers · 稀疏专家','Switch Transformers: sparse experts','https://arxiv.org/abs/2101.03961'),
 'mcp':('MCP · 官方介绍','MCP: official introduction','https://modelcontextprotocol.io/docs/getting-started/intro'),
 'privacy':('Opacus · 差分隐私','Opacus: differential privacy','https://opacus.ai/docs/introduction'),
 'backprop':('3Blue1Brown · 反传推导','3Blue1Brown: backpropagation calculus','https://www.3blue1brown.com/lessons/backpropagation-calculus'),
 }
 result=[]
 for t in allterms:
  id=t['id'];legacy='sequenceparallel' if id=='effective_tokens' else id;english=EN[legacy];category=t['category']
  names=[t['en'],id,*t.get('aliases',[])];anchor=next((anchor_map[norm(n)] for n in names if norm(n) in anchor_map),None)
  sources=[]
  for s in [source_overrides.get(id),('Google · 对应术语','Google: term definition','https://developers.google.com/machine-learning/glossary#'+anchor) if anchor else None,SOURCE[category]]:
   if s and s[2] not in [x['url'] for x in sources]:sources.append(dict(zh=s[0],en=s[1],url=s[2]))
  related=[]
  for family in FAMILIES:
   ids=family.split()
   if id in ids:
    for other in ids:
     if other!=id and other not in related:related.append(other)
  courses=t.get('courses',[]) if id in {'opd','grpo'} else COURSES[category]
  if id in 'scalar vector matrix tensor shape dtype reshape broadcast matmul'.split():courses=['python_numpy','pytorch','bbb_linear']
  if id in 'gradient chainrule jacobian hessian backprop autograd softmax logits crossentropy loss'.split():courses=['bbb_nn','pytorch','zero_to_hero']
  if id in 'cnn pooling convshape resnet'.split():courses=['cs231n','pytorch']
  if id in 'mha mqa gqa mla kvcache'.split():courses=['cs336','nano_vllm']
  if id=='synthetic':courses=['nemo_designer','datasets','cs336']
  if id in 'jepa ijepa vjepa'.split():courses=['cs231n',id if id in resources else 'ijepa']
  if id=='vjepa2':courses=['cs224r','vjepa2']
  if id=='dreamerv3':courses=['cs285','dreamerv3']
  courses=[dict(id=i,path={'course':'courses','project':'projects','book':'books'}[resources[i]['kind']]+'/'+i+'.html',zh=resources[i]['title'],en=resources[i]['en']['title']) for i in courses if i in resources][:3]
  result.append(dict(id=id,category=category,zh=dict(title=t['title'],summary=t['summary'],explain=t['explain'],example=t['example'],pitfall=t['pitfall'],deep=t.get('deep',[])),en=dict(title=t['en'],**english,deep=[]),aliases=list(dict.fromkeys(t.get('aliases',[]))),related=related[:5],sources=sources[:3],courses=courses))
 expanded={t['id']:t for t in result}
 expanded['grpo']['zh']['pitfall']='规范缩写为GRPO；省去critic不代表没有奖励与rollout成本。标准化、裁剪与长度处理应核对具体实现。'
 for id,paras in {
  'grpo':['Track three policies separately: the trainable current policy, the old policy that generated a fixed rollout batch, and any reference policy used for a KL term. Their roles differ.','Group normalization is an illustrative version, not a universal GRPO specification. Check reward scaling, sequence-length reduction and clipping in the chosen implementation.'],
  'opd':['The student produces the prefixes on which feedback is requested. This targets a distribution the student actually visits, including its imperfect continuations.','The teacher is normally fixed. Access to teacher logits, tokenizer compatibility, divergence direction and sampling details determine the usable implementation.'],
  'tensor':['Read a shape together with axis names. In (B,S,H), a reduction over S averages tokens; a reduction over H averages features. Equal axis lengths do not make these operations equivalent.','Dtype determines representation and device determines placement. Gradient tracking records dependencies; it is separate from the tensor being a trainable model parameter.'],
  'softmax':['Adding the same constant to all logits leaves the distribution unchanged. Subtracting the maximum therefore improves numerical behavior without changing the ideal result.','A cross-entropy API that expects logits generally incorporates the necessary normalization. Applying softmax first can change the intended computation.'],
  'pooling':['Local spatial pooling reduces height and width while typically retaining channel count. Global average pooling and sentence-embedding pooling reduce different axes, so always check the operator and input layout.'],
  'attention':['The score matrix has one row per query and one column per key position. Normalization is usually across allowed keys for each query; the weighted mixture then uses the value representations.'],
  'synthetic':['Design coverage and validation before scaling generation. Data Designer supports configured columns and dependencies; a validator can check format or constraints but cannot establish every factual claim.','Compare downstream behavior using held-out data. A large generated dataset can amplify repeated mistakes or contaminate evaluation if its provenance is not tracked.'],
  'jepa':['The predicted object is a target representation. Whether that representation supports action-conditioned planning depends on additional training and evaluation, not on the JEPA name alone.'],
 }.items():expanded[id]['en']['deep']=paras
 expanded['synthetic']['zh']['deep']=['先确定希望覆盖的任务、字段关系与验收规则，再扩大生成量。NeMo Data Designer可按列与依赖组织数据，并接入验证器；格式通过不代表事实一定正确。','用独立评测比较生成数据的作用，记录来源和过滤过程。重复错误、单一风格与评测污染都可能随着生成量一起放大。']
 ids={t['id'] for t in result};assert len(ids)==len(result)==len(seed['terms'])+len(NEW)
 canonical={norm(t[lang]['title']):t['id'] for t in result for lang in ['zh','en'] if norm(t[lang]['title'])}
 for t in result:
  t['aliases']=[a for a in t['aliases'] if norm(a) not in canonical or canonical[norm(a)]==t['id']]
  assert t['related'] and all(i in ids for i in t['related']),t['id']
 for cat in CATS:
  order=ORDER.get(cat[0],'').split();positions={id:i for i,id in enumerate(order)}
  selected=[t for t in result if t['category']==cat[0]];selected.sort(key=lambda t:positions.get(t['id'],1000))
  for i,t in enumerate(selected):t['order']=i
 result.sort(key=lambda t:([c[0] for c in CATS].index(t['category']),t['order']))
 data=dict(version=1,updated='2026-11-01',legacy_count=300,migrations={'sequenceparallel':'effective_tokens'},categories=[dict(id=id,zh=zh,en=en,description={'zh':zs,'en':es}) for id,zh,en,zs,es in CATS],terms=result)
 (root/'data/knowledge.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 return data

def write_knowledge(root,language,data):
 docs=root/('docs' if language=='zh' else 'docs_en');dest=docs/'knowledge';dest.mkdir(exist_ok=True)
 zh=language=='zh'
 text='---\nhide:\n  - toc\n---\n\n# '+('AI 知识 Bingo' if zh else 'AI Knowledge Bingo')+'\n\n'
 text+='<div id="ai-bingo-app" data-language="'+language+'"><p>'+('正在载入知识网格…' if zh else 'Loading the knowledge board…')+'</p></div>\n\n'
 text+='<noscript>'+('请启用JavaScript以查看本地词条。' if zh else 'Enable JavaScript to use the local knowledge board.')+'</noscript>\n\n<link rel="stylesheet" href="bingo.css">\n<script src="bingo-data.js" defer></script>\n<script src="bingo.js" defer></script>\n'
 (dest/'index.md').write_text(text,encoding='utf-8')
 for name in ['bingo.js','bingo.css']:shutil.copy2(root/'web'/name,dest/name)
 (dest/'bingo-data.js').write_text('window.AI_BINGO='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';',encoding='utf-8')
 refs=json.loads((root/'data/knowledge_sources.json').read_text(encoding='utf-8'))
 text=('# 词典与交互参考\n\n按主题、机制、例子与易混点整理词条；相关术语按概念关系编排。下列项目用于核对术语和参考讲解方式。\n\n' if zh else '# Glossaries and Interactive References\n\nEntries use definitions, mechanisms, examples and distinctions. Related concepts follow semantic relationships. These sources inform terminology checks and explanatory design.\n\n')
 text+=''.join('- ['+r['title']+']('+r['url']+')\n' for r in refs)
 (dest/'sources.md').write_text(text,encoding='utf-8')

def index_terms(site,data,language):
 path=site/'search/search_index.json';index=json.loads(path.read_text(encoding='utf-8'))
 index['docs']=[item for item in index['docs'] if not item['location'].startswith('knowledge/index.html#t=')]
 for t in data['terms']:
  d=t[language];index['docs'].append(dict(location='knowledge/index.html#t='+t['id'],title=d['title'],text=' '.join([t['id'],t['zh']['title'],d['summary'],*d['explain'],d['example'],d['pitfall'],*t['aliases']])))
 path.write_text(json.dumps(index,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
 (site/'search/search_index.js').write_text('var __index = '+json.dumps(index,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
