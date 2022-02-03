from vkbottle.bot import Blueprint, Message
from vkbottle_types.objects import UsersUserXtrType
import re
from typing import List
from src.commands.mention_commands import (
    string_with_everyone,
    string_with_user
)
from src.commands.image_load import get_photo
from src.utils import choose_file
from src.rules import ChatOrPrivateRegex

bp = Blueprint("For mention response")


async def extract_users(message: Message) -> List[UsersUserXtrType]:
    all_users: List[str] = re.findall(r"(?:id)\d+", message.text)
    if all_users:
        users: List[UsersUserXtrType] = []
        for user in all_users:
            usersQuery: List[UsersUserXtrType] = await bp.api.users.get(user)
            users.append(usersQuery[0])
        return users
    else:
        return await bp.api.users.get(message.from_id)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(обни|обня).*(чарли|слайма|все|all|онлайн|\[id).*",
        r"(?i).*(чарли|слайм).*(обни|обня).*"
    ],
    privateRE=[
        r"(?i).*(обни|обня).*"
    ]
))
async def hug_command(message: Message) -> None:
    returnMessage: str = ""
    if re.findall(r"all|все|онлайн", message.text):
        returnMessage = await string_with_everyone(
            "localization/choices/hug_to.txt"
        )
    else:
        users: List[UsersUserXtrType] = await extract_users(message)
        returnMessage = await string_with_user(
            "localization/choiceswnames/hug_someone.txt",
            users[0]
        )
    photo_att: str = await get_photo(await choose_file("images/hug"), bp.api)
    await message.answer(returnMessage, attachment=photo_att)


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(цело|целу|чмок).*(чарли|слайма|\[id).*",
        r"(?i).*(чарли|слайм).*поцелуй.*(меня|\[id)"
    ],
    privateRE=[
        r"(?i).*(цело|целу|чмок).*"
    ]
))
async def kiss_command(message: Message) -> None:
    users: List[UsersUserXtrType] = await extract_users(message)
    localization_file: str = ""
    if re.findall(r"\[id", message.text):
        localization_file = "localization/choiceswnames/kiss_someone.txt"
    else:
        localization_file = "localization/choices/kiss_to.txt"
    photo_att: str = await get_photo(await choose_file("images/kiss"), bp.api)
    await message.answer(
        await string_with_user(localization_file, users[0]),
        attachment=photo_att
    )


@bp.on.message(ChatOrPrivateRegex(
    chatRE=[
        r"(?i).*(глад|глаж).*(чарли|слайма|\[id).*",
        r"(?i).*(чарли|слайм).*(глад|глаж)*(меня|\[id).*"
    ],
    privateRE=[
        r"(?i).*(глад|глаж).*"
    ]
))
async def pet_command(message: Message) -> None:
    users: List[UsersUserXtrType] = await extract_users(message)
    localization_file: str = ""
    if re.findall(r"\[id", message.text) or re.findall(r"меня|нас", message.text):
        localization_file = "localization/choiceswnames/pat_someone.txt"
    else:
        localization_file = "localization/choices/pat_to.txt"
    await message.answer(await string_with_user(localization_file, users[0]))
