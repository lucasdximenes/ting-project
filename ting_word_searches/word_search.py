from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    Queue = instance
    list_word_occurrences = []
    for i in range(len(Queue.queue)):
        data = Queue.search(i)
        occurrences = []
        for j in range(len(data['linhas_do_arquivo'])):
            if word.lower() in data['linhas_do_arquivo'][j].lower():
                occurrences.append(
                    {
                        "linha": j + 1,
                    }
                )
        if len(occurrences) > 0:
            list_word_occurrences.append(
                {
                    "palavra": word,
                    "arquivo": data['nome_do_arquivo'],
                    "ocorrencias": occurrences,
                }
            )
    return list_word_occurrences


def search_by_word(word, instance: Queue):
    Queue = instance
    list_word_occurrences = []
    for i in range(len(Queue.queue)):
        data = Queue.search(i)
        occurrences = []
        for j in range(len(data['linhas_do_arquivo'])):
            if word.lower() in data['linhas_do_arquivo'][j].lower():
                occurrences.append(
                    {
                        "linha": j + 1,
                        "conteudo": data['linhas_do_arquivo'][j],
                    }
                )
        if len(occurrences) > 0:
            list_word_occurrences.append(
                {
                    "palavra": word,
                    "arquivo": data['nome_do_arquivo'],
                    "ocorrencias": occurrences,
                }
            )
    return list_word_occurrences
