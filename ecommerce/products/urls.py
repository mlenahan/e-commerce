from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<product_type>', views.ProductByTypeView.as_view()),
    path('<str:id>/', views.ProductDetailView.as_view(), name='detail'),
]