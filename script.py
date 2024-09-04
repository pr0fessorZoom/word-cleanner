import re

def eliminar_caracteres_especiales(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Reemplazar todos los caracteres que no sean letras, números o espacios por una cadena vacía
            cleaned_line = re.sub(r'[^a-zA-Z0-9\s]', '', line)
            outfile.write(cleaned_line)

# Ejemplo de uso
input_file = 'test.txt'  # Archivo de entrada
output_file = 'test_limpio.txt'  # Archivo de salida

eliminar_caracteres_especiales(input_file, output_file)
