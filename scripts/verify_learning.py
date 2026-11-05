"""Check course-video coverage, resource boundaries and goal-based navigation."""
from pathlib import Path
from urllib.parse import urlsplit
import json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from navigation_content import PROJECT_GOALS,STARTS,PROJECT_STARTS
D=json.loads((ROOT/'data/catalog.json').read_text(encoding='utf-8'))
B=json.loads((ROOT/'data/bilibili_resources.json').read_text(encoding='utf-8'))
R={r['id']:r for r in D['entries']};errors=[]
courses={r['id'] for r in R.values() if r['kind']=='course'}
projects={r['id'] for r in R.values() if r['kind']=='project'}
if set(B['courses'])!=courses:errors.append('Video review must cover every active course')
if set(PROJECT_GOALS)!=projects:errors.append('Every project needs its own goal and outcome')
if set(STARTS)!={g[0] for g in D['course_groups']}:errors.append('Missing course goal choices')
if set(PROJECT_STARTS)!={g[0] for g in D['project_groups']}:errors.append('Missing project goal choices')
if {r['id'] for r in R.values() if r['kind']=='project' and r['group']=='synthesis'}!={'nemo_designer','distilabel'}:errors.append('Synthetic data boundary is wrong')
if any(R[i]['group']!='data' for i in ['datasets','datatrove']):errors.append('Existing-data tools should remain separate')
if R['deepspeed']['group']=='engineering':errors.append('Training infrastructure is not evaluation tooling')
if any(r['kind']=='course' and r['group']=='engineering' for r in R.values()):errors.append('Misleading MLOps course category remains')
linked=0
for id in courses:
 item=B['courses'][id]
 for video in item['items']:
  linked+=1;u=urlsplit(video['url'])
  if u.netloc!='www.bilibili.com' or not u.path.startswith('/video/BV') or u.query:errors.append('Use direct, tracking-free video URLs: '+id)
  if not all(video.get(k) for k in ['label_zh','label_en','note_zh','note_en']):errors.append('Missing edition/scope notes: '+id)
 for prefix in ['','en/']:
  p=ROOT/'site'/prefix/'courses'/(id+'.html');text=p.read_text(encoding='utf-8')
  for video in item['items']:
   if video['url'] not in text:errors.append('Missing per-course viewing link: '+prefix+id)
for prefix in ['','en/']:
 for retired in ['fsdl2022','cs239a_pending','group-engineering']:
  if (ROOT/'site'/prefix/'courses'/(retired+'.html')).exists():errors.append('Retired course page remains: '+retired)
 for kind in ['courses','projects']:
  text=(ROOT/'site'/prefix/kind/'index.html').read_text(encoding='utf-8')
  if 'resource-table goal-index' not in text:errors.append('Goal overview missing: '+prefix+kind)
report=dict(passed=not errors,reviewed_courses=B['reviewed_course_count'],active_courses=len(courses),courses_with_videos=sum(bool(v['items']) for v in B['courses'].values()),direct_video_links=linked,projects_with_goals=len(PROJECT_GOALS),errors=errors)
(ROOT/'qa').mkdir(exist_ok=True)
(ROOT/'qa/learning_integrity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False));raise SystemExit(bool(errors))
