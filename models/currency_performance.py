from dataclasses import dataclass
from typing import List
from dataclass_wizard import JSONWizard


@dataclass
class CurrencyPerformance:
    id: str
    symbol: str
    name: str
    image: str
    market_cap_rank: int
    usd: float
    usd_24h_vol: float
    usd_24h_change: float  # actual percentage change


@dataclass
class GainersAndLosers(JSONWizard):
    top_gainers: List[CurrencyPerformance]
    top_losers: List[CurrencyPerformance]
