from fastapi import APIRouter, status
from src.port.usecase.order_get_usecase import OrderGetUseCase
from src.core.usecase.order_get_usecase import OrderGetUseCaseImpl
from src.adapter.spi.api.mapper.order_mapper import OrderMapper

router = APIRouter()
__orderGetUseCase: OrderGetUseCase = OrderGetUseCaseImpl()



@router.get(path='/status/pending', status_code=status.HTTP_200_OK)
async def getByOrderPending():    
    return OrderMapper.parseToResponseList(__orderGetUseCase.getByOrderPending())    
