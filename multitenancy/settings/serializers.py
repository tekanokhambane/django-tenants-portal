from rest_framework import serializers
from .models import Logo


class LogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logo
        fields = ["id", "logo"]
