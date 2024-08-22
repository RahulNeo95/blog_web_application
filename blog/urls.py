from django.urls import path
from .views import BlogListView, BlogDetailView, BlogEditView, BlogDeleteView, BlogCreateView


from .views import PostAPIListView, PostAPIDetailView

urlpatterns=[
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/create', BlogCreateView.as_view(), name='post_create'),

    path('api/posts/', PostAPIListView.as_view(), name='post_api_list'),
    path('api/posts/<int:pk>/', PostAPIDetailView.as_view(), name="post_api_detail"),
]






