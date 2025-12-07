from . import views
from django.urls import path

urlpatterns = [
    path('get/', views.getData),
    path('post/', views.insertData),
    path('delete/<int:id>/', views.delData),
    path('put/', views.updateData),
]