import os

# Ruta de la carpeta a limpiar
carpeta_objetivo = "carpeta_ejemplo"  # puedes cambiar esto

# Extensiones a eliminar
extensiones_inutiles = ['.tmp', '.log', '.bak']

# Contador de archivos eliminados
eliminados = 0

# Recorrer archivos
for archivo in os.listdir(carpeta_objetivo):
    ruta = os.path.join(carpeta_objetivo, archivo)
    if os.path.isfile(ruta):
        _, extension = os.path.splitext(archivo)
        if extension in extensiones_inutiles:
            os.remove(ruta)
            print(f"Eliminado: {archivo}")
            eliminados += 1

print(f"\n✅ Archivos eliminados: {eliminados}")

