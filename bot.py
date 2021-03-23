#ライブラリのロード
import discord
from discord.ext import commands
import subprocess
import ffmpeg
from voice_generator import creat_WAV
from return_token import return_token

#トークンを別ファイルから取得
TOKEN = return_token()

#グローバル変数の定義
global yom_channel
#変数の初期化
yom_channel = 0000

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
    print('------')

#イベントハンドラー
@client.event
#テキストチャンネルに何か書き込まれたときに実行
async def on_message(message):
    global yom_channel
    #.joinコマンドでVCに接続
    if message.content == ".join":
        await message.author.voice.channel.connect()
        yom_channel = message.channel.id
    else:
        #そのテキストチャンネルだけ読み上げる
        if yom_channel == message.channel.id:
          #.leaveでBOTを切断
          if message.content == ".leave":
            await message.author.guild.voice_client.disconnect() 
        #コンソールに書き込まれたテキストを出力
        print(message.content)
        if not message.content.startswith("http://") and not message.content.startswith("https://"):
          #WAVファイルを作成
          creat_WAV(message.content)
          #WAVファイルをDiscordにインプット
          source = discord.FFmpegPCMAudio("output.wav")
          #読み上げる
          if yom_channel == message.channel.id:
            message.guild.voice_client.play(source)

#BOT起動
client.run(TOKEN)