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
from . import models as MD
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)
# Create your views here.


def home(request):
    auth = False
    if request.user.is_authenticated:
        auth = True
    return render(request, 'home.html', {'auth':auth})

@login_required(login_url='/')
def profile(request):
    logger.warning(request.user.is_admin)
    logger.warning(request.user.is_driver)
    if request.user.is_admin:
        return render(request, 'profile/admin.html',{"drivers":MD.Driver.objects.all()})
    elif request.user.is_driver:

        return render(request, 'profile/driver.html')
    else:
        return redirect("/admin/")

class BusUpdate(UpdateView):
    model = MD.Bus
    fields = "__all__"
    template_name = "profile/BusEdit.html"
    success_url = reverse_lazy('bsys:BusList')

# from django.forms import inlineformset_factory
class DriverUpdate(UpdateView):
    model = MD.Driver
    # TODO: create a form class that exclude user / form that include user editable fields and use it as form_class
    fields = [
        "bus",
        "licenceNum"
    ]
    template_name = "profile/DriverEdit.html"
    success_url = reverse_lazy('bsys:DriverList')

class DriverUpdatePersonal(UpdateView):
    model = MD.User
    # user_formset = inlineformset_factory(MD.User,fields="first_name")
    fields = [
        "first_name",
        "last_name",
        "email",

    ]
    template_name = "profile/DriverPersonalEdit.html"
    success_url = reverse_lazy('bsys:DriverPersonalList')



def index(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    if request.method == 'POST':
        logger.warning(str(request.POST['role']) == str(1))
        DrForm = FM.DriverAuthForm()
        AdForm = FM.ManagerAuthForm()
        if str(request.POST['role']) == str(1):
            form = FM.DriverAuthForm(data=request.POST)
        else:
            form = FM.ManagerAuthForm(data=request.POST)
        if form.is_valid():
            logger.warning("form validate")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            logger.warning(user.first_name)
            if user is not None:
                logger.warning("user not none")
                # user = authenticate(request,username=username, password=raw_password)
                login(request, user)
                return redirect("/profile/")
            else:
                logger.warning("form error")
        if str(request.POST['role']) == str(1):
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

@login_required(login_url='/')
def BusCreationFormView(request):
    if request.method == "POST":
        form = FM.BusCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # return redirect('/show')
            except:
                pass
    else:
        form = FM.BusCreationForm()
    return render(request,'profile/form_base.html',{'form':form,"form_id":"BusForm","form_title":"Bus Creation"})

class BusList(ListView):
    model = MD.Bus
    template_name = "profile/BusList.html"

class DriverList(ListView):
    model = MD.Driver
    template_name = "profile/DriverList.html"

class BusDeleteView(DeleteView):
    model = MD.Bus
    template_name="profile/BusDeleteConfirm.html"
    success_url = reverse_lazy('bsys:BusList')

class DriverDeleteView(DeleteView):
    model = MD.Driver
    template_name="profile/BusDeleteConfirm.html"
    success_url = reverse_lazy('bsys:DriverList')

@login_required(login_url='/')
def BusUpdateView(request, pk, template_name='profile/form_base.html'):
    Bus= get_object_or_404(MD.Bus, pk=pk)
    form = FM.BusCreationForm(request.POST or None, instance=MD.Bus)
    if form.is_valid():
        form.save()
        return redirect('/profile/b/update/?status=success')
    return render(request, template_name, {'form':form})

# def book_delete(request, pk, template_name='books/book_confirm_delete.html'):
#     book= get_object_or_404(Book, pk=pk)
#     if request.method=='POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request, template_name, {'object':book})



def success_test(request):
    return render(request, 'st.html')

def faliur_test(request):
    return render(request, 'fl.html')


def sign_up(request):
    form = FM.DriverCreationForm()
    return render(request, 'signup.html',{'form': form,"type":"Driver"})
