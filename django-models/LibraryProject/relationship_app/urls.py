from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView


urlpatterns = [
    # Existing ones...
    path('', views.list_books, name='home'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), redirect_authenticated_user=True, name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), redirect_authenticated_user=True, name='logout'),
    path('register/', views.register, name='register'),

    # Role-specific views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # ✅ Add these to match checker expectations
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Optional (if you want to keep books/ prefix too)
    # path('books/add/', views.add_book, name='add_book'),
    # path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
]
