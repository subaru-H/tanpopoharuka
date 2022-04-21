from django.forms import ModelForm
from cms.models import Book


class BookEditForm(ModelForm):
    class Meta:
        model = Book
        fields = ('book_num', 'name', 'publisher',)

class BookRentForm(ModelForm):
    class Meta:
        model = Book
        fields = ('renter', )
