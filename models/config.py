from dataclasses import dataclass
from typing import Literal
from dataclass_wizard import JSONWizard


@dataclass
class Config(JSONWizard):
    amount: int
    stop_loss: int
    take_profit: int
    bot_frequency_in_seconds: int
    vs_currency: str
    number_of_assets: int
    mode: Literal["GAINING", "LOSING"]
