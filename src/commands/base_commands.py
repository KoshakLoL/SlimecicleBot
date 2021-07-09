from aiofiles import open as aioopen
from src.utils import get_choices_from_string
from random import choice
from typing import List


async def get_localization_no_choice(localizationPath: str) -> str:
    """Gets the localization for a no choice command (ex. help)

    :param localizationPath: Path to localization file
    :returns: A no choice string
    :raises: TODO
    """
    async with aioopen(localizationPath, mode="r") as f:
        return await f.read()


async def get_localization_with_choice(localizationPath: str) -> str:
    """Gets the localization for a choice command (ex. good_bot)

    :param localizationPath: Path to localization file
    :returns: A random choice string
    :raises: TODO
    """
    async with aioopen(localizationPath, mode="r") as f:
        content: str = await f.read()
    all_choices: List[str] = await get_choices_from_string(content)
    return choice(all_choices)
