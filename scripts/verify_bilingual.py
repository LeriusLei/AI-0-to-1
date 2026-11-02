"""Verify local links, language pairs, revised coverage and bilingual content."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
from functools import cache
import json,re
ROOT=Path(__file__).resolve().parents[1];SITE=ROOT/'site'
# The build is complete before validation. Cache repeated navigation targets
# rather than resolving the same Windows paths tens of thousands of times.
@cache
def resolve_path(path):return path.resolve()
@cache
def target_exists(path):return path.exists()
SITE_ROOT=resolve_path(SITE)
D=json.loads((ROOT/'data/catalog.json').read_text(encoding='utf-8'))
M=json.loads((ROOT/'data/github_metadata.json').read_text(encoding='utf-8'))
changes=json.loads((ROOT/'data/selection_changes.json').read_text(encoding='utf-8'))
R={r['id']:r for r in D['entries']}
class Document(HTMLParser):
 def __init__(self):super().__init__();self.urls=[];self.article=False;self.heading=False;self.text=[];self.h1=[];self.switch=None;self.lang=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='article':self.article=True
  if tag=='h1' and self.article:self.heading=True
  if 'data-ai-language-switch' in a:self.switch=a['href']
  if tag in {'a','link'} and a.get('href'):self.urls.append(a['href'])
  if tag in {'script','img'} and a.get('src'):self.urls.append(a['src'])
 def handle_endtag(self,tag):
  if tag=='h1':self.heading=False
  if tag=='article':self.article=False
 def handle_data(self,data):
  if self.article:self.text.append(data)
  if self.heading:self.h1.append(data)
errors=[];references=0;external=set();documents={}
for p in SITE.rglob('*.html'):
 parser=Document();source=p.read_text(encoding='utf-8');parser.feed(source);documents[p.resolve()]=parser
 if '按GitHub star排序' in source or '低星项目保留了用户指定条目' in source:errors.append('outdated description: '+str(p))
 for url in parser.urls:
  if url.startswith(('http://','https://')):external.add(url);continue
  if url.startswith(('data:','javascript:','mailto:','tel:','#')):continue
  part=unquote(urlsplit(url).path)
  if not part:continue
  if part.startswith('/'):
   if not part.startswith('/AI-0-to-1/'):errors.append('unexpected host-root link: '+url)
   target=SITE/part.removeprefix('/AI-0-to-1/')
  else:target=p.parent/part
  if part.endswith('/'):target=target/'index.html'
  target=resolve_path(target);references+=1
  if not target.is_relative_to(SITE_ROOT):errors.append('outside site: '+url)
  elif not target_exists(target):errors.append('missing: '+str(p.relative_to(SITE))+': '+url)
  if target.suffix=='.md':errors.append('Markdown reading link: '+url)
 paired=(SITE/p.relative_to(SITE/'en')) if p.is_relative_to(SITE/'en') else SITE/'en'/p.relative_to(SITE)
 if p.name!='404.html':
  actual=(p.parent/parser.switch).resolve() if parser.switch else None
  if actual!=paired.resolve():errors.append('wrong language switch: '+str(p.relative_to(SITE)))
  if parser.lang!=('en' if p.is_relative_to(SITE/'en') else 'zh'):errors.append('wrong document language: '+str(p))
 if p.is_relative_to(SITE/'en') and re.search('[\u4e00-\u9fff]',''.join(parser.text).replace('中文','')):errors.append('untranslated English article: '+str(p.relative_to(SITE)))
for r in R.values():
 folder={'book':'books','course':'courses','project':'projects'}[r['kind']]
 for lang in ['zh','en']:
  p=(SITE/('en' if lang=='en' else '')/folder/(r['id']+'.html')).resolve();doc=documents.get(p)
  if not doc:errors.append('missing entry: '+str(p));continue
  if ''.join(doc.h1)!=(r['en']['title'] if lang=='en' else r['title']):errors.append('wrong title: '+r['id']+lang)
  text=''.join(doc.text)
  if r['kind']=='course' and ('Who it is for' if lang=='en' else '适合人群') not in text:errors.append('missing audience '+r['id'])
  if r['kind']=='project' and any(x not in text for x in (['Purpose and differences','Suggested use'] if lang=='en' else ['是什么，有什么区别','学习建议'])):errors.append('missing project advice '+r['id'])
for x in changes:
 if x['id'] in R:errors.append('removed item still active: '+x['id'])
 for prefix in ['', 'en']:
  if (SITE/prefix/'projects'/(x['id']+'.html')).exists():errors.append('stale removed page: '+x['id'])
for lang in ['','en']:
 if not (SITE/lang/'search/search_index.js').exists():errors.append('missing offline search '+lang)
for r in R.values():
 if r.get('repo') and not any(r['repo'].lower() in {m['requested'].lower(),m.get('repo','').lower()} and isinstance(m.get('stars'),int) for m in M['repositories']):errors.append('missing GitHub metadata '+r['id'])
report=dict(passed=not errors,name=D['name'],entries=len(R),languages=['zh','en'],html_pages=len(documents),local_link_entries=references,external_urls=len(external),active_repositories=len({r['repo'].lower() for r in R.values() if r.get('repo')}),legacy_retained=sum(bool(r.get('legacy_id')) for r in R.values()),removed=len(changes),errors=errors)
(ROOT/'qa').mkdir(exist_ok=True)
(ROOT/'qa/site_integrity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False));raise SystemExit(bool(errors))
