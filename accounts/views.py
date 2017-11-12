from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .forms import SignUpForm


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
