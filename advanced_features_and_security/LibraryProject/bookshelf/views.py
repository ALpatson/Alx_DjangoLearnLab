from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

from django.db.models import Q

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
