from aiofiles import open as aioopen
from random import choice
from os import listdir, path
from vkbottle.bot import rules, Message
from typing import Union, Dict, List, Pattern
import re

#  Custom rule to find any names in a message:


class FindAllRule(rules.ABCMessageRule):
    def __init__(self, characters_list: Dict[str, List[str]]):
        self.characters_list = characters_list

    async def check(self, message: Message) -> Union[dict, bool]:
        all_matches = []
        for character in self.characters_list:
            for character_name in self.characters_list[character]:
                if message.text.find(character_name) != -1:
                    all_matches.append(character)
        return {"match": all_matches} if all_matches else False


async def get_choices_from_string(string: str) -> List[str]:
    """Returns choices from string, separated by "\n\n" union of characters

    :param string: original string with separated choices
    :returns: list of separated strings
    :raises: TODO
    """

    return list(filter(lambda line: line, string.split("\n\n")))


async def replace_string_username(string: str, username: str) -> str:
    """Returns string's $username replaced by username variable

    :param string: original string
    :param: username: replacemenet for $username
    :returns: string with replaced $username
    :raises: TODO
    """
    return string.replace("$username", username)


async def choose_file(directory: str) -> str:
    """Lists directory and returns a random filename

    :param directory: directory to choose from (with an absolute path!)
    :returns: random filename from a folder
    :raises: TODO
    """
    return path.join(directory, choice(listdir(directory)))
