from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from .forms import RegisterForm, EditProfileForm, RecordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash

from .models import *

def index(request):
    return render(request, 'main/index.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = RegisterForm()
    return render(request, "main/registration.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request, "main/auth.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request, username):
    return render(request, 'main/profile.html', {'username': username})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.cleaned_data['new_password1']:
                request.user.set_password(form.cleaned_data['new_password1'])
            form.save()
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Профиль обновлен')
            return redirect('profile', {'user': request.user})
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'main/edit_profile.html', {'form': form})


def laboratory_seven(request):
    city = City.objects.all()
    age = Age.objects.all()
    workExperience = WorkExperience.objects.all()
    fullName = FullName.objects.all()
    position = Position.objects.all()
    context = {'city': city, 'age': age, 'workExperience': workExperience, 'fullName': fullName, 'position': position}
    return render(request, 'main/laboratory_seven.html', context)

def create_record(request):
    error = ''
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab7')
        else:
            error = 'Ошибка добавления записи'
            return redirect('lab7')
    form = RecordForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_record.html', data)


def delete_rec(request, el_id):
    event = Position.objects.get(pk=el_id)
    event.delete()
    return redirect('lab7')


class UpdateRecord(UpdateView):
    model = Position
    template_name = 'main/update_record.html'
    fields = ['id', 'fullName', 'positiom']
    success_url = reverse_lazy("lab7")