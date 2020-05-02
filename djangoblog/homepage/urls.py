from django.urls import path
from .forms import PostForm


from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>', views.delete_post, name='delete_post'),
    path('new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]