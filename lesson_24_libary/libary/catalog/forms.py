from django import forms
from catalog.models import BookInstance


class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ()
