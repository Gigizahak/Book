from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('book/<slug:slug>/', views.BookView.as_view(), name='book'),
    path('category/<slug:cat_slug>/', views.CategoryView.as_view(), name='category'),
    path('add/', views.CreateBook.as_view(), name='create'),
    path('edit/<slug:slug>/', views.EditBook.as_view(), name='edit'),
    path('delete/<slug:slug>/', views.DeleteBook.as_view(), name='edit'),
]