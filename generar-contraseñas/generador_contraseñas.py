import random
import string
import pyperclip  # copiar al portapapeles

def generar_contraseña(longitud=16):
    if longitud < 8:
        print("⚠️ Recomendado usar mínimo 8 caracteres para seguridad.")
    
    # Caracteres disponibles
    letras = string.ascii_letters  # a-z, A-Z
    numeros = string.digits        # 0-9
    simbolos = string.punctuation  # !@#$%^&*()_+-=...

    # Combinarlos todos
    todos = letras + numeros + simbolos

    # Crear contraseña aleatoria
    contraseña = ''.join(random.choice(todos) for _ in range(longitud))

    # Copiar al portapapeles
    pyperclip.copy(contraseña)

    return contraseña

# ------------------------------

if __name__ == "__main__":
    print("🔐 Generador de Contraseñas Seguras\n")
    
    try:
        longitud = int(input("¿Longitud de la contraseña (recomendado: 12+)? "))
    except ValueError:
        print("⚠️ Entrada no válida. Usando longitud por defecto: 16")
        longitud = 16

    contraseña = generar_contraseña(longitud)
    print(f"\n✅ Contraseña generada: {contraseña}")
    print("📋 Se ha copiado al portapapeles automáticamente.")
