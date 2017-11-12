from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import SignUpForm


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class SignUp(FormView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('index:home')


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('index:home')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})
