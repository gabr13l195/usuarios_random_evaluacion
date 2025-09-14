import requests
from django.shortcuts import render
from django.contrib import messages
from .forms import UserSearchForm

API_URL = "https://randomuser.me/api/"
SEED = "abc"

def get_users_from_api():
    params = {
        'page': 3,
        'results': 10,
        'seed': SEED
    }
    
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.RequestException as e:
        print(f"Error al obtener usuarios de la API: {e}")
        return []

def user_list(request):
    users = get_users_from_api()
    
    search_form = UserSearchForm(request.GET)
    if search_form.is_valid() and search_form.cleaned_data['query']:
        query = search_form.cleaned_data['query'].lower()
        users = [user for user in users if 
                query in user['name']['first'].lower() or 
                query in user['name']['last'].lower() or
                query in user['email'].lower() or
                query in user['location']['city'].lower() or
                query in user['location']['country'].lower()]
        messages.info(request, f'Resultados para: "{query}"')
    
    context = {
        'users': users,
        'search_form': search_form,
    }
    return render(request, 'users/user_list.html', context)

def user_detail(request, user_uuid):
    users = get_users_from_api()
    user = None
    
    for u in users:
        if u['login']['uuid'] == user_uuid:
            user = u
            break
    
    if not user:
        messages.error(request, 'Usuario no encontrado')
        return render(request, 'users/user_list.html', {
            'users': get_users_from_api(),
            'search_form': UserSearchForm(),
        })
    
    context = {
        'user': user,
    }
    return render(request, 'users/user_detail.html', context)

def user_search(request):
    query = request.GET.get('q', '')
    users = []
    
    if query:
        all_users = get_users_from_api()
        query_lower = query.lower()
        users = [user for user in all_users if 
                query_lower in user['name']['first'].lower() or 
                query_lower in user['name']['last'].lower() or
                query_lower in user['email'].lower()]
    
    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'users/user_search.html', context)