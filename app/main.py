from fastapi import FastAPI
from app.models import PaymentRequest, PaymentResponse
from app.constant import STATUS_PAID, MESSAGE_SUCCESS

app = FastAPI()

@app.post("/payment", response_model=PaymentResponse)
async def process_payment(payment: PaymentRequest):
    """
    Заглушка для обработки платежа.
    Всегда возвращает, что оплата успешна.
    """
    return PaymentResponse(
        status=STATUS_PAID,
        message=MESSAGE_SUCCESS
    )
