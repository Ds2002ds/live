import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ---------- Page setup ----------
st.set_page_config(
    page_title="Indian Stock Dashboard",
    layout="wide"
)

st.title("📊 Indian Stock Market Dashboard")

# ---------- Auto refresh every 30 sec ----------
st_autorefresh(interval=30 * 1000, key="refresh")

# ---------- Stock input ----------
stock_symbol = st.text_input(
    "Enter NSE Stock Symbol (RELIANCE.NS, TCS.NS, INFY.NS):",
    value="RELIANCE.NS"
).upper().strip()

if stock_symbol:
    try:
        # ---------- Fetch intraday data ----------
        data = yf.download(
            stock_symbol,
            period="1d",
            interval="1m",
            progress=False
        )

        if data.empty:
            st.warning("No intraday data available (market closed or Yahoo delay).")
            st.stop()

        # ---------- Clean data ----------
        data = data.dropna()

        last_price = float(data["Close"].iloc[-1])
        previous_price = float(data["Close"].iloc[-2])
        change = last_price - previous_price

        # ✅ TOTAL traded volume of the day
        total_volume = int(data["Volume"].sum())

        # ---------- Metrics ----------
        c1, c2, c3 = st.columns(3)
        c1.metric("Stock", stock_symbol.replace(".NS", ""))
        c2.metric(
            "Price (₹)",
            f"{last_price:.2f}",
            f"{change:+.2f}"
        )
        c3.metric("Day Volume", f"{total_volume:,}")

        # ---------- Live price chart ----------
        st.subheader("Intraday Price Movement")
        st.line_chart(data["Close"])

        # ---------- Optional volume chart ----------
        st.subheader("Intraday Volume")
        st.bar_chart(data["Volume"])

        # ---------- Last updated ----------
        st.caption(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")

    except Exception as e:
        st.error(f"Error fetching data: {e}")

else:
    st.info("Enter a valid NSE stock symbol.")

st.caption("Data source: Yahoo Finance (Near-real-time)")
