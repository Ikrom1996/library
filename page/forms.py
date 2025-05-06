from django import forms
from django.core.exceptions import ValidationError
from .models import Authors, Books, FileUpload


# Author Form using ModelForm
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['name', 'birth_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Authors.objects.filter(name=name).exists():
            raise ValidationError("Bu ism allaqachon ishlatilyapti")
        return name


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'author', 'file','image']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

        }



    def clean_title(self):
        title = self.cleaned_data['title']
        if Books.objects.filter(title=title).exists():
            raise ValidationError("Bu kitob nomi allaqachon ishlatilyapti")
        return title

# class FileUpload1(forms.ModelForm):
#     class Meta:
#         model = FileUpload
#         fields = ['name','image']
