from random import choice
from os import listdir, path
from vkbottle.bot import Message
from typing import List, Callable
import asyncio


class AsynchronusTimer:
    # Thanks, Mikhail!

    def __init__(self, original_message: Message, wait_time: int, callback: Callable) -> None:
        self._wait_time: int = wait_time
        self._original_message: Message = original_message
        self._callback: Callable = callback
        self._timer: asyncio.Task = asyncio.create_task(self._wait())

    async def _wait(self) -> None:
        await asyncio.sleep(self._wait_time)
        await self._callback(self._original_message)

    async def cancel(self) -> None:
        self._timer.cancel()


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
