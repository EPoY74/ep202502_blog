"""
    Форма для рекомндации постов по электронной почте
"""
from django import forms

class EmailPostForm(forms.Form):
    """
    Класс для отравки уведомлений по электронной почте
    """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea) 