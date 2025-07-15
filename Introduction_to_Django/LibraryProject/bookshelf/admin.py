from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # ✅ Show these in list view
    list_filter = ('author', 'publication_year')             # ✅ Sidebar filters
    search_fields = ('title', 'author')                      # ✅ Search bar
