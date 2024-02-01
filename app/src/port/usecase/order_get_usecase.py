from abc import abstractmethod, ABC
from typing import List
from src.core.domain.order import Order


class OrderGetUseCase(ABC):
    @abstractmethod
    def getByOrderPending(self) -> List[Order]:
        raise NotImplementedError
