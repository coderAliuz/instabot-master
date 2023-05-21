from instabot import Bot
import shutil
import os
import json
from json.decoder import JSONDecodeError

def followers_list(username,parol,name):
    bot=Bot()
    bot.reset_cache()
    try:
        os.remove(f'config/{username}_uuid_and_cookie.json')
        os.remove(f'config/{username}.checkpoint')
    except:pass
    try:
        bot.login(username=username,password=parol)
        followers=bot.get_user_following(user_id=name)
        with open("followers.json","w+") as fp:
            json.dump(followers, fp,indent=4)
        return True
    except:
        return False

# print(followers_list("rezerv.ali05", "Alisher01", "sariqbolashou_1mln"))

def following_lists(username,parol):
    bot=Bot()
    bot.reset_cache()
    try:
        os.remove(f'config/{username}_uuid_and_cookie.json')
        os.remove(f'config/{username}.checkpoint')
    except:pass
    try:
        with open("followers.json","r+") as fp:
            f=json.load(fp)
        try:
            bot.login(username=username,password=parol)
            bot.follow_users(user_ids=f)
            return True
        except:
            return False
    except JSONDecodeError:
        return False

# print(following_lists("rezerv.ali05", "Alisher01"))
