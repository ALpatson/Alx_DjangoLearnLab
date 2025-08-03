from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)
# [SECURITY] Use ORM filters to prevent SQL injection

class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message'}),
        required=True
    )
