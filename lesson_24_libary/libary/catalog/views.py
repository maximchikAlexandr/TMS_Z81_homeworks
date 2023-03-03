from django.http.request import QueryDict
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from catalog.forms import BookInstanceForm
from catalog.models import Author, Book, BookInstance, Genre, Language


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = (
        BookInstance.objects.all().filter(status__exact="Available").count()
    )

    return render(
        request,
        "index.html",
        {
            "num_books": num_books,
            "num_authors": num_authors,
            "num_instances": num_instances,
            "num_instances_available": num_instances_available,
        },
    )


class AuthorListView(ListView):
    model = Author
    template_name = "authors_list.html"
    context_object_name = "authors_list"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"


class BookListView(ListView):
    model = Book
    template_name = "books_list.html"
    context_object_name = "books_list"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookInstanceDetailView(DetailView):
    model = BookInstance
    template_name = "book_instance_detail.html"
    context_object_name = "book_instance"

    def post(self, request, **kwargs):
        book_inst_content: QueryDict = request.POST
        form = BookInstanceForm(book_inst_content)
        if form.is_valid():
            book_inst = BookInstance.objects.get(pk=kwargs["pk"])
            book_inst.borrower = request.user
            book_inst.status = "Reserved"
            book_inst.save()
        return redirect("book-instance-detail", pk=kwargs["pk"])
