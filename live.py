import streamlit as st
import yfinance as yf
import pandas as pd
import time

st.set_page_config(page_title="Indian Stock Dashboard", layout="wide")
st.title("📊 Live Indian Stock Market Dashboard")

# --- Session state to store searched stocks ---
if "stocks_list" not in st.session_state:
    st.session_state["stocks_list"] = []

# --- Input to search/add stock ---
new_stock = st.text_input(
    "Enter NSE Stock Symbol (e.g., RELIANCE.NS, TCS.NS, INFY.NS):"
).upper().strip()

if st.button("Add Stock") and new_stock:
    if new_stock not in st.session_state["stocks_list"]:
        st.session_state["stocks_list"].append(new_stock)

# --- Display all searched stocks ---
stocks = st.session_state["stocks_list"]

if stocks:
    data_list = []
    charts = []

    for symbol in stocks:
        try:
            # Fetch 1-day 1-min data
            data = yf.download(symbol, period="1d", interval="1m")
            if not data.empty:
                last_price = float(data["Close"].iloc[-1])
                prev_price = float(data["Close"].iloc[-2]) if len(data) > 1 else last_price
                change = last_price - prev_price
                delta_val = float(round(change, 2))
                volume = int(data["Volume"].iloc[-1])

                data_list.append({
                    "Stock": symbol.replace(".NS", ""),
                    "Price (₹)": round(last_price, 2),
                    "Change (₹)": delta_val,
                    "Volume": volume
                })

                charts.append((symbol.replace(".NS", ""), data["Close"]))

            else:
                st.warning(f"No data available for {symbol}.")
        except Exception as e:
            st.warning(f"Error fetching {symbol}: {e}")

    # Show table of all stocks
    if data_list:
        df = pd.DataFrame(data_list)
        st.subheader("Stock Overview")
        st.dataframe(df)

    # Show line chart for each stock
    for name, series in charts:
        st.subheader(f"Price chart: {name}")
        st.line_chart(series)

    # Auto-refresh every 60 seconds
    st.caption("Dashboard auto-refreshes every 60 seconds.")
    time.sleep(60)
    st.experimental_rerun()
else:
    st.info("Search and add NSE stock symbols to see live data.")

st.caption("Data source: Yahoo Finance")
