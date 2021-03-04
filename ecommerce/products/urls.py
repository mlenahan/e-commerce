from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('products/<product_type>/', views.ProductByTypeView.as_view()),
]