from vkbottle.bot import Bot, Message
from src.commands.base_commands import get_localization_no_choice, get_localization_with_choice
from src.commands.image_load import get_photo, get_document
from src.utils import replace_string_username, FindAllRule
from src.commands.name_callout import get_name_callout
from typing import Tuple, List

from os import environ

bot: Bot = Bot(environ["BOT_TOKEN"])


@bot.on.message(regexp=[
    r"(?i).*(чарли|слаймсикл|слайм).*(помощь|помоги).*",
    r"(?i).*(помощь|помоги).*(чарли|слаймсикл|слайм).*"
])
async def help_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_no_choice("localization/noChoices/help.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    r"(?i).*(обнимаю|обнял).*(чарли|слаймсикла|слайма).*",
    r"(?i).*(чарли|слаймсикла|слайма).*обними.*"
])
async def hug_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/hug.txt")
    user = await bot.api.users.get(message.from_id)
    await message.answer(await replace_string_username(msg_string, user[0].first_name))


@bot.on.message(regexp=[
    r"(?i).*(чарли|слаймсикл|слайм).*лор.*"
])
async def lore_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/lore.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    r"(?i).*(хороший|молодец).*(бот|чарли|слаймсикл|слайм).*",
    r"(?i).*(чарли|слайм|слаймсикл|бот).*(хороший|молодец).*",
    r"(?i).*чарли ультра мега супер харош.*"
])
async def good_bot_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/good_bot.txt")
    await message.answer(msg_string)


@bot.on.chat_message(regexp=[
    r"(?i).*доброе утр.*",
    r"(?i).*утречка.*"
])
async def morning_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/morning.txt")
    await message.answer(msg_string)


@bot.on.private_message(regexp=[
    r"(?i).*доброе утр.*",
    r"(?i).*утречка.*"
])
async def morning_dm_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/morning_dm.txt")
    user = await bot.api.users.get(message.from_id)
    await message.answer(await replace_string_username(msg_string, user[0].first_name))


@bot.on.message(regexp=[
    r"(?i).*destroy sex.*",
    r"(?i)!destroysex"
])
async def destroy_sex_command(message: Message, match: Tuple) -> None:
    attachment_str = await get_photo("images/slimeSex", bot.api)
    await message.answer(attachment=attachment_str)


@bot.on.message(regexp=[
    r"(?i).*(чарли|слайм|слайма|слаймсикла|слаймсикл).*(вижу|видно).*",
    r"(?i).*(вижу|видно).*(чарли|слайма|слаймсикла).*",
    r"(?i)!slimepic",
])
async def saw_slime_command(message: Message, match: Tuple) -> None:
    attachment_str = await get_photo("images/slimeImages", bot.api)
    await message.answer(attachment=attachment_str)


@bot.on.message(regexp=[
    r"(?i).*(чарли|слаймсикл|слайм).*танцуй.*"
])
async def dance_slime_command(message: Message, match: Tuple) -> None:
    attachment_str = await get_document("images/slimeDance", "gif", bot.api, message.peer_id)
    await message.answer(attachment=attachment_str)


@bot.on.message(regexp=[
    r"(?i).*(чарли|слаймсикл|слайм).*(слайм|не человек).*"
])
async def human_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/human.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    r"(?i).*(чарли|слаймсикл|слайм).*анекдот.*"
])
async def anecdote_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/anecdote.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    r"(?i).*(чарли|слаймсикл|слайм).*(привет|вечер|х[аэе]й).*",
    r"(?i).*(привет|вечер|х[аэе]й).*(чарли|слаймсикл|слайм).*"
])
async def hello_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/hello.txt")
    user = await bot.api.users.get(message.from_id)
    await message.answer(await replace_string_username(msg_string, user[0].first_name))


@bot.on.message(regexp=[
    r"(?i).*(спасибо|благодарю|спс).*(чарли|слаймсикл|слайм).*",
    r"(?i).*(чарли|слаймсикл|слайм).*(спасибо|благодарю|спс).*"
])
async def thanks_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_no_choice("localization/noChoices/thanks.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    r"(?i).*(пока|прощай|ночи).*(чарли|слаймсикл|слайм).*",
    r"(?i).*(чарли|слаймсикл|слайм).*(пока|прощай|ночи).*",
])
async def goodbye_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_no_choice("localization/noChoices/goodbye.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    r"(?i).*(чарли|слаймсикл|слайм).*"
])
async def callout_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/callout.txt")
    await message.answer(msg_string)


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


bot.run_forever()
