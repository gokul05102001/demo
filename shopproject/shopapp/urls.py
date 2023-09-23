from django.contrib import admin
from django.urls import path
from . import views
app_name='shopapp'

urlpatterns = [
    path('',views.allproductscategory,name='allproductscategory'),
    path('<slug:c_slug>/',views.allproductscategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDets, name='proDets'),
]