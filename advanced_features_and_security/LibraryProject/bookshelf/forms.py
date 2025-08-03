from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)
# [SECURITY] Use ORM filters to prevent SQL injection
