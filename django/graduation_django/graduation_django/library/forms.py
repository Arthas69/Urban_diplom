from django import forms

from .models import Author, Review


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember_me = forms.BooleanField(required=False)


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    publication_date = forms.DateField()
    author = forms.ModelChoiceField(Author.objects.all())
    image = forms.ImageField()


class ReviewForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label='', label_suffix='')


class AuthorForm(forms.Form):
    pass


class GenreForm(forms.Form):
    pass
