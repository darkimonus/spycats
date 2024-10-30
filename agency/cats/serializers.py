from cats.models import SpyCat
from rest_framework import serializers


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['name', 'experience', 'breed', 'salary']


class SpyCatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['salary']
