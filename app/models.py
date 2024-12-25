from pydantic import BaseModel

# Модель запроса, которую будет отправлять сервис subscription
class PaymentRequest(BaseModel):
    user_id: int # пользователь

# Модель ответа, который сервис payment будет возвращать
class PaymentResponse(BaseModel):
    status: str  # статус оплаты