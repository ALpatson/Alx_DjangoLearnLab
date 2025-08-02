from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
    # ✅ Authentication
    path('register/', views.register, name='register'),  # register function view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    path('', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),       # ✅ Ensure this exists
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # ✅ Ensure this exists
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Optional

    # Include other routes like list or detail if you have them
]
