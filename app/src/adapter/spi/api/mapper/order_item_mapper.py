from typing import List
from src.core.domain.order_item import OrderItem
from src.adapter.spi.api.schema.base_response import BaseResponse
from src.adapter.spi.api.schema.order_item_response import OrderItemResponse


class OrderItemMapper:
    @staticmethod
    def parseToResponse(domain: OrderItem) -> BaseResponse[OrderItemResponse]:
        return BaseResponse(data=OrderItemResponse(productCode=domain.productCode,productName=domain.productName, 
                            quantity=domain.quantity,amount=domain.amount,note=domain.note))
    
    @staticmethod
    def parseToResponseList(domainList: List[OrderItemResponse]) -> BaseResponse[OrderItemResponse]:
        return BaseResponse(data=[OrderItemMapper.parseToResponse(domain).data for domain in domainList])        
