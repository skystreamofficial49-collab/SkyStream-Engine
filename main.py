import requests
import json
import time

# BRIDGE_URL: Ye aapka wahi V31 wala link hai jo Chrome mein Success hua hai
BRIDGE_URL = "https://script.google.com/macros/s/AKfycby0K-Gh1rx1L7wQhP-4GLSEsckSE2N9nyjEypV0cbj4BuRHmb1yrr01APVbn8v2BJIPVA/exec"

def run_engine():
    # Hamara channels data
    data = {
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
        response = requests.post(BRIDGE_URL, json=data, timeout=30)
        
        if response.status_code == 200:
            print("✅ SUCCESS: Signal Delivered! Bot check karein.")
        else:
            print(f"❌ Status Code: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    run_engine()
