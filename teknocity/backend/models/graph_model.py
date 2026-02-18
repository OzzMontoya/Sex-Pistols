from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class IntersectionNode:
    id: str
    state: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RoadEdge:
    source: str
    target: str
    metadata: dict[str, Any] = field(default_factory=dict)
