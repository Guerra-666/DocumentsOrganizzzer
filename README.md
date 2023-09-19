# DocumentsOrganizzzer

---

# Proyecto de Organización de Archivos

Este proyecto es un script de Python que organiza archivos descargados en diferentes carpetas según su tipo y contenido. Los archivos se mueven o eliminan de la carpeta de descargas a otras carpetas designadas según su extensión y contenido. A continuación, se presenta una descripción detallada de cómo funciona el script y cómo se organizan los archivos.

## Requisitos

- Python 3.x
- La biblioteca Python Imaging Library (Pillow), que se puede instalar con `python3 -m pip install Pillow`

## Uso

1. Clona o descarga este repositorio en su sistema local.

2. Abre una terminal o línea de comandos y navega hasta la carpeta del repositorio.

3. Ejecute el script principal con el siguiente comando:

   ```bash
   python organize_files.py
   ```

4. El script organizará automáticamente los archivos en diferentes carpetas según su extensión y contenido. A continuación se muestra cómo se organizan los archivos:

   - **Imágenes**: Archivos con extensiones .jpg, .jpeg, .png, .gif, .bmp se comprimen y se almacenan en la carpeta de imágenes.

   - **Música**: Archivos de audio con extensiones .mp3, .wav, .flac, .aac se mueven a la carpeta de música.

   - **Videos**: Archivos de video con extensiones .mp4, .avi, .mkv se mueven a la carpeta de videos.

   - **Documentos**: Archivos de documentos con extensiones .pdf, .docx, .txt se mueven a la carpeta de documentos.

5. Los archivos que no coincidan con las extensiones mencionadas anteriormente en ninguna categoría se mantendrán en la carpeta de descargas.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.

2. Clona tu repositorio fork en tu máquina local.

   ```bash
   git clone https://github.com/tu-usuario/organize-files.git
   ```

3. Crea una rama (branch) para tu contribución.

   ```bash
   git checkout -b mi-contribucion
   ```

4. Realiza los cambios y mejoras que consideres necesarios en tu rama.

5. Haz commit y push de tus cambios a tu repositorio fork.

   ```bash
   git commit -m "Añadida nueva característica"
   git push origin mi-contribucion
   ```

6. Abre un pull request (PR) hacia este repositorio principal explicando tus cambios.


## Autor

- [Guerra-666]

Ojalá te sirva. :)

---
