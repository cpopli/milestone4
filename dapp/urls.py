from django.contrib import admin
from django.urls import path
from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views

from dapp import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/project/', views.project_list),
    re_path(r'^api/projectdetail/(?P<pk>[0-9]+)$', views.project_detail),
    path('api/issue/', views.issue_list),
    re_path(r'^api/issuedetail/(?P<pk>[0-9]+)$', views.issue_detail),
    path('api/assign/', views.assign),

]
