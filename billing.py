import stripe
import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def create_checkout_session(user, plan):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': plan,
            'quantity': 1,
        }],
        mode='subscription',
        success_url='http://localhost:5001/success',
        cancel_url='http://localhost:5001/cancel',
    )
    return session.url