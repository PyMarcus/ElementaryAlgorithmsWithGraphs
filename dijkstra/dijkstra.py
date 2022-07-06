import queue


def dijkstra(origem, vertices, grafo):
    """
    Encontra o menor caminho de uma origem até N vértices
    :param origem:
    :param vertices:
    :param grafo:
    :return:
    """
    custo = [[-1, 0] for i in range(vertices)]  # -1 representa infinito, ou seja, não passou ainda, 0 é para ser
    # aloca para algum vértice
    custo[origem - 1] = [0, origem]  # determina que o custo na posicao de origem é zero (vetor que conterá o menor caminho)
    minimo = queue.Queue()
    minimo.put(custo[origem - 1])  # adiciona na fila, a origem e seu custo (zero)
    while minimo.qsize() > 0:  # enquanto a fila tiver dados, ou seja, nao percorreu todos, executa:
        peso, vertice = minimo.get()  # remove o custo e o vertice predescessor
        for i in range(vertices):
            if grafo[vertice - 1][i] != 0:  # percorre a matriz (grafo) separando os zeros (onde não há conexões)
                if custo[i][0] == -1 or custo[i][0] > peso + grafo[vertice - 1][i]: # se o custo for infinito ou maior que o peso ate o momento,significa
                    # que não passou pelo vértice ainda
                    custo[i] = [peso + grafo[vertice - 1][i], vertice]  # assim, armazena o peso menor e o vertice correspondente
                    minimo.put([custo[i][0], i + 1])  # adiciona o custo e o próximo vértice
    return custo

