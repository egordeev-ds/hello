from django.contrib import admin
from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('static', views.static, name = 'static'),
    path('dynamic', views.dynamic, name = 'dynamic'),
    path('show_people', views.show_people, name = 'show_people'),
    path('create/', views.create, name = 'create'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('delete/<int:id>', views.delete, name = 'delete'),
# ____________________________________________________
    path('details/', views.details),
    path('admin/', admin.site.urls),
]
