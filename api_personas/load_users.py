#!/usr/bin/env python
"""
Script para cargar usuarios desde la API de RandomUser
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_mvt.settings')
django.setup()

from users.services.user_services import load_users_from_api, clear_all_users

def main():
    print("=== Cargador de Usuarios Aleatorios ===")
    print("1. Cargar usuarios desde la API")
    print("2. Limpiar todos los usuarios")
    print("3. Recargar usuarios (limpiar + cargar)")
    
    choice = input("\nSelecciona una opción (1-3): ").strip()
    
    if choice == "1":
        print("\nCargando usuarios desde la API...")
        count = load_users_from_api()
        print(f"\n✅ Se cargaron {count} usuarios exitosamente")
        
    elif choice == "2":
        confirm = input("\n¿Estás seguro de que quieres eliminar todos los usuarios? (s/N): ").strip().lower()
        if confirm == 's':
            clear_all_users()
            print("\n✅ Todos los usuarios han sido eliminados")
        else:
            print("\n❌ Operación cancelada")
            
    elif choice == "3":
        print("\nLimpiando usuarios existentes...")
        clear_all_users()
        print("Cargando usuarios desde la API...")
        count = load_users_from_api()
        print(f"\n✅ Se recargaron {count} usuarios exitosamente")
        
    else:
        print("\n❌ Opción inválida")

if __name__ == "__main__":
    main()
