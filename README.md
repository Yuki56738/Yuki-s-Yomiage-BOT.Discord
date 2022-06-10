# Yuki-s-Yomiage-BOT.Discord  
This project has been moved to（このプロジェクトは以下に移動しました）:  
https://github.com/Yuki56738/Yuki-s-yomiage-BOT-v2.discord  
This project is never updated.（もはやこのプロジェクトは更新されません！）  

Discordで、テキストチャットに入力された文字を音声で出力します。  
Shovelや喋太郎、ALBOTが落ちたときのために創りました！

.joinでVCに接続します。  
.leaveで切断します。  

使うだけなら↓のリンクをクリックすると、BOTを招待できます。  
https://discord.com/oauth2/authorize?client_id=839928955612299275&permissions=3152896&scope=bot  
------------------------------------------------------------------------
導入:  
1. OpenJtalkをインストール  
```bash
sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001  
```
2. ffmpeg, Discord.pyをインストール  
```bash
sudo apt install python3-pip ffmpeg
pip3 install -U discord.py[voice] ffmpeg
```

4. git cloneする  
```bash
git clone https://github.com/Yuki56738/Yuki-s-Yomiage-BOT.Discord.git
```

6. トークンをreturn_token.pyに記述  
```bash
cd Yuki-s-Yomiage-BOT.Discord
vi return_token.py
```

7. 実行する  
```bash
chmod +x bot.py
./bot.py
```

不具合報告、改善点など:  enginner@risaton.net  
