import os
import sys
import telegram

from dotenv import dotenv_values

BASE_PATH: str = os.path.dirname(os.path.realpath(__file__))
ENV_FILENAME: str = "env"
ENV_FILEPATH: str = os.path.join(BASE_PATH, ENV_FILENAME)

def main():
    data = sys.stdin.read().strip()
    cfg = dotenv_values(ENV_FILEPATH)
    bot = telegram.Bot(token=cfg['TOKEN']).sendMessage(chat_id=cfg['CHAT_ID'], text=data)

if __name__ == "__main__":
    main()
