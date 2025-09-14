from django.db import models

# Create your models here.
class UserPicture(models.Model):
    """Modelo para almacenar las imágenes de los usuarios"""
    large = models.URLField(null=True, blank=True)
    medium = models.URLField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Picture {self.id}"

class User(models.Model):
    """Modelo principal para usuarios aleatorios"""
    uuid = models.CharField(max_length=100, primary_key=True, unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, null=True, blank=True)
    cell = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    age = models.IntegerField()
    nationality = models.CharField(max_length=10)  # Código de país (US, RS, FI, etc.)
    
    # Información de ubicación
    street_number = models.IntegerField(null=True, blank=True)
    street_name = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    
    # Fechas
    date_of_birth = models.DateTimeField(null=True, blank=True)
    registered_date = models.DateTimeField(null=True, blank=True)
    
    # Imagen
    picture = models.OneToOneField(UserPicture, on_delete=models.CASCADE, null=True, blank=True)
    
    # Fecha de creación en nuestro sistema
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def location(self):
        if self.city and self.country:
            return f"{self.city}, {self.country}"
        return "Ubicación no disponible"