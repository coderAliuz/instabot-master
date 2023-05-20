from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tgbot.misc import *
from tgbot.models import *
from tgbot.keyboards import *

async def admin_start(message: Message):
    await message.reply("Salom, admin!",reply_markup=home_kb)
    await homeState.home.set()

async def main_account(message: Message):
    await message.reply("Instagram username tanlang",reply_markup=username_kb(all_users()))
    await usermainState.user.set()

async def get_name(message: Message):
    name=message.text
    if name=="⬅️ Asosiy sahifaga":
        await message.answer("🔘 <b>Kerakli tugmani tanlang</b> ⤵️",reply_markup=home_kb)
        await homeState.home.set()
    elif name in all_users():
        await message.reply(f"Instagram <code>{name}</code> hisobiga o'tdi",reply_markup=home_kb)
        update_main(name)
        await homeState.home.set()
    else:
        await message.answer("Bunday hisob mavjud emas")

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(main_account,text="Asosiy hisob",state=homeState.home,is_admin=True)
    dp.register_message_handler(get_name,state=usermainState.user,is_admin=True)
