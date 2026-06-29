from pyrogram import Client
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

# استخدام اسم ثابت للجلسة بدلاً من الذاكرة المؤقتة
bot = Client(
    "musicbot", 
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

# تشغيل البوت مع دالة البدء
if __name__ == "__main__":
    bot.start()
    run()
