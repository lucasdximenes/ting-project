from .file_management import txt_importer
import sys


def process(path_file, instance):
    Queue = instance
    file_lines = txt_importer(path_file)

    if any(path_file == data['nome_do_arquivo'] for data in Queue.queue):
        return

    dict_data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_lines),
        'linhas_do_arquivo': file_lines,
    }

    Queue.enqueue(dict_data)
    sys.stdout.write(str(dict_data))


def remove(instance):
    Queue = instance
    if len(Queue) == 0:
        return sys.stdout.write('Não há elementos\n')

    dequeued_file = Queue.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f'Arquivo {dequeued_file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
