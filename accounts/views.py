from django.shortcuts import render
from django.views.generic import View
from .forms import CustomUserCreationForm


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', context={'form': register_form})

    def post(self, request):
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return render(request, 'accounts/register.html', context={'form': register_form})
