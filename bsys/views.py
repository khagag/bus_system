from django.shortcuts import render
from django.contrib.auth import authenticate, login
from . import forms as FM
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import DriverSignUpForm
from .models import User
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FM.DriverAuthForm(request.POST)
        if form.is_valid():
            # username = request.POST['username']
            # password = request.POST['password']
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
                # form.save()
                # username = form.cleaned_data.get('username')
                # raw_password = form.cleaned_data.get('password')
                # user = authenticate(request,username=username, password=raw_password)
                # login(request, user)

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # return redirect('/success/')
                # Redirect to a success page.

            # else:
                # Return an 'invalid login' error message.
                # return redirect('/faliur/')
            # pass  # does nothing, just trigger the validation
    else:
        form = FM.DriverAuthForm()#request.POST or None, request.FILES or None
    return render(request, 'index.html', {'form': form})

@login_required(login_url='/success/')
def logout_view(request):
    logout(request)


class DriverSignUpView(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/success/')

def success_test(request):
    return render(request, 'st.html')

def faliur_test(request):
    return render(request, 'fl.html')


def sign_up(request):
    form = FM.DriverCreationForm()
    return render(request, 'signup.html',{'form': form,"type":"Driver"})
