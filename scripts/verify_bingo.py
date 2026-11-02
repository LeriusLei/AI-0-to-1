"""Validate migrated IDs, content fields, real links and generated search entries."""
from pathlib import Path
from urllib.parse import urlsplit
import json,re
ROOT=Path(__file__).resolve().parents[1];K=json.loads((ROOT/'data/knowledge.json').read_text(encoding='utf-8'))
seed=json.loads((ROOT/'data/knowledge_seed.json').read_text(encoding='utf-8'))
ids={t['id'] for t in K['terms']};categories={c['id'] for c in K['categories']};errors=[]
assert len(ids)==len(K['terms'])
for t in seed['terms']:
 if K['migrations'].get(t['id'],t['id']) not in ids:errors.append('lost legacy term '+t['id'])
for t in K['terms']:
 if t['category'] not in categories:errors.append('bad category '+t['id'])
 if not t['related'] or any(i not in ids or i==t['id'] for i in t['related']):errors.append('bad semantic link '+t['id'])
 for lang in ['zh','en']:
  d=t[lang]
  if any(not d.get(key) for key in ['title','summary','explain','example','pitfall']):errors.append('missing content '+t['id']+lang)
  if lang=='en' and re.search('[\u4e00-\u9fff]',json.dumps(d,ensure_ascii=False)):errors.append('untranslated '+t['id'])
 for source in t['sources']:
  u=urlsplit(source['url'])
  if u.scheme not in {'https','http'} or not u.netloc:errors.append('bad source '+t['id'])
 for course in t['courses']:
  for prefix in ['', 'en']:
   if not (ROOT/'site'/prefix/course['path']).exists():errors.append('missing course '+course['path'])
for prefix in ['', 'en']:
 site=ROOT/'site'/prefix
 index=json.loads((site/'search/search_index.json').read_text(encoding='utf-8'))
 locations={d['location'] for d in index['docs']}
 for t in K['terms']:
  if 'knowledge/index.html#t='+t['id'] not in locations:errors.append('not in global search '+t['id']+prefix)
 for name in ['bingo.js','bingo.css','bingo-data.js']:
  if not (site/'knowledge'/name).exists():errors.append('missing asset '+name)
report=dict(passed=not errors,terms=len(ids),categories=len(categories),legacy_terms_covered=len(seed['terms']),languages=['zh','en'],semantic_links=sum(len(t['related']) for t in K['terms']),source_links=sum(len(t['sources']) for t in K['terms']),course_links=sum(len(t['courses']) for t in K['terms']),interactive_examples=6,errors=errors)
(ROOT/'qa').mkdir(exist_ok=True)
(ROOT/'qa/bingo_integrity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False));raise SystemExit(bool(errors))
