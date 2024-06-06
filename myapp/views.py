from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import MusicUploadForm
from .models import Music
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')

def home(request):
    return render(request, 'myapp/home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('profile')  # Redirect to the profile page after adding music
    else:
        form = MusicUploadForm()
    
    # Retrieve music uploaded by the current user
    uploaded_music = Music.objects.filter(user=request.user)
    
    return render(request, 'myapp/profile.html', {'uploaded_music': uploaded_music, 'form': form})

def about(request):
    return render(request, 'myapp/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            # Re-render the signup form with error messages
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def add_music(request):
    # Logic for adding music
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('profile')  # Redirect to the profile page after adding music
    else:
        form = MusicUploadForm()
    return render(request, 'myapp/add_music.html', {'form': form})

def index(request):
    return render(request, 'index.html')


def index(request):
    """
    View function for the index page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object with the rendered template.
    """
    return render(request, 'index.html')