/* Offline knowledge board. No network calls or external dependencies. */
(() => {
  'use strict';
  const root = document.getElementById('ai-bingo-app');
  if (!root || !window.AI_BINGO) return;
  const D = window.AI_BINGO, lang = root.dataset.language, zh = lang === 'zh';
  const text = (a, b) => zh ? a : b;
  const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const terms = new Map(D.terms.map(t => [t.id,t])), cats = new Map(D.categories.map(c => [c.id,c]));
  const key = 'ai01-bingo-progress-v1', legacyKey = 'learning-workbench-progress-v1';
  const compact = matchMedia('(max-width: 1050px)');
  const normalize = s => String(s).normalize('NFKC').toLowerCase().trim();
  const canonical = id => terms.has(id) ? id : (typeof D.migrations[id]==='string'&&terms.has(D.migrations[id])?D.migrations[id]:undefined);
  const state = {category:'math',q:'',status:'all',term:null};
  let marked = {}, storageOK = true, explicit = false, legacyMigrated = false;
  function importTerms(value) {
    if (!value || typeof value !== 'object' || Array.isArray(value)) throw Error('format');
    if (value.version !== 1 || !value.terms || typeof value.terms !== 'object' || Array.isArray(value.terms)) throw Error('format');
    let added = 0;
    for (const [id, done] of Object.entries(value.terms)) {
      const target = canonical(id);
      if (target && done === true && !marked[target]) { marked[target] = true; added++; }
    }
    return added;
  }
  try {
    const saved = JSON.parse(localStorage.getItem(key) || 'null');
    if (saved) { importTerms(saved); legacyMigrated=!!saved.legacyMigrated; }
    if(!legacyMigrated){const legacy = JSON.parse(localStorage.getItem(legacyKey) || 'null');if(legacy?.version === 1 && legacy.terms)importTerms(legacy);legacyMigrated=true;}
  } catch { storageOK = false; }
  function save() {
    try { localStorage.setItem(key,JSON.stringify({version:1,terms:marked,legacyMigrated,updatedAt:new Date().toISOString()})); storageOK=true; }
    catch { storageOK=false; }
    progress();
  }
  const total = () => Object.keys(marked).filter(id => marked[id] && terms.has(id)).length;
  document.body.classList.add('bingo-page');
  root.innerHTML = `
    <div class="bingo-intro"><p>${text('按理解顺序排好的知识网格。选词阅读，点圆圈保存自己的进度。','A knowledge board in learning order. Select a term to read; use its circle to save your progress.')}</p><div class="bingo-progress"><span class="progress-ring" aria-hidden="true"></span><span id="bingo-progress-text"></span></div></div>
    <div class="bingo-controls"><label class="bingo-search"><span>${text('查术语','Find a term')}</span><input id="bingo-search" type="search" placeholder="${text('张量、Softmax、GPRO / GRPO、OPD…','Tensor, softmax, GRPO, OPD…')}" autocomplete="off"></label><label class="bingo-filter"><span>${text('显示','Show')}</span><select id="bingo-status"><option value="all">${text('全部','All terms')}</option><option value="todo">${text('未标记','Unmarked')}</option><option value="done">${text('已标记','Marked')}</option></select></label></div>
    <nav id="bingo-categories" class="bingo-categories" aria-label="${text('知识分类','Knowledge categories')}"></nav>
    <div class="bingo-layout"><section class="bingo-board" aria-labelledby="bingo-category-title"><div class="bingo-board-head"><h2 id="bingo-category-title"></h2><span id="bingo-results" role="status" aria-live="polite"></span></div><p id="bingo-category-description" class="bingo-category-description"></p><ul id="bingo-grid" class="bingo-grid"></ul><div class="bingo-save"><span id="bingo-save-status"></span><button type="button" id="bingo-export">${text('导出进度','Export progress')}</button><button type="button" id="bingo-import">${text('导入','Import')}</button><input type="file" id="bingo-file" accept=".json,application/json" hidden><a href="sources.html">${text('词典与交互参考','References')}</a></div><p id="bingo-message" class="bingo-message" role="status" aria-live="polite"></p></section><aside id="bingo-reader" class="bingo-reader" aria-label="${text('术语讲解','Term explanation')}"></aside></div>
    <dialog id="bingo-dialog" aria-label="${text('术语讲解','Term explanation')}"></dialog>`;
  const grid=root.querySelector('#bingo-grid'), reader=root.querySelector('#bingo-reader'), dialog=root.querySelector('#bingo-dialog');
  const boardLayout=root.querySelector('.bingo-layout'), search=root.querySelector('#bingo-search'), status=root.querySelector('#bingo-status');
  function progress() {
    root.querySelector('#bingo-progress-text').textContent=text(`已标记 ${total()} / ${D.terms.length}`,`${total()} / ${D.terms.length} marked`);
    root.querySelector('.progress-ring').style.setProperty('--progress',`${total()/D.terms.length*360}deg`);
    root.querySelector('#bingo-save-status').textContent=storageOK?text('进度自动保存在此浏览器','Progress saved in this browser'):text('当前无法自动保存，请导出备份','Storage unavailable; export a backup');
  }
  function message(s) { root.querySelector('#bingo-message').textContent=s; }
  function readURL() {
    let hash=location.hash.slice(1);
    if(hash.startsWith('knowledge/')) hash=hash.split('?')[1]||'';
    const p=new URLSearchParams(hash), id=canonical(p.get('t')||p.get('term')||'');
    state.category=cats.has(p.get('c'))?p.get('c'):p.get('c')==='all'?'all':id?terms.get(id).category:'math';
    state.q=p.get('q')||'';state.status=['done','todo'].includes(p.get('s'))?p.get('s'):'all';
    state.term=id||(!compact.matches?'tensor':null);explicit=!!id;
  }
  function updateURL(push=false) {
    const p=new URLSearchParams();p.set('c',state.category);
    if(state.q)p.set('q',state.q);if(state.status!=='all')p.set('s',state.status);if(state.term&&explicit)p.set('t',state.term);
    history[push?'pushState':'replaceState'](null,'','#'+p);
    languageLink();
  }
  function languageLink() { const a=document.querySelector('[data-ai-language-switch]');if(a)a.hash=location.hash; }
  function categoryBar() {
    const list=[{id:'all',zh:'全部',en:'All'},...D.categories];
    const active=state.q?'all':state.category;
    root.querySelector('#bingo-categories').innerHTML=list.map(c=>`<button type="button" data-category="${c.id}" aria-pressed="${active===c.id}" class="${active===c.id?'selected':''}">${esc(c[lang])}</button>`).join('');
  }
  function filtered() {
    const q=normalize(state.q), parts=q.split(/\s+/).filter(Boolean);
    return D.terms.map((t,index)=>{
      const names=[t.zh.title,t.en.title,t.id,...t.aliases].map(normalize);
      const content=names.concat(t.zh.summary,t.en.summary,t.zh.explain,t.en.explain,t.zh.example,t.en.example,t.zh.pitfall,t.en.pitfall).join(' ').toLowerCase();
      const match=!q||parts.every(p=>content.includes(p));
      const score=names.includes(q)?100:names.some(n=>n.startsWith(q))?20:0;
      return {t,index,match,score};
    }).filter(({t,match})=>match&&(state.q||state.category==='all'||t.category===state.category)&&(state.status==='all'||(state.status==='done'?marked[t.id]:!marked[t.id])))
      .sort((a,b)=>state.q?b.score-a.score||a.index-b.index:a.index-b.index).map(x=>x.t);
  }
  function renderBoard() {
    categoryBar();const list=filtered(), category=cats.get(state.category);
    root.querySelector('#bingo-category-title').textContent=state.q?text('搜索结果','Search results'):category?category[lang]:text('全部术语','All terms');
    root.querySelector('#bingo-category-description').textContent=state.q?text('搜索中文、英文与别名；讲解始终显示规范名称。','Search names and aliases; explanations use the canonical term.'):category?category.description[lang]:text('按主题与理解顺序排列。','Organized by topic and learning order.');
    root.querySelector('#bingo-results').textContent=text(`${list.length} 项`,`${list.length} terms`);
    grid.innerHTML=list.length?list.map(t=>`<li class="bingo-cell ${marked[t.id]?'is-marked':''} ${state.term===t.id?'is-selected':''}"><a href="#c=${t.category}&t=${t.id}" data-term="${t.id}" aria-controls="bingo-reader"><span class="bingo-cell-title">${esc(t[lang].title)}</span>${zh?`<span class="bingo-cell-en" lang="en">${esc(t.en.title)}</span>`:`<span class="bingo-cell-en">${esc(cats.get(t.category).en)}</span>`}</a><button type="button" class="bingo-mark" data-mark="${t.id}" aria-pressed="${!!marked[t.id]}" aria-label="${esc(text('标记 / 取消：','Mark / unmark: ')+t[lang].title)}"><span aria-hidden="true">${marked[t.id]?'✓':''}</span></button></li>`).join(''):`<li class="bingo-empty">${text('没有匹配的词条。可以换个关键词，或切换显示状态。','No matching terms. Try another keyword or status filter.')}</li>`;
    progress();
  }
  const formulas={
    tensor:'(B, S, H) → B × S × H elements',softmax:'pᵢ = exp((zᵢ − max z) / T) / Σⱼ exp((zⱼ − max z) / T)',
    crossentropy:'L = −log p(target)',gradient:'w′ = w − η ∂L/∂w',chainrule:'∂L/∂w = (∂L/∂z)(∂z/∂w)',
    attention:'Attention(Q,K,V) = softmax(QKᵀ/√dₖ + mask)V',grpo:'Âᵢ = (rᵢ − mean(r)) / (std(r) + ε)',
    lora:'W′ = W + (α/r)BA; trainable update: r(dᵢₙ + dₒᵤₜ)',kvcache:'bytes ≈ 2 × layers × batch × tokens × KV heads × head dimension × bytes/element',
    bellman:'Vπ(s) = E[r + γVπ(s′) | s, π]',advantage:'Aπ(s,a) = Qπ(s,a) − Vπ(s)',
    metrics:'Precision = TP / (TP + FP)',recall:'Recall = TP / (TP + FN)',f1:'F1 = 2PR / (P + R)',
  };
  function explain(id,focus=false) {
    const t=terms.get(id);
    if(!t){reader.removeAttribute('aria-labelledby');reader.innerHTML=`<div class="reader-placeholder">${text('选一个名词，看机制、例子和相关课程。','Select a term for its mechanism, example and related courses.')}</div>`;placeReader(false);return;}
    const d=t[lang], peers=filtered(), at=peers.findIndex(x=>x.id===id);
    reader.innerHTML=`<header class="reader-header"><span>${esc(cats.get(t.category)[lang])}</span><button type="button" data-close-reader aria-label="${text('返回网格','Back to board')}">×</button></header><div class="reader-body"><h2 id="bingo-term-title" tabindex="-1">${esc(d.title)}</h2>${zh?`<p class="reader-english" lang="en">${esc(t.en.title)}</p>`:''}<p class="reader-definition">${esc(d.summary)}</p><section><h3>${text('怎么理解','How it works')}</h3>${d.explain.map(s=>`<p>${esc(s)}</p>`).join('')}${formulas[id]?`<div class="bingo-formula">${esc(formulas[id])}</div>`:''}</section>${simulation(id)}<section><h3>${text('一个例子','A concrete example')}</h3><p>${esc(d.example)}</p></section><section class="reader-distinction"><h3>${text('分清这件事','Important distinction')}</h3><p>${esc(d.pitfall)}</p></section>${d.deep?.length?`<section><h3>${text('再深入一点','A closer look')}</h3>${d.deep.map(s=>`<p>${esc(s)}</p>`).join('')}</section>`:''}<section><h3>${text('连接这些概念','Related concepts')}</h3><div class="reader-related">${t.related.map(id=>`<a href="#c=${terms.get(id).category}&t=${id}" data-related="${id}">${esc(terms.get(id)[lang].title)}</a>`).join('')}</div></section><section><h3>${text('课程与原始资料','Courses and primary references')}</h3><ul class="reader-links">${t.courses.map(c=>`<li><a href="../${c.path}">${esc(c[lang])}</a></li>`).join('')}${t.sources.map(s=>`<li><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s[lang])} ↗</a></li>`).join('')}</ul></section></div><footer class="reader-footer"><button type="button" data-mark="${id}" class="reader-mark" aria-pressed="${!!marked[id]}">${marked[id]?'✓ ':''}${text(marked[id]?'已标记 · 点击取消':'标记已了解',marked[id]?'Marked · undo':'Mark as read')}</button><div>${peers[at-1]?`<button type="button" data-related="${peers[at-1].id}">← ${text('上一个','Previous')}</button>`:''}${peers[at+1]?`<button type="button" data-related="${peers[at+1].id}">${text('下一个','Next')} →</button>`:''}</div></footer>`;
    reader.setAttribute('aria-labelledby','bingo-term-title');reader.scrollTop=0;dialog.scrollTop=0;placeReader(focus);updateSimulation();
  }
  function placeReader(focus) {
    if(compact.matches){
      if(explicit&&state.term){dialog.append(reader);if(!dialog.open)dialog.showModal();}
      else if(dialog.open)dialog.close('layout');
    } else {if(dialog.open)dialog.close('layout');boardLayout.append(reader);}
    if(focus)reader.querySelector('h2')?.focus({preventScroll:true});
  }
  function openTerm(id) {
    if(!terms.has(id))return;if(!filtered().some(t=>t.id===id)){state.category=terms.get(id).category;state.q='';state.status='all';search.value='';status.value='all';}state.term=id;explicit=true;updateURL(true);renderBoard();explain(id,true);
  }
  function closeReader() {
    const id=state.term;explicit=false;state.term=null;if(dialog.open)dialog.close('user');updateURL(true);renderBoard();explain(null);
    grid.querySelector(`[data-term="${id}"]`)?.focus({preventScroll:true});
  }
  function mark(id) {
    if(!terms.has(id))return;if(marked[id])delete marked[id];else marked[id]=true;
    save();renderBoard();
    if(state.term===id){reader.querySelectorAll('[data-mark]').forEach(b=>{b.setAttribute('aria-pressed',String(!!marked[id]));b.textContent=(marked[id]?'✓ ':'')+text(marked[id]?'已标记 · 点击取消':'标记已了解',marked[id]?'Marked · undo':'Mark as read');});}
    message(text(`${terms.get(id).zh.title}：${marked[id]?'已标记':'已取消'}`,`${terms.get(id).en.title}: ${marked[id]?'marked':'unmarked'}`));
  }
  root.addEventListener('click',event=>{
    const el=event.target.closest('button,a');if(!el)return;
    if(el.dataset.term){event.preventDefault();openTerm(el.dataset.term);}
    else if(el.dataset.related){event.preventDefault();openTerm(el.dataset.related);}
    else if(el.dataset.mark){const id=el.dataset.mark,fromGrid=!!el.closest('#bingo-grid');mark(id);if(fromGrid)grid.querySelector(`[data-mark="${id}"]`)?.focus({preventScroll:true});}
    else if(el.dataset.category){state.category=el.dataset.category;state.q='';search.value='';explicit=false;state.term=compact.matches?null:(D.terms.find(t=>state.category==='all'||t.category===state.category)?.id||null);updateURL();renderBoard();explain(state.term);}
    else if(el.hasAttribute('data-close-reader'))closeReader();
  });
  search.addEventListener('input',()=>{state.q=search.value;updateURL();renderBoard();});
  status.addEventListener('change',()=>{state.status=status.value;updateURL();renderBoard();});
  grid.addEventListener('keydown',e=>{
    if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)||!e.target.matches('[data-term]'))return;
    const links=[...grid.querySelectorAll('[data-term]')],i=links.indexOf(e.target),columns=getComputedStyle(grid).gridTemplateColumns.split(' ').length;
    const change={ArrowLeft:-1,ArrowRight:1,ArrowUp:-columns,ArrowDown:columns}[e.key];if(links[i+change]){e.preventDefault();links[i+change].focus();}
  });
  dialog.addEventListener('cancel',e=>{e.preventDefault();closeReader();});
  dialog.addEventListener('click',e=>{if(e.target===dialog)closeReader();});
  compact.addEventListener('change',()=>placeReader(false));
  root.querySelector('#bingo-export').addEventListener('click',()=>{
    const blob=new Blob([JSON.stringify({format:'ai01-bingo',version:1,terms:marked,updatedAt:new Date().toISOString()},null,2)],{type:'application/json'});
    const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ai01-bingo-progress.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),500);
    message(text('进度已导出。','Progress exported.'));
  });
  const file=root.querySelector('#bingo-file');root.querySelector('#bingo-import').addEventListener('click',()=>file.click());
  file.addEventListener('change',async()=>{
    try{const f=file.files[0];if(!f)return;if(f.size>2_000_000)throw Error('size');const value=JSON.parse(await f.text());const n=importTerms(value);save();renderBoard();if(state.term)explain(state.term);message(text(`已合并 ${n} 项进度，原有标记保留。`,`Merged ${n} marks; existing progress retained.`));}
    catch{message(text('无法读取进度。请选择新版或旧知识地图导出的JSON文件。','Cannot import progress. Choose a JSON export from this board or the previous knowledge map.'));}
    finally{file.value='';}
  });
  function sync(){readURL();search.value=state.q;status.value=state.status;renderBoard();explain(state.term);languageLink();}
  addEventListener('hashchange',sync);addEventListener('popstate',sync);
  function input(name,label,value,step='1',min='-100',max='100'){return `<label>${esc(label)}<input data-sim="${name}" type="number" value="${value}" step="${step}" min="${min}" max="${max}"></label>`;}
  function simulation(id){
    let kind=['softmax','temperature','topk','topp'].includes(id)?'softmax':['gradient','chainrule','backprop','autograd'].includes(id)?'gradient':id;
    let controls='';
    if(kind==='tensor')controls=input('b','B',2,'1','1','64')+input('s','S',3,'1','1','4096')+input('h','H',4,'1','1','4096');
    if(kind==='softmax')controls=[2,1,0].map((n,i)=>input('z'+i,'z'+(i+1),n)).join('')+input('temp',text('温度 T','Temperature T'),1,'.1','.1','10');
    if(kind==='pooling')controls=[1,3,2,4].map((n,i)=>input('p'+i,'x'+(i+1),n)).join('');
    if(kind==='gradient')controls=input('w','w',2,'.1')+input('x','x',3,'.1')+input('y','y',4,'.1')+input('eta','η',.1,'.01','0','1');
    if(kind==='grpo')controls=[0,0,1,1].map((n,i)=>input('r'+i,'r'+(i+1),n)).join('');
    if(kind==='attention')controls=input('qx','Q₁',1,'.1')+input('qy','Q₂',0,'.1')+`<label class="sim-checkbox"><input type="checkbox" data-sim="mask">${text('屏蔽第3个位置','Mask position 3')}</label>`;
    if(!controls)return '';
    return `<section class="bingo-simulation" data-simulation="${kind}"><h3>${text('动一下，看变化','Change a value')}</h3><div class="sim-inputs">${controls}</div><div class="sim-output" aria-live="polite"></div></section>`;
  }
  function updateSimulation(){
    const sim=reader.querySelector('[data-simulation]');if(!sim)return;
    const n=(name,fallback=0)=>{const input=sim.querySelector(`[data-sim="${name}"]`),v=Number(input?.value);return Number.isFinite(v)?Math.max(Number(input.min),Math.min(Number(input.max),v)):fallback;};
    const f=v=>Number(v.toFixed(4)).toString(),out=sim.querySelector('.sim-output'),kind=sim.dataset.simulation;
    const bars=weights=>weights.map((v,i)=>`<div class="sim-bar"><span>${i+1}</span><span class="sim-track"><span style="width:${Math.max(0,Math.min(100,v*100))}%"></span></span><strong>${(v*100).toFixed(1)}%</strong></div>`).join('');
    const softmax=zs=>{const m=Math.max(...zs),es=zs.map(x=>Number.isFinite(x)?Math.exp(x-m):0),sum=es.reduce((a,b)=>a+b,0);return es.map(x=>x/sum);};
    if(kind==='tensor'){const b=Math.max(1,Math.trunc(n('b',1))),s=Math.max(1,Math.trunc(n('s',1))),h=Math.max(1,Math.trunc(n('h',1)));out.innerHTML=`<div class="tensor-sketch" aria-hidden="true">${Array.from({length:Math.min(4,b)},()=>`<div>${Array.from({length:Math.min(4,s)},()=>`<span>${'▦ '.repeat(Math.min(4,h))}</span>`).join('')}</div>`).join('')}</div><p>(B,S,H) = (${f(b)},${f(s)},${f(h)})</p><strong>${f(b*s*h)} ${text('个元素','elements')}</strong><p>FP32: ${f(b*s*h*4)} bytes · BF16: ${f(b*s*h*2)} bytes</p>`;}
    if(kind==='softmax'){const temp=Math.max(.1,n('temp',1)),weights=softmax([n('z0'),n('z1'),n('z2')].map(x=>x/temp));out.innerHTML=bars(weights)+`<p>Σp = ${f(weights.reduce((a,b)=>a+b,0))} · T = ${f(temp)}</p>`;}
    if(kind==='pooling'){const v=[0,1,2,3].map(i=>n('p'+i));out.innerHTML=`<div class="pooling-example"><div class="pooling-values">${v.map(x=>`<span>${f(x)}</span>`).join('')}</div><span>→</span><div><p>Max: <strong>${f(Math.max(...v))}</strong></p><p>Mean: <strong>${f(v.reduce((a,b)=>a+b,0)/4)}</strong></p></div></div>`;}
    if(kind==='gradient'){const w=n('w'),x=n('x'),y=n('y'),eta=n('eta'),z=w*x+1,loss=(z-y)**2,g=2*(z-y)*x,next=w-eta*g;out.innerHTML=`<p>z = wx + 1 = ${f(z)}<br>L = (z − y)² = ${f(loss)}</p><p>∂L/∂w = 2(z − y)x = <strong>${f(g)}</strong></p><p>w′ = w − ηg = <strong>${f(next)}</strong><br>L(w′) = ${f((next*x+1-y)**2)}</p>`;}
    if(kind==='grpo'){const rs=[0,1,2,3].map(i=>n('r'+i)),mean=rs.reduce((a,b)=>a+b)/4,std=Math.sqrt(rs.reduce((a,b)=>a+(b-mean)**2,0)/4),a=rs.map(r=>(r-mean)/(std+1e-8));out.innerHTML=`<p>mean = ${f(mean)} · std = ${f(std)}</p><strong>Â = [${a.map(f).join(', ')}]</strong><p>${std===0?text('同组同分：没有相对区分信号。','Equal rewards: no within-group distinction.'):text('此示例使用总体标准差。真实训练的标准化、归约、裁剪与KL设置需看具体实现。','This example uses population standard deviation. Actual normalization, reduction, clipping and KL settings depend on the implementation.')}</p>`;}
    if(kind==='attention'){const qx=n('qx'),qy=n('qy'),mask=sim.querySelector('[data-sim="mask"]').checked,scores=[qx/Math.sqrt(2),qy/Math.sqrt(2),(qx+qy)/Math.sqrt(2)];if(mask)scores[2]=-Infinity;const weights=softmax(scores),answer=weights[0]*10+weights[1]*20+weights[2]*30;out.innerHTML=`<p>K = [(1,0), (0,1), (1,1)]<br>V = [10, 20, 30] · dₖ = 2</p>${bars(weights)}<p>${text('加权输出','Weighted output')} = <strong>${f(answer)}</strong></p>`;}
  }
  reader.addEventListener('input',updateSimulation);sync();save();
})();
