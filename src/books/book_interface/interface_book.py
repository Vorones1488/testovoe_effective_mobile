from typing import Any

from src.core.interface_core.interface_core import InterfaceDatabase
from src.core.interface_core.model import AbstractModel


class BookInterface(InterfaceDatabase):
    async def add(self, title: str, author: str, year: int) -> AbstractModel:
        raise NotImplementedError

    async def get_key(self, search_object: Any, value: Any) -> AbstractModel:
        raise NotImplementedError

    async def put(self, id: int, status: str) -> Any:
        raise NotImplementedError
