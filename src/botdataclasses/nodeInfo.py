from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class NodeInfo:
    message: str
    attachment: Optional[str]
