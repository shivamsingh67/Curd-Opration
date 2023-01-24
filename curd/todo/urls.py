from django.urls import path, re_path
from . import views
urlpatterns = [
    path('about/', views.INDEX, name='index'),
    path('about/<int:id>/', views.Student, name="student"),
    re_path(r'^(?P<id>\d+)', views.random, name="random")
]
