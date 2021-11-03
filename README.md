# Yuki-s-Yomiage-BOT.Discord  

Discordで、テキストチャットに入力された文字を音声で出力します。  
Shovelや喋太郎、ALBOTが落ちたときのために創りました！

`.join` でVCに接続します。  
`.leave` で切断します。  

使うだけなら↓のリンクをクリックすると、BOTを招待できます。  

[Discordに招待する](https://discord.com/oauth2/authorize?client_id=839928955612299275&permissions=3152896&scope=bot)

------------------------------------------------------------------------

## 導入
  
1. OpenJtalkをインストール  

```bash
$ sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001  
```

2. ffmpeg, Discord.pyをインストール  

```bash
$ sudo apt install python3-pip ffmpeg  
$ pip3 install -U discord.py[voice]  
$ pip3 install -U ffmpeg  
```

3. git cloneする  

```bash
$ git clone https://github.com/Yuki56738/Yuki-s-Yomiage-BOT.Discord.git  
```

4. トークンをreturn_token.pyに記述  

```bash
$ cd Yuki-s-Yomiage-BOT.Discord  
$ vi return_token.py 
```

4. 実行する  

```bash
$ chmod +x bot.py  
$ ./bot.py
```

不具合報告、改善点などは[メールで。](<mailto:yuki0104@protonmail.com>)
