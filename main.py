import requests
import json

# --- CONFIGURATION (Rahul Bhai ka naya setup) ---
TOKEN = "8511752027:AAHLZTCkDCXDSltZm_hhNzPDQHgKU0FuBaw"
CHAT_ID = "5545938511"
# Aapka URL jo screenshot mein dikh raha hai:
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbyz0pHO4EmbgHVbjnQ1IcYLrgt32YBrd-_o-hat7SZCpKQtgNAGI-g9kkQlCVONMFMC0w/exec"

def send_to_google_script(data):
    try:
        # Webhook ko activate karne ke liye pehle GET request
        requests.get(f"{WEBHOOK_URL}?setWebhook=true")
        
        # Phir data bhejne ke liye POST request
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 200:
            print("✅ Signal Sent! 'Ting' check kijiye.")
        else:
            print(f"❌ Error Code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error: {str(e)}")

def main():
    # Test Data: India aur Pakistan ke channels
    channels = {
        "india": [
            {"name": "Star Sports 1", "url": "https://example.com/ss1.m3u8"},
            {"name": "Sony Ten 3", "url": "https://example.com/st3.m3u8"}
        ],
        "pakistan": [
            {"name": "PTV Sports", "url": "https://example.com/ptv.m3u8"},
            {"name": "Ten Sports Pak", "url": "https://example.com/tensport.m3u8"}
        ]
    }
    
    print("🚀 SkyStream Engine Signal Bhej Raha Hai...")
    send_to_google_script(channels)

if __name__ == "__main__":
    main()
