from instabot import Bot
import shutil
import json
from json.decoder import JSONDecodeError
path=("D:/bot/instabot-master/config")


def followers_list(username,parol,name):
    bot=Bot()
    try:
        bot.login(username=username,password=parol)
        # followers=bot.get_user_followers(user_id=name)
        # with open("followers.json","w+") as fp:
        #     json.dump(followers, fp)
        bot.logout()
        shutil.rmtree(path)c
        return True
    except:
        bot.logout()
        shutil.rmtree(path)
        return False

print(followers_list("rezerv.ali05", "Alisher01", "coder_ali_uz"))

def following_lists():
    bot=Bot()
    try:
        with open("followers.json","w+") as fp:
            f=json.load(fp)
        try:
            bot.login(username=username,password=parol)
            bot.follow_users(user_ids=f)
            bot.logout()
            shutil.rmtree(path)
            return True
        except:
            bot.logout()
            shutil.rmtree(path)
            return False
    except JSONDecodeError:
        bot.logout()
        shutil.rmtree(path)
        return False

