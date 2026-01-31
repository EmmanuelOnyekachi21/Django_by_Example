from django.urls import path
from . import views

urlpatterns = [
    # Post views
    path('', views.post_list, name='post_list'),
    path('<uuid:id>/', views.post_detail, name='post_detail'),
]
