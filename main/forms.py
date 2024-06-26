from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, label='Search')
