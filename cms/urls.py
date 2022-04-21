from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/add/', views.book_edit, name='book_add'),
    path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),
    path('book/del/<int:book_id>/', views.book_del, name='book_del'),
]