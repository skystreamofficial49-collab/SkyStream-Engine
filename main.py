import requests
import os

# GitHub Secrets se data uthana
firebase_url = os.getenv('FIREBASE_DB_URL')
script_url = os.getenv('SCRIPT_URL')

def check_links():
    print("🚀 Rahul Bhai, Checking shuru ho rahi hai...")
    
    # 1. Firebase se channels ka data lena
    try:
        # Hum .json lagate hain taaki Firebase data de sake
        response = requests.get(f"{firebase_url}.json")
        channels = response.json()
        
        if not channels:
            print("❌ Firebase khali mila!")
            return

        # 2. Har channel ko check karna
        for key, data in channels.items():
            # Agar data list mein hai ya direct dict mein
            channel_name = data.get('name', key)
            url = data.get('url')

            if url:
                try:
                    # Link ko check karna (5 second ka time)
                    check = requests.get(url, timeout=5, stream=True)
                    if check.status_code == 200:
                        print(f"✅ {channel_name}: OK")
                    else:
                        # Dead link ki khabar Google Script ko bhejna
                        msg = f"❌ Rahul Bhai, '{channel_name}' dead ho gaya! (Status: {check.status_code})"
                        requests.post(script_url, json={"message": msg})
                except:
                    msg = f"⚠️ Rahul Bhai, '{channel_name}' ka link connect nahi ho raha!"
                    requests.post(script_url, json={"message": msg})

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_links()
