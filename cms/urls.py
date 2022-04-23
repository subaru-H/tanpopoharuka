from django.urls import path

#from cms import views
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('book/', views.book_list, name='book_list'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    # path('book/add/', views.book_edit, name='book_add'),
    # path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),
    path('book/rent/<int:book_id>/', views.book_rent, name='book_rent'),
    path('book/return/<int:book_id>/', views.book_return, name='book_return'),
    # path('book/del/<int:book_id>/', views.book_del, name='book_del'),
]