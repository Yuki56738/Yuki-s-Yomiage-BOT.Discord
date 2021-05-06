# Yuki-s-Yomiage-BOT.Discord  
Discordで、テキストチャットに入力された文字を音声で出力します。  

.joinでVCに接続します。  
.leaveで切断します。  

------------------------------------------------------------------------
導入:  
1. OpenJtalkをインストール  
$ sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001  

2. ffmpeg, Discord.pyをインストール  
$ sudo apt install python3-pip ffmpeg  
$ pip3 install -U discord.py[voice]  
$ pip3 install -U ffmpeg  
