# accounts/views.py
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django import forms

User = get_user_model()

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(form.cleaned_data["password"])
            u.save()
            login(request, u)
            messages.success(request, "Welcome! Your account was created.")
            return redirect("tournaments:index")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "accounts/profile.html")

@login_required
def profile_edit(request):
    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name", "").strip()
        request.user.last_name = request.POST.get("last_name", "").strip()
        request.user.email = request.POST.get("email", "").strip()
        request.user.save()
        messages.success(request, "Profile updated.")
        return redirect("accounts:profile")
    return render(request, "accounts/profile_edit.html")

def user_public(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    return render(request, "accounts/user_public.html", {"u": u})
