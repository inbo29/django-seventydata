from django.urls import path
from . import views
from .views import *

# BookmarkListView , BookmarkCreateVeiw ,BookmarkDetailVeiw 이렇게 길게 써도되나 다써도 되나 * <이걸로 바꿔도 됨

urlpatterns = [
    # http://127.0.0.1/bookmark/???
    # 이게 있었으나 ""은 다떄고온다는뜻 -> ??? 이것만 남음 그러므로 본래적으로 http://127.0.0.1/bookmark/ 이것만 남음
    path("", home, name='home'),
    path('company-info/', views.companyinfo, name='companyinfo'),
    path('service-info/', views.service, name='service'),
]