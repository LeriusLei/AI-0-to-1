"""Check publishable Git files and the generated website before release."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,re,subprocess,xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
URL='https://leriuslei.github.io/AI-0-to-1/'
REPO='https://github.com/LeriusLei/AI-0-to-1'
errors=[]
result=subprocess.run(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT,capture_output=True,check=True)
files=sorted(set(x.decode('utf-8') for x in result.stdout.split(b'\0') if x))
patterns={
 'absolute local path':re.compile(r'(?i)\b[A-Z]:[\\/]'),
 'private workstation reference':re.compile(r'(?i)Users[/\\][A-Za-z0-9_~.-]+|codex-clipboard|AppData[/\\](?:Local|Roaming)'),
 'private plan reference':re.compile(r'两份本地学习计划|supplied local study plans|planTopics'),
 'GitHub credential':re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b|github_pat_[A-Za-z0-9_]{30,}'),
 'API credential':re.compile(r'\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}\b'),
 'private key':re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),
}
for name in files:
 path=Path(name)
 if any(part in {'.tools','.venv','research','qa','__pycache__'} for part in path.parts) or path.suffix in {'.zip','.log','.pyc','.pdf','.ipynb'} or path.name.startswith('.env'):
  errors.append({'file':name,'rule':'private or generated file in Git'})
 if path.name in {'task_plan.md','findings.md','progress.md'}:errors.append({'file':name,'rule':'private working notes'})
 content=(ROOT/path).read_bytes()
 if b'\0' in content:
  if name!='assets/branding/social-card.png':errors.append({'file':name,'rule':'unexpected binary'})
  continue
 if name=='scripts/verify_public.py':continue
 text=content.decode('utf-8')
 for rule,pattern in patterns.items():
  if pattern.search(text):errors.append({'file':name,'rule':rule})
 for address in re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',text):
  # Preserve upstream attribution exactly; these public license contacts
  # are not the maintainer's private contact information.
  if path.parts[0]=='third-party' or path.name=='LICENSE':continue
  if not address.endswith(('gnu.org','fsf.org','users.noreply.github.com')) and address!='noreply@github.com':errors.append({'file':name,'rule':'review email address'})

class Head(HTMLParser):
 def __init__(self):super().__init__();self.canonical=None;self.alternates={};self.github=0;self.description=False;self.structured=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
  if tag=='link' and a.get('hreflang'):self.alternates[a['hreflang']]=a.get('href')
  if tag=='a' and a.get('href')==REPO:self.github+=1
  if tag=='meta' and a.get('name')=='description' and a.get('content'):self.description=True
  if tag=='script' and a.get('type')=='application/ld+json':self.structured=True

pages=list((ROOT/'site').rglob('*.html'))
for path in pages:
 text=path.read_text(encoding='utf-8')
 for rule,pattern in patterns.items():
  if pattern.search(text):errors.append({'file':str(path.relative_to(ROOT)),'rule':rule})
 if path.name=='404.html':continue
 head=Head();head.feed(text)
 if not head.canonical or not head.canonical.startswith(URL):errors.append({'file':str(path.relative_to(ROOT)),'rule':'missing public canonical'})
 if not head.description or not head.structured:errors.append({'file':str(path.relative_to(ROOT)),'rule':'missing discovery metadata'})
 if head.github<2:errors.append({'file':str(path.relative_to(ROOT)),'rule':'missing header/footer GitHub links'})
for name in ['sitemap.xml','sitemap.xml.gz','robots.txt','assets/branding/social-card.png','.nojekyll']:
 if not (ROOT/'site'/name).exists():errors.append({'file':name,'rule':'missing publication asset'})
sitemap=ET.parse(ROOT/'site/sitemap.xml')
locations=[x.text for x in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
for entry in sitemap.getroot():
 alternates=entry.findall('{http://www.w3.org/1999/xhtml}link')
 if {x.get('hreflang') for x in alternates}!={'zh-Hans','en','x-default'}:errors.append({'file':'sitemap.xml','rule':'missing language alternatives'})
if len(locations)!=len(set(locations)) or not any(x.startswith(URL+'en/') for x in locations):errors.append({'file':'sitemap.xml','rule':'duplicate URLs or missing English edition'})
for location in locations:
 relative=location.removeprefix(URL)
 target=ROOT/'site'/relative
 if not relative or relative.endswith('/'):target=target/'index.html'
 if not location.startswith(URL) or not target.exists():errors.append({'file':'sitemap.xml','rule':'invalid sitemap URL'})
report=dict(passed=not errors,source_files=len(files),html_pages=len(pages),sitemap_urls=len(locations),errors=errors)
(ROOT/'qa').mkdir(exist_ok=True)
(ROOT/'qa/public_integrity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False));raise SystemExit(bool(errors))
