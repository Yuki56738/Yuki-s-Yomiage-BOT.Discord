import datetime
import os


def log(arg):
    dt_now = datetime.datetime.now()
    path = './log/'
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    with open("./log/bot.log", "a") as f:
        f.write(str(dt_now) + ": " + str(arg) + "\n")

