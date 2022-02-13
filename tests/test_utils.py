from src.utils import get_choices_from_string, replace_string_username, choose_file
from aiofiles import open as aioopen
from os import listdir
from typing import List
import pytest


@pytest.mark.asyncio
async def test_choices_from_string() -> None:
    res: List[str] = await get_choices_from_string("\n\nfirst choice\n\nsecond choice\n\n")
    assert res == ["first choice", "second choice"]


@pytest.mark.asyncio
async def test_username_replacement() -> None:
    username: str = "TestUsername"
    string: str = "Hey, $username!"
    assert await replace_string_username(string, username) == "Hey, TestUsername!"


@pytest.mark.asyncio
async def test_localization_files() -> None:
    file_output: str = ""
    for file in listdir("localization/choices"):
        async with aioopen(f"localization/choices/{file}", mode="r") as f:
            file_output = await f.read()
        assert file_output.find("\n\n\n") == -1
    for file in listdir("localization/choiceswithplaceholders"):
        async with aioopen(f"localization/choiceswithplaceholders/{file}", mode="r") as f:
            file_output = await f.read()
        assert file_output.find("\n\n\n") == -1


@pytest.mark.asyncio
async def test_file_random() -> None:
    assert await choose_file("src") in list(map(lambda file: f"src/{file}", listdir("src")))
