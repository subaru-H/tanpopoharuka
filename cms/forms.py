from django.forms import ModelForm
from cms.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('book_num', 'name', 'publisher',)