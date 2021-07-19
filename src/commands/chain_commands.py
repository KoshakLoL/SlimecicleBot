from __future__ import annotations
from json import loads
from aiofiles import open as aioopen
from typing import Dict, List, Union, Tuple
from os import path

import traceback
import re


class AnswerNode:
    def __init__(self, triggers: str, response: str, children: List[AnswerNode]) -> None:
        self.triggers: str = triggers
        self.response: str = response
        self.choices: List[AnswerNode] = children
        self._parent: Union[AnswerNode, None] = None

    async def add_answer(self, answer: AnswerNode) -> None:
        answer._parent = self
        self.choices.append(answer)

    async def has_choices(self) -> bool:
        return bool(self.choices)


class AnswerChain:
    def __init__(self, localization_path: str) -> None:
        self._localization_path: str = localization_path
        self._current_tree: AnswerNode = AnswerNode("", "", [])
        self._initialized = False

    async def load_tree(self) -> None:
        if self._initialized:
            raise TreeAlreadyInitialized(self._localization_path)
        async with aioopen(self._localization_path, mode="r") as f:
            file_content: str = await f.read()
        json_content: Dict = loads(file_content)
        await self.__set_current_tree(await dict_to_tree(json_content))
        self._initialized = True

    async def read_choice(self, text: str) -> str:
        tree = await self.current_tree
        if await tree.has_choices():
            for choice in tree.choices:
                if re.findall(re.compile(choice.triggers), text):
                    await self.__set_current_tree(choice)
                    return choice.response
        return ""

    @property
    async def current_tree(self) -> AnswerNode:
        """
        A note on how to retrieve information from the tree:
        It is HIGHLY discouraged to retrieve information straight from the tree,
        as it could be uninitialized, if someone decides to not call load_tree().

        What you should do instead, is ensure that the tree has been initizlied by doing
        Go-styled checks, like:
            tree, loaded = await chain.current_tree
            if not loaded:
                return  # or anything else you want to do with an error
            # ----

        It is not that ideal, yes, but it's better to completely break the script and get
        unexpected results. I've tried using the ":=" operator, but it completely breaks
        intellisense and also any sanity from python-exclusive logic.
        """
        if not self._initialized:
            raise TreeIsNotInitialized(self._localization_path)
        return self._current_tree

    async def __set_current_tree(self, new_tree: AnswerNode) -> None:
        self._current_tree = new_tree


class TreeAlreadyInitialized(Exception):
    def __init__(self, tree_path: str):
        super().__init__(f"Tree already initialized with path {tree_path}")


class TreeIsNotInitialized(Exception):
    def __init__(self, tree_path: str):
        super().__init__(
            f"Tree for {tree_path}. Have you called load_tree yet?"
        )


async def dict_to_tree(current_dict: Dict) -> AnswerNode:
    """Recursively converts dictionary to AnswerNode tree

    :param current_dict: Dictionary to convert
    :returns: AnswerNode with children
    :raises: TODO
    """
    current_node: AnswerNode = AnswerNode(
        current_dict["triggers"],
        current_dict["response"],
        []
    )
    if current_dict["choices"]:
        for choice in current_dict["choices"]:
            await current_node.add_answer(await dict_to_tree(choice))
    return current_node
