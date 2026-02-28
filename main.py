import requests
import os

# GitHub Secrets se raste uthana
firebase_url = os.getenv('FIREBASE_DB_URL')
script_url = os.getenv('SCRIPT_URL')

def check_and_fix():
    print("🚀 Rahul Bhai, 1-Hour Checking Shuru ho gayi hai...")
    
    try:
        # 1. Firebase se data uthana
        response = requests.get(f"{firebase_url}.json")
        channels = response.json()
        
        if not channels:
            print("❌ Firebase khali mila!")
            return

        # 2. Har link ko pehre par rakhna
        for key, data in channels.items():
            name = data.get('name', key)
            url = data.get('url')

            if url:
                try:
                    # Link check karna
                    check = requests.get(url, timeout=7, stream=True)
                    if check.status_code == 200:
                        print(f"✅ {name}: Bilkul Mast Chal Raha Hai")
                    else:
                        # ⚠️ Dead link ki khabar dena (Hunter mode next update mein activate hoga)
                        msg = f"❌ Rahul Bhai, '{name}' dead mila (Status: {check.status_code}). Jaldi naya link dhoond raha hoon!"
                        requests.post(script_url, json={"message": msg})
                except:
                    msg = f"⚠️ Rahul Bhai, '{name}' connect nahi ho raha. Server down lag raha hai!"
                    requests.post(script_url, json={"message": msg})

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_and_fix()
