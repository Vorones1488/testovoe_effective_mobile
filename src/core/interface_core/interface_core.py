from abc import ABC, abstractmethod

from src.core.interface_core.model import AbstractModel


class InterfaceDatabase(ABC):
    # @abstractmethod
    # async def get_id(self,  id: int)-> AbstractModel:
    #     '''an abstract method for working with a database is getting by id'''
    #     raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> list[AbstractModel]:
        """abstract method getting a list of records"""
        raise NotImplementedError

    @abstractmethod
    async def add(self) -> AbstractModel:
        """an abstract method for adding"""
        raise NotImplementedError

    @abstractmethod
    async def dell_id(self, id: int) -> bool:
        """abstract method of deleting"""
        raise NotImplementedError

    @abstractmethod
    async def put(self, id) -> AbstractModel:
        raise NotImplementedError
