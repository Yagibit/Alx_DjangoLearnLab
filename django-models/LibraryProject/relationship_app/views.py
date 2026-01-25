from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.as_p and form.is_valid():
            user = form.save()
            login(request, user) # Log the user in after registration
            return redirect('list_books') # Redirect to your book list
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})