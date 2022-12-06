from django.shortcuts import render,HttpResponse, redirect
from .models import Author, Book, BookInstance,Genre
from django.views.generic import ListView, DetailView
from .forms import BookForm, AuthorForm
# Create your views here.


def index(request):
    num_books=Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='Available')
    num_authors = Author.objects.count()

    return render(
        request,
        'catalog/index.html',
        context=
        {
                 'num_books':num_books,
                 'num_instances':num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors
        },
    )


class BooksListView(ListView):
    model = Book
    context_object_name = 'my_book_list'
    template_name = 'catalog/books_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'


class AuthorsListView(ListView):
    model = Author
    context_object_name = 'authors_list'
    template_name = 'catalog/authors_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'


def addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'catalog/add_book.html', {'form': form})


def addauthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'catalog/add_author.html', {'form': form})