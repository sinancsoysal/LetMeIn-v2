from rest_framework import serializers

from .models import Verification, ShortenedId


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = '__all__'


class ShortenedIdSerializer(serializers.ModelSerializer):
    verification = VerificationSerializer(required=False)

    class Meta:
        model = ShortenedId
        fields = '__all__'
