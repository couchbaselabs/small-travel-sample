from dataclasses import dataclass, field


@dataclass
class Query:
    id: str
    query: str
    docs: list[str] = field(default_factory=list)
    no_docs: int = field(default=0)
