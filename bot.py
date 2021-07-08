from vkbottle.bot import Bot, Message
from src.commands.base_commands import get_localization_no_choice, get_localization_with_choice
from src.commands.image_load import get_photo, get_document
from src.utils import replace_string_username, FindAllRule
from src.commands.name_callout import get_name_callout
from typing import List, Tuple, Set

from os import environ

bot = Bot(environ["bot_token"])


@bot.on.message(regexp=[
    "(?i)чарли помощь",
    "(?i)слайм помощь",
    "(?i)слаймсикл помощь",
    "(?i)чарли помоги",
    "(?i)слайм помоги",
    "(?i)слаймсикл помоги"
])
async def help_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_no_choice("localization/noChoices/help.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)обнимаю чарли",
    "(?i)чарли обними меня",
    r"\*обнял чарли\*",
    "(?i)обнимаю слайма",
    "(?i)слайм обними меня",
    r"\*обнял слайма\*",
    "(?i)обнимаю слаймсикла",
    "(?i)слаймсикл обними меня",
    r"\*обнял слаймсикла\*",
])
async def hug_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/hug.txt")
    user = await bot.api.users.get(message.from_id)
    msg_string: str = await replace_string_username(msg_string, user[0].first_name)
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)чарли лор",
    "(?i)слаймсикл лор",
    "(?i)слайм лор"
])
async def lore_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choices/lore.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)хороший чарли",
    "(?i)хороший бот",
    "(?i)хороший слаймсикл",
    "(?i)хороший слайм",
    "(?i)чарли молодец",
    "(?i)слайм молодец",
    "(?i)слаймсикл молодец",
    "(?i)чарли ультра мега супер харош"
])
async def good_bot_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choices/good_bot.txt")
    await message.answer(msg_string)


@bot.on.chat_message(regexp=[
    "(?i)доброе утро",
    "(?i)утра",
    "(?i)утречка",
    "(?i)хорошего утречка"
])
async def morning_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choices/morning.txt")
    await message.answer(msg_string)


@bot.on.private_message(regexp=[
    "(?i)доброе утро",
    "(?i)утра",
    "(?i)утречка",
    "(?i)хорошего утречка"
])
async def morning_dm_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/morning_dm.txt")
    user = await bot.api.users.get(message.from_id)
    msg_string: str = await replace_string_username(msg_string, user[0].first_name)
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)destroy sex",
    "(?i)!destroysex",
    "(?i)destroy sex!"
])
async def destroy_sex_command(message: Message, match: Tuple):
    attachment_str = await get_photo("images/slimeSex", bot.api)
    await message.answer(attachment=attachment_str)


@bot.on.message(regexp=[
    "(?i)чарли я тебя вижу",
    "(?i)тебя видно чарли",
    "(?i)слайм тебя видно",
    "(?i)я тебя вижу слайм",
    "(?i)слайм я тебя вижу",
    "(?i)!slimepic",
    "(?i)чарли тебя видно"
])
async def saw_slime_command(message: Message, match: Tuple):
    attachment_str = await get_photo("images/slimeImages", bot.api)
    await message.answer(attachment=attachment_str)


@bot.on.message(regexp=[
    "(?i)чарли танцуй",
    "(?i)слаймсикл танцуй",
    "(?i)станцуй чарли",
    "(?i)станцуй слайм"
])
async def dance_slime_command(message: Message, match: Tuple):
    attachment_str = await get_document("images/slimeDance", "gif", bot.api, message.peer_id)
    await message.answer(attachment=attachment_str)


@bot.on.message(regexp=[
    "(?i)чарли ты человек?",
    "(?i)ты слайм",
    "(?i)чарли ты слайм",
    "(?i)слайм ты слайм",
    "(?i)ты не человек чарли",
    "(?i)чарли ты не человек",
    "(?i)чарли ты слайм?"
])
async def human_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choices/human.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)слайм расскажи анекдот",
    "(?i)чарли расскажи анекдот",
    "(?i)слаймсикл расскажи анекдот"
])
async def anecdote_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choices/anecdote.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)привет чарли",
    "(?i)приветик чарли",
    "(?i)слайм привет",
    "(?i)чарли добрый вечер",
    "(?i)приветик слайм",
    "(?i)слайм добрый вечер"
])
async def hello_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/hello.txt")
    user = await bot.api.users.get(message.from_id)
    msg_string: str = await replace_string_username(msg_string, user[0].first_name)
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)спасибо чарли",
    "(?i)благодарю чарли",
    "(?i)спасибо слайм",
    "(?i)благодарю слайм",
    "(?i)чарли спасибо",
    "(?i)слайм спасибо",
    "(?i)слаймсикл спасибо"
])
async def thanks_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_no_choice("localization/noChoices/thanks.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)пока чарли",
    "(?i)пока слаймсикл",
    "(?i)пока слайм",
    "(?i)прощай чарли",
    "(?i)прощай слайм",
    "(?i)прощай слаймсикл"
])
async def goodbye_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_no_choice("localization/noChoices/goodbye.txt")
    await message.answer(msg_string)


@bot.on.message(regexp=[
    "(?i)чарли",
    "(?i)слайм",
    "(?i)слаймсикл"
])
async def callout_command(message: Message, match: Tuple):
    msg_string: str = await get_localization_with_choice("localization/choices/callout.txt")
    await message.answer(msg_string)


@bot.on.message(FindAllRule({
    "quackity": [
        "quackity",
        "квакити"
    ]
}))
# You can add more names in here ^^, just make sure it's in the JSON file pls
async def name_callout_command(message: Message, match: Set[str]):
    messages = await get_name_callout(
        "localization/choicesJSON/name_callout.json",
        match
    )
    for msg in messages:
        await message.answer(msg)


bot.run_forever()
