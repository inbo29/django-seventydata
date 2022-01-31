from django.urls import path
from .views import *


urlpatterns = [
    path("", blog, name='blog'),
    path("list/", BlogListView.as_view(), name='Insight'),
    path("add/", BlogCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BlogDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name='delete'),
]