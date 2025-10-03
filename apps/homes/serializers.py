from rest_framework import serializers

from apps.homes.models import Category, Size, HomeImage, Home


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


class HomeSerializers(serializers.ModelSerializer):
    size = SizeSerializers(read_only=True)
    category = CategorySerializers(read_only=True)
    images = HomeImageSerializers(read_only=True, many=True)

    class Meta:
        model = Home
        fields = (
            "id", "name", "price", "review", "description", "size","category", "images", "color"
        )

