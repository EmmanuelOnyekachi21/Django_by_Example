from django.urls import path
from . import views

urlpatterns = [
    # Post views
    # view tags - must come before the date-based pattern
    path('tags/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('', views.post_list, name='post_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'
    ),
    path('<uuid:post_id>/share/', views.post_share, name="post_share"),
    path(
        '<uuid:post_id>/comment/',
        views.post_comment,
        name="post_comment"
    ),
]
