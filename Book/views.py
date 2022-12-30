from django.shortcuts import render
from django.urls import reverse_lazy, reverse
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
        return Book.objects.filter(category__slug=self.kwargs['cat_slug'])


class CreateBook(CreateView):
    model = Book
    form_class = 'BookForm'
    template_name = 'Book/order.html'

    def get_success_url(self):
        return reverse('home')


class EditBook(UpdateView):
    form_class = 'BookForm'
    template_name = 'Book/edit.html'

    def get_success_url(self):
        return reverse('home')


class DeleteBook(DeleteView):
    model = Book
    template_name = 'Book/delete.html'

    def get_success_url(self):
        return reverse('home')
