from rest_framework import serializers
from .models import Category, Subcategory, Website, Visitor
from users.models import User

class CategoryOriginalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
        )
class VisitorSerializere(serializers.ModelSerializer):
    total_users = serializers.IntegerField()
    tasix_users = serializers.IntegerField()
    joined_date = serializers.DateTimeField()
    class Meta:
        model = Visitor
        fields = (
            'total_users',
            'tasix_users',
            'joined_date'
        )



class CategorySerializer(serializers.ModelSerializer):
    category_title = serializers.CharField()
    website_percentage = serializers.FloatField()
    class Meta:
        model = Category
        fields = (
            'id',
            'category_title',
            'website_percentage'
        )



class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = (
            'id',
            'title',
            'category'
        )

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = (
            'id',
            'url',
            'title',
            'description',
            'position_in_list',
            'is_tasix',
            'subcategory'
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

class UserOsSerializer(serializers.ModelSerializer):
    operation_system = serializers.CharField()
    user_count = serializers.IntegerField()
    percentage = serializers.FloatField()
    class Meta:
        model = User
        fields = (
            'operation_system',
            'user_count',
            'percentage'
        )

class UserBrowserSerializer(serializers.ModelSerializer):
    browser_name = serializers.CharField()
    user_count = serializers.IntegerField()
    percentage = serializers.FloatField()
    class Meta:
        model = User
        fields=(
            'browser_name',
            'user_count',
            'percentage'
        )






























