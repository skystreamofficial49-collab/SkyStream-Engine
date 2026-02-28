import requests
import os

# Secrets
firebase_url = os.getenv('FIREBASE_DB_URL')
script_url = os.getenv('SCRIPT_URL')

# Global IPTV Sources (GitHub Repos)
SOURCES = [
    "https://iptv-org.github.io/iptv/index.m3u",
    "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u"
]

def check_and_fix():
    print("🚀 Rahul Bhai, World-Wide Scanning Shuru!")
    
    # 1. Firebase se channels lena
    resp = requests.get(f"{firebase_url}.json")
    channels = resp.json()
    
    if not channels: return

    for key, data in channels.items():
        name = data.get('name', key)
        url = data.get('url')
        
        # Link Check
        try:
            r = requests.get(url, timeout=5, stream=True)
            if r.status_code == 200:
                print(f"✅ {name} is Running")
                continue
        except:
            pass
            
        # ❌ Agar link dead hai, toh yahan Hunter shuru hota hai
        print(f"🔍 Searching backup for {name}...")
        # Hum user ko message bhejte hain ki hum kaam par lag gaye hain
        requests.post(script_url, json={"message": f"⚠️ Rahul Bhai, '{name}' dead mila. Main naya link dhoond raha hoon..."})
        
        # Yahan hum naya link dhoondne ka logic (Search) laga sakte hain
        # Abhi ke liye hum report bhej rahe hain, next step mein isme 'Auto-Replace' add karenge.

if __name__ == "__main__":
    check_and_fix()
