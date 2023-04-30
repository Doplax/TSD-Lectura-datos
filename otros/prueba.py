# prueba.py
import os

# Obtiene la ruta absoluta al directorio en el que se encuentra este script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Crea la ruta absoluta al archivo que deseamos crear
file_path = os.path.join(dir_path, 'hola_mundo.txt')

# Abre el archivo en modo escritura ('w' significa 'write')
with open(file_path, 'w') as fichero:
    # Escribe 'Hola Mundo' en el archivo
    fichero.write('Hola Mundo')

# Imprime un mensaje para confirmar que el archivo fue creado y escrito
print(f"Archivo creado y escrito exitosamente en {file_path}")