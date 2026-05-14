<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📊 오늘의 한국 증시</title>
<meta property="og:title" content="📊 오늘의 한국 증시 리포트">
<meta property="og:description" content="매일 오전 7시 업데이트 — 가족을 위한 증시 브리핑">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/lightweight-charts@4.1.3/dist/lightweight-charts.standalone.production.js"></script>
<style>
:root{
  --bg:#0d0f14;--bg2:#161820;--bg3:#1e2028;--bg4:#252830;
  --border:rgba(255,255,255,0.07);--border2:rgba(255,255,255,0.12);
  --text:#f0f0f0;--muted:#8a8d99;--dim:#545766;
  --up:#ff6b6b;--down:#4d9eff;--neutral:#a0a8c0;
  --accent:#7c6dfa;--accent2:#4fc4a8;--warn:#f5a623;
  --font:'Noto Sans KR',sans-serif;--mono:'DM Mono',monospace;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:var(--font);min-height:100vh;padding-bottom:60px;}

/* 헤더 & 탭 */
.header{background:linear-gradient(135deg,#1a1730 0%,#0d1420 100%);border-bottom:0.5px solid var(--border2);padding:16px 16px 0;position:sticky;top:0;z-index:20;backdrop-filter:blur(8px);}
.header-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
.header-title{font-size:16px;font-weight:700;}
.header-title span{color:var(--accent);}
.update-badge{font-size:11px;color:var(--muted);font-family:var(--mono);background:rgba(255,255,255,0.05);padding:3px 9px;border-radius:20px;border:0.5px solid var(--border);}
.update-badge.live{color:var(--accent2);border-color:rgba(79,196,168,0.3);}
.tabs{display:flex;}
.tab{flex:1;text-align:center;padding:10px 0;font-size:13px;font-weight:500;color:var(--muted);border-bottom:2px solid transparent;cursor:pointer;transition:all .2s;}
.tab.active{color:var(--accent);border-bottom-color:var(--accent);}

/* 페이지 */
.page{display:none;max-width:480px;margin:0 auto;padding:16px 16px 0;}
.page.active{display:block;}

/* 공통 카드 */
.section{background:var(--bg2);border:0.5px solid var(--border);border-radius:14px;padding:16px;margin-bottom:12px;}
.section-header{display:flex;align-items:center;gap:8px;margin-bottom:14px;}
.section-icon{width:28px;height:28px;background:rgba(124,109,250,0.15);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;}
.section-title{font-size:14px;font-weight:500;}

/* 시장 현황 */
.index-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px;}
.idx-card{background:var(--bg2);border:0.5px solid var(--border2);border-radius:14px;padding:16px;position:relative;overflow:hidden;}
.idx-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;border-radius:14px 14px 0 0;}
.idx-card.up::before{background:linear-gradient(90deg,#ff6b6b,#ff9f9f);}
.idx-card.down::before{background:linear-gradient(90deg,#4d9eff,#7ab8ff);}
.idx-card.flat::before{background:linear-gradient(90deg,#545766,#8a8d99);}
.idx-name{font-size:11px;color:var(--muted);margin-bottom:6px;font-family:var(--mono);}
.idx-price{font-size:22px;font-weight:700;font-family:var(--mono);letter-spacing:-1px;margin-bottom:4px;}
.idx-change{font-size:13px;font-weight:500;}
.idx-status{font-size:11px;color:var(--muted);margin-top:6px;}
.ref-bar{background:var(--bg2);border:0.5px solid var(--border);border-radius:12px;padding:12px 16px;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px;}
.ref-item{text-align:center;}
.ref-name{font-size:10px;color:var(--muted);font-family:var(--mono);margin-bottom:3px;}
.ref-val{font-size:13px;font-weight:500;font-family:var(--mono);}
.ref-pct{font-size:11px;}
.oneliner{background:linear-gradient(135deg,rgba(124,109,250,0.1),rgba(79,196,168,0.1));border:0.5px solid rgba(124,109,250,0.3);border-radius:12px;padding:14px 16px;font-size:14px;text-align:center;color:#c8c3ff;line-height:1.5;margin-bottom:12px;}
.oneliner .lbl{font-size:11px;color:var(--muted);margin-bottom:4px;font-family:var(--mono);}
.signal-box{border-radius:10px;padding:12px 14px;font-size:13px;line-height:1.6;border:0.5px solid;}
.signal-box.positive{background:rgba(255,107,107,0.08);border-color:rgba(255,107,107,0.25);color:#ffb3b3;}
.signal-box.negative{background:rgba(77,158,255,0.08);border-color:rgba(77,158,255,0.25);color:#a0c8ff;}
.signal-box.neutral{background:rgba(160,168,192,0.08);border-color:rgba(160,168,192,0.2);color:var(--muted);}
.news-item{padding:10px 0;border-bottom:0.5px solid var(--border);display:flex;gap:10px;align-items:flex-start;text-decoration:none;color:inherit;}
.news-item:last-child{border-bottom:none;padding-bottom:0;}
.news-num{font-size:11px;font-family:var(--mono);color:var(--dim);min-width:16px;padding-top:2px;}
.news-title{font-size:13px;line-height:1.55;color:var(--text);margin-bottom:2px;}
.news-pub{font-size:11px;color:var(--dim);font-family:var(--mono);}

/* 종목 검색 */
.search-wrap{position:relative;margin-bottom:12px;}
.search-input{width:100%;background:var(--bg3);border:0.5px solid var(--border2);border-radius:12px;padding:13px 52px 13px 16px;font-size:15px;color:var(--text);font-family:var(--font);outline:none;transition:border-color .2s;}
.search-input:focus{border-color:var(--accent);}
.search-input::placeholder{color:var(--dim);}
.search-btn{position:absolute;right:10px;top:50%;transform:translateY(-50%);background:var(--accent);border:none;border-radius:8px;color:#fff;padding:7px 12px;cursor:pointer;font-size:13px;font-family:var(--font);}
.popular-tags{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:4px;}
.tag{background:var(--bg3);border:0.5px solid var(--border2);border-radius:20px;padding:5px 12px;font-size:12px;color:var(--muted);cursor:pointer;transition:all .2s;}
.tag:hover,.tag:active{border-color:var(--accent);color:var(--accent);}

/* 종목 결과 */
.stock-result{display:none;}
.stock-result.on{display:block;}
.scard{background:var(--bg2);border:0.5px solid var(--border2);border-radius:14px;padding:18px;margin-bottom:12px;}
.sname{font-size:18px;font-weight:700;margin-bottom:2px;}
.scode{font-size:12px;color:var(--muted);font-family:var(--mono);margin-bottom:12px;}
.sprice{font-size:32px;font-weight:700;font-family:var(--mono);letter-spacing:-1px;}
.sbadge{display:inline-block;font-size:13px;font-weight:500;padding:3px 10px;border-radius:6px;margin-top:6px;}
.sbadge.up{background:rgba(255,107,107,0.14);color:var(--up);}
.sbadge.down{background:rgba(77,158,255,0.14);color:var(--down);}
.sbadge.flat{background:rgba(160,168,192,0.1);color:var(--neutral);}

.mgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px;}
.mcard{background:var(--bg2);border:0.5px solid var(--border);border-radius:12px;padding:12px;text-align:center;}
.mlabel{font-size:10px;color:var(--muted);font-family:var(--mono);margin-bottom:5px;letter-spacing:.04em;}
.mval{font-size:14px;font-weight:700;font-family:var(--mono);}
.msub{font-size:10px;color:var(--dim);margin-top:3px;}

.chart-wrap{background:var(--bg2);border:0.5px solid var(--border);border-radius:14px;padding:16px;margin-bottom:12px;}
.chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
.chart-ttl{font-size:13px;font-weight:500;}
.pbtns{display:flex;gap:4px;}
.pbtn{background:var(--bg3);border:0.5px solid var(--border);border-radius:6px;color:var(--muted);font-size:11px;padding:4px 9px;cursor:pointer;font-family:var(--mono);}
.pbtn.active{background:var(--accent);color:#fff;border-color:var(--accent);}
.malegend{display:flex;gap:14px;justify-content:center;margin-top:8px;}
.malegend span{font-size:11px;}
#candleChart{width:100%;height:220px;}

.rangebox{background:var(--bg2);border:0.5px solid var(--border);border-radius:12px;padding:14px 16px;margin-bottom:12px;}
.range-labels{display:flex;justify-content:space-between;font-size:11px;color:var(--muted);font-family:var(--mono);margin-bottom:8px;}
.range-track{width:100%;height:6px;background:var(--bg3);border-radius:3px;position:relative;margin-bottom:8px;}
.range-fill{height:100%;background:linear-gradient(90deg,var(--down),var(--up));border-radius:3px;}
.range-dot{position:absolute;top:-5px;width:16px;height:16px;border-radius:50%;background:var(--accent);border:2px solid var(--bg);transform:translateX(-50%);}
.range-now{text-align:center;font-size:12px;color:var(--muted);}

.loading-sm{text-align:center;padding:40px;color:var(--muted);font-size:13px;}
.spin{display:inline-block;width:18px;height:18px;border:2px solid var(--border2);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite;vertical-align:middle;margin-right:6px;}
@keyframes spin{to{transform:rotate(360deg);}}
.errmsg{background:rgba(255,107,107,0.08);border:0.5px solid rgba(255,107,107,0.2);border-radius:10px;padding:14px;font-size:13px;color:#ffb3b3;text-align:center;margin-bottom:12px;}

.loading-full{display:flex;align-items:center;justify-content:center;min-height:280px;flex-direction:column;gap:12px;color:var(--muted);font-size:14px;}
.spin-lg{width:28px;height:28px;border:2px solid var(--border2);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite;}

.c-up{color:var(--up);}.c-down{color:var(--down);}.c-flat{color:var(--neutral);}
.disclaimer{text-align:center;font-size:11px;color:var(--dim);padding:8px 16px 0;line-height:1.6;}
</style>
</head>
<body>

<div class="header">
  <div class="header-top">
    <div class="header-title"><span>📊</span> 한국 증시 대시보드</div>
    <div class="update-badge" id="upBadge">로딩 중...</div>
  </div>
  <div class="tabs">
    <div class="tab active" onclick="switchTab('market')">🏠 시장 현황</div>
    <div class="tab" onclick="switchTab('stock')">🔍 종목 분석</div>
  </div>
</div>

<!-- 탭1: 시장 현황 -->
<div id="pgMarket" class="page active">
  <div id="marketApp">
    <div class="loading-full"><div class="spin-lg"></div><span>시황 불러오는 중...</span></div>
  </div>
</div>

<!-- 탭2: 종목 분석 -->
<div id="pgStock" class="page">
  <div class="section">
    <div class="search-wrap">
      <input class="search-input" id="stockInput" type="text"
        placeholder="종목명 또는 6자리 코드 (예: 삼성전자, 005930)" autocomplete="off">
      <button class="search-btn" onclick="doSearch()">검색</button>
    </div>
    <div style="font-size:12px;color:var(--muted);margin-bottom:8px;">인기 종목 바로가기</div>
    <div class="popular-tags" id="popTags"></div>
  </div>
  <div id="stockResult" class="stock-result"></div>
  <div class="disclaimer">본 페이지는 투자 권유가 아닌 정보 제공 목적입니다. 투자 결정은 반드시 본인 판단으로 하세요.</div>
</div>

<script>
// ─── 인기 종목 ────────────────────────────────────────────
const POPULAR = [
  {n:'삼성전자', c:'005930.KS'},{n:'SK하이닉스', c:'000660.KS'},
  {n:'현대차',   c:'005380.KS'},{n:'NAVER',      c:'035420.KS'},
  {n:'카카오',   c:'035720.KS'},{n:'LG에너지솔루션',c:'373220.KS'},
  {n:'셀트리온', c:'068270.KS'},{n:'에코프로비엠', c:'247540.KQ'},
];
const popEl = document.getElementById('popTags');
POPULAR.forEach(s=>{
  const t=document.createElement('div');
  t.className='tag'; t.textContent=s.n;
  t.onclick=()=>{ document.getElementById('stockInput').value=s.n; doSearch(s.c); };
  popEl.appendChild(t);
});

// ─── 탭 전환 ─────────────────────────────────────────────
function switchTab(tab){
  document.querySelectorAll('.tab').forEach((t,i)=>t.classList.toggle('active',(i===0&&tab==='market')||(i===1&&tab==='stock')));
  document.getElementById('pgMarket').classList.toggle('active',tab==='market');
  document.getElementById('pgStock').classList.toggle('active',tab==='stock');
}

// ─── 유틸 ────────────────────────────────────────────────
const fmt  = n=>Number(n).toLocaleString('ko-KR',{maximumFractionDigits:2});
const sign = n=>n>=0?'+':'';
const cc   = n=>n>0.1?'up':n<-0.1?'down':'flat';

// ─── 시장 현황 ────────────────────────────────────────────
async function loadMarket(){
  const app=document.getElementById('marketApp');
  const badge=document.getElementById('upBadge');
  try{
    const r=await fetch('data/market.json?t='+Date.now());
    const d=await r.json();
    badge.textContent=d.updated_at; badge.className='update-badge live';
    const kc=cc(d.kospi.pct), qc=cc(d.kosdaq.pct);
    const refH=(lbl,o)=>`<div class="ref-item">
      <div class="ref-name">${lbl}</div>
      <div class="ref-val c-${cc(o.pct)}">${o.price>0?fmt(o.price):'-'}</div>
      <div class="ref-pct c-${cc(o.pct)}">${o.price>0?sign(o.pct)+o.pct.toFixed(2)+'%':''}</div>
    </div>`;
    const newsH=d.news.length>0
      ? d.news.map((n,i)=>`<a class="news-item" href="${n.link||'#'}" target="_blank" rel="noopener">
          <div class="news-num">0${i+1}</div>
          <div><div class="news-title">${n.title}</div>${n.pub?`<div class="news-pub">${n.pub.slice(0,16)}</div>`:''}</div>
        </a>`).join('')
      : '<div style="color:var(--muted);font-size:13px;text-align:center;padding:12px 0">뉴스를 불러오지 못했습니다</div>';
    app.innerHTML=`
      <div class="index-grid">
        <div class="idx-card ${kc}">
          <div class="idx-name">KOSPI</div>
          <div class="idx-price">${d.kospi.price>0?fmt(d.kospi.price):'-'}</div>
          <div class="idx-change ${kc}">${d.kospi.price>0?sign(d.kospi.change)+fmt(d.kospi.change)+' ('+sign(d.kospi.pct)+d.kospi.pct.toFixed(2)+'%)':'-'}</div>
          <div class="idx-status">${d.kospi.emoji||''} ${d.kospi.label||''}</div>
        </div>
        <div class="idx-card ${qc}">
          <div class="idx-name">KOSDAQ</div>
          <div class="idx-price">${d.kosdaq.price>0?fmt(d.kosdaq.price):'-'}</div>
          <div class="idx-change ${qc}">${d.kosdaq.price>0?sign(d.kosdaq.change)+fmt(d.kosdaq.change)+' ('+sign(d.kosdaq.pct)+d.kosdaq.pct.toFixed(2)+'%)':'-'}</div>
          <div class="idx-status">${d.kosdaq.emoji||''} ${d.kosdaq.label||''}</div>
        </div>
      </div>
      <div class="ref-bar">${refH('S&P500',d.sp500)}${refH('NASDAQ',d.nasdaq)}${refH('USD/KRW',d.usdkrw)}</div>
      <div class="oneliner"><div class="lbl">💬 오늘의 시장 요약</div>${d.one_liner}</div>
      <div class="section">
        <div class="section-header"><div class="section-icon">🧭</div><div class="section-title">오늘의 투자 시그널</div></div>
        <div class="signal-box ${d.signal.type}">${d.signal.text}</div>
      </div>
      <div class="section">
        <div class="section-header"><div class="section-icon">📰</div><div class="section-title">오늘의 증시 뉴스</div></div>
        ${newsH}
      </div>
      <div class="disclaimer">본 페이지는 투자 권유가 아닌 정보 제공 목적입니다.<br>투자 결정은 반드시 본인 판단으로 하세요.</div>`;
  }catch(e){
    badge.textContent='오류';
    app.innerHTML=`<div class="loading-full"><span style="font-size:24px">⚠️</span><span>데이터를 불러오지 못했습니다</span>
      <button onclick="loadMarket()" style="padding:8px 20px;background:var(--accent);color:#fff;border:none;border-radius:8px;cursor:pointer;font-size:13px">다시 시도</button></div>`;
  }
}

// ─── 종목 검색 & 분석 ─────────────────────────────────────
let _chart=null, _chartData=null;

async function doSearch(symOverride){
  const inp=document.getElementById('stockInput').value.trim();
  if(!inp&&!symOverride) return;
  let sym=symOverride||'';
  if(!sym){
    if(/^\d{6}$/.test(inp)){
      sym=inp+'.KS';
    } else {
      const found=POPULAR.find(s=>s.n.includes(inp)||inp.includes(s.n));
      sym=found?found.c:inp+'.KS';
    }
  }
  const res=document.getElementById('stockResult');
  res.className='stock-result on';
  res.innerHTML=`<div class="loading-sm"><span class="spin"></span>데이터 로딩 중...</div>`;
  try{
    const url=`https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(sym)}?interval=1d&range=1y`;
    const r=await fetch(url,{headers:{'User-Agent':'Mozilla/5.0'}});
    const j=await r.json();
    if(!j.chart.result) throw new Error('종목 없음');
    const meta=j.chart.result[0].meta;
    const q=j.chart.result[0].indicators.quote[0];
    const ts=j.chart.result[0].timestamp;

    const price=meta.regularMarketPrice;
    const prev=meta.chartPreviousClose;
    const chg=price-prev, pct=chg/prev*100;
    const h52=meta.fiftyTwoWeekHigh, l52=meta.fiftyTwoWeekLow;
    const vol=meta.regularMarketVolume;
    const cap=meta.marketCap;
    const name=meta.shortName||meta.longName||sym;
    const cur=meta.currency||'KRW';
    const rPos=((price-l52)/(h52-l52)*100).toFixed(1);

    // 캔들 데이터
    const candles=[];
    for(let i=0;i<ts.length;i++){
      if(q.open[i]&&q.high[i]&&q.low[i]&&q.close[i])
        candles.push({time:ts[i],open:q.open[i],high:q.high[i],low:q.low[i],close:q.close[i]});
    }

    // 이동평균
    function ma(data,p){
      return data.map((d,i)=>{
        if(i<p-1)return null;
        const avg=data.slice(i-p+1,i+1).reduce((s,v)=>s+v.close,0)/p;
        return{time:d.time,value:parseFloat(avg.toFixed(2))};
      }).filter(Boolean);
    }
    const ma5=ma(candles,5),ma20=ma(candles,20),ma60=ma(candles,60);

    // RSI 14일
    function rsi14(data){
      if(data.length<15)return null;
      let g=0,l=0;
      for(let i=1;i<=14;i++){const d=data[i].close-data[i-1].close; d>0?g+=d:l+=Math.abs(d);}
      let ag=g/14,al=l/14;
      for(let i=15;i<data.length;i++){
        const d=data[i].close-data[i-1].close;
        ag=(ag*13+(d>0?d:0))/14; al=(al*13+(d<0?Math.abs(d):0))/14;
      }
      return al===0?100:parseFloat((100-(100/(1+ag/al))).toFixed(1));
    }
    const rsi=rsi14(candles);
    const rsiTxt=rsi===null?'-':rsi>70?`${rsi} 🔥 과열`:rsi<30?`${rsi} 🧊 침체`:`${rsi} ✅ 정상`;

    // 거래량 비율
    const avgV=candles.slice(-20).reduce((s,c)=>s+(c.volume||0),0)/20;
    const volR=vol&&avgV?((vol/avgV)*100).toFixed(0)+'%':'-';

    // MA20 대비
    const ma20last=ma20.length?ma20[ma20.length-1].value:null;
    const ma20diff=ma20last?sign(price-ma20last)+((price/ma20last-1)*100).toFixed(1)+'%':'-';

    const fmtCap=cap?(cap>1e12?(cap/1e12).toFixed(1)+'조':(cap/1e8).toFixed(0)+'억'):'-';
    const dc=cc(pct);

    res.innerHTML=`
      <div class="scard">
        <div class="sname">${name}</div>
        <div class="scode">${sym} · ${cur}</div>
        <div class="sprice c-${dc}">${fmt(price)}</div>
        <div class="sbadge ${dc}">${sign(chg)}${fmt(chg)} (${sign(pct)}${pct.toFixed(2)}%)</div>
      </div>

      <div class="mgrid">
        <div class="mcard"><div class="mlabel">거래량</div><div class="mval" style="font-size:12px">${vol?fmt(vol):'-'}</div><div class="msub">평균 대비 ${volR}</div></div>
        <div class="mcard"><div class="mlabel">시가총액</div><div class="mval" style="font-size:13px">${fmtCap}</div><div class="msub">${cur}</div></div>
        <div class="mcard"><div class="mlabel">RSI (14)</div><div class="mval" style="font-size:12px">${rsiTxt}</div><div class="msub">상대강도지수</div></div>
        <div class="mcard"><div class="mlabel">52주 최고</div><div class="mval c-up" style="font-size:12px">${fmt(h52)}</div><div class="msub">대비 ${((price/h52-1)*100).toFixed(1)}%</div></div>
        <div class="mcard"><div class="mlabel">52주 최저</div><div class="mval c-down" style="font-size:12px">${fmt(l52)}</div><div class="msub">대비 +${((price/l52-1)*100).toFixed(1)}%</div></div>
        <div class="mcard"><div class="mlabel">MA20 대비</div><div class="mval" style="font-size:13px">${ma20diff}</div><div class="msub">20일 이동평균</div></div>
      </div>

      <div class="rangebox">
        <div class="range-labels"><span>52주 최저 ${fmt(l52)}</span><span>52주 최고 ${fmt(h52)}</span></div>
        <div class="range-track">
          <div class="range-fill" style="width:100%"></div>
          <div class="range-dot" style="left:${rPos}%"></div>
        </div>
        <div class="range-now">현재 ${fmt(price)} — 52주 범위 내 <strong>${rPos}%</strong> 위치</div>
      </div>

      <div class="chart-wrap">
        <div class="chart-head">
          <div class="chart-ttl">📈 캔들 차트 + 이동평균</div>
          <div class="pbtns">
            <button class="pbtn" onclick="chgPeriod('1M',this)">1M</button>
            <button class="pbtn active" onclick="chgPeriod('3M',this)">3M</button>
            <button class="pbtn" onclick="chgPeriod('6M',this)">6M</button>
            <button class="pbtn" onclick="chgPeriod('1Y',this)">1Y</button>
          </div>
        </div>
        <div id="candleChart"></div>
        <div class="malegend">
          <span style="color:#ffd700">── MA5</span>
          <span style="color:#4d9eff">── MA20</span>
          <span style="color:#ff6b6b">── MA60</span>
        </div>
      </div>
    `;

    _chartData={candles,ma5,ma20,ma60};
    renderChart('3M');

  }catch(e){
    console.error(e);
    res.innerHTML=`<div class="errmsg">⚠️ 종목 데이터를 불러오지 못했습니다.<br>6자리 종목코드(예: 005930)로 다시 시도해 보세요.</div>`;
  }
}

function renderChart(period){
  const el=document.getElementById('candleChart');
  if(!el||!_chartData)return;
  const{candles,ma5,ma20,ma60}=_chartData;
  const cutDays={'1M':30,'3M':90,'6M':180,'1Y':365};
  const cut=Date.now()/1000-cutDays[period]*86400;
  const fc=candles.filter(c=>c.time>=cut);
  const fm5=ma5.filter(c=>c.time>=cut);
  const fm20=ma20.filter(c=>c.time>=cut);
  const fm60=ma60.filter(c=>c.time>=cut);
  if(_chart){_chart.remove();_chart=null;}
  _chart=LightweightCharts.createChart(el,{
    width:el.clientWidth||360,height:220,
    layout:{background:{color:'#161820'},textColor:'#8a8d99'},
    grid:{vertLines:{color:'rgba(255,255,255,0.04)'},horzLines:{color:'rgba(255,255,255,0.04)'}},
    rightPriceScale:{borderColor:'rgba(255,255,255,0.1)'},
    timeScale:{borderColor:'rgba(255,255,255,0.1)',timeVisible:true},
    crosshair:{mode:LightweightCharts.CrosshairMode.Normal},
  });
  const cs=_chart.addCandlestickSeries({
    upColor:'#ff6b6b',downColor:'#4d9eff',
    borderUpColor:'#ff6b6b',borderDownColor:'#4d9eff',
    wickUpColor:'#ff6b6b',wickDownColor:'#4d9eff',
  });
  cs.setData(fc);
  const l5=_chart.addLineSeries({color:'#ffd700',lineWidth:1,priceLineVisible:false});
  l5.setData(fm5);
  const l20=_chart.addLineSeries({color:'#4d9eff',lineWidth:1.5,priceLineVisible:false});
  l20.setData(fm20);
  const l60=_chart.addLineSeries({color:'#ff6b6b',lineWidth:1.5,priceLineVisible:false});
  l60.setData(fm60);
  _chart.timeScale().fitContent();
}

function chgPeriod(p,btn){
  document.querySelectorAll('.pbtn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  renderChart(p);
}

document.getElementById('stockInput').addEventListener('keydown',e=>{if(e.key==='Enter')doSearch();});

// ─── 초기화 ──────────────────────────────────────────────
loadMarket();
setInterval(loadMarket,10*60*1000);
</script>
</body>
</html>
