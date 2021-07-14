from vkbottle.bot import Bot, Message
from vkbottle import load_blueprints_from_package
from src.rules import FindAllRule
from src.commands.name_callout import get_name_callout
from typing import List, Final

from os import environ

bot: Final[Bot] = Bot(environ["BOT_TOKEN"])


@bot.on.message(FindAllRule({
    "quackity": [
        "(?i)quackity",
        "(?i)квакити"
    ]
}))
# You can add more names in here ^^, just make sure it's in the JSON file pls
async def name_callout_command(message: Message, match: List[str]) -> None:
    messages: List[str] = await get_name_callout(
        "localization/choicesJSON/name_callout.json",
        match
    )
    for msg in messages:
        await message.answer(msg)

if __name__ == "__main__":
    for bp in load_blueprints_from_package("src/blueprints"):
        bp.load(bot)
    bot.run_forever()
