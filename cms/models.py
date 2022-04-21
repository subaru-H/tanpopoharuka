from django.db import models


class Book(models.Model):
    book_num = models.IntegerField('蔵書番号')
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    isavailable = models.BooleanField('貸出可否', default=True)
    renter = models.CharField('借りている人', default="", max_length=64)

    def __str__(self):
        return self.name
