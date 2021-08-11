from vkbottle.bot import Blueprint, Message
from src.commands.base_commands import get_localization_no_choice, get_localization_with_choice
from src.commands.image_load import get_photo, get_document
from src.utils import replace_string_username, choose_file
from typing import Tuple

bp = Blueprint("For base responses")


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм).*(помощь|помоги).*",
    r"(?i).*(помощь|помоги).*(чарли|слайм).*"
])
async def help_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_no_choice("localization/no_choices/help.txt")
    await message.answer(msg_string)


@bp.on.message(regexp=[
    r"(?i).*(обним|обнял|обнять).*(чарли|слайма).*",
    r"(?i).*(чарли|слайм).*обними.*"
])
async def hug_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/hug.txt")
    user = await bp.api.users.get(message.from_id)
    await message.answer(await replace_string_username(msg_string, user[0].first_name))


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм).*лор.*"
])
async def lore_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/lore.txt")
    await message.answer(msg_string)


@bp.on.message(regexp=[
    r"(?i).*(хороший|молодец).*(бот|чарли|слайм).*",
    r"(?i).*(чарли|слайм|бот).*(хороший|молодец).*",
    r"(?i).*чарли ультра мега супер харош.*"
])
async def good_bot_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/good_bot.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(чарли|слайм).*добр.*утр.*",
    r"(?i).*добр.*утр.*(чарли|слайм)"
])
async def morning_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/morning.txt")
    await message.answer(msg_string)


@bp.on.private_message(regexp=[
    r"(?i).*добр.* утр.*",
])
async def morning_dm_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/morning_dm.txt")
    user = await bp.api.users.get(message.from_id)
    await message.answer(await replace_string_username(msg_string, user[0].first_name))


@bp.on.message(regexp=[
    r"(?i).*destroy sex.*",
    r"(?i)!destroysex"
])
async def destroy_sex_command(message: Message, match: Tuple) -> None:
    random_file: str = await choose_file("images/slimeDestroy")
    attachment_str = await get_photo(random_file, bp.api)
    await message.answer(attachment=attachment_str)


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм|слайма).*(вижу|видно).*",
    r"(?i).*(вижу|видно).*(чарли|слайма).*",
    r"(?i)!slimepic",
])
async def saw_slime_command(message: Message, match: Tuple) -> None:
    random_file: str = await choose_file("images/slimeImages")
    attachment_str = await get_photo(random_file, bp.api)
    await message.answer(attachment=attachment_str)


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм).*танцуй.*"
])
async def dance_slime_command(message: Message, match: Tuple) -> None:
    random_file: str = await choose_file("images/slimeDance")
    attachment_str = await get_document(random_file, bp.api, message.peer_id)
    await message.answer(attachment=attachment_str)


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм).*(слайм|(ты|не) человек).*"
])
async def human_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/human.txt")
    await message.answer(msg_string)


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм).*анекдот.*"
])
async def anecdote_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/anecdote.txt")
    await message.answer(msg_string)


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм).*(привет|вечер|х[аэе]й).*",
    r"(?i).*(привет|вечер|х[аэе]й).*(чарли|слайм).*"
])
async def hello_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/hello.txt")
    user = await bp.api.users.get(message.from_id)
    await message.answer(await replace_string_username(msg_string, user[0].first_name))


@bp.on.message(regexp=[
    r"(?i).*(спасибо|благодарю|спс).*(чарли|слайм).*",
    r"(?i).*(чарли|слайм).*(спасибо|благодарю|спс).*"
])
async def thanks_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/thanks.txt")
    await message.answer(msg_string)


@bp.on.message(regexp=[
    r"(?i).*(пока|прощай|ночи|снов).*(чарли|слайм).*",
    r"(?i).*(чарли|слайм).*(пока|прощай|ночи|снов).*",
])
async def goodbye_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/goodbye.txt")
    await message.answer(msg_string)


@bp.on.message(regexp=[
    r"(?i).*(чарли|слайм).*"
])
async def callout_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/callout.txt")
    await message.answer(msg_string)
