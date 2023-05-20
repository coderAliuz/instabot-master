from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove

def username_kb(but):
    keyboard=ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    keyboard.add(*but).row("⬅️ Asosiy sahifaga")
    return keyboard

home_kb=ReplyKeyboardMarkup(
    [
        [
            "Obuna bo'lish",
            "Hisob qo'shish",
    ],
        [
            "Obunachilar olish",
            "Asosiy hisob"
        ]
    ],resize_keyboard=True
)
back_kb=ReplyKeyboardMarkup(
    [["⬅️ Asosiy sahifaga"]],resize_keyboard=True
)
