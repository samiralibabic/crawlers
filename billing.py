import stripe

stripe.api_key = 'sk_test_51NHtKhGWWC4TWCaW3qnVFCeC5FXmQYrvpr2XJPU8An4nWlKxO8HWUOfI7WLQI9LAl0FPzqp3NF46DOlxUOlC6QLH00wsVFVVve'

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