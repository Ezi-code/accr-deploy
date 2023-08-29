from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sport/', views.sport, name="sport"),
    path('groups/<str:category>', views.groups, name="groups"),
    path('read_blog/<str:title>', views.read_blog, name="read_blog")
]
