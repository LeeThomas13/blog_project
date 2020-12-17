from django.urls import path

from .views import BlogListView, BlogDeleteView, BlogCreateView, BlogDetailView, BlogUpdateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('delete/', BlogDeleteView.as_view(), name='delete page'),
    path('create/', BlogCreateView.as_view(), name='create page'),
    path('detail/', BlogDetailView.as_view(), name='detail page'),
    path('update/', BlogUpdateView.as_view(), name='update page'),
]