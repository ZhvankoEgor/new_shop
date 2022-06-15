from django.test import TestCase
from django.urls import reverse


class ViewTestCase(TestCase):

    def test_edit_settings_bot_another_user(self):
        url = reverse("payment:payment_notification")
        data2 = {
                      "type": "notification",
                      "event": "payment.waiting_for_capture",
                      "object": {
                    "id": "29f88651-000f-5000-8000-1a92f12695bc",
                        "status": "waiting_for_capture",
                        "paid": 1,
                        "amount": {
                          "value": "2.00",
                          "currency": "RUB"
                        },
                        "authorization_details": {
                          "rrn": "10000000000",
                          "auth_code": "000000",
                          "three_d_secure": {
                            "applied": 1
                          }
                        },
                        "created_at": "2018-07-10T14:27:54.691Z",
                        "description": "Заказ №72",
                        "expires_at": "2018-07-17T14:28:32.484Z",
                        "metadata": {},
                        "payment_method": {
                          "type": "bank_card",
                          "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                          "saved": 0,
                          "card": {
                            "first6": "555555",
                            "last4": "4444",
                            "expiry_month": "07",
                            "expiry_year": "2021",
                            "card_type": "MasterCard",
                          "issuer_country": "RU",
                          "issuer_name": "Sberbank"
                          },
                          "title": "Bank card *4444"
                        },
                        "refundable": 1,
                        "test": 1
                      }
                    }
        response2 = self.client.post(url, data2)
        self.assertEqual(response2.status_code, 200)
