from vkbottle.bot import Blueprint, Message
from typing import Dict, List
from src.commands.chain_commands import AnswerChain
from src.rules import CheckChainsRule, FindAllRule
from src.botdataclasses.nodeInfo import NodeInfo

bp = Blueprint("On chain messages")
chains: Dict[int, AnswerChain] = {}


@bp.on.message(FindAllRule({
    "ranboo": [
        r"(?i)^(ранбу|ranboo)$"
    ]
}))
async def chains_start(message: Message, match: List[str]) -> None:
    message_author: int = message.from_id
    if message_author not in chains:
        new_chain: AnswerChain = AnswerChain(
            f"localization/trees/{match[0]}.json",
            bp.api,
            message.peer_id
        )
        await new_chain.load_tree()
        # Getting the starting message as the only choice:
        starting_message: NodeInfo = await new_chain.read_current_choice()
        await message.answer(
            starting_message.message,
            attachment=starting_message.attachment
        )
        chains[message_author] = new_chain


@bp.on.message(CheckChainsRule(chains))
async def check_chains(message: Message, match: NodeInfo) -> None:
    message_author: int = message.from_id
    chain = chains[message_author]
    if await chain.is_destroyed():
        await pop_chain(message_author)
    else:
        await chain.cancel_timer()
        await message.answer(
            match.message,
            attachment=match.attachment
        )
        tree = await chain.current_tree
        continuing = await tree.has_choices()
        if not continuing:
            await pop_chain(message_author)


async def pop_chain(pop_id: int) -> None:
    chains.pop(pop_id)
