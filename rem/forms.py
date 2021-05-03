from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation, authenticate
from django.forms import ModelForm
from django.shortcuts import redirect

from .models import contactsModel, ExtendUser
from django import forms


class AccountLoginForm(forms.Form):
    login = forms.CharField(max_length=100, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, label='Пароль')


class contactsForm(ModelForm):
    name = forms.CharField(label='Введите Ваше имя', max_length=150)
    phone = forms.IntegerField(label='Введите Ваш номер телефона', widget=forms.NumberInput, help_text='только цифры(80xxxxxxxxxx)')
    email = forms.CharField(max_length=100, label='Введите Ваш Email', widget=forms.EmailInput)
    description = forms.CharField(max_length=1500, required=False,
                                  label='Опишите объект: Площадь объекта, тип объекта(Квартира, Дом, Офис, Другое.'
                                        'Тип недвижимости (Новое жилье, Вторичное жилье, Наличие дизайн-проекта', widget=forms.Textarea)

    class Meta:
        model = contactsModel
        fields = ['name', 'phone', 'email', 'description']


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput, max_length=75, label='Старый пароль')
    new_password1 = forms.CharField(widget=forms.PasswordInput, max_length=75, label='Новый пароль')
    new_password2 = forms.CharField(widget=forms.PasswordInput, max_length=75, label='Повторить пароль')

    class Meta:
        model = ExtendUser
        fields = ['old_password', 'new_password1', 'new_password2']


class UserFormRegister(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль', help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторить пароль', help_text='Введите пароль повторно для проверки')

    def clean_password1(self):
        # валидный ли пароль
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = False
        if commit:
            user.save()
        return user
            # username = self.cleaned_data.get('username')
            # password = self.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # return redirect('rem:profile')

    class Meta:
        model = ExtendUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

