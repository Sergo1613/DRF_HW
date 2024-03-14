import re

from rest_framework import serializers


def validator_scam_url(value):
    """ Валидация ссылки на материал """

    pattern = re.compile(r'^https?://(?:www\.)?youtube\.com/.*')
    for link in value.split():
        if not pattern.match(link):
            raise serializers.ValidationError(f"Invalid YouTube URL: '{link}'")
