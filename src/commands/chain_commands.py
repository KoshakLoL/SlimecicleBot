from __future__ import annotations
from json import loads
from aiofiles import open as aioopen
from typing import Dict, List, Optional
from src.commands.image_load import get_photo, get_document
from vkbottle.api import API
from src.botdataclasses.nodeInfo import NodeInfo

import re


class AnswerNode:
    def __init__(self,
                 triggers: str,
                 response: Optional[str],
                 image: Optional[str],
                 document: Optional[str],
                 children: List[AnswerNode]) -> None:
        self.triggers: str = triggers
        self.response: Optional[str] = response
        self.image: Optional[str] = image
        self.document: Optional[str] = document
        self.choices: List[AnswerNode] = children
        self.__parent: Optional[AnswerNode] = None

    async def add_answer(self, answer: AnswerNode) -> None:
        answer.__parent = self
        self.choices.append(answer)

    async def has_choices(self) -> bool:
        return bool(self.choices)


class AnswerChain:
    def __init__(self, localization_path: str, vk_api: API, pid: int) -> None:
        self.__localization_path: str = localization_path
        self.vk_api: API = vk_api
        self.pid: int = pid
        self.__current_tree: AnswerNode = AnswerNode(
            "", None, None, None, []
        )
        self.__initialized = False

    async def load_tree(self) -> None:
        if self.__initialized:
            raise TreeAlreadyInitialized(self.__localization_path)
        async with aioopen(self.__localization_path, mode="r") as f:
            file_content: str = await f.read()
        json_content: Dict = loads(file_content)
        await self.__set_current_tree(await dict_to_tree(json_content))
        self.__initialized = True

    async def read_next_choice(self, text: str) -> NodeInfo:
        tree = await self.current_tree
        if await tree.has_choices():
            for choice in tree.choices:
                if re.findall(re.compile(choice.triggers), text):
                    await self.__set_current_tree(choice)
                    return await self.read_node(choice)
        return NodeInfo("", None)

    async def read_current_choice(self) -> NodeInfo:
        return await self.read_node(await self.current_tree)

    async def read_node(self, node: AnswerNode) -> NodeInfo:
        messageStr: str = ""
        attachmentStr: str = ""
        if node.response:
            messageStr += f"{node.response} "
        if node.image:
            attachmentStr += f"{await get_photo(node.image, self.vk_api)} "
        elif node.document:
            document = await get_document(
                node.document,
                self.vk_api,
                self.pid
            )
            attachmentStr += f"{document} "
        return NodeInfo(messageStr, attachmentStr if attachmentStr else None)

    @property
    async def current_tree(self) -> AnswerNode:
        if not self.__initialized:
            raise TreeIsNotInitialized(self.__localization_path)
        return self.__current_tree

    async def __set_current_tree(self, new_tree: AnswerNode) -> None:
        self.__current_tree = new_tree


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
        current_dict["image"],
        current_dict["document"],
        []
    )
    if current_dict["choices"]:
        for choice in current_dict["choices"]:
            await current_node.add_answer(await dict_to_tree(choice))
    return current_node
