from vkbottle.bot import Blueprint, Message
from src.commands.base_commands import get_localization_no_choice, get_localization_with_choice
from vkbottle_types.objects import UsersUserSettingsXtr
from src.commands.image_load import get_photo, get_document
from src.utils import replace_string_username, choose_file
from typing import Tuple, List

bp = Blueprint("For base responses")


async def string_append_user(msg_string: str, user_id: int) -> str:
    users: List[UsersUserSettingsXtr] = await bp.api.users.get(user_id)
    return await replace_string_username(msg_string, users[0].first_name)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(помощь|помоги)(.|\n)*",
    r"(?i)(.|\n)*(помощь|помоги)(.|\n)*(чарли|слайм)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(помощь|помоги)(.|\n)*"
])
async def help_command(message: Message) -> None:
    msg_string: str = await get_localization_no_choice("localization/no_choices/help.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*лор(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*лор(.|\n)*"
])
async def lore_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/lore.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(хор[оа]ш|молодец)(.|\n)*(чарли|слайм)(.|\n)*",
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(хор[оа]ш|молодец)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(хор[оа]ш|молодец)(.|\n)*"
])
async def good_bot_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/good_bot.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*утр(.|\n)*",
    r"(?i)(.|\n)*утр(.|\n)*(чарли|слайм)"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*утр(.|\n)*"
])
async def morning_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswithplaceholders/morning.txt")
    await message.answer(await string_append_user(msg_string, message.from_id))


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(секс)",
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*секс(.|\n)*"
])
async def destroy_sex_command(message: Message) -> None:
    random_file: str = await choose_file("images/destroy")
    attachment_str = await get_photo(random_file, bp.api)
    await message.answer(attachment=attachment_str)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм|слайма)(.|\n)*(вижу|видно)(.|\n)*",
    r"(?i)(.|\n)*(вижу|видно)(.|\n)*(чарли|слайма)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(вижу|видно)(.|\n)*"
])
async def saw_slime_command(message: Message) -> None:
    random_file: str = await choose_file("images/justimages")
    attachment_str = await get_photo(random_file, bp.api)
    await message.answer(attachment=attachment_str)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*танцуй(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*танцуй(.|\n)*"
])
async def dance_slime_command(message: Message) -> None:
    random_file: str = await choose_file("images/dance")
    attachment_str = await get_document(random_file, bp.api, message.peer_id)
    await message.answer(attachment=attachment_str)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(слайм|(ты|не) человек)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*ты(.|\n)*(слайм|человек)(.|\n)*"
])
async def human_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/human.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*анекдот(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*анекдот(.|\n)*"
])
async def anecdote_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/anecdote.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(привет|вечер|х[аэе]й)(.|\n)*",
    r"(?i)(.|\n)*(привет|вечер|х[аэе]й)(.|\n)*(чарли|слайм)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(привет|вечер|х[аэе]й)(.|\n)*"
])
async def hello_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswithplaceholders/hello.txt")
    await message.answer(await string_append_user(msg_string, message.from_id))


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(спасибо|благодарю|спс)(.|\n)*(чарли|слайм)(.|\n)*",
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(спасибо|благодарю|спс)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(спасибо|благодарю|спс)(.|\n)*"
])
async def thanks_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/thanks.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(пока|прощай|бай)(.|\n)*(чарли|слайм)(.|\n)*",
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(пока|прощай|бай)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(пока|прощай|бай)(.|\n)*"
])
async def goodbye_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/goodbye.txt")
    await message.answer(msg_string)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(ночи|снов)(.|\n)*(чарли|слайм)(.|\n)*"
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(ночи|снов)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(ночи|снов)(.|\n)*"
])
async def good_night_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswithplaceholders/night.txt")
    await message.answer(await string_append_user(msg_string, message.from_id))


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(люблю)(.|\n)*(чарли|слайм)(.|\n)*",
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(люблю)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*люблю(.|\n)*тебя(.|\n)*",
    r"(?i)(.|\n)*тебя(.|\n)*люблю"
])
async def love_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswithplaceholders/love.txt")
    await message.answer(await string_append_user(msg_string, message.from_id))


@bp.on.message(regexp=[
    r"(?i)^(чарли|слайм)$"
])
async def callout_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/callout.txt")
    await message.answer(msg_string)
