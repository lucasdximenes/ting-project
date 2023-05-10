import os
import sys


def txt_importer(path_file):
    # Verifica se o arquivo existe
    if not os.path.exists(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    # Verifica se a extensão do arquivo é .txt
    if not path_file.endswith('.txt'):
        return sys.stderr.write("Formato inválido\n")

    # Importa as linhas do arquivo e retorna em uma lista
    with open(path_file, 'r') as file:
        lines = file.read().split('\n')
    return lines
