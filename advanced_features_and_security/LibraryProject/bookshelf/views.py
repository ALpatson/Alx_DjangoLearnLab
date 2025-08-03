from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

from django.db.models import Q
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)) if query else Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})
# [SECURITY] Use ORM filters to prevent SQL injection


def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Securely process form.cleaned_data here
            name = form.cleaned_data['name']
            return render(request, 'bookshelf/form_example.html', {
                'form': ExampleForm(), 'success': True, 'name': name
            })
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

def raise_exception(request):
    # Example of raising a permission-related exception
    raise PermissionDenied("You do not have permission to access this resource.")
