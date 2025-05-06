from django.shortcuts import render, redirect
from accounts.forms import UserForm, LoginForm,ForgotPasswordForm,RestorePasswordForm
from django.contrib.auth import login, logout
from accounts.models import User
from django.views import View
from accounts.service import send_email_thread, send_email
from accounts.models import Code
from django.urls import reverse




def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('accounts:login_user')
        return render(request, 'accounts/register.html', {'form': form})

    form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
           user = form.cleaned_data.get('user')
           login(request, user)
           return redirect('book_list')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')


class ForgotPasswordView(View):
    def get(self,request):
        form = ForgotPasswordForm()
        return render(request,'accounts/forgot_password.html',{'form':form})

    def post(self,request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username = form.cleaned_data.get('username'))
            code = Code.objects.create(
                user = user
            )
            send_email(
                subject="Parol tiklash kodi",
                message=f'Code: {code.code}\n<a '
                        f'href="http://127.0.0.1:8000{reverse('accounts:restore_password')}"?username={user.username} class="button">Link</a>',

                to_email=user.email
            )
            return render(request, 'accounts/done.html')

        return render(request,'accounts/forgot_password.html',{'form':form})


class RestorePasswordView(View):
    def get(self,request):
        form = RestorePasswordForm()
        return render(request,'accounts/restore_password.html',{'form':form})


    def post(self,request):
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            pass
        return render(request, 'accounts/restore_password.html', {'form':form})
