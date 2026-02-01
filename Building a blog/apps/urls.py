from django.urls import path, include


urlpatterns = [
    path('posts/', include('apps.blog.urls'))
]
