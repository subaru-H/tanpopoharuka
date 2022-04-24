from re import A
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from django.core.paginator import Paginator
from django.views import generic
#from cms.models import Book
#from cms.forms import BookEditForm, BookRentForm
from .forms import LoginForm, BookEditForm, BookRentForm
from .models import Book



# Create your views here.
def top(request):
    return render(request, 'cms/base.html')

class IndexView(generic.TemplateView):
    template_name = "cms/index.html"

def book_list(request):
    #return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('book_num')
    if "action" in request.GET:
        action = request.GET.get("action")
        if "book_num_asc" in action:
            books = books.order_by("book_num")
        elif "book_name" in action:
            books = books.order_by("name")
        elif "publisher" in action:
            books = books.order_by("publisher")
        elif "available" in action:
            books = books.order_by("isavailable")

        if "des" in action:
            books = books.reverse()
    
    paginator = Paginator(books, 10)
    if "page" in request.GET:
        books = paginator.get_page(request.GET["page"])
    else:
        books = paginator.get_page(1)

    return render(request,'cms/book_list.html',{'books': books})


def book_rent(request, book_id):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookRentForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.isavailable = False
            book.save()
            return redirect('cms:book_list')
    else:
        form = BookRentForm(instance=book)

    return render(request, 'cms/book_rent.html', dict(form=form, book_id=book_id, book=book))


def book_return(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.isavailable = True
    book.renter = ""
    book.save()
    return redirect('cms:book_list')



class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'cms/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'cms/login.html'
    
#LoginRequiredMixin, 
