from rest_framework import filters

from django.shortcuts import render
from rest_framework import generics

from www_uz.models import Category, Website
from www_uz.serializers import CategorySerializer, WebsiteSerializer, CategorywithSubSerializer


# Create your views here.

class CategoriesListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WebsiteDetailApiView(generics.RetrieveAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

class WebsiteTasixListApiView(generics.ListAPIView):
    queryset = Website.website_manager.tasix()
    serializer_class = WebsiteSerializer


class WebsitesCategoryTitleListApiView(generics.ListAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subcategory__category__title']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.request.query_params.get('category_title')
        if category_title:
            queryset = queryset.filter(subcategory__category__title=category_title)
        return queryset


class WebsitesSubcategoryTitleListApiView(generics.ListAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subcategory__title']

    def get_queryset(self):
        queryset = super().get_queryset()
        subcategory_title = self.request.query_params.get('subcategory_title')
        if subcategory_title:
            queryset = queryset.filter(subcategory__title=subcategory_title)
        return queryset


class CategorywithSubListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorywithSubSerializer
