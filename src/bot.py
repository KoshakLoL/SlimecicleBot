from vkbottle.bot import Bot
from vkbottle import load_blueprints_from_package
from typing import Final

from os import environ

bot: Final[Bot] = Bot(environ["BOT_TOKEN"])

if __name__ == "__main__":
    for bp in load_blueprints_from_package("src/blueprints"):
        bp.load(bot)
    bot.run_forever()
