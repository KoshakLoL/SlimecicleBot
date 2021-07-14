from vkbottle.bot import Blueprint, Message
from vkbottle_types.objects import UsersUser
from typing import Dict, Tuple
from src.commands.chain_commands import AnswerChain
from src.rules import CheckChainsRule
from src.utils import AsynchronusTimer

bp = Blueprint("On chain messages")
chains: Dict[int, AnswerChain] = {}
timers: Dict[int, AsynchronusTimer] = {}


@bp.on.message(regexp=[
    r"(?i).*(ранбу|ranboo).*"
])
async def ranboo_chain_start(message: Message, match: Tuple) -> None:
    if message.from_id not in chains:
        new_chain: AnswerChain = AnswerChain("localization/trees/ranboo.json")
        if await new_chain.load_tree():
            chains[message.from_id] = new_chain
            tree, loaded = await new_chain.current_tree
            if loaded:
                await message.answer(tree.response)
            timers[message.from_id] = AsynchronusTimer(message, 20, pop_chain)


@bp.on.message(CheckChainsRule(chains))
async def check_chains(message: Message, match: str) -> None:
    tree, loaded = await chains[message.from_id].current_tree
    if loaded:
        await timers[message.from_id].cancel()
        timers[message.from_id] = AsynchronusTimer(message, 20, pop_chain)
        await message.answer(match)
        if not await tree.check_choices():
            chains.pop(message.from_id)


async def pop_chain(original_message: Message) -> None:
    if original_message.from_id in chains:
        chains.pop(original_message.from_id)
        user: UsersUser = await original_message.get_user()
        await original_message.answer(
            f"well, I think that I'm out of time, {user.first_name}!\n"
            f"I crawl back into my slimy hole BYEee-BYEEEEE !"
        )
