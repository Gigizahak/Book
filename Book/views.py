from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'Book/home.html'
    context_object_name = 'books'


class BookView(DetailView):
    model = Book
    template_name = 'Book/book.html'
    context_object_name = 'book'


class CategoryView(ListView):
    model = Book
    template_name = 'Book/category.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(cat__slug=self.kwargs['cat_slug'])


class CreateBook(CreateView):
    form_class = 'BookForm'
    template_name = 'Book/order.html'
    success_url = reverse_lazy('home')


class EditBook(UpdateView):
    form_class = 'BookForm'
    template_name = 'Book/edit.html'
    success_url = reverse_lazy('home')


class DeleteBook(DeleteView):
    template_name = 'Book/delete.html'
    success_url = reverse_lazy('home')
