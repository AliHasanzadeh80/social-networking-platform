from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dear {username} your account have been successfully created. now you can login!')
            return redirect('account-login')
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', context = {'title': 'sign-up', 'form': form})