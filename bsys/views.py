from django.shortcuts import render
from django.contrib.auth import authenticate, login
from . import forms as FM
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template                import RequestContext
import logging
from .forms import DriverSignUpForm
from .models import User


logger = logging.getLogger(__name__)
# Create your views here.


def home(request):
    auth = False
    if request.user.is_authenticated:
        auth = True
    return render(request, 'home.html', {'auth':auth})

# @login_required(login_url='/')
def profile(request):
    logger.warning(request.user.is_admin)
    logger.warning(request.user.is_driver)
    if request.user.is_admin:
        return render(request, 'profile/admin.html')
    elif request.user.is_driver:
        return render(request, 'profile/driver.html')
    else:
        return redirect("/admin/")


def index(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    if request.method == 'POST':
        if request.POST['role'] == 1:
            form = FM.DriverAuthForm(data=request.POST)
        else:
            form = FM.ManagerAuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                # user = authenticate(request,username=username, password=raw_password)
                login(request, user)
                return redirect("/profile/")
        if request.user.is_driver:
            DrForm = form
        else:
            AdForm = form
    return render(request, 'index.html', {'AdForm': AdForm,"DrForm":DrForm})

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('/')

class DriverSignUpView(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/profile/')

class DriverSignUpFormView(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'profile/DriverCreate.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/profile/d/create/')


def success_test(request):
    return render(request, 'st.html')

def faliur_test(request):
    return render(request, 'fl.html')


def sign_up(request):
    form = FM.DriverCreationForm()
    return render(request, 'signup.html',{'form': form,"type":"Driver"})
