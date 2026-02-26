import requests
import json

# --- CONFIGURATION (Rahul Bhai ka Setup) ---
# Ye wahi link hai jo aapne abhi Google Script se nikaala hai
BRIDGE_URL = "https://script.google.com/macros/s/AKfycbyFiE8c1fXLKeO-RPpoxloDBEvEJG2MrYUmIeCj74z6rlh7ccQgeHmjT548v09_1T8trA/exec"

def start_engine():
    print("🚀 SkyStream Engine Shuru Ho Raha Hai...")
    
    # Fake Data for Testing (India aur Pakistan ke channels)
    data = {
        "india": [
            {"name": "Star Sports 1", "url": "http://example.com/ss1"},
            {"name": "Sony Ten 3", "url": "http://example.com/st3"}
        ],
        "pakistan": [
            {"name": "PTV Sports", "url": "http://example.com/ptv"},
            {"name": "Ten Sports PK", "url": "http://example.com/tenpk"}
        ]
    }
    
    try:
        print("📡 Signal Bhej Raha Hoon Google Script (Bridge) Ko...")
        response = requests.post(BRIDGE_URL, json=data)
        
        if response.status_code == 200:
            print("✅ Signal Pahunch Gaya! Bot Ting Karega.")
        else:
            print(f"❌ Error: Script ne jawab nahi diya. Code: {response.status_code}")
            
    except Exception as e:
        print(f"⚠️ Connection Fail: {str(e)}")

if __name__ == "__main__":
    start_engine()
