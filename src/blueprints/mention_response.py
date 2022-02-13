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


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(обни|обня)(.|\n)*(чарли|слайма|все|all|онлайн|\[id)(.|\n)*",
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(обни|обня)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(обни|обня)(.|\n)*"
])
async def hug_command(message: Message) -> None:
    returnMessage: str = ""
    if re.findall(r"all\b|все(\b|х)|онлайн\b", message.text):
        returnMessage = await string_with_everyone(
            "localization/choices/hug_to.txt"
        )
    else:
        users: List[UsersUserXtrType] = await extract_users(message)
        returnMessage = await string_with_user(
            "localization/choiceswithplaceholders/hug_someone.txt",
            users[0]
        )
    photo_att: str = await get_photo(await choose_file("images/hug"), bp.api)
    await message.answer(returnMessage, attachment=photo_att)


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(цело|целу|чмок)(.|\n)*(чарли|слайма|\[id)(.|\n)*",
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*поцелуй(.|\n)*(меня|\[id)"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(цело|целу|чмок)(.|\n)*"
])
async def kiss_command(message: Message) -> None:
    users: List[UsersUserXtrType] = await extract_users(message)
    localization_file: str = ""
    if re.findall(r"\[id", message.text):
        localization_file = "localization/choiceswithplaceholders/kiss_someone.txt"
    else:
        localization_file = "localization/choices/kiss_to.txt"
    photo_att: str = await get_photo(await choose_file("images/kiss"), bp.api)
    await message.answer(
        await string_with_user(localization_file, users[0]),
        attachment=photo_att
    )


@bp.on.chat_message(regexp=[
    r"(?i)(.|\n)*(глад|глаж)(.|\n)*(чарли|слайма|\[id)(.|\n)*",
    r"(?i)(.|\n)*(чарли|слайм)(.|\n)*(глад|глаж)*(меня|\[id)(.|\n)*"
])
@bp.on.private_message(regexp=[
    r"(?i)(.|\n)*(глад|глаж)(.|\n)*"
])
async def pet_command(message: Message) -> None:
    users: List[UsersUserXtrType] = await extract_users(message)
    localization_file: str = ""
    if re.findall(r"\[id", message.text) or re.findall(r"меня|нас", message.text):
        localization_file = "localization/choiceswithplaceholders/pat_someone.txt"
    else:
        localization_file = "localization/choices/pat_to.txt"
    await message.answer(await string_with_user(localization_file, users[0]))
