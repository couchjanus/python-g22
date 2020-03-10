from django.urls import path  
from . import views  
  
app_name = 'blog'  
  
urlpatterns = [  
    # post views  
    path('', views.PostListView.as_view(), name='post_list'),  
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'), 
]

