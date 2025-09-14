from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import User
from .forms import UserSearchForm
from .services.user_services import load_users_from_api

def user_list(request):
    """
    Vista para listar todos los usuarios con paginación y búsqueda
    """
    # Cargar usuarios desde la API si no hay usuarios en la base de datos
    if User.objects.count() == 0:
        load_users_from_api()
    
    users = User.objects.all().order_by('first_name', 'last_name')
    
    # Formulario de búsqueda
    search_form = UserSearchForm(request.GET)
    if search_form.is_valid() and search_form.cleaned_data['query']:
        query = search_form.cleaned_data['query']
        users = users.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(city__icontains=query) |
            Q(country__icontains=query)
        )
        messages.info(request, f'Resultados para: "{query}"')
    
    # Paginación - 10 usuarios por página
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'users': page_obj,
        'search_form': search_form,
    }
    return render(request, 'users/user_list.html', context)

def user_detail(request, user_uuid):
    """
    Vista para mostrar los detalles de un usuario específico
    """
    user = get_object_or_404(User, uuid=user_uuid)
    
    context = {
        'user': user,
    }
    return render(request, 'users/user_detail.html', context)

def user_search(request):
    """
    Vista para buscar usuarios por nombre
    """
    query = request.GET.get('q', '')
    users = []
    
    if query:
        users = User.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        ).order_by('first_name', 'last_name')
    
    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'users/user_search.html', context)

def refresh_users(request):
    """
    Vista para recargar usuarios desde la API
    """
    from .services.user_services import refresh_users
    
    try:
        count = refresh_users()
        messages.success(request, f'Se cargaron {count} usuarios desde la API')
    except Exception as e:
        messages.error(request, f'Error al cargar usuarios: {str(e)}')
    
    return render(request, 'users/user_list.html', {
        'users': User.objects.all().order_by('first_name', 'last_name'),
        'search_form': UserSearchForm(),
    })