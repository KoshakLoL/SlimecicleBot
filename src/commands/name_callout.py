from src.utils import get_choices_from_string
from aiofiles import open as aioopen
from random import choice
from json import loads
from re import findall
from typing import List


async def get_name_callout(localizationPath: str, all_names: List[str]) -> List[str]:
    """The name_callout searches for all sightings of every name from a JSON file in all_names

    :param localizationPath: Path to localization file
    :param all_names: All names to search
    :returns: A name_callout string list to send one by one
    :raises: TODO
    """
    all_callouts: List[str] = []
    async with aioopen(localizationPath, mode="r") as f:
        content = await f.read()
    content = loads(content)
    for name in all_names:
        if name in content:
            all_callouts.append(choice(content[name]))
    return all_callouts
