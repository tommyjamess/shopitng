from django.urls import path
from . import views 

urlpatterns = [
    path('blog_content/', views.blogcontent, name='bcontent'),
    path('blog_detail/<str:id>/<slug:slug>', views.blogdetail, name='bdetail'),
    # path('comment/<str:id>', views.comment, name='comment')
]
