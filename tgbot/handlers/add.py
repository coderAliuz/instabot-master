from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tgbot.misc import *
from tgbot.models import *
from tgbot.keyboards import *

async def add_account(message: Message):
    await message.reply("Instagram username yuboring",reply_markup=back_kb)
    await usernameState.name.set()

async def get_name(message: Message,state:FSMContext):
    name=message.text
    await state.update_data(name=name)
    await message.reply(f"Instagram {name} parolini yuboring")
    await usernameState.next()

async def get_parol(message: Message,state:FSMContext):
    parol=message.text
    data=await state.get_data()
    name=data['name']
    user_add(name,parol)
    await message.reply("Instagram hisob ma'lumoti saqlandi")
    await message.answer("🔘 <b>Kerakli tugmani tanlang</b> ⤵️",reply_markup=home_kb)
    await homeState.home.set()

async def to_back(message: Message):
    await message.answer("🔘 <b>Kerakli tugmani tanlang</b> ⤵️",reply_markup=home_kb)
    await homeState.home.set()

def register_add_user(dp: Dispatcher):
    dp.register_message_handler(add_account,text="Hisob qo'shish",state=homeState.home,is_admin=True)
    dp.register_message_handler(to_back,text="⬅️ Asosiy sahifaga",state=usernameState,is_admin=True)
    dp.register_message_handler(get_name,state=usernameState.name,is_admin=True)
    dp.register_message_handler(get_parol,state=usernameState.password,is_admin=True)
