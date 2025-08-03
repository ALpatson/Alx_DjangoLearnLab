from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Make sure this points to your actual CustomUser

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # ✅ Show these in list view
    list_filter = ('author', 'publication_year')             # ✅ Sidebar filters
    search_fields = ('title', 'author')                      # ✅ Search bar

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# ✅ Add this line to register your custom user model with the admin site




