import os
import subprocess
import platform
import psutil  # Necesita instalarse con pip

def abrir_aplicacion(nombre_app):
    print(f"🟢 Abriendo: {nombre_app}")
    subprocess.Popen(nombre_app)

def cerrar_aplicacion(nombre_proceso):
    print(f"🔴 Cerrando: {nombre_proceso}")
    for proceso in psutil.process_iter(['name']):
        if proceso.info['name'] and nombre_proceso.lower() in proceso.info['name'].lower():
            proceso.kill()
            print(f"✔️ Proceso {proceso.info['name']} terminado.")

# -------- CONFIGURA AQUÍ --------

sistema = platform.system()

if sistema == "Windows":
    # Ruta o nombre de la app (ej: Chrome, Notepad)
    abrir_aplicacion("notepad.exe")  # abre el Bloc de notas
    # cerrar_aplicacion("notepad.exe")  # cierra el Bloc de notas

elif sistema == "Linux":
    abrir_aplicacion("gedit")  # o cualquier editor
    # cerrar_aplicacion("gedit")

else:
    print("⛔ Sistema operativo no soportado")
