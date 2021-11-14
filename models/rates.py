from pydantic import BaseModel
from typing import List, Optional


class RateInfo(BaseModel):
    no: str
    effectiveDate: str
    tradingDate: Optional[str]
    mid: Optional[float]
    bid: Optional[float]
    ask: Optional[float]


class Rate(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[RateInfo]
