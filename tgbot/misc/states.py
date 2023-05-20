from aiogram.dispatcher.filters.state import State,StatesGroup

class homeState(StatesGroup):
    home=State()

class usernameState(StatesGroup):
    name=State()
    password=State()

class usermainState(StatesGroup):
    user=State()

class followerState(StatesGroup):
    name=State()
    other=State()