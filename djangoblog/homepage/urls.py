from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/edit/', views.edit, name='edit')
]