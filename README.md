### VIDEO STREAM USERBOT ✨

an another telegram userbot for streaming video trought the telegram video chat.

## Environmental Variables 📌

- `API_ID` : Get this value from my.telegram.org/apps
- `API_HASH` : Get this value from my.telegram.org/apps
- `SESSION` : visit [here](https://replit.com/@levinalab/StringSession#main.py) to obtain this value.
- `SUDO` : User ID of users who have access to use the bot commands, separate each with space.
- `BOT_TOKEN` : (Optional) Get this value from [BotFather](https://telegram.dog/BotFather).

## 🛠 Commands (sudo only)

you can change who's people can access the userbot command, try to fork this repo and remove the `filters.user{Var.SUDO}` change to anything filters type available on pyrogram

- !play (reply to video/file/provide yt url) - to stream video
- !stream (provide yt url) - to stream a youtube live streaming
- !stop - to stop the video streaming
- !leave - order the userbot to leave from vc
- !logs - send you the userbot logs
- !term (for dev) - to know about this, see on this [file](https://github.com/levina-lab/video-stream2/blob/main/vcbot/plugins/run_cmd.py)

## HOST ON HEROKU 💜
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/levina-lab/vsu)

## HOST ON RAILWAY 🚄
[![Deploy+on+Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/levina-lab/vsu&envs=API_ID,API_HASH,BOT_TOKEN,SESSION,SUDO)

## VPS Deployment 📡
```sh
- sudo apt update && upgrade -y
- sudo apt install python3-pip -y virtualenv
- sudo apt install ffmpeg -y
- nvm install v16.5.0
- git clone https://github.com/levina-lab/vsu
- cd vsu
- virtualenv venv #Create Virtual Environment.
- source venv/bin/activate #Activate Virtual Environment
- pip3 install --upgrade pip
- pip3 install -U -r requirements.txt
- npm i -g npm
- cp -r sample.env local.env
- nano local.env #Fill it with your variables value.
- python3 -m vcbot
```

## Special Credits 💖

- [Levina](https://t.me/dlwrml)
- [Wrench](https://t.me/EverythingSuckz) Dev

made with [py-tgcalls](https://github.com/pytgcalls/pytgcalls) and [pyrogram](https://github.com/pyrogram/pyrogram) ❤️
