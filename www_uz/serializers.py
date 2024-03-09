from rest_framework import serializers
from .models import Category, Subcategory, Website

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = (
            'id',
            'title',
            'category'
        )

class CategorywithSubSerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'subcategories'
        )


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = (
            'id',
            'title',
            'description',
            'position_in_list',
            'is_tasix',
            'visitors',
            'views',
            'subcategory'
        )
