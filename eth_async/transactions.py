from __future__ import annotations
from typing import TYPE_CHECKING

from web3 import Web3

from .models import TokenAmount

if TYPE_CHECKING:
    from .client import Client


class Transactions:
    def __init__(self, client: Client) -> None:
        self.client = client

    @staticmethod
    async def gas_price(w3: Web3) -> TokenAmount:
        return TokenAmount(amount=await w3.eth.gas_price(), wei=True)
