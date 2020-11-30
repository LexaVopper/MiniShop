from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from cart.models import Order
from account.models import Profile
# Create your views here.
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(FormView):
    form_class = UserCreationForm
    success_url = "registration/login.html"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterForm, self).form_invalid(form)


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('login/')
#     else:
#         return redirect('register/')





