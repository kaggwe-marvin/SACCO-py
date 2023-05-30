from django.urls import path
from . import views
app_name = 'app32'
urlpatterns = [
 path('home', views.home, name='home'),
 path('about', views.about, name='about'),
 path('apply', views.apply, name='apply'),
 path('contact', views.contact, name='contact'),
 path('approval', views.approval, name='approval'),
]