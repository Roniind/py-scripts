import os

# Ruta del directorio que quieres analizar
directorio_objetivo = "."

# Tamaño mínimo en megabytes (MB)
tamano_minimo_mb = 100

# Convertir MB a bytes
tamano_minimo_bytes = tamano_minimo_mb * 1024 * 1024

print(f"\n🔍 Buscando archivos mayores a {tamano_minimo_mb} MB en '{directorio_objetivo}':\n")

# Recorrer todos los archivos (incluyendo subcarpetas)
for carpeta_actual, _, archivos in os.walk(directorio_objetivo):
    for archivo in archivos:
        ruta = os.path.join(carpeta_actual, archivo)
        try:
            tamano = os.path.getsize(ruta)
            if tamano >= tamano_minimo_bytes:
                tamano_mb = round(tamano / (1024 * 1024), 2)
                print(f"📁 {ruta} — {tamano_mb} MB")
        except FileNotFoundError:
            pass  # Ignorar archivos que fueron movidos/eliminados durante el escaneo
