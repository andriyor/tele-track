# Tele track

Track channel messages based on keywords and receive notification from bot


## Configure

`.env` file example:

```
API_ID=****
API_HASH=****
BOT_TOKEN=****
TRACK_CHAT_ID=****
SEND_CHAT_ID=****
KEYWORD=****
```

## Install

```sh
poetry install
```
install on ubuntu

```sh
sudo apt install pipx -y
pipx ensurepath
pipx install poetry==1.2.0
poetry install
```


## Run

```sh
poetry run python main.py
```


## Related docs

[App configuration](https://my.telegram.org/apps)

[Telethon](https://github.com/LonamiWebs/Telethon)

[Python Telegram bot api.](https://github.com/eternnoir/pyTelegramBotAPI?tab=readme-ov-file)


## TODO

- more filtering options
