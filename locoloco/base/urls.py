from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('register', views.register_page, name='register'),

    path('create-post', views.create_post, name='create-post'),

    path('update-post/<str:pk>', views.update_post, name='update-post'),
    path('delete-post/<str:pk>', views.delete_post, name='delete-post'),

    path('create-comment/<str:pk>', views.create_comment, name='create-comment'),
    path('like/<str:pk>', views.like_post, name='like_post'),
]
