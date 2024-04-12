import stripe
from materials.models import Course

API_KEY = 'sk_test_51P4pXmIXyokdXewBsMpiK2csqmf1ZAcBX2eXfM15j7h79s7jXALg3sYbeKupU63CuBJ6cJ6MzpeV4YaZbE7jGBxH001oyoP7jZ'


def get_link_of_payment():
    """Функция создания ссылки для оплаты курсов"""

    stripe.api_key = API_KEY

    product = stripe.Product.create(
        name=Course.preview
    )

    price = stripe.Price.create(
        currency="usd",
        unit_amount=Course.price,
        recurring={"interval": "month"},
        product_data={"name": product.id},
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
    )

    return session.url


def get_session(instance):
    """Функция создания ссылки для оплаты курсов"""

    stripe.api_key = API_KEY

    product = stripe.Product.create(
        name=f'{Course.preview}'
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
