# Importar la clase Image desde la biblioteca PIL (Pillow)
from PIL import Image
import os

# Rutas de carpetas de origen y destino para diferentes tipos de archivos
downloadsFolder = "/Users/#YOUR_USER#/Downloads"
picturesFolder = "/Users/#YOUR_USER#/Pictures/"
musicFolder = "/Users/#YOUR_USER#/Music/"
documentsFolder = "/Users/#YOUR_USER#/Documents/"
videosFolder = "/Users/#YOUR_USER#/Videos/"

# Función principal que se ejecuta al iniciar el script
if __name__ == "__main__":
    # Iterar a través de los archivos en la carpeta de descargas
    for filename in os.listdir(downloadsFolder):
        # Obtener el nombre del archivo y su extensión
        name, extension = os.path.splitext(downloadsFolder + filename)

        # Comprobar si la extensión está en la lista de extensiones de imágenes
        if extension.lower() in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
            # Abrir la imagen
            picture = Image.open(downloadsFolder + filename)
            # Guardar la imagen comprimida en la carpeta de imágenes
            picture.save(picturesFolder + "compressed_" + filename, optimize=True, quality=60)
            # Eliminar el archivo original de la carpeta de descargas
            os.remove(downloadsFolder + filename)
            # Imprimir el nombre del archivo y su extensión
            print(name + ": " + extension)

        # Comprobar si la extensión está en la lista de extensiones de audio
        elif extension.lower() in [".mp3", ".wav", ".flac", ".aac"]:
            # Mover el archivo a la carpeta de música
            os.rename(downloadsFolder + filename, musicFolder + filename)

        # Comprobar si la extensión está en la lista de extensiones de video
        elif extension.lower() in [".mp4", ".avi", ".mkv"]:
            # Mover el archivo a la carpeta de videos
            os.rename(downloadsFolder + filename, videosFolder + filename)

        # Comprobar si la extensión está en la lista de extensiones de documentos
        elif extension.lower() in [".pdf", ".docx", ".txt"]:
            # Mover el archivo a la carpeta de documentos
            os.rename(downloadsFolder + filename, documentsFolder + filename)
