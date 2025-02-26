"""
    Форма для рекомндации постов по электронной почте
"""
from django import forms

class EmailPostForm(forms.Form):
    """
    Класс для отравки уведомлений по электронной почте
    """
    name = forms.CharField(max_length=50, label='Ваше имя:')
    email = forms.EmailField(label='Ваш e-mail:')
    to = forms.EmailField(label='E-mail получателя')
    comments = forms.CharField(required=False,
                               widget=forms.Textarea,
                               label='Комментарий') 