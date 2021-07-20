import json

from config.celery import wait_payment_task
from django.http import HttpResponseRedirect
from subscriptions.payment_system.payment_factory import AbstractPaymentSystem
from django.conf import settings
from yookassa import Configuration, Payment
from yookassa.domain.response import PaymentResponse


CONFIG = settings.PAYMENT_SYSTEMS[settings.YOOMONEY]
RETURN_UTL = CONFIG["return_url"]

Configuration.configure(CONFIG["shop_id"], CONFIG["key"])


class YoomoneyPaymentSystem(AbstractPaymentSystem):

    def process_payment(self):
        response: PaymentResponse = Payment.create(
            {
                "amount": {
                    "value": self.payment.amount,
                    "currency": "RUB"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": RETURN_UTL
                },
                "capture": self.payment.amount,
                "description": f"Заказ {self.payment.amount}",
                "save_payment_method": True,
                "metadata": {
                  "order_id": "lalala"
                }
            }
        )
        data = json.loads(response.json())
        self.logger.info(data)
        self.payment.info = data
        self.payment.save()
        wait_payment_task.apply_async((response.id,), countdown=10, expires=60*5)
        return HttpResponseRedirect(response.confirmation.confirmation_url)

    def callback(self, *args, **kwargs):
        self.logger.info(args)
        self.logger.info(kwargs)

    def check_payment_status(self):
        payment_id = self.payment.info['id']
        response: PaymentResponse = Payment.find_one(payment_id=payment_id)
        self.logger.error(response.json())
        return response.status