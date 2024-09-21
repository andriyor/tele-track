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
poetry install --no-root
```
install on ubuntu

```sh
sudo apt install pipx -y
pipx ensurepath
pipx install poetry==1.8.3
poetry install --no-root
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
