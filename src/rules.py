from vkbottle.bot import rules, Message
from typing import Dict, List, Union
from src.commands.chain_commands import AnswerChain
from src.botdataclasses.nodeInfo import NodeInfo
import re


class ChatOrPrivateRegex(rules.ABCRule):
    #  Custom rule for choosing between private message regular expression and a public one
    def __init__(self, chatRE: List[str], privateRE: List[str]):
        self.chatRE: List[str] = chatRE
        self.privateRE: List[str] = privateRE

    async def check(self, message: Message) -> bool:
        checkRE: List[str] = []
        checkRE = self.chatRE if message.peer_id != message.from_id else self.privateRE
        for rx in checkRE:
            match = re.match(re.compile(rx), message.text)
            if match:
                return True
        return False


class CheckChainsRule(rules.ABCRule):
    #  Custom rule to check all chains and find if there's anything that needs to be continued
    def __init__(self, chains_list: Dict[int, AnswerChain]):
        self.chains_list: Dict[int, AnswerChain] = chains_list

    async def check(self, message: Message) -> Union[Dict[str, NodeInfo], bool]:
        if message.from_id in self.chains_list:
            currentChain: AnswerChain = self.chains_list[message.from_id]
            result: NodeInfo = await currentChain.read_next_choice(message.text)
            if result.message:
                return {"match": result}
        return False


class FindAllRule(rules.ABCRule):
    #  Custom rule to find any names in a message
    def __init__(self, characters_list: Dict[str, List[str]]):
        self.characters_list: Dict[str, List[str]] = characters_list

    async def check(self, message: Message) -> Union[Dict[str, List[str]], bool]:
        all_matches: List[str] = []
        for character in self.characters_list:
            for character_name in self.characters_list[character]:
                if re.findall(re.compile(character_name), message.text):
                    all_matches.append(character)
        return {"match": list(set(all_matches))} if all_matches else False
