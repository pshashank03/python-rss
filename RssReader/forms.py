from django import forms
import json
from django.core.exceptions import ValidationError


class RssReaderForm(forms.Form):
    url = forms.CharField(label='Enter Rss URl')

    def __init__(self, *args, **kwargs):
        super(RssReaderForm, self).__init__(*args, **kwargs)


