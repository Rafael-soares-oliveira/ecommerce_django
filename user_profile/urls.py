from django.urls import path
from user_profile import views

app_name = 'profile'

urlpatterns = [
    path('register/', views.ProfileRegister.as_view(),
         name='profile_register'),
    path('profile_update/', views.ProfileUpdate.as_view(),
         name='profile_update'),
    path('login/', views.Login.as_view(),
         name='login'),
    path('logout', views.Logout.as_view(),
         name='logout'),
]
