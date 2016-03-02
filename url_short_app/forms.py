from django import forms
from url_short_app.models import Bookmark


class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        exclude = ['shortened']
