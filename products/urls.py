from django.urls import path
from .import views 


urlpatterns = [
    path('product_page/', views.products, name='products'),
    path('product_detail/<str:id>', views.prod_detail, name = 'prod_detail'),
    path('category/<str:id>', views.category, name='category'),
    path('brands/<str:id>', views.brands, name='brands'),
    path('review/', views.review_rate, name='review'),
]
