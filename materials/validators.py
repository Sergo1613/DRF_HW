from urllib.parse import urlparse

from rest_framework import serializers


def validator_scam_url(value):
    """Валидация ссылки на материал"""

    for link in value.split():
        parsed_url = urlparse(link)
        if parsed_url.netloc != 'youtube.com':
            raise serializers.ValidationError(f"You are using banned link: '{parsed_url.netloc}', only 'youtube.com'")