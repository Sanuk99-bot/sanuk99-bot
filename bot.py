import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = '7615711374:AAGLz9iXyxyUQEMgnya1sORoWn_xVBNpiso'

# List of available banner image URLs
banner_images = [
    	'https://sanuk99-public.s3.ap-southeast-1.amazonaws.com/backend/production/1733405140359/5468/SANUK_Banner_01_EN_1900x600.png',
	'https://sanuk99-public.s3.ap-southeast-1.amazonaws.com/backend/production/1734163089499/6370/SANUK_Banner_05_EN_1900x600.png',
	'https://sanuk99-public.s3.ap-southeast-1.amazonaws.com/backend/production/1734161736543/1617/SANUK_Banner_03_EN_1900x600.png',
	'https://sanuk99-public.s3.ap-southeast-1.amazonaws.com/backend/production/1734161612166/5067/SANUK_Banner_02_EN_1900x600.png',
	'https://sanuk99-public.s3.ap-southeast-1.amazonaws.com/backend/production/1734162996681/7601/SANUK_Banner_04_EN_1900x600.png',
]

# ฟังก์ชันข้อความต้อนรับ (พร้อมภาพต้อนรับและจุดขาย)
async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # เลือกรูปภาพแบบสุ่มจากรายชื่อภาพ
    welcome_image_url = random.choice(banner_images)

    # แป้นพิมพ์สำหรับ Inline Buttons
    keyboard = [
        [InlineKeyboardButton("💰 สมัครสมาชิก", url="https://www.sanuk99.com/th-th/register?aff=2aaeda9552")],
        [InlineKeyboardButton("🎁 โปรโมชั่น", url="https://www.sanuk99.com/th-th/promotions")],
        [InlineKeyboardButton("🛎 ติดต่อแอดมิน", url="https://line.me/ti/p/~@Sanuk99")],
        [InlineKeyboardButton("🏆 ช่องทางทางการ", url="https://t.me/Sanuk99")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ส่งภาพต้อนรับ
    await update.message.reply_photo(
        photo=welcome_image_url,
        caption=(
            "🎉 ยินดีต้อนรับสู่ *Sanuk99* 🎰\n"
            "แหล่งรวมความสนุกของสล็อต PG ที่คุณห้ามพลาด!\n\n"
            "🌟 **ทำไมต้องเลือก Sanuk99?**\n"
            "- 💰 **โบนัสต้อนรับสุดคุ้ม** สำหรับสมาชิกใหม่\n"
            "- 🎁 **โปรโมชั่นรายวัน** รับได้ไม่อั้น\n"
            "- 🏆 **เกม PG สล็อต** คัดสรรมาอย่างดี เล่นง่าย โบนัสแตกบ่อย\n"
            "- 🛎 **บริการลูกค้าตลอด 24 ชม.** พร้อมช่วยเหลือทุกปัญหา\n"
            "- 🏅 **ระบบฝาก-ถอน ออโต้** รวดเร็ว ปลอดภัย\n\n"
            "👇 เลือกเมนูด้านล่างเพื่อเริ่มต้นความสนุก:"
        ),
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ฟังก์ชันที่ถูกเรียกเมื่อผู้ใช้พิมพ์ /start
    app.add_handler(CommandHandler("start", send_welcome))

    # ฟังก์ชันที่ถูกเรียกเมื่อผู้ใช้พิมพ์ข้อความใดๆ
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_welcome))

    app.run_polling()
