import asyncio
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN", "")
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

async def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN .env faylida ko‘rsatilmagan.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
