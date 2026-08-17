
вчера 19:29
import sqlite3
yig'uv sexi bilan press sexi o'ynaydi
import os
...
2-payvandlash sexi va texnologiya chorak finalda 
shuni grafik qilib ber

Сформированное изображение


Редактировать


Сформированное изображение


Редактировать


Сформированное изображение: Футбольный турнир: путь в полуфинал


Редактировать


Сформированное изображение: Yarim Finalga Yo‘l Kurashlari


Редактировать


Сформированное изображение: Футбольный турнир: следующий этап определён


Редактировать

🏆⚽️ MUSOBAQANING KEYINGI BOSQICHI ANIQLANDI!

🇺🇿 Mustaqilligimizning 35 yilligi munosabati bilan tashkil etilgan futbol musobaqasida 12 ta jamoa ishtirok etdi va ular A hamda B qatorlarga ajratildi.

🔥 Yarim finalga to‘g‘ridan-to‘g‘ri yo‘llanma olgan jamoalar:

🅰️ A qator: ⚙️ Texnologiya jamoasi
🅱️ B qator: 🧑‍🏭 2-payvandlash sexi jamoasi

⚔️ CHORAK FINAL BAHSLARI:

🔵 Yig‘uv sexi 🆚 Press sexi
➡️ G‘olib Texnologiya jamoasiga qarshi yarim finalda maydonga tushadi.

🟢 Sifat bo‘limi 🆚 Bo‘yoqlash sexi-1
➡️ G‘olib 2-payvandlash sexi jamoasiga qarshi yarim finalda o‘ynaydi.

🏆 YARIM FINAL YO‘NALISHLARI:

Texnologiya 🆚 Yig‘uv/Press g‘olibi

2-payvandlash sexi 🆚 Sifat/Bo‘yoqlash-1 g‘olibi

🔥 Endi haqiqiy kurash boshlanadi!
⚽️ Kim final yo‘llanmasini qo‘lga kiritadi?

💪 Barcha jamoalarga omad va g‘alaba tilaymiz!

#UzAutoMotors #Futbol #Mustaqillik35 #Sport #YarimFinal #ChorakFinal


75e5a969-2860-4eb1-867c-68b7a987f535.png

2e178ff8-aeac-44c5-bf9f-113b24246586.png

78d37c03-8283-4eed-9c7c-b4dbaa798836.png

e126d1e0-6cd9-4527-9c5a-f8eabe8e950f.png

4f69783f-9eac-42cb-bdfd-0e5811d39eed.png
qaysi

19d2935d-e521-499c-8c9f-c340ef6fed50.png

1e2387fd-d5d7-40a8-8c40-db9cfa9fecc9.png

3e373a6b-e0b2-4559-ad49-c5b8c5aa3ff6.png

4e5ba1d4-79d4-4f3d-8eff-67ff6fb11a8f.png

2c9d3954-9122-40b9-8ec5-4954526f233f.png

cb3a3f91-857c-4797-a861-56dd9f445d74.png

38049a01-e607-4910-a6a6-aa209c03f948.png

Ha, xatoni ko‘rdim. 👍 Kodning o‘zida xato ko‘rinmayapti. Muammo pip paketni PyPI'dan yuklayotganda yuz bergan.

Logdagi asosiy xato:

too many 502 error responses

Ya'ni Render → PyPI serveriga ulanishda vaqtinchalik 502 xatolik bo‘lgan. Build failed shuning uchun chiqdi.

🟢 1-qadam — qayta Deploy qilamiz
Render sahifasining yuqori o‘ng tomonida:

Manual Deploy tugmasini bosing.

Keyin:

Deploy latest commit

ni tanlang.

🟢 2-qadam
Yangi deploy boshlanadi.

Logda yana:

Running build command
pip install -r requirements.txt
chiqadi.

Bu safar paketlar muvaffaqiyatli yuklanishi mumkin.

⚠️ Hozircha hech narsani o‘zgartirmang
BOT_TOKEN — o‘zgartirmang

COMPANY_NAME — o‘zgartirmang

WEBHOOK_SECRET — o‘zgartirmang

GitHub kodini — o‘zgartirmang

Faqat Manual Deploy → Deploy latest commit.

Agar yana 502 chiqsa, yana bir marta qayta deploy qilmaymiz — men requirements.txtni o‘zgartirib, paket versiyasini aniq belgilab beraman.

👉 Hozir Manual Deploy → Deploy latest commit ni bosing va natijasini yuboring.


62373aee-c262-4cfb-a355-340c89bcf4c2.png

Zo‘r! 🎉 Muammo hal bo‘ldi. Bu safar build muvaffaqiyatli yakunlangan.

Skrinshotda:

✅ Successfully installed...

✅ Build successful 🎉

✅ Deploying...

✅ Running 'python bot.py'

demak, bot hozir ishga tushish bosqichida.

Hozir hech narsani bosmang
⏳ 30–60 soniya kuting.

Keyin yuqoridagi holat:

Building → Live

bo‘lishi kerak.

Keyingi tekshiruv
Agar Live bo‘lsa, menga skrinshot yuboring.

Agar loglarda:

Application started

Listening on...

yoki boshqa yashil/muvaffaqiyatli xabar

chiqsa, bu ham yaxshi.

⚠️ Agar Error / Traceback / Failed chiqsa, aynan o‘sha joyning skrinshotini yuboring.

Hozirgi holat: bot serverga o‘rnatildi, faqat ishga tushishini kutyapmiz. 🚀


6ef4d83c-bbe3-49f9-9761-05a8df73d752.png

Ha, endi aniq sabab topildi. Sizdagi xato:

No open ports detected
Port scan timeout reached

Render botni ishga tushiryapti, lekin bot.py avval Telegram webhook'ni sozlashga urinib, portni keyin ochyapti. Render esa portni tezda ko‘rmagani uchun deployni to‘xtatyapti.

Buni tuzatamiz. Hozircha Render'da boshqa tugma bosmang.

1-QADAM — yangi bot.pyni yuklab oling
Men aynan shu xatoni tuzatib, bot.pyni tayyorladim:

Tuzatilgan bot.py — yuklab olish

2-QADAM — GitHub'ga kiring
GitHub → YOSHlar-HUB repository'siga kiring.

bot.pyni oching.

Yuqoridagi ✏️ Edit tugmasini bosing.

3-QADAM — eski kodni almashtiring
GitHub'dagi bot.py ichidagi barcha eski kodni o‘chiring.

Men bergan:

bot_render_fixed.py

faylini kompyuteringizda oching.

Undagi barcha kodni nusxalang va GitHub'dagi bot.pyga joylang.

⚠️ Fayl nomini bot.py qilib qoldiring.

4-QADAM — saqlash
GitHub sahifasining pastiga tushing.

Commit changes tugmasini bosing.

Shundan keyin GitHub'da bot.py yangilanadi.

5-QADAM — Render'ga qaytamiz
Render avtomatik ravishda GitHub'dagi yangi commitni ko‘radi.

Agar avtomatik deploy boshlanmasa:

Manual Deploy → Deploy latest commit

ni bosing.

Nima o‘zgaradi?
Yangi kod avval:

Render
   ↓
PORT 10000 ochiladi
   ↓
Render portni ko‘radi ✅
   ↓
Telegram webhook sozlanadi
   ↓
YOSHlar HUB ishlaydi 🤖
bo‘ladi.

Oldingi kodda esa webhook sozlash port ochilishidan oldin bajarilayotgan edi.

Hozir siz faqat 1–4-qadamlarni bajaring.
GitHub'dagi bot.py yangilangach, menga skrinshot yuboring. Men keyin siz bilan Render'da Deploy latest commit bosishdan boshlab davom etaman.


bot_render_fixed.py
Код


Библиотека
/
bot_render_fixed.py


import asyncio
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Update
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiohttp import web

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN", "")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "yoshlarhub-webhook-secret")
ADMIN_IDS = {int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip().isdigit()}
COMPANY = os.getenv("COMPANY_NAME", "UzAuto Motors AJ Xorazm viloyati filiali")

conn = sqlite3.connect("yoshlar_hub.db")
conn.row_factory = sqlite3.Row
conn.execute("""CREATE TABLE IF NOT EXISTS users(
 id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER UNIQUE, full_name TEXT,
 department TEXT, phone TEXT, created_at TEXT)""")
conn.execute("""CREATE TABLE IF NOT EXISTS announcements(
 id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, body TEXT, created_at TEXT)""")
conn.execute("""CREATE TABLE IF NOT EXISTS events(
 id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, date TEXT, place TEXT,
 created_at TEXT)""")
conn.execute("""CREATE TABLE IF NOT EXISTS registrations(
 id INTEGER PRIMARY KEY AUTOINCREMENT, event_id INTEGER, tg_id INTEGER,
 created_at TEXT, UNIQUE(event_id,tg_id))""")
conn.execute("""CREATE TABLE IF NOT EXISTS feedback(
 id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER, kind TEXT, text TEXT,
 status TEXT DEFAULT 'Yangi', created_at TEXT)""")
conn.commit()

bot = Bot(TOKEN)
dp = Dispatcher()

class Register(StatesGroup):
    full_name = State()
    department = State()
    phone = State()

class Feedback(StatesGroup):
    text = State()

def menu(admin=False):
    rows = [
        [InlineKeyboardButton(text="📢 E'lonlar", callback_data="ann")],
        [InlineKeyboardButton(text="📝 Tadbirga ro'yxatdan o'tish", callback_data="events")],
        [InlineKeyboardButton(text="💡 Taklif / Muammo", callback_data="feedback")],
        [InlineKeyboardButton(text="🏆 Sport musobaqalari", callback_data="sports")],
        [InlineKeyboardButton(text="👤 Profil", callback_data="profile")],
    ]
    if admin:
        rows.append([InlineKeyboardButton(text="⚙️ Admin panel", callback_data="admin")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

@dp.message(CommandStart())
async def start(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(
        f"🇺🇿 <b>YOSHlar HUB</b>\n\n{COMPANY}\n\n"
        "Yoshlar va xodimlar bilan ishlashning elektron platformasiga xush kelibsiz!",
        reply_markup=menu(m.from_user.id in ADMIN_IDS)
    )

@dp.callback_query(F.data == "profile")
async def profile(c: CallbackQuery):
    u = conn.execute("SELECT * FROM users WHERE tg_id=?", (c.from_user.id,)).fetchone()
    if not u:
        await c.message.answer("Profil topilmadi. /register buyrug‘i orqali ro‘yxatdan o‘ting.")
    else:
        await c.message.answer(f"👤 <b>Profil</b>\n\nF.I.Sh.: {u['full_name']}\nBo‘lim: {u['department']}\nTelefon: {u['phone']}")
    await c.answer()

@dp.message(Command("register"))
async def register(m: Message, state: FSMContext):
    await state.set_state(Register.full_name)
    await m.answer("F.I.Sh.ingizni kiriting:")

@dp.message(Register.full_name)
async def reg_name(m: Message, state: FSMContext):
    await state.update_data(full_name=m.text)
    await state.set_state(Register.department)
    await m.answer("Bo‘lim/sexingizni kiriting:")

@dp.message(Register.department)
async def reg_dep(m: Message, state: FSMContext):
    await state.update_data(department=m.text)
    await state.set_state(Register.phone)
    await m.answer("Telefon raqamingizni kiriting:")

@dp.message(Register.phone)
async def reg_phone(m: Message, state: FSMContext):
    d = await state.update_data(phone=m.text)
    conn.execute("""INSERT INTO users(tg_id,full_name,department,phone,created_at)
                    VALUES(?,?,?,?,?) ON CONFLICT(tg_id) DO UPDATE SET
                    full_name=excluded.full_name, department=excluded.department, phone=excluded.phone""",
                 (m.from_user.id,d["full_name"],d["department"],d["phone"],datetime.now().isoformat()))
    conn.commit()
    await state.clear()
    await m.answer("✅ Profilingiz saqlandi.", reply_markup=menu(m.from_user.id in ADMIN_IDS))

@dp.callback_query(F.data == "ann")
async def announcements(c: CallbackQuery):
    rows = conn.execute("SELECT * FROM announcements ORDER BY id DESC LIMIT 10").fetchall()
    if not rows:
        await c.message.answer("Hozircha e'lonlar mavjud emas.")
    else:
        await c.message.answer("\n\n".join([f"📢 <b>{r['title']}</b>\n{r['body']}" for r in rows]))
    await c.answer()

@dp.callback_query(F.data == "events")
async def events(c: CallbackQuery):
    rows = conn.execute("SELECT * FROM events ORDER BY id DESC LIMIT 20").fetchall()
    if not rows:
        await c.message.answer("Hozircha tadbirlar kiritilmagan.")
    else:
        kb=[]
        for r in rows:
            kb.append([InlineKeyboardButton(text=f"📝 {r['title']}", callback_data=f"join:{r['id']}")])
        await c.message.answer("Tadbirni tanlang:", reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))
    await c.answer()

@dp.callback_query(F.data.startswith("join:"))
async def join_event(c: CallbackQuery):
    eid=int(c.data.split(":")[1])
    try:
        conn.execute("INSERT INTO registrations(event_id,tg_id,created_at) VALUES(?,?,?)",
                     (eid,c.from_user.id,datetime.now().isoformat()))
        conn.commit()
        await c.message.answer("✅ Tadbirga ro‘yxatdan o‘tishingiz qabul qilindi.")
    except sqlite3.IntegrityError:
        await c.message.answer("ℹ️ Siz bu tadbirga avval ro‘yxatdan o‘tgansiz.")
    await c.answer()

@dp.callback_query(F.data == "feedback")
async def feedback_start(c: CallbackQuery, state: FSMContext):
    await state.set_state(Feedback.text)
    await c.message.answer("💡 Taklif yoki muammoingizni batafsil yozing.\n\nMasalan: muammo, taklif, yechim yoki murojaat.")
    await c.answer()

@dp.message(Feedback.text)
async def feedback_save(m: Message, state: FSMContext):
    conn.execute("INSERT INTO feedback(tg_id,kind,text,created_at) VALUES(?,?,?,?)",
                 (m.from_user.id,"Taklif/Muammo",m.text,datetime.now().isoformat()))
    conn.commit()
    await state.clear()
    await m.answer("✅ Murojaatingiz qabul qilindi. Mas'ul xodim ko‘rib chiqadi.",
                    reply_markup=menu(m.from_user.id in ADMIN_IDS))

@dp.callback_query(F.data == "sports")
async def sports(c: CallbackQuery):
    await c.message.answer(
        "🏆 <b>SPORT MODULI</b>\n\n"
        "⚽️ Mini-futbol\n💪 Arqon tortish\n🏋️ Tosh ko‘tarish\n♟️ Shaxmat\n"
        "⚫ Shashka\n🏓 Stol tennisi\n🏃 Yugurish\n🎯 Darts\n\n"
        "Keyingi bosqichda bu bo‘limga jamoa ro‘yxati, qur'a, jadval va natijalar qo‘shiladi."
    )
    await c.answer()

@dp.callback_query(F.data == "admin")
async def admin(c: CallbackQuery):
    if c.from_user.id not in ADMIN_IDS:
        return await c.answer("Ruxsat yo‘q.", show_alert=True)
    u=conn.execute("SELECT COUNT(*) n FROM users").fetchone()["n"]
    f=conn.execute("SELECT COUNT(*) n FROM feedback WHERE status='Yangi'").fetchone()["n"]
    e=conn.execute("SELECT COUNT(*) n FROM events").fetchone()["n"]
    await c.message.answer(
        f"⚙️ <b>ADMIN PANEL</b>\n\n"
        f"👥 Foydalanuvchilar: {u}\n💡 Yangi murojaatlar: {f}\n📅 Tadbirlar: {e}\n\n"
        "Buyruqlar:\n"
        "/add_announcement — e'lon qo‘shish\n"
        "/add_event — tadbir qo‘shish\n"
        "/feedbacks — murojaatlarni ko‘rish\n"
        "/stats — statistika"
    )
    await c.answer()

@dp.message(Command("add_announcement"))
async def add_ann(m: Message):
    if m.from_user.id not in ADMIN_IDS: return
    await m.answer("Format: /add_announcement Sarlavha | Matn")

@dp.message(Command("add_event"))
async def add_event(m: Message):
    if m.from_user.id not in ADMIN_IDS: return
    await m.answer("Format: /add_event Nomi | Sana | Joy")

@dp.message(Command("stats"))
async def stats(m: Message):
    if m.from_user.id not in ADMIN_IDS: return
    vals = {
        "Foydalanuvchilar": conn.execute("SELECT COUNT(*) n FROM users").fetchone()["n"],
        "Tadbirlar": conn.execute("SELECT COUNT(*) n FROM events").fetchone()["n"],
        "Ro‘yxatdan o‘tishlar": conn.execute("SELECT COUNT(*) n FROM registrations").fetchone()["n"],
        "Murojaatlar": conn.execute("SELECT COUNT(*) n FROM feedback").fetchone()["n"],
    }
    await m.answer("📊 <b>YOSHlar HUB statistikasi</b>\n\n" + "\n".join(f"• {k}: {v}" for k,v in vals.items()))

@dp.message(Command("feedbacks"))
async def feedbacks(m: Message):
    if m.from_user.id not in ADMIN_IDS: return
    rows=conn.execute("SELECT * FROM feedback ORDER BY id DESC LIMIT 20").fetchall()
    if not rows: return await m.answer("Murojaatlar yo‘q.")
    await m.answer("\n\n".join(f"#{r['id']} | {r['status']}\n{r['text']}" for r in rows))

async def health(request):
    return web.Response(text="YOSHlar HUB is running")

async def webhook(request):
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != WEBHOOK_SECRET:
        return web.Response(status=403, text="Forbidden")
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return web.Response(text="OK")

async def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN .env faylida ko‘rsatilmagan.")

    port = int(os.getenv("PORT", "10000"))
    external_url = os.getenv("RENDER_EXTERNAL_URL", "").rstrip("/")
    if not external_url:
        raise RuntimeError("RENDER_EXTERNAL_URL Render tomonidan berilmagan.")

    webhook_url = f"{external_url}/webhook"

    # Start the HTTP server FIRST so Render detects the port immediately.
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)
    app.router.add_post("/webhook", webhook)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"YOSHlar HUB running on port {port}")

    # Configure Telegram webhook after the HTTP port is already listening.
    for attempt in range(1, 6):
        try:
            await bot.set_webhook(
                url=webhook_url,
                secret_token=WEBHOOK_SECRET,
                drop_pending_updates=True
            )
            print(f"Telegram webhook set: {webhook_url}")
            break
        except Exception as exc:
            print(f"Webhook setup attempt {attempt}/5 failed: {exc}")
            if attempt < 5:
                await asyncio.sleep(5)

    try:
        await asyncio.Event().wait()
    finally:
        await bot.delete_webhook(drop_pending_updates=False)
        await runner.cleanup()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
