#!/usr/bin/env python3
# ライブラリのロード
import discord
from discord.ext import commands
from voice_generator import create_WAV
from return_token import return_token
import re
from log import log

# トークンを別ファイルから取得
print("Bot started. See ./log/bot.log")
log("-----------")
log("Script started.")
TOKEN = return_token()
GREETING = """Created by Yuki.
.joinで接続。
.leaveで切断。
※たまにメンテナンスで落ちます。その際は再度.joinにて接続をお願い致します。

https://github.com/Yuki56738/Yuki-s-Yomiage-BOT.Discord"""

# グローバル変数の定義
global yom_channel
# 変数の初期化
# 読むテキストチャンネルの配列
yom_channel = []

# BOTの初期化
# client = commands.Bot(command_prefix='.')
# voice_client = None
client = discord.Bot()


# イベントハンドラー
@client.event
# 起動時に実行
async def on_ready():
    log('Logged in as')
    log(client.user.name)
    log(client.user.id)
    log(f"Connected to following guilds:")
    i = 0
    for x in client.guilds:
        i += 1
        log(f"{i}: {x}")
    log('------')

@client.slash_command(guild_ids=[813401986299854859])
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello.")

@client.slash_command(guild_ids=[813401986299854859])
async def joinyuki(ctx: discord.ApplicationContext):
    # await ctx.interaction.send_message("Connecting to VC...")
    await ctx.respond("Connecting to VC...")
    await ctx.author.voice.channel.connect()
    # yom_channelに読み上げるテキストチャンネルのIDを追加
    yom_channel.append(ctx.channel.id)
    log(f"debug: join: yom_channel: {yom_channel}")
    await ctx.channel.send(GREETING)
    log(f"Joined to {ctx.guild.name}: {ctx.channel.name}")

@client.slash_command(guild_ids=[813401986299854859])
async def leaveyuki(ctx: discord.ApplicationContext):
    await ctx.respond("Disconnecting from VC...")
    # await ctx.author.voice.channel.disconnect()
    for vc in client.voice_clients:
        await vc.disconnect()
    # 切断と同時に、yom_channelから該当のテキストチャンネルのIDを削除
    i = 0
    for x in yom_channel:
        if ctx.channel.id == x:
            del yom_channel[i]
        i = i + 1
    log(f"debug: leave: yom_channel: {yom_channel}")
    log(f"Left from {ctx.guild.name}: {ctx.channel.name}")
    return
@client.event
async def on_guild_join(guild):
    log(f"This BOT has joined to new guild: {guild}")

# イベントハンドラー
@client.event
# テキストチャンネルに何か書き込まれたときに実行
async def on_message(message):
    global yom_channel
    # print(message.content)
    # .joinコマンドでVCに接続
    if message.content == ".join":
        await message.author.voice.channel.connect()
        # yom_channelに読み上げるテキストチャンネルのIDを追加
        yom_channel.append(message.channel.id)
        log(f"debug: join: yom_channel: {yom_channel}")
        await message.channel.send(GREETING)
        log(f"Joined to {message.guild.name}: {message.channel.name}")
    else:
        if message.content == GREETING:
            return
        if message.author == client.user:
            return
        # log(f"debug: else: yom_channel: {yom_channel}")
        # log("--------")
        # .leaveコマンドでVCから切断
        if message.content == ".leave":
            await message.author.guild.voice_client.disconnect()
            # 切断と同時に、yom_channelから該当のテキストチャンネルのIDを削除
            i = 0
            for x in yom_channel:
                if message.channel.id == x:
                    del yom_channel[i]
                i = i + 1
            log(f"debug: leave: yom_channel: {yom_channel}")
            log(f"Left from {message.guild.name}: {message.channel.name}")
            return
        # そのテキストチャンネルだけ読み上げる
        for x in yom_channel:
            if x == message.channel.id:
                msg = message.content
                # URLを読み上げない
                if message.content.startswith("http://") or message.content.startswith("https://"):
                    msg = "URL省略"
                # 50文字までしか読み上げない
                if len(message.content) <= 50:
                    # メンションを読み上げない
                    pattern = r'<@!'
                    text = re.sub(pattern, '', msg)  # 置換処理
                    pattern = r'[0-9]+>'
                    # return re.sub(pattern,'',msg) # 置換処理
                    text_alt = re.sub(pattern, '', msg)

                    # WAVファイルを作成
                    create_WAV(text_alt)
                    # WAVファイルをDiscordにインプット
                    source = discord.FFmpegPCMAudio("output.wav")
                    # 読み上げる
                    # if yom_channel == message.channel.id:
                    message.guild.voice_client.play(source)


# BOT起動
client.run(TOKEN)
