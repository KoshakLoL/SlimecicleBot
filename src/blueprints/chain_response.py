from vkbottle.bot import Blueprint, Message
from vkbottle_types.objects import UsersUser
from typing import Dict, Tuple
from src.commands.chain_commands import AnswerChain
from src.rules import CheckChainsRule, FindAllRule
from src.utils import AsynchronusTimerToCallback

bp = Blueprint("On chain messages")
chains: Dict[int, AnswerChain] = {}
timers: Dict[int, AsynchronusTimerToCallback] = {}


@bp.on.message(FindAllRule({
    "ranboo": [
        r"(?i)^(ранбу|ranboo)$"
    ]
}))
async def chains_start(message: Message, match: list[str]) -> None:
    message_author: int = message.from_id
    if message_author not in chains:
        new_chain: AnswerChain = AnswerChain(
            f"localization/trees/{match[0]}.json"
        )
        await new_chain.load_tree()
        chains[message_author] = new_chain
        tree = await new_chain.current_tree
        await message.answer(tree.response)
        timers[message_author] = AsynchronusTimerToCallback(
            pop_chain, 20, message_author
        )


@bp.on.message(CheckChainsRule(chains))
async def check_chains(message: Message, match: str) -> None:
    message_author: int = message.from_id
    await timers[message_author].cancel_timer()
    await message.answer(match)
    tree = await chains[message_author].current_tree
    if await tree.has_choices():
        timers[message_author] = AsynchronusTimerToCallback(
            pop_chain, 20, message_author
        )
    else:
        await pop_chain(message_author)


async def pop_chain(pop_id: int) -> None:
    chains.pop(pop_id)
    timers.pop(pop_id)
