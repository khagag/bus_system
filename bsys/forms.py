from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from . import models as MD
from .models import User
from django.db import transaction


class DriverSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
            model = User
    def __init__(self, *args, **kwargs):
        super(DriverSignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.Role = 1
        user.save()
        driver = MD.Driver.objects.create(user=user)
        return user

class DriverAuthForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
    def __init__(self, *args, **kwargs):
        super(DriverAuthForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

            # class Meta:
            #     model = MD.User
            #     fields = ('username', 'email')


# class AdminSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#             model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.Role = 1
#         user.save()
#         driver = MD.Driver.objects.create(user=user)
#         return user
#




class PrivilegedUserAuthForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

    def __init__(self, *args, **kwargs):
        super(PrivilegedUserAuthForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    # class Meta:
    #     model = MD.PrivilegedUser
    #     fields = ('username', 'email')


class PrivilegedUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(PrivilegedUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = MD.PrivilegedUser
        fields = ('username', 'email')


class PrivilegedUserChangeForm(UserChangeForm):

    class Meta:
        model = MD.PrivilegedUser
        fields = ('username', 'email')

    # def __init__(self, *args, **kwargs):
    #     super(PrivilegedUserChangeForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'


#
#
# class DriverCreationForm(UserCreationForm):
#
#     def __init__(self, *args, **kwargs):
#         super(DriverCreationForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#             visible.field.widget.attrs['placeholder'] = visible.field.label
#
#     class Meta:
#         model = MD.Driver
#         fields = ('username', 'email')
#
# class DriverChangeForm(UserChangeForm):
#
#     class Meta:
#         model = MD.Driver
#         fields = ('username', 'email')
