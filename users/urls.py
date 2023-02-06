from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.loginUser,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logoutUser,name='logout'),
    path('update',views.updateUser,name='update'),
    path('updatepicture',views.updatePicture,name='updatepicture'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password/reset_password.html'), name='reset_password'),

    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='password/reset_password_sent.html'),name='password_reset_done'),
    
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_form.html'),name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password/reset_password_confirm.html'),name='password_reset_complete'),

]
