from django import forms

class UserSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': 'Buscar usuario por nombre...',
        }),
        label='',
        required=False
    )