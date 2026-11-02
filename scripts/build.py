"""Build both languages and merge their public sitemaps."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
from mkdocs.config import load_config
from mkdocs.commands.build import build
from build_bingo import index_terms
import json
import gzip
import xml.etree.ElementTree as ET
knowledge=json.loads((ROOT/'data/knowledge.json').read_text(encoding='utf-8'))
for name,output in [('mkdocs.yml',ROOT/'site'),('mkdocs.en.yml',ROOT/'site/en')]:
 config=load_config(config_file=str(ROOT/name),strict=True)
 assert Path(config['site_dir']).resolve()==output.resolve()
 assert output.resolve().is_relative_to(ROOT.resolve())
 build(config)
 index_terms(output,knowledge,'en' if name=='mkdocs.en.yml' else 'zh')
namespace='http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('',namespace)
ET.register_namespace('xhtml','http://www.w3.org/1999/xhtml')
chinese=ROOT/'site/sitemap.xml';english=ROOT/'site/en/sitemap.xml'
tree=ET.parse(chinese)
for entry in ET.parse(english).getroot():tree.getroot().append(entry)
public='https://leriuslei.github.io/AI-0-to-1/'
for entry in tree.getroot():
 location=entry.find('{'+namespace+'}loc').text
 relative=location.removeprefix(public).removeprefix('en/')
 for language,href in [('zh-Hans',public+relative),('en',public+'en/'+relative),('x-default',public+relative)]:
  ET.SubElement(entry,'{http://www.w3.org/1999/xhtml}link',{'rel':'alternate','hreflang':language,'href':href})
xml=ET.tostring(tree.getroot(),encoding='utf-8',xml_declaration=True)
chinese.write_bytes(xml)
(ROOT/'site/sitemap.xml.gz').write_bytes(gzip.compress(xml))
(ROOT/'site/.nojekyll').write_text('',encoding='utf-8')
