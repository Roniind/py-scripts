from reportlab.pdfgen import canvas
import pandas as pd
import os

def txt_a_pdf(archivo_txt, archivo_pdf):
    try:
        with open(archivo_txt, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        c = canvas.Canvas(archivo_pdf)
        y = 800
        for linea in lineas:
            if y < 50:
                c.showPage()
                y = 800
            c.drawString(40, y, linea.strip())
            y -= 20

        c.save()
        print(f"✅ {archivo_pdf} generado con éxito.")
    except Exception as e:
        print(f"❌ Error al convertir TXT a PDF: {e}")

def csv_a_xlsx(archivo_csv, archivo_excel):
    try:
        df = pd.read_csv(archivo_csv)
        df.to_excel(archivo_excel, index=False)
        print(f"✅ {archivo_excel} generado con éxito.")
    except Exception as e:
        print(f"❌ Error al convertir CSV a Excel: {e}")

# ------------------------------

if __name__ == "__main__":
    print("🧾 Conversor de Archivos\n")
    print("1. Convertir .txt a .pdf")
    print("2. Convertir .csv a .xlsx")

    opcion = input("\nSelecciona una opción (1/2): ").strip()

    if opcion == "1":
        txt = input("📄 Ruta del archivo .txt: ").strip()
        pdf = input("📄 Nombre del archivo .pdf de salida: ").strip()
        txt_a_pdf(txt, pdf)

    elif opcion == "2":
        csv = input("📄 Ruta del archivo .csv: ").strip()
        xlsx = input("📄 Nombre del archivo .xlsx de salida: ").strip()
        csv_a_xlsx(csv, xlsx)

    else:
        print("❌ Opción inválida.")
