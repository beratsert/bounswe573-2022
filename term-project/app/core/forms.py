from django import forms
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    desc = forms.CharField(label="Your Contribution", widget=CKEditorWidget())