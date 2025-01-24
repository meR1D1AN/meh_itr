from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from itr.models import Vacation, VacationStatus
from users.forms import UserProfileForm


@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Важно для сохранения авторизации
            messages.success(request, "Пароль успешно изменен!")
            return redirect("home")  # Перенаправление после смены пароля
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "users/change_password.html", {"form": form})


@login_required
def profile(request):
    vacations = Vacation.objects.filter(
        user=request.user)
    return render(request, "users/profile.html", {"vacations": vacations})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return redirect("users:profile")
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, "users/edit_profile.html", {"form": form})
