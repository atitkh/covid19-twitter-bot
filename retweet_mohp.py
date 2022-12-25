import main_bot_api as bot
import time

while True:
    bot.fav_retweet_user(bot.api, 'mohpnep')
    time.sleep(5)