import streamlit as st
import requests
import base64

# API Base URL
API_BASE_URL = "https://neurotrade-api.onrender.com"  # Replace with your actual API URL

st.set_page_config(page_title="NeuroTrade - AI Trading Platform", layout="wide")

st.title("📈 NeuroTrade - AI-Powered Smart Trading")
st.sidebar.header("Navigation")
option = st.sidebar.radio("Go to", ["Home", "Candlestick Charts", "Paper Trading", "Sentiment Analysis", "Portfolio Analytics"])

if option == "Home":
    st.markdown("Welcome to **NeuroTrade**, an AI-powered trading assistant!")
    st.markdown("Select a feature from the sidebar to explore the app.")

elif option == "Candlestick Charts":
    st.header("📊 Stock Candlestick Chart")
    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    if st.button("Generate Chart"):
        response = requests.get(f"{API_BASE_URL}/candlestick/{symbol}")
        if response.status_code == 200:
            data = response.json()
            chart = base64.b64decode(data["chart"])
            st.image(chart, caption=f"{symbol} Candlestick Chart")
        else:
            st.error("Failed to retrieve chart. Please check the stock symbol.")

elif option == "Paper Trading":
    st.header("📈 Start Paper Trading")
    username = st.text_input("Username:")
    stock_symbol = st.text_input("Stock Symbol:")
    quantity = st.number_input("Quantity:", min_value=1, step=1)
    purchase_price = st.number_input("Purchase Price:", min_value=0.0, step=0.01)
    if st.button("Execute Trade"):
        trade_data = {
            "username": username,
            "stock_symbol": stock_symbol,
            "quantity": quantity,
            "purchase_price": purchase_price
        }
        response = requests.post(f"{API_BASE_URL}/paper_trade", json=trade_data)
        if response.status_code == 200:
            st.success("Trade successfully executed!")
        else:
            st.error("Trade execution failed.")

elif option == "Sentiment Analysis":
    st.header("📰 Stock Sentiment Analysis")
    if st.button("Get Sentiment Analysis"):
        response = requests.get(f"{API_BASE_URL}/sentiment")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
        else:
            st.error("Failed to fetch sentiment analysis.")

elif option == "Portfolio Analytics":
    st.header("📊 Portfolio Analytics")
    if st.button("Analyze Portfolio"):
        response = requests.get(f"{API_BASE_URL}/portfolio_analytics")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
        else:
            st.error("Failed to fetch portfolio analytics.")
