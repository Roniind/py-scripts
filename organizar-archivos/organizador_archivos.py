import os
import shutil

# Ruta de la carpeta que quieres organizar
carpeta_objetivo = "archivos_desordenados"

# Diccionario de categorías y extensiones asociadas
tipos_de_archivo = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "videos": [".mp4", ".avi", ".mov"],
    "musica": [".mp3", ".wav", ".aac"],
    "comprimidos": [".zip", ".rar", ".7z"]
}

# Crear carpetas si no existen
for categoria in tipos_de_archivo:
    ruta = os.path.join(carpeta_objetivo, categoria)
    if not os.path.exists(ruta):
        os.makedirs(ruta)

# Mover archivos
for archivo in os.listdir(carpeta_objetivo):
    ruta_actual = os.path.join(carpeta_objetivo, archivo)
    if os.path.isfile(ruta_actual):
        _, extension = os.path.splitext(archivo)
        for categoria, extensiones in tipos_de_archivo.items():
            if extension.lower() in extensiones:
                destino = os.path.join(carpeta_objetivo, categoria, archivo)
                shutil.move(ruta_actual, destino)
                print(f"✅ {archivo} → {categoria}/")
                break
