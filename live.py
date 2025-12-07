import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Indian Stock Dashboard", layout="wide")
st.title("📊 Indian Stock Market Dashboard")

# Stock selector
stock_symbol = st.selectbox(
    "Select Stock",
    ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS"]
)

# Fetch 1-day data with 1-minute interval
data = yf.download(stock_symbol, period="1d", interval="1m")

if not data.empty:
    last_price = float(data["Close"].iloc[-1])
    prev_price = float(data["Close"].iloc[-2]) if len(data) > 1 else last_price
    change = last_price - prev_price

    # Convert to native Python float for Streamlit
    delta_val = float(round(change, 2)) if change is not None else 0.0

    # Display metrics safely
    col1, col2, col3 = st.columns(3)
    col1.metric("Stock", stock_symbol)
    col2.metric("Price (₹)", round(last_price, 2), delta_val)
    col3.metric("Volume", int(data["Volume"].iloc[-1]))

    st.line_chart(data["Close"])
else:
    st.error("Failed to load data. Market may be closed or data unavailable.")

st.caption("Data source: Yahoo Finance")
