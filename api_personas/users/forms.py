from django import forms

class UserSearchForm(forms.Form):
    """
    Formulario para búsqueda de usuarios
    """
    query = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': 'Buscar usuario por nombre...',
            'style': 'width: 300px; padding: 12px 20px; border: none; border-radius: 25px; background: rgba(255, 255, 255, 0.1); color: #e0e0e0;'
        }),
        label='',
        required=False
    )