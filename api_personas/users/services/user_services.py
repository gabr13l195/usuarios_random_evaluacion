import requests
from datetime import datetime
from users.models import User, UserPicture

API_URL = "https://randomuser.me/api/"
SEED = "abc"  # Seed fijo para obtener siempre los mismos usuarios

def get_users_from_api(page=3, results=10):
    """
    Obtiene usuarios de la API de RandomUser con seed fijo
    """
    params = {
        'page': page,
        'results': results,
        'seed': SEED
    }
    
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener usuarios de la API: {e}")
        return None

def load_users_from_api():
    """
    Carga usuarios desde la API y los guarda en la base de datos
    """
    print("Cargando usuarios desde la API de RandomUser...")
    
    api_data = get_users_from_api()
    if not api_data:
        print("No se pudieron obtener datos de la API")
        return
    
    users_data = api_data.get('results', [])
    loaded_count = 0
    
    for user_data in users_data:
        try:
            # Verificar si el usuario ya existe
            uuid = user_data['login']['uuid']
            if User.objects.filter(uuid=uuid).exists():
                print(f"Usuario {user_data['name']['first']} {user_data['name']['last']} ya existe, saltando...")
                continue
            
            # Crear la imagen del usuario
            picture_data = user_data.get('picture', {})
            picture = UserPicture.objects.create(
                large=picture_data.get('large'),
                medium=picture_data.get('medium'),
                thumbnail=picture_data.get('thumbnail')
            )
            
            # Parsear fechas
            dob_date = None
            registered_date = None
            
            if user_data.get('dob', {}).get('date'):
                dob_date = datetime.fromisoformat(user_data['dob']['date'].replace('Z', '+00:00'))
            
            if user_data.get('registered', {}).get('date'):
                registered_date = datetime.fromisoformat(user_data['registered']['date'].replace('Z', '+00:00'))
            
            # Crear el usuario
            user = User.objects.create(
                uuid=uuid,
                username=user_data['login']['username'],
                first_name=user_data['name']['first'],
                last_name=user_data['name']['last'],
                email=user_data['email'],
                phone=user_data.get('phone'),
                cell=user_data.get('cell'),
                gender=user_data['gender'],
                age=user_data['dob']['age'],
                nationality=user_data['nat'],
                street_number=user_data['location']['street']['number'],
                street_name=user_data['location']['street']['name'],
                city=user_data['location']['city'],
                state=user_data['location']['state'],
                country=user_data['location']['country'],
                postcode=user_data['location']['postcode'],
                date_of_birth=dob_date,
                registered_date=registered_date,
                picture=picture
            )
            
            loaded_count += 1
            print(f"Usuario {user.full_name} cargado exitosamente")
            
        except Exception as e:
            print(f"Error cargando usuario: {e}")
            continue
    
    print(f"Total de usuarios cargados: {loaded_count}")
    return loaded_count

def clear_all_users():
    """
    Elimina todos los usuarios de la base de datos
    """
    User.objects.all().delete()
    UserPicture.objects.all().delete()
    print("Todos los usuarios han sido eliminados")

def refresh_users():
    """
    Limpia y recarga todos los usuarios desde la API
    """
    clear_all_users()
    return load_users_from_api()
