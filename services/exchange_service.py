from models.order import OrderResponse
from utils.load_env import *
from binance.client import Client


class Binance:
    def __init__(self):
        self.client = Client(binance_api_key, binance_api_secret)

    def buy(
        self, coin: str, amount_in_vs_currency: float, vs_currency: str = "USDT"
    ) -> OrderResponse:
        response = self.client.order_market_buy(
            symbol=(coin + vs_currency).upper(),
            quoteOrderQty=amount_in_vs_currency,
        )
        return OrderResponse.from_dict(response)

    def sell(self, coin: str, amount_in_vs_currency: float) -> OrderResponse:
        response = self.client.order_market_sell(
            symbol=(coin).upper(),
            quoteOrderQty=amount_in_vs_currency,
        )
        return OrderResponse.from_dict(response)

    def get_current_price(self, coin: str) -> float:
        return float(self.client.get_ticker(symbol=coin)["lastPrice"])
