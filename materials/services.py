import os

import stripe

API_KEY = os.getenv('STRIPE_SECRET_API_KEY')


def get_session(instance):
    """Функция создания ссылки для оплаты курсов"""

    stripe.api_key = API_KEY

    product = stripe.Product.create(
        name=f'{instance.name}'
    )

    price = stripe.Price.create(
        unit_amount=instance.price_amount,
        currency='usd',
        product=f'{product.id}',
    )

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[
            {
                'price': f'{price.id}',
                'quantity': 1,
            }
        ],
        mode='payment',
    )
    return session.url
