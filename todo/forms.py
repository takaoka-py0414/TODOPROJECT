from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=10,
        label='ユーザー名',
        help_text='10文字以内。使用可能な文字：英数字と @ . / + - _',
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9@./+\-_]+$',
                message='使用可能な文字は英数字と @ . / + - _ のみです。'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'maxlength': '10',
            'pattern': r'^[A-Za-z0-9@./+\-_]+$',
            'title': '使用可能な文字：英数字と @ . / + - _'
        })
    )

    birthdate = forms.DateField(
        required=False,
        label='生年月日',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'birthdate', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})