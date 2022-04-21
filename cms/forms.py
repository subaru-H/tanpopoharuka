from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import AuthenticationForm #Djangoのログオン用のモジュールをインポーと

class BookEditForm(ModelForm):
    class Meta:
        model = Book
        fields = ('book_num', 'name', 'publisher',)

class BookRentForm(ModelForm):
    class Meta:
        model = Book
        fields = ('renter', )

class LoginForm(AuthenticationForm):
    #ログインフォーム，元のAuthenticationFormクラスではusernameとパスワードがセットで格納されている
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
