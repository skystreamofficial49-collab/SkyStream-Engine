import requests
import json
import time

# --- RAHUL BHAI KI MASTER CHABI (VERSION 32) ---
# Ye wahi URL hai jo abhi 'Webhook Set Ho Gaya' bol chuka hai.
BRIDGE_URL = "https://script.google.com/macros/s/AKfycbwUiOYzM6Mjp6rf2QJJ_WGhBGJkfDI7bAgMXDltQg6E9e7XOYyG8lqDuf4mTj36A6vr/exec"

def start_engine():
    # Hamara channel data jo Firebase mein jayega
    payload = {
        "pakistan": [
            {"name": "PTV Sports LIVE", "url": "https://raw.githubusercontent.com/Rahul-Bhai/links/main/ptv.m3u8"}
        ],
        "india": [
            {"name": "Star Sports 1 Hindi", "url": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"}
        ]
    }

    print(f"🚀 Signal bhej rahe hain: {time.strftime('%H:%M:%S')}")
    
    try:
        # Google Script ko data bhej rahe hain
        response = requests.post(BRIDGE_URL, json=payload, timeout=30)
        
        if response.status_code == 200:
            print("✅ SUCCESS: Signal Delivered! Bot check karein.")
        else:
            print(f"❌ Error: Status Code {response.status_code}")
            
    except Exception as e:
        print(f"❌ Connection Failed: {str(e)}")

if __name__ == "__main__":
    start_engine()
