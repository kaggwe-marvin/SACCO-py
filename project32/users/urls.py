from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
 path('', include(
 'django.contrib.auth.urls')),
path('', views.register_view,
name='register'),
path('login', views.login_view,
name='login'),

]