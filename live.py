import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Indian Stock Dashboard", layout="wide")
st.title("📊 Indian Stock Market Dashboard")

# ---------------- Stock Suggestions ----------------
st.subheader("📌 Stock Suggestions (Live Prices – Yahoo Finance)")

suggestions = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "State Bank of India": "SBIN.NS"
}

symbols = list(suggestions.values())

@st.cache_data(ttl=60)
def fetch_suggestion_prices(symbols):
    ticker = yf.Tickers(" ".join(symbols))
    rows = []

    for name, sym in suggestions.items():
        t = ticker.tickers[sym]
        info = t.fast_info

        last_price = info.get("lastPrice")
        prev_close = info.get("previousClose")

        change = None
        if last_price is not None and prev_close:
            change = last_price - prev_close

        rows.append({
            "Company": name,
            "Symbol": sym,
            "Price (₹)": last_price,
            "Change (₹)": change
        })

    return rows

suggestion_data = fetch_suggestion_prices(symbols)

# display suggestion cards
cols = st.columns(3)

for i, row in enumerate(suggestion_data):
    with cols[i % 3]:
        price = row["Price (₹)"]
        change = row["Change (₹)"]

        price_str = f"₹ {price:.2f}" if price is not None else "₹ —"
        if change is None:
            emoji = "⚪"
            change_str = "—"
        else:
            emoji = "🟢" if change > 0 else "🔴"
            change_str = f"{change:+.2f}"

        st.markdown(f"""
        **{row['Company']}**  
        `{row['Symbol']}`  
        **{price_str}**  
        {emoji} {change_str}
        """)

st.divider()

# ---------------- SEARCH BAR (instead of dropdown) ----------------
st.subheader("🔎 Search Stock to View Details")

stock_symbol = st.text_input(
    "Enter Stock Symbol",
    value="RELIANCE.NS",
    placeholder="Eg: RELIANCE.NS, TCS.NS, AAPL"
).upper().strip()

# ---------------- Fetch selected stock data ----------------
data = yf.download(stock_symbol, period="5d", interval="1d", progress=False)

if not data.empty:
    last_price = float(data["Close"].iloc[-1])
    prev_price = float(data["Close"].iloc[-2]) if len(data) > 1 else last_price
    change = last_price - prev_price
    percent_change = (change / prev_price) * 100 if prev_price else 0
    volume = int(data["Volume"].iloc[-1])

    col1, col2, col3 = st.columns(3)
    col1.metric("Stock", stock_symbol.replace(".NS", ""))
    col2.metric(
        "Price (₹)",
        f"{last_price:.2f}",
        f"{change:+.2f} ({percent_change:+.2f}%)"
    )
    col3.metric("Day Volume", f"{volume:,}")

else:
    st.error("❌ Stock not found, market closed, or Yahoo unavailable.")

st.caption("Data source: Yahoo Finance (near real-time)")
