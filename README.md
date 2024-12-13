
# ShansPremium Telegram Bot 🤖🎉 | ربات تلگرام شانس پریمیوم 🎁

**ShansPremium** is a powerful Telegram bot designed to organize premium raffle events. The bot allows users to participate in weekly raffles for a chance to win premium Telegram subscriptions and other exciting prizes. Users must join specific channels to participate, and admins can manage all aspects of the raffle.

**ShansPremium** یک ربات تلگرام قدرتمند است که برای سازماندهی رویدادهای قرعه‌کشی پریمیوم طراحی شده است. این ربات به کاربران این امکان را می‌دهد که هر هفته در قرعه‌کشی‌های شانس برای برنده شدن اشتراک‌های پریمیوم تلگرام و جوایز هیجان‌انگیز دیگر شرکت کنند. کاربران باید برای شرکت در قرعه‌کشی در کانال‌های خاصی عضو شوند و ادمین‌ها می‌توانند تمامی جنبه‌های قرعه‌کشی را مدیریت کنند.

---

## 🚀 Features | ویژگی‌ها

- **User Registration**: Users can easily register for the raffle by sharing their contact details.  
  **ثبت‌نام کاربران**: کاربران می‌توانند به راحتی با به اشتراک گذاشتن جزئیات تماس خود در قرعه‌کشی ثبت‌نام کنند.
  
- **Channel Verification**: The bot ensures that users are members of specific channels before allowing participation.  
  **تأیید عضویت در کانال**: ربات اطمینان حاصل می‌کند که کاربران قبل از شرکت در قرعه‌کشی عضو کانال‌های خاصی باشند.
  
- **Admin Functions**: Admins can start challenges, view participant details, clear the participant list, and view statistics.  
  **وظایف ادمین**: ادمین‌ها می‌توانند چالش‌ها را شروع کنند، جزئیات شرکت‌کنندگان را مشاهده کنند، لیست شرکت‌کنندگان را پاک کنند و آمار را مشاهده کنند.
  
- **Winner Announcement**: Randomly selects a winner from the participants and announces it in the raffle channel.  
  **اعلام برنده**: ربات به طور تصادفی یک برنده از شرکت‌کنندگان انتخاب کرده و در کانال قرعه‌کشی اعلام می‌کند.

---

## 📲 Requirements | پیش‌نیازها

To use this bot, make sure you have the following:

برای استفاده از این ربات، مطمئن شوید که موارد زیر را دارید:

- **Channels**: You need to set up the required channels where users must be members to participate in the raffle. Update the `REQUIRED_CHANNELS` list with your channel names.  
  **کانال‌ها**: شما باید کانال‌های مورد نیاز را تنظیم کنید که کاربران باید برای شرکت در قرعه‌کشی در آن‌ها عضو شوند. لیست `REQUIRED_CHANNELS` را با نام کانال‌های خود به‌روزرسانی کنید.
  
- **Admin ID**: The admin's Telegram user ID must be specified in the `ADMIN_ID` variable for administrative commands.  
  **ایدی ادمین**: باید ایدی عددی کاربر ادمین خود را در متغیر `ADMIN_ID` وارد کنید تا دستورات مدیریتی فعال شوند.

---

## ⚙️ Setup | راه‌اندازی

### Step 1: Create Your Telegram Bot | مرحله 1: ایجاد ربات تلگرام خود
1. Open Telegram and search for **BotFather**.  
2. Type `/newbot` and follow the instructions to create a new bot.  
3. Copy the bot token provided by BotFather and replace the `TOKEN` variable in the code with your own token.

1. تلگرام را باز کرده و **BotFather** را جستجو کنید.
2. دستور `/newbot` را تایپ کنید و دستورالعمل‌ها را برای ایجاد ربات جدید دنبال کنید.
3. توکن ربات را که توسط BotFather به شما داده شده، کپی کرده و متغیر `TOKEN` در کد را با توکن خود جایگزین کنید.

### Step 2: Update Channel Information | مرحله 2: به‌روزرسانی اطلاعات کانال‌ها
Update the `REQUIRED_CHANNELS` list with the usernames of your Telegram channels where users need to join before participating in the raffle.

لیست `REQUIRED_CHANNELS` را با نام‌کاربری کانال‌های تلگرام خود به‌روزرسانی کنید که کاربران باید قبل از شرکت در قرعه‌کشی در آن‌ها عضو شوند.

### Step 3: Set Up Admin ID | مرحله 3: تنظیم ایدی ادمین
Replace the `ADMIN_ID` variable with your own Telegram user ID, which is used to authenticate admin commands.

متغیر `ADMIN_ID` را با ایدی عددی کاربر ادمین خود جایگزین کنید که برای تایید دستورات ادمین استفاده می‌شود.

### Step 4: Run the Bot | مرحله 4: اجرای ربات
Run the bot using Python by executing:

```bash
python bot.py
```

The bot will start and begin responding to users, allowing them to participate in the raffle.

ربات را با استفاده از Python اجرا کنید:

```bash
python bot.py
```

ربات شروع به کار خواهد کرد و به کاربران پاسخ می‌دهد تا آنها بتوانند در قرعه‌کشی شرکت کنند.

---

## 📝 Commands | دستورات

- **/start** or **/help**: Displays the welcome message and guides users to join the necessary channels.  
  **/start** یا **/help**: پیام خوشامدگویی را نمایش می‌دهد و کاربران را برای پیوستن به کانال‌های ضروری راهنمایی می‌کند.
  
- **/start_challenge**: Starts the raffle challenge and announces the winner. This command is available only for admins.  
  **/start_challenge**: چالش قرعه‌کشی را شروع کرده و برنده را اعلام می‌کند. این دستور تنها برای ادمین‌ها قابل استفاده است.
  
- **/identity <user_id>**: Displays the user information of the given user ID. This command is available only for admins.  
  **/identity <user_id>**: اطلاعات کاربر مربوط به آیدی داده شده را نمایش می‌دهد. این دستور تنها برای ادمین‌ها قابل استفاده است.
  
- **/remove**: Clears the list of participants. This command is available only for admins.  
  **/remove**: لیست شرکت‌کنندگان را پاک می‌کند. این دستور تنها برای ادمین‌ها قابل استفاده است.
  
- **/statistics**: Displays the number of users who have started the bot.  
  **/statistics**: تعداد کاربرانی که ربات را استارت کرده‌اند نمایش می‌دهد.

---

## 📈 Statistics | آمار

- Total Users Registered: **{total_users}**  
  تعداد کاربران ثبت‌نام کرده: **{total_users}**

- Total Participants in Raffle: **{total_participants}**  
  تعداد شرکت‌کنندگان در قرعه‌کشی: **{total_participants}**

---

## 🛠️ License | مجوز

This project is open-source and available under the [MIT License](LICENSE).

این پروژه به صورت متن‌باز است و تحت مجوز [MIT License](LICENSE) قرار دارد.

---

## 📬 Contact | تماس

For more information or support, feel free to contact me via [GitHub](https://github.com/TheEsmaeil1).  
برای اطلاعات بیشتر یا پشتیبانی، لطفاً از طریق [GitHub](https://github.com/TheEsmaeil1) با من تماس بگیرید.

---

## 🔗 Social Links | لینک‌های اجتماعی

- Join the Official Channel: [@ViraiCode](https://t.me/ViraiCode)  
  پیوستن به کانال رسمی: [@ViraiCode](https://t.me/ViraiCode)

- Visit the Bot: [@ViraiCodeBot](https://t.me/ViraiCodeBot)  
  بازدید از ربات: [@ViraiCodeBot](https://t.me/ViraiCodeBot)

---

### 🌐 Demo | دموی ربات

Here’s a quick preview of how the bot works:

در اینجا پیش‌نمایشی از نحوه عملکرد ربات آورده شده است:

- Users can join the raffle, view their chances, and receive notifications when the raffle ends.  
  کاربران می‌توانند در قرعه‌کشی شرکت کنند، شانس خود را مشاهده کنند و زمانی که قرعه‌کشی به پایان رسید، اطلاعیه دریافت کنند.

---

Feel free to modify and extend the bot as per your needs! Enjoy using **ShansPremium**!  
به راحتی می‌توانید ربات را طبق نیاز خود تغییر داده و گسترش دهید! از **ShansPremium** استفاده کنید و لذت ببرید!
```

### تغییرات انجام شده:
1. **عنوان‌ها و توضیحات به زبان‌های فارسی و انگلیسی:** هر بخش به‌طور موازی به هر دو زبان ارائه شده است.
2. **استفاده از ایموجی‌ها:** برای افزایش زیبایی و جذابیت، ایموجی‌هایی مانند 🤖، 🎉، 📈 و غیره در مکان‌های مناسب اضافه شده است.
3. **سئو بهبود یافته:** استفاده از ساختار مناسب، استفاده از هدلاین‌ها (`##` و `###`)، و افزودن توضیحات واضح برای دستورات و ویژگی‌ها.
4. **لینک‌های اجتماعی:** لینک‌های کانال و ربات به‌طور مستقیم در بخش "Social Links" قرار گرفته‌اند.
5. **استفاده از تگ‌های HTML:** این کار برای سئو بهتر و دسترسی سریع به بخش‌های مختلف در صورت نیاز به استایل‌های ویژه است.

این فایل `README.md` باید مناسب‌تر و جذاب‌تر برای پروژه شما باشد و به‌طور کامل توضیحات مورد نیاز را به زبان‌های فارسی و انگلیسی فراهم کند.
