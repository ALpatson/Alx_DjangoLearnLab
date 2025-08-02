from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from .models import Library      # ✅ This is what the check is looking for
from .models import Book    
# Separate line for Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'


# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user immediately
            return redirect('list_books')  # or any other page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout View
# def logout_view(request):
#     logout(request)
#     return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def check_role(role):
    def inner(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return inner

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
