from pydantic import BaseModel
from typing import List, Optional


class Rate(BaseModel):
    currency: str
    code: str
    mid: Optional[float]
    bid: Optional[float]
    ask: Optional[float]


class ExchangeRate(BaseModel):
    table: str
    no: str
    effectiveDate: str
    tradingDate: Optional[str]
    rates: List[Rate]
