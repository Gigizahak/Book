from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.BookListView.as_view(), name='home'),
    path('home/book/<slug:slug>/', views.BookView.as_view(), name='book'),
    path('home/category/<slug:cat_slug>/', views.CategoryView.as_view(), name='category'),
    path('add/', views.CreateBook.as_view(), name='create'),
    path('home/edit/<slug:slug>/', views.EditBook.as_view(), name='edit'),
    path('home/delete/<slug:slug>/', views.DeleteBook.as_view(), name='edit'),
]