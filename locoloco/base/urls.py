from django.urls import path
from . import views
from .views import ResetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('register', views.register_page, name='register'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile-form/<int:pk>', views.edit_profile, name='profile-form'),
    path('profile-picture-form/<int:pk>', views.edit_profile_picture, name='profile-picture-form'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_complete.html'),
         name='password_reset_complete'),

    path('create-post', views.create_post, name='create-post'),

    path('update-post/<str:pk>', views.update_post, name='update-post'),
    path('delete-post/<str:pk>', views.delete_post, name='delete-post'),

    path('create-comment/<str:pk>', views.create_comment, name='create-comment'),
    path('like/<str:pk>', views.like_post, name='like_post'),

    path('full-map', views.full_map, name='full-map'),
]
