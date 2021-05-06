#!/usr/bin/python3
#ライブラリのロード
import discord
from discord.ext import commands
import subprocess
import ffmpeg
from voice_generator import creat_WAV
from return_token import return_token
import re

#トークンを別ファイルから取得
TOKEN = return_token()

#グローバル変数の定義
global yom_channel
#変数の初期化
yom_channel = []

#BOTの初期化
client = commands.Bot(command_prefix='.')
voice_client = None

#イベントハンドラー
@client.event
#起動時に実行
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(f"Connected to following guilds:")
    for x in client.guilds:
      print(f"{x}")
    print('------')

#イベントハンドラー
@client.event
#テキストチャンネルに何か書き込まれたときに実行
async def on_message(message):
  global yom_channel
  #.joinコマンドでVCに接続
  if message.content == ".join":
    await message.author.voice.channel.connect()
    yom_channel.append(message.channel.id)
    print(f"debug: yom_channel: {yom_channel}")
  else:
    print(f"debug: else: yom_channel: {yom_channel}")
    if message.content == ".leave":
      await message.author.guild.voice_client.disconnect() 
      i = 0
      for x in yom_channel:
        if message.channel.id == x:
          del yom_channel[i]
          i = i + 1
    #そのテキストチャンネルだけ読み上げる
    for x in yom_channel:
      if x == message.channel.id:
        #コンソールに書き込まれたテキストを出力
        #print(message.content)
        #URLを読み上げない
        if not message.content.startswith("http://") and not message.content.startswith("https://"):
          if len(message.content) <= 50:
            #メンションを読み上げない
            msg = message.content
            pattern = r'<@!'
            text = re.sub(pattern,'',msg) # 置換処理
            pattern = r'[0-9]+>'
            # return re.sub(pattern,'',msg) # 置換処理
            text_alt = re.sub(pattern, '', msg)
            
            #WAVファイルを作成
            creat_WAV(text_alt)
            #WAVファイルをDiscordにインプット
            source = discord.FFmpegPCMAudio("output.wav")
            #読み上げる
            # if yom_channel == message.channel.id:
            message.guild.voice_client.play(source)

#BOT起動
client.run(TOKEN)
