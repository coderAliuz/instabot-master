from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tgbot.misc import *
from tgbot.models import *
from tgbot.keyboards import *
from tgbot.instagram import *

async def follower_home(message: Message):
    await message.reply("Do'stlari ro'yxatini olish uchun Instagram username yuboring",reply_markup=back_kb)
    await followerState.name.set()

async def get_name(message: Message):
    name=message.text
    user=main_user()
    if name=="⬅️ Asosiy sahifaga":
        await message.answer("🔘 <b>Kerakli tugmani tanlang</b> ⤵️",reply_markup=home_kb)
        await homeState.home.set()
    elif user is not None:
        await message.reply("Obunachilarni olish boshlandi.\nBu jarayonda bot faoliyati to'xtatiladi.\nJarayon tugagach botdan foydalanish mumkin!!!",reply_markup=ReplyKeyboardRemove())
        username=user[0]
        parol=user[1]
        await followerState.other.set()
        followers=followers_list(username, parol, name)
        if followers:
            await message.answer(f"{name} obunachilari ro'yxati shakllantirildi")
            await message.answer("🔘 <b>Kerakli tugmani tanlang</b> ⤵️",reply_markup=home_kb)
            await homeState.home.set()
        else:
            await message.answer("Instagram bilan ulanishda xatolik!!!",reply_markup=back_kb)
        await followerState.name.set()    
    else:
        await message.reply("Asosiy hisob o'rnatilmagan.")
        await message.answer("🔘 <b>Kerakli tugmani tanlang</b> ⤵️",reply_markup=home_kb)
        await homeState.home.set()

async def following_home(message: Message):
    await followerState.other.set()
    await message.reply("Obuna bo'lish boshlandi.\nBu jarayonda bot faoliyati to'xtatiladi.\nJarayon tugagach botdan foydalanish mumkin!!!",reply_markup=ReplyKeyboardRemove())
    user=main_user()
    username=user[0]
    parol=user[1]
    await followerState.other.set()
    following=following_lists(username, parol)
    if following:
        await message.answer("Barcha obunachilarga obuna bo'lindi!!!")
    else:
        await message.answer("Instagram bilan ulanishda xatolik!!!")
    await message.answer("🔘 <b>Kerakli tugmani tanlang</b> ⤵️",reply_markup=home_kb)
    await homeState.home.set()

    
def register_follower(dp: Dispatcher):
    dp.register_message_handler(follower_home, text="Obunachilar olish", state=homeState.home, is_admin=True)
    dp.register_message_handler(following_home, text="Obuna bo'lish", state=homeState.home, is_admin=True)
    dp.register_message_handler(get_name,state=followerState.name,is_admin=True)
