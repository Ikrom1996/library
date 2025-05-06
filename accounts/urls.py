
from django.urls import path
from accounts import views


app_name = 'accounts'


urlpatterns = [

        path('register/',views.register, name='register'),
        path('login_user/',views.login_user, name='login_user'),
        path('logout_user/',views.logout_user, name='logout_user'),
        path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
        path('restore_password/', views.RestorePasswordView.as_view(), name='restore_password'),
]
