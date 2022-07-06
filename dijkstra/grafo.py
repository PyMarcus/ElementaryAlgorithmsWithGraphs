from dijkstra import dijkstra


class Grafo:
    def __init__(self, vertice) -> None:
        self.__vertice = vertice
        self.__grafo = []
        self.__matriz = [self.grafo.append([0] * vertice) for i in range(self.vertice)]

    @property
    def vertice(self):
        return self.__vertice

    @property
    def grafo(self):
        return self.__grafo

    @property
    def matriz(self):
        return self.__matriz

    def insereArestaComPesoNaoDirecionada(self, u, v, peso):
        self.grafo[u - 1][v - 1] = peso
        self.grafo[v - 1][u - 1] = peso

    def __str__(self):
        """
        imprime o grafo
        :return:
        """
        for line in range(self.vertice):
            for c in range(self.vertice):
                print(self.grafo[line][c], end=' ')
            print()
        return ''


if __name__ == '__main__':
    grafo = Grafo(7)
    grafo.insereArestaComPesoNaoDirecionada(1, 1, 0)  # origem
    grafo.insereArestaComPesoNaoDirecionada(1, 2, 5)  # armazem
    grafo.insereArestaComPesoNaoDirecionada(1, 3, 6)  # pracinha
    grafo.insereArestaComPesoNaoDirecionada(1, 4, 10)  # quitanda
    grafo.insereArestaComPesoNaoDirecionada(3, 4, 3)  # padaria à quitanda
    grafo.insereArestaComPesoNaoDirecionada(2, 5, 13)  # armazem à banca
    grafo.insereArestaComPesoNaoDirecionada(3, 5, 11)  # padaria `a quitanda
    grafo.insereArestaComPesoNaoDirecionada(5, 4, 6)  # padaria à cancela
    grafo.insereArestaComPesoNaoDirecionada(5, 7, 3)  # padaria à cancela
    grafo.insereArestaComPesoNaoDirecionada(3, 6, 6)  # padaria à cancela
    grafo.insereArestaComPesoNaoDirecionada(4, 6, 4)  # padaria à cancela
    grafo.insereArestaComPesoNaoDirecionada(7, 6, 8)  # padaria à cancela
    print(dijkstra(1, 7, grafo.grafo))

