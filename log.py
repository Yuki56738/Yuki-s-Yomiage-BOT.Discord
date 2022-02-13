import datetime
import os

dt_now = datetime.datetime.now()
def log(arg):
  global dt_now
  path = './log/'
  if os.path.exists(path):
      pass
  else:
      os.mkdir(path)
  with open("./log/bot.log", "a")as f:
    f.write(str(dt_now) + ": " + str(arg) + "\n")

