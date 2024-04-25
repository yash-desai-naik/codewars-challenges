from dataclasses import dataclass


@dataclass
class Status:
    verified: bool
    sentCount: int
    feedback: str | None = None


@dataclass
class CatFact:
    _id: str
    status: Status
    user: str
    source: str
    updatedAt: str
    type: str
    createdAt: str
    deleted: bool
    used: bool
    text: str
    __v: int = 0  # Set default value to 0
