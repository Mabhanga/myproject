from django import forms
from django.shortcuts import redirect, render
from .models import Music
from django.contrib.auth.decorators import login_required

class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'genre', 'audio_file']

@login_required
def add_music(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or back to the add music page
            return redirect('profile')  # Assuming you want to redirect to the profile page after adding music
    else:
        form = MusicUploadForm()
    return render(request, 'myapp/add_music.html', {'form': form})