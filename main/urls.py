from django.contrib import admin
from main import views
from django.urls import path


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('add_todo/', views.add_todo),
  path('delete_todo/<int:todo_id>/', views.delete_todo, name="delete"),
]
