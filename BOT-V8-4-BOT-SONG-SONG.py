
import asyncio
import os
from telegram import Bot
from telegram.constants import ParseMode

# === CẤU HÌNH CỦA BẠN ===
BOT_TOKEN = os.getenv("BOT_TOKEN", "8266700974:AAH..." )  # token con TungLamDo_003
# Điền ID 4 nhóm của bạn vào đây sau khi lấy được
CHANNELS = {
    "RUONG_THUONG": "-1002852762375",  # BOT_TUNGLAMDO - ID bạn vừa lấy được
    "RUONG_CUI": "-1002852762375",
    "BAG": "-1002852762375", 
    "RUONG_TREO": "-1002852762375",
}

# List live test - bạn thay bằng list 20k live sau
TARGETS = ["rosa_forev", "edc_fabii", "lisa__live"]

bot = Bot(token=BOT_TOKEN)

async def send_to_telegram(username, coins, viewers, ratio, box_type="BOX"):
    msg = f"""
🎁 {box_type} - {username}
- TT-ID > {username}
- ⏳ TIME: 01:40s
- 🎁 BOX: {coins}/25 👀 {viewers}
- ⚖️ Ratio: {ratio} xu
> https://www.tiktok.com/@{username}/live
"""
    try:
        # Hiện tại gửi vào 1 nhóm chính trước, sau chia 4 nhóm
        await bot.send_message(
            chat_id=CHANNELS["RUONG_THUONG"], 
            text=msg,
            parse_mode=ParseMode.MARKDOWN
        )
        print(f"Đã gửi {username} - {coins} xu")
    except Exception as e:
        print(f"Lỗi gửi: {e}")

async def fake_scan():
    """Bản test - sau này thay bằng quét thật TikTok"""
    print("Bot V8 - 4 BOT SONG SONG đang chạy...")
    while True:
        for user in TARGETS:
            # Giả lập có rương
            await send_to_telegram(user, 120, 55, 4.8)
            await asyncio.sleep(5)
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(fake_scan())
