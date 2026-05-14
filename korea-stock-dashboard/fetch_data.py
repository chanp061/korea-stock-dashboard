import requests
import json
import os
from datetime import datetime
import pytz
from xml.etree import ElementTree as ET

KST = pytz.timezone('Asia/Seoul')
now = datetime.now(KST)

def fetch_index(symbol):
    """Yahoo Finance 비공식 API로 지수 데이터 수집"""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        d = r.json()
        meta = d["chart"]["result"][0]["meta"]
        price = meta.get("regularMarketPrice", 0)
        prev  = meta.get("chartPreviousClose", price)
        change = price - prev
        pct    = (change / prev * 100) if prev else 0
        return {
            "price":  round(price, 2),
            "change": round(change, 2),
            "pct":    round(pct, 2)
        }
    except Exception as e:
        print(f"[ERROR] {symbol}: {e}")
        return {"price": 0, "change": 0, "pct": 0}

def fetch_news():
    """네이버 금융 뉴스 RSS"""
    url = "https://finance.naver.com/news/news_list.naver?mode=LPRICE&section_ids=&category=0&date="
    rss_url = "https://finance.naver.com/news/rss.naver?mode=LSS2D&section_ids=Stock_Market&date="
    headers = {"User-Agent": "Mozilla/5.0"}
    news_list = []

    try:
        r = requests.get(rss_url, headers=headers, timeout=10)
        r.encoding = 'utf-8'
        root = ET.fromstring(r.content)
        items = root.findall('.//item')[:6]
        for item in items:
            title = item.findtext('title', '').strip()
            link  = item.findtext('link', '').strip()
            pub   = item.findtext('pubDate', '').strip()
            if title:
                news_list.append({"title": title, "link": link, "pub": pub})
    except Exception as e:
        print(f"[ERROR] news RSS: {e}")

    # 뉴스가 없으면 네이버 증시 뉴스 HTML 파싱으로 폴백
    if not news_list:
        try:
            from bs4 import BeautifulSoup
            r2 = requests.get(
                "https://finance.naver.com/news/news_list.naver?mode=LPRICE&section_ids=&category=0",
                headers=headers, timeout=10
            )
            r2.encoding = 'cp949'
            soup = BeautifulSoup(r2.text, 'html.parser')
            for a in soup.select('dl dd.articleSubject a')[:6]:
                title = a.get_text(strip=True)
                link  = "https://finance.naver.com" + a.get('href', '')
                news_list.append({"title": title, "link": link, "pub": ""})
        except Exception as e:
            print(f"[ERROR] news fallback: {e}")

    return news_list

def get_market_status(pct):
    if pct >= 1.5:   return {"label": "강세", "emoji": "🚀"}
    elif pct >= 0.3: return {"label": "소폭 강세", "emoji": "📈"}
    elif pct >= -0.3:return {"label": "보합", "emoji": "➡️"}
    elif pct >= -1.5:return {"label": "소폭 약세", "emoji": "📉"}
    else:            return {"label": "약세", "emoji": "🔻"}

def get_signal(kospi_pct, kosdaq_pct):
    avg = (kospi_pct + kosdaq_pct) / 2
    if avg >= 1.0:
        return {"text": "오늘 시장은 강세입니다. 추격 매수보다 보유 전략이 유리할 수 있어요.", "type": "positive"}
    elif avg >= 0:
        return {"text": "소폭 상승권. 뚜렷한 방향성보다 관망이 적절합니다.", "type": "neutral"}
    elif avg >= -1.0:
        return {"text": "소폭 하락권. 패닉셀보다 분할 매수 기회를 살펴보세요.", "type": "neutral"}
    else:
        return {"text": "시장 조정 국면. 손절보다 비중 축소 후 상황을 지켜보세요.", "type": "negative"}

# ── 데이터 수집 ──────────────────────────────────────────────
print("📡 데이터 수집 시작...")

kospi  = fetch_index("^KS11")
kosdaq = fetch_index("^KQ11")
# 추가 참고 지수
sp500  = fetch_index("^GSPC")
nasdaq = fetch_index("^IXIC")
usdkrw = fetch_index("KRW=X")

news = fetch_news()
kospi_status  = get_market_status(kospi["pct"])
kosdaq_status = get_market_status(kosdaq["pct"])
signal = get_signal(kospi["pct"], kosdaq["pct"])

data = {
    "updated_at": now.strftime("%Y년 %m월 %d일 %H:%M"),
    "updated_date": now.strftime("%Y-%m-%d"),
    "kospi": {**kospi,  **kospi_status},
    "kosdaq":{**kosdaq, **kosdaq_status},
    "sp500": sp500,
    "nasdaq":nasdaq,
    "usdkrw":usdkrw,
    "news":  news,
    "signal":signal,
    "one_liner": f"코스피 {kospi_status['emoji']} {kospi_status['label']} · 코스닥 {kosdaq_status['emoji']} {kosdaq_status['label']}"
}

os.makedirs("data", exist_ok=True)
with open("data/market.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 저장 완료: KOSPI {kospi['price']} ({kospi['pct']:+.2f}%) / KOSDAQ {kosdaq['price']} ({kosdaq['pct']:+.2f}%)")
