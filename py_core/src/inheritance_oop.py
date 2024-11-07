#Inheritance
class Python:
    def __init__(self):
        self.is_cool = True

class FastAPI(Python):
    pass

f = FastAPI()
print(f.is_cool)

#Output: True

#Multiple Inheritance
class PaypalPayment:
    payment_approved = True

    def is_approved(self):
        return self.payment_approved

class StripePayment:
    payment_approved = False

    def is_approved(self):
        return self.payment_approved

class PaymentVerification(StripePayment, PaypalPayment):
    pass

payment = PaymentVerification
print(payment.is_approved)

#Output: False