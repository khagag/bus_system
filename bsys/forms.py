from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from . import models as MD
from .models import User
from django.db import transaction


class BusCreationForm(forms.ModelForm):
    class Meta:
        model = MD.Bus
        fields = "__all__"
        widgets = {
                'lastCheckUp': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            }
            
class ToggleBusStatus(forms.ModelForm):
    class Meta:
        model = MD.Bus
        fields = ["status"]

class DriverSignUpForm(UserCreationForm):
    bus = forms.ModelChoiceField(MD.Bus.objects.all(),required=False,label="choose bus")
    def __init__(self, *args, **kwargs):
        super(DriverSignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta(UserCreationForm.Meta):
            model = User
            fields = [
                'username',
                "first_name",
                "last_name",
                "email",
            ]
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
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
    # role = forms.IntegerField(
    #     widget=forms.HiddenInput(),
    #     required = False,
    #     initial=1
    # )

class ManagerAuthForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

    def __init__(self, *args, **kwargs):
        super(ManagerAuthForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    # role = forms.IntegerField(
    #     widget=forms.HiddenInput(),
    #     required = False,
    #     initial=2
    # )
class ManagerCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ManagerCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        driver = MD.Manager.objects.create(user=user)
        return user





# class ManagerUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = MD.Manager
