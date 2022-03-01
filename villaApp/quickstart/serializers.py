from rest_framework import serializers
from quickstart.models import villa


class villaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 150)
    description = serializers.CharField(max_length = 200)
    price = serializers.CharField(max_length=50)
    image = serializers.ImageField(default='', use_url=True)

    def create(self,validated_data):
        return villa.objects.create(**validated_data)
    

        