from dataclasses import dataclass
from enum import Enum, StrEnum
from typing import Literal, TypedDict


@dataclass(frozen=True)
class Filters:
    """Filters for laptops."""

    producer: tuple[str, ...]
    screen: tuple[str, ...]
    disk: tuple[str, ...]


@dataclass(frozen=True)
class FormData:
    """Form data."""

    filters: Filters
    search_term: str
    sort_by: str
    sort_order: dict[str, str]


@dataclass(frozen=True)
class Laptop:
    """Laptop data."""

    model: str
    screen: str
    disk: str
    ram: str
    weight: str
    performance: str
    price: str
    producer: str
