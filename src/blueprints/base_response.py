from vkbottle.bot import Blueprint, Message
from src.commands.base_commands import get_localization_no_choice, get_localization_with_choice
from vkbottle_types.objects import UsersUserSettingsXtr
from src.commands.image_load import get_photo, get_document
from src.utils import replace_string_username, choose_file
from typing import Tuple, List
from src.rules import ChatOrPrivateRegex

bp = Blueprint("For base responses")


async def string_append_user(msg_string: str, user_id: int) -> str:
    users: List[UsersUserSettingsXtr] = await bp.api.users.get(user_id)
    return await replace_string_username(msg_string, users[0].first_name)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*(помощь|помоги).*",
        r"(?i).*(помощь|помоги).*(чарли|слайм).*"
    ],
    privateRE=[
        r"(?i).*(помощь|помоги).*"
    ]
))
async def help_command(message: Message) -> None:
    msg_string: str = await get_localization_no_choice("localization/no_choices/help.txt")
    await message.answer(msg_string)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*лор.*"
    ],
    privateRE=[
        r"(?i).*лор.*"
    ]
))
async def lore_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/lore.txt")
    await message.answer(msg_string)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(хор[оа]ш|молодец).*(чарли|слайм).*",
        r"(?i).*(чарли|слайм).*(хор[оа]ш|молодец).*"
    ],
    privateRE=[
        r"(?i).*(хор[оа]ш|молодец).*"
    ]
))
async def good_bot_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/good_bot.txt")
    await message.answer(msg_string)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*утр.*",
        r"(?i).*утр.*(чарли|слайм)"
    ],
    privateRE=[
        r"(?i).*утр.*"
    ]
))
async def morning_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/morning.txt")
    await message.answer(await string_append_user(msg_string, message.from_id))


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*(секс)",
    ],
    privateRE=[
        r"(?i).*секс.*"
    ]
))
async def destroy_sex_command(message: Message) -> None:
    random_file: str = await choose_file("images/destroy")
    attachment_str = await get_photo(random_file, bp.api)
    await message.answer(attachment=attachment_str)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм|слайма).*(вижу|видно).*",
        r"(?i).*(вижу|видно).*(чарли|слайма).*"
    ],
    privateRE=[
        r"(?i).*(вижу|видно).*"
    ]
))
async def saw_slime_command(message: Message) -> None:
    random_file: str = await choose_file("images/justimages")
    attachment_str = await get_photo(random_file, bp.api)
    await message.answer(attachment=attachment_str)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*танцуй.*"
    ],
    privateRE=[
        r"(?i).*танцуй.*"
    ]
))
async def dance_slime_command(message: Message) -> None:
    random_file: str = await choose_file("images/dance")
    attachment_str = await get_document(random_file, bp.api, message.peer_id)
    await message.answer(attachment=attachment_str)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*(слайм|(ты|не) человек).*"
    ],
    privateRE=[
        r"(?i).*(слайм|человек).*"
    ]
))
async def human_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/human.txt")
    await message.answer(msg_string)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*анекдот.*"
    ],
    privateRE=[
        r"(?i).*анекдот.*"
    ]
))
async def anecdote_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/anecdote.txt")
    await message.answer(msg_string)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(чарли|слайм).*(привет|вечер|х[аэе]й).*",
        r"(?i).*(привет|вечер|х[аэе]й).*(чарли|слайм).*"
    ],
    privateRE=[
        r"(?i).*(привет|вечер|х[аэе]й).*"
    ]
))
async def hello_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/hello.txt")
    await message.answer(await string_append_user(msg_string, message.from_id))


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(спасибо|благодарю|спс).*(чарли|слайм).*",
        r"(?i).*(чарли|слайм).*(спасибо|благодарю|спс).*"
    ],
    privateRE=[
        r"(?i).*(спасибо|благодарю|спс).*"
    ]
))
async def thanks_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/thanks.txt")
    await message.answer(msg_string)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(пока|прощай|ночи|снов|бай).*(чарли|слайм).*",
        r"(?i).*(чарли|слайм).*(пока|прощай|ночи|снов|бай).*"
    ],
    privateRE=[
        r"(?i).*(пока|прощай|ночи|снов|бай).*"
    ]
))
async def goodbye_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/goodbye.txt")
    await message.answer(msg_string)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(люблю).*(чарли|слайм).*",
        r"(?i).*(чарли|слайм).*(люблю).*"
    ],
    privateRE=[
        r"(?i).*люблю.*тебя.*",
        r"(?i).*тебя.*люблю"
    ]
))
async def love_command(message: Message) -> None:
    msg_string: str = await get_localization_with_choice("localization/choiceswnames/love.txt")
    await message.answer(await string_append_user(msg_string, message.from_id))


@bp.on.message(regexp=[
    r"(?i)^(чарли|слайм)\S+$"
])
async def callout_command(message: Message, match: Tuple) -> None:
    msg_string: str = await get_localization_with_choice("localization/choices/callout.txt")
    await message.answer(msg_string)
