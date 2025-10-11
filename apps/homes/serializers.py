from rest_framework import serializers

from apps.homes.models import Category, Size, HomeImage, Home, Color


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id", "name"
        )

class SizeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = (
            "id", "name"
        )

class HomeImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = HomeImage
        fields = (
            "id", "image"
        )


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = (
            "id", "name"
        )


class HomeSerializers(serializers.ModelSerializer):
    size = SizeSerializers(read_only=True, many=True)
    category = CategorySerializers(read_only=True)
    images = HomeImageSerializers(read_only=True, many=True)
    discount_price = serializers.SerializerMethodField(read_only=True)
    color = ColorSerializer(many=True)

    class Meta:
        model = Home
        fields = (
            "id", "name", "price", "discount", "discount_price", "scu", "review", "description", "size","category", "images", "color"
        )

    @staticmethod
    def get_discount_price(obj):
        if obj.discount:
            return obj.price - (obj.price * obj.discount / 100)
        return obj.price

