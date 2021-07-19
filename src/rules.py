from vkbottle.bot import rules, Message
from typing import Dict, List, Union
from src.commands.chain_commands import AnswerChain
import re


class CheckChainsRule(rules.ABCMessageRule):
    #  Custom rule to check all chains and find if there's anything that needs to be continued
    def __init__(self, chains_list: Dict[int, AnswerChain]) -> None:
        self.chains_list: Dict[int, AnswerChain] = chains_list

    async def check(self, message: Message) -> Union[Dict[str, str], bool]:
        if message.from_id in self.chains_list:
            result = await self.chains_list[message.from_id].read_choice(message.text)
            if result:
                return {"match": result}
        return False


class FindAllRule(rules.ABCMessageRule):
    #  Custom rule to find any names in a message
    def __init__(self, characters_list: Dict[str, List[str]]) -> None:
        self.characters_list: Dict[str, List[str]] = characters_list

    async def check(self, message: Message) -> Union[Dict[str, List[str]], bool]:
        all_matches: List[str] = []
        for character in self.characters_list:
            for character_name in self.characters_list[character]:
                if re.findall(re.compile(character_name), message.text):
                    all_matches.append(character)
        return {"match": list(set(all_matches))} if all_matches else False
