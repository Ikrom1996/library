from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput()
         }

    def save(self,commit =True):
        return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        data =self.cleaned_data
        username = data.get('username')
        password = data.get('password')

        # auth ichida xam filtri bor xam check passwordi bor
        user = authenticate(username=username,password=password)
        if not user:
           raise ValidationError('Login yoki Password Xatolik')
        return {"user": user}



class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length = 200)

    def clean(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise ValidationError('Bunday foydalanuvchi mavjud emas')
        return self.cleaned_data



class RestorePasswordForm(forms.Form):
    code = forms.CharField(max_length = 200)
    password = forms.CharField(widget=forms.PasswordInput())
    repassword = forms.CharField(widget=forms.PasswordInput())


