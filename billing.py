import stripe
from flask import request, url_for
import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def create_checkout_session(user, plan):
    # Get the base URL from the current request
    base_url = request.url_root.rstrip('/')
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': plan,
            'quantity': 1,
        }],
        mode='subscription',
        success_url=f"{base_url}{url_for('success')}",
        cancel_url=f"{base_url}{url_for('cancel')}",
    )
    return session.url