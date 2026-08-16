import requests
import time
import json
from datetime import datetime

def fetch_btc_price():
    """Fetch latest BTC/USDT spot price from Binance"""
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        price = float(data['price'])
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "symbol": "BTCUSDT",
            "price": price,
            "source": "Binance"
        }
        
        print(json.dumps(log_entry))
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching BTC price: {e}")

if __name__ == "__main__":
    print("Starting BTC/USDT price bot...")
    while True:
        fetch_btc_price()
        time.sleep(300)  # 5 minutes
