import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class OLHCV:
    unix_time: int
    time: datetime
    symbol: str
    open: int
    low: int
    high: int
    close: int
    volume: float
