from django.urls import path
from www_uz import views


urlpatterns = [
    path('categories/', views.CategoriesListApiView.as_view()),
    path('website/<int:pk>', views.WebsiteDetailApiView.as_view()),
    path('website-ct-title/', views.WebsitesCategoryTitleListApiView.as_view()),

    path('website-sub-title/', views.WebsitesSubcategoryTitleListApiView.as_view()),
    path('website-tasix/', views.WebsiteTasixListApiView.as_view()),
    path('categories-subcategories/', views.CategorywithSubListApiView.as_view()),
    path('os-diagram/', views.OsDiagramListApiView.as_view()),

    path('browser-diagram/', views.BrowserDiagramListApiView.as_view()),
    path('websites/', views.websitelar.as_view()),
    path('website-statistics/<int:website_id>', views.WebsiteStatisticsAPIView.as_view()),
    # path('category-diagram/', views.CategoryDiagramListApiView.as_view()),


    path('homepage/', views.home_page),
]



