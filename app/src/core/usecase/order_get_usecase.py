from typing import List
from src.core.domain.order import Order
from src.core.domain.order_item import OrderItem
from src.core.domain.product import Product
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.port.usecase.order_get_usecase import OrderGetUseCase
from src.port.usecase.product_get_usecase import ProductGetUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.order_repository import OrderRepository
from src.adapter.spi.persistence.mapper.order_mapper import OrderMapper
from src.core.util.string_util import StringUtil
from src.core.util.logger_custom import Logger


class OrderGetUseCaseImpl(OrderGetUseCase):
    def __init__(self):
        self.__respository: Repository = OrderRepository()
       
    def getByOrderPending(self) -> List[Order]:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search order peding")
        orderList: List[Order] = OrderMapper.parseToDomainList(self.__respository.findByFilter({'status': {'$ne': OrderStatusEnum.FINISHED.value}}))
        orderList.sort(key=lambda order: order.issueDateTime, reverse=True)        
        return orderList
