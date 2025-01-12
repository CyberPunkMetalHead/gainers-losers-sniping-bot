from dataclasses import dataclass
import datetime
from typing import List
from dataclass_wizard import JSONWizard


@dataclass
class Fill:
    price: str
    qty: str
    commission: str
    commissionAsset: str
    tradeId: int


@dataclass
class OrderResponse(JSONWizard):
    symbol: str
    orderId: int
    orderListId: int
    clientOrderId: str
    transactTime: int
    price: str
    origQty: str
    executedQty: str
    origQuoteOrderQty: str
    cummulativeQuoteQty: str
    status: str
    timeInForce: str
    type: str
    side: str
    workingTime: datetime
    fills: List[Fill]
    selfTradePreventionMode: str
