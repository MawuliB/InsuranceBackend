from knox import views as knox_views
from .views import LoginAPI
from django.urls import path, include
from .views import RegisterAPI


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]