import os

# Ruta de la carpeta con archivos a renombrar
carpeta = "archivos"

# Prefijo base para el nuevo nombre
prefijo = "documento_"

# Obtener la lista de archivos
archivos = os.listdir(carpeta)

# Filtrar solo archivos (no carpetas)
archivos = [f for f in archivos if os.path.isfile(os.path.join(carpeta, f))]

# Renombrar cada archivo
for i, nombre_archivo in enumerate(archivos, start=1):
    ruta_antigua = os.path.join(carpeta, nombre_archivo)
    extension = os.path.splitext(nombre_archivo)[1]
    nuevo_nombre = f"{prefijo}{i}{extension}"
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)
    os.rename(ruta_antigua, ruta_nueva)
    print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
