import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Indian Stock Dashboard", layout="wide")
st.title("📊 Indian Stock Market Dashboard")

# ---------------- Stock Suggestions ----------------
st.subheader("📌 Stock Suggestions (Popular NSE Companies)")

suggestions = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "State Bank of India": "SBIN.NS"
}

for name, symbol in suggestions.items():
    st.markdown(f"• **{name}** ({symbol})")

st.divider()

# ---------------- Stock Selector ----------------
stock_symbol = st.selectbox(
    "📈 Select Stock to View Price",
    list(suggestions.values())
)

# ---------------- Fetch data (stable) ----------------
# Use 5-day daily data instead of 1-minute (Yahoo-safe)
data = yf.download(stock_symbol, period="5d", interval="1d", progress=False)

if not data.empty:
    last_price = float(data["Close"].iloc[-1])
    prev_price = float(data["Close"].iloc[-2]) if len(data) > 1 else last_price
    change = last_price - prev_price
    percent_change = (change / prev_price) * 100 if prev_price != 0 else 0

    volume = int(data["Volume"].iloc[-1])

    # ---------------- Display metrics ----------------
    col1, col2, col3 = st.columns(3)
    col1.metric("Stock", stock_symbol.replace(".NS", ""))
    col2.metric(
        "Price (₹)",
        f"{last_price:.2f}",
        f"{change:+.2f} ({percent_change:+.2f}%)"
    )
    col3.metric("Day Volume", f"{volume:,}")

else:
    st.error("Failed to load data. Data unavailable or market closed.")

st.caption("Data source: Yahoo Finance | Prices are near real-time")
