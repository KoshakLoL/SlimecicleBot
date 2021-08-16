from vkbottle.bot import Blueprint, Message
from src.rules import FindAllRule
from typing import List
from src.commands.callout_command import get_name_callout


bp = Blueprint("For callout responses")


@bp.on.message(FindAllRule({
    "quackity": [
        r"(?i)(quackity|квакити)",
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
