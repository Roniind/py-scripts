from pytube import YouTube
import os
from moviepy.editor import AudioFileClip

def descargar_video(url, solo_audio=False):
    try:
        yt = YouTube(url)
        titulo = yt.title
        print(f"\n🎬 Título: {titulo}")
        
        if solo_audio:
            print("🔊 Descargando solo el audio...")
            stream = yt.streams.filter(only_audio=True).first()
            salida = stream.download(output_path="descargas", filename_prefix="AUDIO_")
            
            # Convertir a .mp3
            base, _ = os.path.splitext(salida)
            nuevo_archivo = base + ".mp3"
            clip = AudioFileClip(salida)
            clip.write_audiofile(nuevo_archivo)
            clip.close()
            os.remove(salida)  # eliminar archivo mp4 temporal
            print(f"✅ Audio guardado como: {nuevo_archivo}")
        else:
            print("📹 Descargando video en alta calidad...")
            stream = yt.streams.get_highest_resolution()
            salida = stream.download(output_path="descargas", filename_prefix="VIDEO_")
            print(f"✅ Video guardado en: {salida}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

# ------------------------------

if __name__ == "__main__":
    print("🎵 Descargador de YouTube (Video o Audio)\n")

    url = input("🔗 Pega la URL del video: ").strip()

    modo = input("¿Quieres solo audio? (s/n): ").strip().lower()
    solo_audio = modo == "s"

    descargar_video(url, solo_audio)
