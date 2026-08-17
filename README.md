# YOSHlar HUB — Telegram bot

UzAuto Motors AJ Xorazm viloyati filiali uchun yoshlar va xodimlar bilan ishlashni elektronlashtirishga mo‘ljallangan Telegram bot namunasi.

## Imkoniyatlar
- E'lonlarni yuborish
- Tadbirlar uchun ro‘yxatdan o‘tish
- Muammo/taklif qabul qilish
- Sport musobaqalariga ro‘yxatga olish
- Admin orqali foydalanuvchilar va murojaatlarni ko‘rish
- Ma'lumotlarni SQLite bazasida saqlash

## Ishga tushirish
1. Python 3.11+ o‘rnating.
2. `pip install -r requirements.txt`
3. `.env.example` faylidan `.env` yarating.
4. Telegram @BotFather orqali bot ochib, tokenni `.env` ga yozing.
5. O‘z Telegram ID'ingizni `ADMIN_IDS` ga yozing.
6. `python bot.py` buyrug‘i bilan ishga tushiring.

## Muhim
Bot tokenini hech kimga bermang. Ishlab chiqarish muhitida server/VPS va muntazam backup tavsiya qilinadi.
