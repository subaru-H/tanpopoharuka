from django.contrib import admin
#from cms.models import Book
from .models import Book
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Impression)



class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_num', 'name', 'publisher', 'isavailable')
    list_display_links = ('id', 'name')

admin.site.register(Book, BookAdmin)
