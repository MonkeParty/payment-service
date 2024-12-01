from pydantic import BaseModel

# Модель запроса, которую будет отправлять сервис subscription
class PaymentRequest(BaseModel):
    user_id: int # пользователь
    subscription: str # какую подписку собирается купить
    # предлагаю сделать 2 вида 'premium' & 'base' ну как вариант

# Модель ответа, который сервис payment будет возвращать
class PaymentResponse(BaseModel):
    status: str  # статус оплаты
    message: str  # описание