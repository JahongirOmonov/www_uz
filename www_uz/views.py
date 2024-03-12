from django.http import HttpResponse
from requests import Response
from rest_framework import filters
from django.db.models import Count
from utils.choices import Browsers
from utils.choices import Operation_systems
from rest_framework import generics
from users.models import User
from www_uz.models import Category, Website, Visitor
from www_uz import serializers
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.

class CategoriesListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryOriginalSerializer

class WebsiteDetailApiView(generics.RetrieveAPIView):
    queryset = Website.objects.all()
    serializer_class = serializers.WebsiteSerializer

class WebsitesCategoryTitleListApiView(generics.ListAPIView):
    queryset = Website.objects.all()
    serializer_class = serializers.WebsiteSerializer
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
    serializer_class = serializers.WebsiteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subcategory__title']

    def get_queryset(self):
        queryset = super().get_queryset()
        subcategory_title = self.request.query_params.get('subcategory_title')
        if subcategory_title:
            queryset = queryset.filter(subcategory__title=subcategory_title)
        return queryset

class WebsiteTasixListApiView(generics.ListAPIView):
    queryset = Website.website_manager.tasix()
    serializer_class = serializers.WebsiteSerializer



class CategorywithSubListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorywithSubSerializer

class OsDiagramListApiView(generics.ListAPIView):
    serializer_class = serializers.UserOsSerializer

    def get_queryset(self):
        total_os = User.objects.all().count()

        os_count = User.objects.values('operatsion_system').annotate(user_count = Count('operatsion_system'))
        list_info = list()
        fornow = []
        for i in os_count:
            operation_system = i['operatsion_system']
            fornow.append(operation_system)
            user_count = i['user_count']
            percentage = user_count/total_os *100 if total_os > 0 else 0
            list_info.append({
                'operation_system':operation_system,
                'user_count':user_count,
                'percentage':percentage
            })

        for i in Operation_systems:
            if str(i) not in fornow:
                list_info.append({
                    'operation_system': str(i),
                    'user_count': 0,
                    'percentage': 0
                })

        return list_info

class BrowserDiagramListApiView(generics.ListAPIView):
    serializer_class = serializers.UserBrowserSerializer

    def get_queryset(self):
        total_users = User.objects.all().count()
        browser_count = User.objects.values('browser').annotate(user_count = Count('browser'))
        info_list = []
        fornow = []
        for i in browser_count:
            browser_name = i['browser']
            fornow.append(browser_name)
            user_count = i['user_count']
            if total_users > 0:
                browser_percentage = user_count/total_users  * 100
            else:
                browser_percentage = 0
            info_list.append({
                'browser_name':browser_name,
                'user_count':user_count,
                'percentage':browser_percentage
            })

        for i in Browsers:
            if str(i) not in fornow:
                info_list.append({
                    'browser_name': str(i),
                    'user_count': 0,
                    'percentage': 0
                })

        return info_list


class websitelar(generics.ListAPIView):
    queryset = Website.objects.all()
    serializer_class = serializers.WebsiteSerializer

class WebsiteStatisticsAPIView(APIView):
    def get(self, request, website_id):
        website = Website.objects.get(id=website_id)
        thirty_days_ago = timezone.now() - timedelta(days=30)
        total_visitors = Visitor.objects.filter(website=website, joined_date__gte=thirty_days_ago).count()
        tasix_visitors = Visitor.objects.filter(website=website, user__is_tasix=True, joined_date__gte=thirty_days_ago).count()
        data = {
            'website_id': website.id,
            'website_title': website.title,
            'total_visitors_last_30_days': total_visitors,
            'tasix_visitors_last_30_days': tasix_visitors
        }
        return Response(data)



def home_page(request):
    return HttpResponse("<html><title>To-Do lists</title></html>")


from django.utils import timezone
from datetime import datetime
class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
                # filter(date_joined__year = '2024',
                #                          date_joined__month = '03',
                #                          date_joined__day = '07'
                #                          ))
    serializer_class = serializers.UserBrowserSerializer


















# class VisitorListApiView(generics.ListAPIView):
#     queryset = Visitor.objects.all()
#     serializer_class = VisistorSerializer






#prosta




# class CategoryDiagramListApiView(generics.ListAPIView):
#     serializer_class = CategorySerializer  # Define your serializer class
#
#
#     def get_queryset(self):
#         queryset = Category.objects.all()
#         xxx = Category.objects.annotate(
#             total_websites=Count('subcategories__websites', distinct=True)
#         )
#
#         # Calculate the total number of websites across all categories
#         total_websites_count = sum(category.total_websites for category in xxx)
#
#         # Calculate the percentage of websites for each category
#         data = []
#         for category in queryset:
#             category_percentage = (category.total_websites / total_websites_count) * 100
#             data.append({
#                 'category_title': category.title,
#                 'website_percentage': category_percentage
#             })
#
#         return Response(data)















