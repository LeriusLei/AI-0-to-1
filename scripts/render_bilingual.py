"""Render two complete MkDocs editions from the reviewed bilingual catalog."""
from pathlib import Path
import json,re,sys,shutil
ROOT=Path(__file__).resolve().parents[1]
PUBLIC_URL='https://leriuslei.github.io/AI-0-to-1/'
import yaml
from editorial_content import COURSE_GUIDES,PROJECT_GUIDES,LINK_LABELS
from site_pages import write_tools,write_coverage,CSS
from business_pages import write_business
from build_bingo import build_data,write_knowledge
D=json.loads((ROOT/'data/catalog.json').read_text(encoding='utf-8'))
M=json.loads((ROOT/'data/github_metadata.json').read_text(encoding='utf-8'))
changes=json.loads((ROOT/'data/selection_changes.json').read_text(encoding='utf-8'))
R={r['id']:r for r in D['entries']}
KNOWLEDGE=build_data(ROOT)
meta={m['requested'].lower():m for m in M['repositories']}
meta.update({m['repo'].lower():m for m in M['repositories'] if m.get('repo')})
FRAMEWORK=[
 ('编程与工具','Programming and tools',['cs50p','python_numpy','missing_semester'],[], '先掌握Python、数组、命令行与Git。','Learn Python, arrays, the shell and Git.'),
 ('数学基础','Mathematics',['bbb_linear','bbb_calculus','mit1806','stat110'],[], '3Blue1Brown建立直觉，正式课程补系统知识。','Use visual intuition alongside systematic mathematics courses.'),
 ('机器学习与经典AI','Machine learning and classical AI',['cs229','cs188'],['aima_python'],'统计学习、搜索、规划与决策。','Statistical learning, search, planning and decisions.'),
 ('深度学习','Deep learning',['bbb_nn','pytorch','zero_to_hero'],['micrograd','makemore'],'反传公式→自动微分→训练循环。','Backpropagation calculus, autodiff and a training loop.'),
 ('大模型与预训练','Language models and pretraining',['dw-happy','cs336'],['nanogpt','nanochat','litgpt'],'tiny GPT之后做CS336 A1，再读完整流程。','Build a tiny GPT, complete CS336 A1, then inspect a fuller pipeline.'),
 ('数据处理与合成','Data processing and synthesis',['cs336','fsdl2022'],['datasets','datatrove','nemo_designer','distilabel'],'真实数据处理与生成数据分开比较；都要评估。','Distinguish real-data preparation from synthesis; evaluate both.'),
 ('微调与后训练','Fine-tuning and post-training',['smol_course','hf_llm'],['minimind','trl','llamafactory','unsloth'],'SFT/LoRA→DPO→GRPO；分布式放在后面。','SFT/LoRA, then DPO and GRPO; distributed work comes later.'),
 ('检索与RAG','Retrieval and RAG',['dw-rag','dw-universe'],['faiss','llamaindex','ragflow'],'先完成一个知识库，再加重排与评测。','Build one knowledge base before adding reranking and evaluation.'),
 ('智能体','Agents',['dw-agents','hf_agents','cs329z'],['learn_claudecode','mcp_sdk','langgraph','hermes'],'工具循环→状态/记忆→评测→完整应用。','Tool loop, state and memory, evaluation, then a complete application.'),
 ('推理与训练系统','Inference and training systems',['csapp','dw-zerosglang','pytorch_distributed','dlsys'],['nano_vllm','vllm','sglang','deepspeed'],'推理学调度与缓存；训练学分片与通信。','Study scheduling and caches for serving; sharding and communication for training.'),
 ('视觉与多模态','Vision and multimodality',['cs231n'],['yolo','sam','llava'],'按检测、分割、视觉语言任务选项目。','Choose a detection, segmentation or vision-language task.'),
 ('图学习与概率建模','Graphs and probabilistic modeling',['cs224w','cs228'],['pyg'],'图神经网络与概率图模型分别学习。','Distinguish graph neural networks from probabilistic graphical models.'),
 ('生成模型','Generative models',['hf_diffusion','mit_diffusion','cs236'],['diffusers'],'Notebook动手与连续模型数学相互补充。','Combine notebook practice with continuous-model mathematics.'),
 ('强化学习','Reinforcement learning',['dw-easyrl','cs285','cs224r'],['gymnasium','cleanrl','sb3'],'环境接口→算法→基线比较。','Environment interfaces, algorithms and baseline comparisons.'),
 ('JEPA与世界模型','JEPA and world models',['cs285'],['ijepa','vjepa','vjepa2','dreamerv3'],'表征预测与想象轨迹中的决策分成两条线。','Keep representation prediction and behavior learned in imagined trajectories distinct.'),
 ('VLA与机器人','VLA and robotics',['mit_diffusion','cs224r'],['lerobot','mujoco','libero','openpi','openvla'],'先数据与仿真，再选策略表示。','Start with data and simulation, then choose a policy representation.'),
 ('评测与工程','Evaluation and engineering',['fsdl2022','fsdl'],['lmeval','deepeval','mlflow'],'固定任务、实验记录、部署与监控。','Fixed tasks, experiment tracking, deployment and monitoring.'),
]
LANGUAGE_EN={'中文 / 英文':'Chinese / English','英文':'English','数学':'Mathematics','C / x86-64 汇编':'C / x86-64 assembly','C / x86 汇编':'C / x86 assembly','以论文和体系结构设计为主；项目语言按选题':'Architecture and paper reading; implementation language depends on the project','按项目使用 Python / JavaScript 等':'Python / JavaScript, depending on the project','待定位':'Not identified','不要求编程':'No programming required','不要求编程；代码对照使用Python':'No programming required; Python for the implementation companion','Python / 数学':'Python / mathematics'}
STATUS_EN={'dw-scratch':'The 2026-10-24 catalog check listed chapters 6–8 as forthcoming. Follow the repository for subsequent publication.','dw-universe':'The 2026-10-24 check marked the advanced RAG section as work in progress. Check the current repository contents.','dw-rag':'The 2026-10-24 check listed the second project in chapter 10 as planned. Check the current repository contents.','dw-zerosglang':'The 2026-10-24 check listed some advanced topics as forthcoming. Check the current repository for updates.','cs239a_pending':'Course identity pending.'}

def clean(s):return str(s).replace('|',' / ').replace('\n',' ')
def table(rows,headers):return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(clean(x) for x in row)+' |\n' for row in rows)
def page(r):return {'course':'courses','project':'projects','book':'books'}[r['kind']]+'/'+r['id']+'.md'
def rating(r):return ('待确认' if ZH else 'Pending') if r['level'] is None else str(r['level'])+' / 5'
def title(r):return r['title'] if ZH else r['en']['title']
def value(r,k):return r[k] if ZH else r['en'][k]
def link(id,base='',short=True):
 r=R[id];t=title(r).split(' · ')[0] if short else title(r)
 return '['+clean(t)+']('+base+page(r)+')'
def star(r):return f"{meta[r['repo'].lower()]['stars']:,}"
def write(name,text):
 if not ZH:text=text.replace('：**',':**').replace('：',': ')
 p=DOCS/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def label(s):
 if ZH:return s
 if s in LINK_LABELS:return LINK_LABELS[s]
 if re.match(r'Reading \d+ · ',s):return s.split(' · ')[0]+': Reading and discussion'
 assert not re.search('[\u4e00-\u9fff]',s),'Missing link translation: '+s
 return s
def provider(r):
 mapping={'cs50':'Harvard','python_numpy':'Python / NumPy','pytorch':'PyTorch','zero_to_hero':'Andrej Karpathy','csapp':'CMU','cs140':'Stanford','hf_llm':'Hugging Face','hf_agents':'Hugging Face','dlai_agentic':'DeepLearning.AI','cs2680':'Harvard','fsdl':'Full Stack Deep Learning','cs285':'UC Berkeley','mit_diffusion':'MIT','cs258':'UC Berkeley','cs239a_pending':'待确认' if ZH else 'Not identified'}
 return r.get('provider') or ('Datawhale' if r['origin']=='Datawhale' else mapping.get(r['id'],'Stanford'))

def render_entries():
 for r in R.values():
  text='# '+title(r)+'\n\n'
  website='['+T('官网与资源','Website and resources')+']('+r['url']+')' if r['url'] else T('编号待确认','Identity pending')
  text+='**'+T('入口','Start here')+'：** '+website+'\n\n'
  if r['kind']=='course':
   tech=r['language'] if ZH else LANGUAGE_EN.get(r['language'],r['language'])
   text+=f"- {T('提供方','Provider')}：{provider(r)}\n- {T('难度','Difficulty')}：{rating(r)}\n- {T('适合人群','Who it is for')}：{value(r,'audience')}\n- {T('先修要求','Prerequisites')}：{value(r,'prereq')}\n- {T('编程 / 工具','Programming / tools')}：{tech}\n"
   text+='\n## '+T('讲什么','What you will learn')+'\n\n'+value(r,'summary')+'\n'
  elif r['kind']=='project':
   m=meta[r['repo'].lower()]
   text+=f"- {T('维护者','Maintainer')}：{r['repo'].split('/')[0]}\n- {T('难度','Difficulty')}：{rating(r)}\n- GitHub star：{star(r)} · {D['date']}\n- {T('个人运行条件','Personal setup')}：{value(r,'personal')}\n"
   if m.get('archived'):text+='- '+T('仓库状态：已归档。','Repository status: archived.')+'\n'
   if m.get('fork'):text+='- '+T('仓库类型：fork。','Repository type: fork.')+'\n'
   text+='\n## '+T('是什么，有什么区别','Purpose and differences')+'\n\n'+value(r,'summary')+'\n\n'+value(r,'difference')+'\n'
   text+='\n## '+T('学习建议','Suggested use')+'\n\n'+value(r,'recommendation')+'\n'
  else:
   text+=f"- {T('难度','Difficulty')}：{rating(r)}\n- {T('语言','Language')}：{r['language'] if ZH else LANGUAGE_EN.get(r['language'],r['language'])}\n- {T('获取方式','Access')}：{value(r,'personal')}\n"
   text+='\n'+value(r,'summary')+'\n'
   if not ZH:text+='\n**Who it is for:** '+r['en']['audience']+'\n'
  if r['status']:text+='\n**'+T('资源状态','Publication status')+(' · '+r['status_date'] if r.get('status_date') else '')+'：** '+(r['status'] if ZH else STATUS_EN[r['id']])+'\n'
  extra=[];seen={r['url']}
  for x in r['links']:
   if x['url'] and x['url'] not in seen:extra.append('- ['+label(x['title'])+']('+x['url']+')');seen.add(x['url'])
  if extra:text+='\n## '+T('资料与练习链接','Materials and exercises')+'\n\n'+'\n'.join(extra)+'\n'
  if r['id']=='bbb_nn':text+='\n## '+T('观看顺序','Viewing order')+'\n\n'+T('网络与梯度下降 → 反向传播直觉 → 反向传播公式推导 → ', 'Networks and gradient descent → backpropagation intuition → chain-rule derivation → ')+link('micrograd','../')+'\n'
  if r['kind']=='project' and r['group'] in {'pretrain','data','post','robotics','world','engineering'}:
   ids={'pretrain':['dw-happy','cs336'],'data':['cs336','fsdl2022'],'post':['smol_course','cs336'],'robotics':['mit_diffusion','cs224r'],'world':['cs285'],'engineering':['fsdl2022']}[r['group']]
   if r['id']=='deepspeed':ids=['pytorch_distributed','csapp']
   text+='\n## '+T('相关课程','Related courses')+'\n\n'+' / '.join(link(i,'../') for i in ids)+'\n'
  write(page(r),text)

def render_groups():
 course_nav=[];project_nav=[]
 for kind,groups,guides,nav,folder in [('course',D['course_groups'],COURSE_GUIDES,course_nav,'courses'),('project',D['project_groups'],PROJECT_GUIDES,project_nav,'projects')]:
  overview=[]
  for group,name in groups:
   g=guides[group];heading=name if ZH else g['name_en'];items=[r for r in R.values() if r['kind']==kind and r['group']==group]
   if kind=='project':items.sort(key=lambda r:-meta[r['repo'].lower()]['stars'])
   text='# '+heading+'\n\n'+g['intro_zh' if ZH else 'intro_en']+'\n\n**'+T('怎么选','How to choose')+'：** '+g['guide_zh' if ZH else 'guide_en']+'\n\n'
   rows=[]
   for r in items:
    first=f"[{title(r)}]({r['id']}.md)<br>{rating(r)}"
    if kind=='course':
     if r['url']:first+=' · ['+T('官网','Website')+']('+r['url']+')'
     rows.append([first,value(r,'audience'),value(r,'summary')])
    else:
     first+=f" · ★ {star(r)}<br>[GitHub]({r['url']})"
     rows.append([first,value(r,'difference'),value(r,'recommendation')])
   text+=table(rows,[T('课程','Course'),T('适合谁','Who it is for'),T('讲什么','What it covers')] if kind=='course' else [T('项目','Project'),T('特点与区别','Purpose and differences'),T('学习建议','Suggested use')])
   if group=='world' and kind=='project':text+='\n'+T('历史背景：','Historical background: ')+'[World Models](https://worldmodels.github.io/).\n'
   if group=='robotics' and kind=='project':text+='\n'+T('研究参考（不作为开源复现项目）：','Research reference (not listed as an open-source reproduction): ')+'[Gemini Robotics](https://deepmind.google/models/gemini-robotics/).\n'
   write(f'{folder}/group-{group}.md',text);nav.append({heading:[{T('概览','Overview'):f'{folder}/group-{group}.md'},*[{title(r):page(r)} for r in items]]})
   overview.append([f'[{heading}](group-{group}.md)',g['intro_zh' if ZH else 'intro_en']])
  intro=T('先选一个方向，再按概览中的建议选择主课。难度综合先修知识与实践工作量。','Choose a direction, then use its overview to select a main course. Difficulty reflects prerequisites and workload.') if kind=='course' else T('按你要解决的问题选项目。每个概览直接比较项目职责、特点与适用阶段，并提供源码链接。','Choose by the problem you want to solve. Each overview compares purpose, design and learning stage, with direct source links.')
  write(folder+'/index.md','# '+(T('课程','Courses') if kind=='course' else T('开源项目','Open-source Projects'))+'\n\n'+intro+'\n\n'+table(overview,[T('方向','Track'),T('为什么学','Why it matters')]))
 return course_nav,project_nav

def render_main():
 write('index.md',T('''# AI 0 to 1

**AI 0 to 1**，从理解一个模型，到做出自己的 AI 项目。

先建立编程、数学和深度学习基础，再进入模型训练、应用或机器人方向。这里整理课程、书籍和开源项目，说明适合谁、讲什么，以及相近资料如何选择。

- [学习路线](framework.md)：公共基础与各方向的课程、项目衔接。
- [课程推荐](courses/index.md)：大学公开课、官方教程与Datawhale。
- [开源项目](projects/index.md)：特点、区别与学习建议。
- [知识 Bingo](knowledge/index.md)：按主题查术语、看例子和交互演示。
- [书目推荐](books/index.md)：按当前阶段选择参考。
- [AI 商业认知](business/index.md)：技术趋势、产品落地与行业研究。
''','''# AI 0 to 1

**AI 0 to 1** — from understanding a model to building your own AI project.

Build foundations in programming, mathematics and deep learning, then choose model training, applications or robotics. This guide compares courses, books and open-source projects by audience, content and purpose.

- [Learning roadmap](framework.md): foundations and specialization paths.
- [Courses](courses/index.md): university courses, official tutorials and Datawhale.
- [Projects](projects/index.md): purpose, differences and suggested use.
- [Knowledge Bingo](knowledge/index.md): terms, examples and interactive explanations.
- [Books](books/index.md): references for your current stage.
- [AI & Business](business/index.md): technology shifts, products and industry research.
'''))
 text='# '+T('AI 学习路线','AI Learning Roadmap')+'\n\n'
 text+=T('基础顺序：**编程与数学 → 机器学习与深度学习 → 模型训练或应用方向**。视觉、强化学习、系统和机器人各有前置，按方向进入。','Foundation: **programming and mathematics → machine learning and deep learning → model training or applications**. Vision, RL, systems and robotics have their own prerequisites.')+'\n\n'
 text+='## '+T('一条贯通的代码练习线','One connected implementation path')+'\n\n'
 text+=' → '.join([link('pytorch'),link('micrograd'),link('makemore'),T('自己实现tiny GPT（对照','Build your own tiny GPT (compare with ')+link('nanogpt')+T('）',')'),'[CS336 Assignment 1](https://github.com/stanford-cs336/assignment1-basics)'])+'\n\n'
 text+=T('练习依次做线性回归、FashionMNIST分类、自动微分、字符模型、小型Transformer与Tokenizer/训练集成。3Blue1Brown补数学与反传直觉，CS229补统计学习。此后按下表选择方向。','Practice linear regression, FashionMNIST classification, autodiff, character models, a small Transformer, and tokenization/training integration. Use 3Blue1Brown for intuition and CS229 for statistical foundations, then choose a track below.')+'\n\n'
 text+='## '+T('课程与项目地图','Course and project map')+'\n\n'+table([[name if ZH else en,' / '.join(link(i) for i in cs),' / '.join(link(i) for i in ps) or '—',zh if ZH else note] for name,en,cs,ps,zh,note in FRAMEWORK],[T('阶段 / 方向','Stage / track'),T('课程','Courses'),T('项目','Projects'),T('衔接','Sequence')])
 text+='\n## '+T('框架来源','Framework sources')+'\n\n'
 for x in json.loads((ROOT/'data/framework_sources.json').read_text(encoding='utf-8')):text+='- ['+x['title']+']('+x['url']+')\n'
 text+='\n'+T('公开框架提供整体顺序，具体课程与项目搭配由本指南编排。','Public frameworks inform the sequence; the course and project combinations are this guide\'s editorial choices.')+'\n'
 write('framework.md',text)
 books=[r for r in R.values() if r['kind']=='book']
 write('books/index.md','# '+T('书目推荐','Books')+'\n\n'+T('书籍用于补推导、查概念和对照代码。入门选鱼书或D2L；LLM选Raschka；数学选MML；理论进阶再读ESL、PML和Deep Learning。Chollet的书提供Keras视角，与PyTorch课程互补。','Books support derivations, reference and code comparisons. Begin with Deep Learning from Scratch or D2L; use Raschka for LLMs, MML for mathematics, and ESL/PML/Deep Learning for more advanced theory. Chollet adds a Keras-oriented perspective.')+'\n\n'+table([[f"[{title(r)}]({r['id']}.md)",rating(r),value(r,'summary')] for r in books],[T('书籍','Book'),T('难度','Difficulty'),T('介绍','Introduction')]))
 return books

for language in ['zh','en']:
 ZH=language=='zh';DOCS=ROOT/('docs' if ZH else 'docs_en');DOCS.mkdir(exist_ok=True)
 T=lambda zh,en:zh if ZH else en
 render_entries();course_nav,project_nav=render_groups();books=render_main();write_tools(write,T);write_coverage(write,T,R,D,changes,link)
 write_knowledge(ROOT,language,KNOWLEDGE)
 write_business(write,T)
 nav=[
  {T('前言','Preface'):'index.md'},
  {T('AI学习路线','AI Learning Roadmap'):'framework.md'},
  {T('必学工具','Essential Tools'):[{T('概览','Overview'):'tools/index.md'},{T('如何使用','How to Use This Guide'):'tools/reading.md'},{T('环境与运行','Environment and Execution'):'tools/environment.md'},{T('信息检索','Finding Information'):'tools/search.md'}]},
  {T('课程推荐','Courses'):[{T('课程概览','Course Overview'):'courses/index.md'},*course_nav]},
  {T('开源项目','Open-source Projects'):[{T('项目概览','Project Overview'):'projects/index.md'},*project_nav]},
  {T('书目推荐','Books'):[{T('概览','Overview'):'books/index.md'},*[{title(r):page(r)} for r in books]]},
  {T('AI 商业认知','AI & Business'):'business/index.md'},
  {T('收录与来源','Sources and Selection'):'coverage.md'}
 ]
 nav.insert(2,{T('知识Bingo','Knowledge Bingo'):[{T('知识网格','Knowledge Board'):'knowledge/index.md'},{T('词典与交互参考','References'):'knowledge/sources.md'}]})
 config=dict(site_name='AI 0 to 1',site_description=T('从基础到AI项目的课程与实践指南','A practical guide from foundations to AI projects'),docs_dir='docs' if ZH else 'docs_en',site_dir='site' if ZH else 'site/en',use_directory_urls=False,theme=dict(name='material',custom_dir='overrides',language=language,font=False,palette=[dict(scheme='default',primary='light blue',accent='deep purple',toggle=dict(icon='material/weather-sunny',name=T('切换到深色','Switch to dark mode'))),dict(scheme='slate',primary='cyan',accent='deep purple',toggle=dict(icon='material/weather-night',name=T('切换到浅色','Switch to light mode')))],features=['navigation.footer']),markdown_extensions=['attr_list','md_in_html','footnotes','tables'],plugins=[{'search':{'lang':['zh','en'] if ZH else ['en']}},'offline'],extra=dict(polyfills=['javascripts/iframe-worker-1.0.4.js'],alternate=[dict(name='中文',lang='zh',link='index.html'),dict(name='English',lang='en',link='en/index.html')],language_code=language),extra_css=['stylesheets/extra.css'],nav=nav,copyright=T('AI 0 to 1 · 资料归原作者所有','AI 0 to 1 · Resources belong to their respective authors'))
 config['site_url']=PUBLIC_URL+('' if ZH else 'en/')
 config['site_author']='LeriusLei'
 config['site_description']=T('AI 0 to 1：从编程、数学、机器学习与深度学习，到大模型预训练、后训练、RAG、Agent、世界模型和VLA。双语课程、项目、书籍与知识Bingo。','AI 0 to 1: a bilingual AI learning roadmap covering programming, mathematics, deep learning, LLM training, RAG, agents, world models and robotics, with courses, projects and a knowledge glossary.')
 config['extra']['social']=[dict(icon='fontawesome/brands/github',link='https://github.com/LeriusLei/AI-0-to-1',name='AI 0 to 1 on GitHub — Star')]
 config['extra']['public_url']=PUBLIC_URL
 # Language links in the custom head and header preserve the current article.
 config['extra'].pop('alternate',None)
 (ROOT/('mkdocs.yml' if ZH else 'mkdocs.en.yml')).write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False,width=120),encoding='utf-8')
 write('stylesheets/extra.css',CSS)
 dest=DOCS/'javascripts';dest.mkdir(exist_ok=True)
 shutil.copy2(ROOT/'assets/javascripts/iframe-worker-1.0.4.js',dest/'iframe-worker-1.0.4.js')
 shutil.copytree(ROOT/'assets/branding',DOCS/'assets/branding',dirs_exist_ok=True)
 write('robots.txt','User-agent: *\nAllow: /\n\nSitemap: '+PUBLIC_URL+'sitemap.xml\n')

report=dict(name=D['name'],entries=len(R),courses=sum(r['kind']=='course' for r in R.values()),projects=sum(r['kind']=='project' for r in R.values()),books=len(books),languages=['zh','en'],removed=len(changes),legacy_retained=sum(bool(r.get('legacy_id')) for r in R.values()))
(ROOT/'data/content_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
