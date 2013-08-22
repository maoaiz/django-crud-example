#encoding:utf-8
from django.forms import ModelForm
from article.models import articles

class ArticleForm(ModelForm):
    class Meta:
        model = articles
        # fields = ['name', 'description', 'is_active']