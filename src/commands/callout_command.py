from aiofiles import open as aioopen
from random import choice
from json import loads
from typing import List, Dict


async def get_name_callout(localizationPath: str, all_names: List[str]) -> List[str]:
    """The name_callout searches for all sightings of every name from a JSON file in all_names

    :param localizationPath: Path to localization file
    :param all_names: All names to search
    :returns: A name_callout string list to send one by one
    :raises: TODO
    """
    all_callouts: List[str] = []
    async with aioopen(localizationPath, mode="r") as f:
        file_content: str = await f.read()
    json_content: Dict = loads(file_content)
    for name in all_names:
        if name in json_content:
            all_callouts.append(choice(json_content[name]))
    return all_callouts
