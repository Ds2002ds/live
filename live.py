import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Indian Stock Dashboard", layout="wide")
st.title("📊 Indian Stock Market Dashboard")

# --- Search input for stock ---
stock_symbol = st.text_input(
    "Enter NSE Stock Symbol (e.g., RELIANCE.NS, TCS.NS, INFY.NS):",
    value="RELIANCE.NS"
).upper().strip()

if stock_symbol:
    try:
        # Fetch 1-day 1-min data
        data = yf.download(stock_symbol, period="1d", interval="1m")

        if not data.empty:
            last_price = float(data["Close"].iloc[-1])
            prev_price = float(data["Close"].iloc[-2]) if len(data) > 1 else last_price
            change = last_price - prev_price
            delta_val = float(round(change, 2))
            volume = int(data["Volume"].iloc[-1])

            # Display metrics safely
            col1, col2, col3 = st.columns(3)
            col1.metric("Stock", stock_symbol.replace(".NS", ""))
            col2.metric("Price (₹)", round(last_price, 2), delta_val)
            col3.metric("Volume", volume)

            st.line_chart(data["Close"])
        else:
            st.error(f"No data available for {stock_symbol}. Market may be closed.")
    except Exception as e:
        st.error(f"Error fetching data for {stock_symbol}: {e}")
else:
    st.info("Enter a valid NSE stock symbol to see live data.")

st.caption("Data source: Yahoo Finance")
