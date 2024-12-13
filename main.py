import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

TOKEN = 'token' #توکن خود را وارد کنید
bot = telebot.TeleBot(TOKEN)

# لیست ایدی کانال های را وارد کنید و همچنین ربات باید در تمام کانال ها عضو باشد
REQUIRED_CHANNELS = [
    '@YourChannel1',
    '@YourChannel2',
    '@YourChannel3',
    '@YourChannel4',
    '@YourChannel5',
]

ADMIN_ID = 6420452304 # ایدی عددی ادمین
RAFFLE_CHANNEL_ID = -1002184468533 # ایدی عددی کانال اصلی اطلاعیه
participants = []
all_users = set()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('🎉 شرکت در قرعه کشی', request_contact=True)
button2 = KeyboardButton('📣 کانال ما')
button3 = KeyboardButton('🔅 راهنما')
keyboard.add(button1)
keyboard.add(button2, button3)

def is_user_in_channels(user_id):
    for channel in REQUIRED_CHANNELS:
        try:
            status = bot.get_chat_member(channel, user_id).status
            if status not in ['member', 'administrator', 'creator']:
                return False
        except Exception:
            return False
    return True

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.from_user.id
    all_users.add(user_id)
    if not is_user_in_channels(user_id):
        bot.reply_to(message, "📢 برای استفاده از ربات، ابتدا باید در کانال‌های زیر عضو شوید:\n" +
                     '\n'.join(REQUIRED_CHANNELS))
        return

    bot.reply_to(message, """🎉 به دنیای شانس و هیجان خوش آمدید!

🔥 فرصت استثنایی برای شما:
با عضویت در کانال و استفاده از بات ما، هر هفته شانس برنده شدن اشتراک پریمیوم تلگرام و جوایز ویژه را خواهید داشت!

📌 چرا همین حالا شروع نکنید؟
1️⃣ عضو شوید.
2️⃣ در بات ثبت‌نام کنید.
3️⃣ و منتظر خبرهای هیجان‌انگیز ما باشید!

✨ ما آماده‌ایم تا شما را برنده کنیم!
🌟 بهترین‌ها منتظر شماست!""", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '📣 کانال ما')
def handle_channel(message):
    bot.reply_to(message, "- ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ : @ViraiCode") # ایدی کانال جایگزین شود

@bot.message_handler(func=lambda message: message.text == '🔅 راهنما')
def handle_help(message):
    caption = f"""قرعه‌کشی شانس پریمیوم 🎉

🎁 شانس شما برای برنده شدن اشتراک پریمیوم تلگرام!

🔥هر هفته قرعه‌کشی هیجان‌انگیز و جوایز ویژه.

📲 فقط با عضویت و مشارکت شما!

🆔 @ViraiCode - عضو بمونید
🤖 @ViraiCode - ثبت نام"""
    
    with open('logo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo, caption=caption)

@bot.message_handler(content_types=['contact'])
def handle_raffle(message):
    user_id = message.from_user.id
    if not is_user_in_channels(user_id):
        bot.reply_to(message, "📢 برای استفاده از ربات، ابتدا باید در کانال‌های زیر عضو شوید:\n" +
                     '\n'.join(REQUIRED_CHANNELS))
        return

    if user_id not in participants:
        participants.append(user_id)
        contact = message.contact
        bot.send_message(RAFFLE_CHANNEL_ID, f"کاربر {user_id} در قرعه کشی شرکت کرد.")
        bot.send_message(ADMIN_ID, f"نام: {contact.first_name}\nیوزرنیم: @{message.from_user.username}\nایدی عددی: {user_id}\nشماره تلفن: {contact.phone_number}")
        bot.reply_to(message, "🎉 شما با موفقیت در قرعه‌کشی ثبت نام کردید!")
    else:
        bot.reply_to(message, "ℹ️ شما قبلاً در قرعه‌کشی شرکت کرده‌اید.")

@bot.message_handler(commands=['start_challenge'])
def start_challenge(message):
    if message.from_user.id != ADMIN_ID:
        return

    if participants:
        winner = random.choice(participants)
        bot.send_message(RAFFLE_CHANNEL_ID, f"🎉 کاربر با ایدی عددی {winner} برنده این هفته قرعه کشی شد!")
        participants.clear()
    else:
        bot.reply_to(message, "⚠️ لیست شرکت‌کنندگان خالی است!")

@bot.message_handler(commands=['identity'])
def get_identity(message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])

        if user_id in participants:
            try:
                user = bot.get_chat_member(message.chat.id, user_id).user
                contact_info = "شماره تلفن: ..."
                username = f"@{user.username}" if user.username else "یوزرنیم موجود نیست"
                first_name = user.first_name if user.first_name else "نام موجود نیست"
                last_name = user.last_name if user.last_name else "نام خانوادگی موجود نیست"

                bot.reply_to(message, f"""ایدی عددی: {user_id}
یوزرنیم: {username}
نام: {first_name} {last_name}
{contact_info}""")
            except telebot.apihelper.ApiTelegramException:
                bot.reply_to(message, "⚠️ کاربر در این چت موجود نیست یا خطای دیگری رخ داده است.")
        else:
            bot.reply_to(message, "⚠️ کاربر یافت نشد.")
    except (IndexError, ValueError):
        bot.reply_to(message, "⚠️ فرمت دستور اشتباه است. دستور صحیح: /identity <id>")

@bot.message_handler(commands=['remove'])
def remove_participants(message):
    if message.from_user.id != ADMIN_ID:
        return

    participants.clear()
    bot.reply_to(message, "✅ لیست شرکت‌کنندگان پاک شد.")

@bot.message_handler(commands=['statistics'])
def statistics(message):
    if message.from_user.id != ADMIN_ID:
        return

    bot.reply_to(message, f"تعداد کاربران استارت شده: {len(all_users)}")

print("ربات شروع به کار کرد...")
bot.polling()
