
from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name = 'edit'),
    path('update/<int:id>', views.Update, name='update'),
    path('delete/<int:id>', views.Delete, name='delete'),
    path('', include('todo.urls'))
    
]
