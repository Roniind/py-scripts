import webbrowser
import urllib.parse

# Texto que quieres buscar
termino = input("¿Qué quieres buscar en Google?: ")

# Codificar la búsqueda para que sea compatible con URLs
termino_codificado = urllib.parse.quote_plus(termino)

# Construir la URL de búsqueda
url = f"https://www.google.com/search?q={termino_codificado}"

# Abrir en el navegador por defecto (Chrome si está configurado como predeterminado)
webbrowser.open(url)

print("Abriendo Google con tu búsqueda...")
