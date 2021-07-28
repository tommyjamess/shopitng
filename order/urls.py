from django.urls import path
from . import views



app_name = 'order'

urlpatterns = [
    path('', views.index, name='order'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('shopcart/', views.cart, name='cart' ),
    path('checkout/', views.checkout, name='checkout'),
    path('placeorder/', views.placeorder, name = 'placeorder'),
    path('ordercompleted/', views.ordercompleted, name='ordercompleted'),
    # path('updatequantity/', views.updatequantity, name= 'updatequantity'),
    path('deletefromcart/<str:id>', views.deletefromcart, name='deletefromcart'),
]