from rest_framework import serializers
from network.models import Link, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError({'debt': 'вы не должны изменять это поле', })
        return super().update(instance, validated_data)

    class Meta:
        model = Link
        fields = '__all__'
