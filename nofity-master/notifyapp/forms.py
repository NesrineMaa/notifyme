from django import forms
from notifyapp.models import Url

from notifyapp.models import Category


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

