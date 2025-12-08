import streamlit as st
import yfinance as yf
import pandas as pd
import time
from datetime import datetime

# ---------- Page config ----------
st.set_page_config(
    page_title="Indian Stock Prices",
    layout="wide"
)

st.title("📊 Indian Live Stock Prices (Yahoo Finance)")
st.caption("Near real-time prices | NSE stocks")

# ---------- Stock list ----------
default_stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

selected_stocks = st.multiselect(
    "Select stocks to view:",
    options=default_stocks,
    default=default_stocks[:3]
)

@st.cache_data(ttl=30)
def get_stock_data(symbols):
    tickers = yf.Tickers(" ".join(symbols))
    rows = []

    for sym in symbols:
        t = tickers.tickers[sym]
        info = t.fast_info

        rows.append({
            "Stock": sym.replace(".NS", ""),
            "Price (₹)": info.get("lastPrice"),
            "Change (₹)": info.get("lastPrice") - info.get("previousClose")
            if info.get("previousClose") else None,
            "Change (%)": (
                ((info.get("lastPrice") - info.get("previousClose"))
                / info.get("previousClose")) * 100
            ) if info.get("previousClose") else None,
            "Day Volume": info.get("volume")
        })

    return pd.DataFrame(rows)

if selected_stocks:
    try:
        df = get_stock_data(selected_stocks)

        st.dataframe(
            df.style.format({
                "Price (₹)": "{:.2f}",
                "Change (₹)": "{:+.2f}",
                "Change (%)": "{:+.2f}",
                "Day Volume": "{:,}"
            }),
            use_container_width=True
        )

        st.caption(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")

        # auto refresh
        time.sleep(30)
        st.rerun()

    except Exception as e:
        st.error(f"Error fetching stock prices: {e}")
else:
    st.info("Select at least one stock to view.")

st.caption("Data source: Yahoo Finance")
