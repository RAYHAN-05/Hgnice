import requests
import time
import datetime
import random

# কনফিগারেশন
BOT_TOKEN = '8564357681:AAHERKPgVWgxf9ecRKQrMqeIHmJnn6IBX0c'
CHAT_ID = '-1002396116905'

def send_signal(period, res, num):
    message = (
        f"🚀 *𝑹𝑺_𝑹𝑨𝒀𝑯𝑨𝑵 𝑽𝑰𝑷 𝑺𝑰𝑮𝑵𝑨𝑳* 🤖\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💎 *𝑴𝑨𝑹𝑲𝑬𝑻:* `WINGO 30S`\n"
        f"📅 *𝑷𝑬𝑹𝑰𝑶𝑫:* `{period}` \n\n"
        f"🔮 *𝑷𝑹𝑬𝑫𝑰𝑪𝑻𝑰𝑶𝑵:* *{res} ({num})*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except:
        pass

def main():
    last_period = ""
    while True:
        now = datetime.datetime.utcnow()
        date_str = now.strftime("%Y%m%d")
        seconds = (now.hour * 3600) + (now.minute * 60) + now.second
        slot = (seconds // 30) + 1
        period = f"{date_str}1000{str(slot).zfill(5)}"
        remaining = 30 - (now.second % 30)

        if remaining >= 27 and period != last_period:
            is_big = random.choice([True, False])
            res = "BIG" if is_big else "SMALL"
            num = random.randint(5, 9) if is_big else random.randint(0, 4)
            send_signal(period, res, num)
            last_period = period
        time.sleep(1)

if __name__ == "__main__":
    main()