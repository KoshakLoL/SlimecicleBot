from src.utils import get_choices_from_string, replace_string_username, choose_file
from aiofiles import open as aioopen
from os import listdir, path
import pytest


@pytest.mark.asyncio
async def test_choices_from_string():
    res = await get_choices_from_string("\n\nfirst choice\n\nsecond choice\n\n")
    assert res == ["first choice", "second choice"]


@pytest.mark.asyncio
async def test_username_replacement():
    username = "TestUsername"
    string = "Hey, $username!"
    assert await replace_string_username(string, username) == "Hey, TestUsername!"


@pytest.mark.asyncio
async def test_localization_files():
    for file in listdir("localization/choices"):
        async with aioopen(f"localization/choices/{file}", mode="r") as f:
            res = await f.read()
        assert res.find("\n\n\n") == -1
    for file in listdir("localization/choiceswnames"):
        async with aioopen(f"localization/choiceswnames/{file}", mode="r") as f:
            res = await f.read()
        assert res.find("\n\n\n") == -1


@pytest.mark.asyncio
async def test_file_random():
    assert await choose_file("src") in list(map(lambda file: f"src/{file}", listdir("src")))
