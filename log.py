import datetime

dt_now = datetime.datetime.now()


def log(arg):
    global dt_now
    with open("./log/bot.log", "a") as f:
        f.write(str(dt_now) + ": " + str(arg) + "\n")
