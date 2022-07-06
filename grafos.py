"""
Grafos são um conjunto de véritces (nós) e arestas (arcos), muito utilizado para determinar rotas, ou problemas
correlacionados.
A representação de gráfos pode ser feitas de duas formas, listas de adjacência e matriz de adjacência
Grafo = (V, A)
# normalmente, listas são mais utilizados
# grau de um vértice: Número de arestas sobre ele
# podem ser direcionados (orientados) ou não (possuem grau de entrada e saída). Laço (quando uma aresta liga ao msm vértice - grau 2)
# multigrafo => vértice com arestas paralelas
# vértice folha é aquele ligado apenas por um outro, se ciclos, como em uma árvore
# grafo completo é o que possui ciclo completo
# passeio => sequência de arestas de um ponto ao outro (não vale pular arestas)
# trilha => todas as arestas são distintas (não se repete arestas)
# trilha fechada => vértice final é igual ao inicial
# caminho => não repete vértices (todo caminho é uma trilha, mas não o contrário)
"""
from typing import Any


"""
Representacao por listas:
"""
class GrafoRepresentacaoLista:
    # vantagem -> usa o menos memória é mais usada,
    # desvantagens -> maiortempo em buscas
    def __init__(self, vertice: Any) -> None:
        """
        O vértice deve ser definido considerando o inicio em 1,por conveniência
        :param vertice:
        """
        self.__vertices: Any = vertice
        self.grafo: list[list] = [[] for total in
                       range(1, self.vertice + 1)]  # a quantidade de linhas é igual a quantidade de vértices

    @property
    def vertice(self) -> Any:
        return self.__vertices

    def inserirArestaNaoDirecionada(self, u: Any, v: Any) -> None:
        """
        Arestas não direcionadas fazem referência uma a outra.
        :param u: inicio
        :param v: fim
        :return: None
        """
        self.grafo[u - 1].append(v)
        self.grafo[v - 1].append(u)

    def exibirListaDeAdjacenciaNaoDirecionada(self) -> None:
        # imprime a lista, como ida e volta, já que não é direcionada
        print(self.grafo)

    def inserirArestaNaoDirecionadaComPeso(self, u: Any, v: Any, peso: int or float) -> None:
        """
        Insere peso nas arestas
        :param u:
        :param v:
        :param peso:
        :return:
        """
        self.grafo[u - 1].append([v, peso])
        self.grafo[v - 1].append([u, peso])

    def inserirArestaDirecionada(self, u: Any, v: Any) -> None:
        """
        Insere aresta direcionada
        :param u:
        :param v:
        :return:
        """
        self.grafo[u - 1].append(v)

    def exibirArestaDirecionada(self) -> None:
        print("LISTA DE ADJACÊNCIA DIRECIONADA")
        for linha in range(self.vertice):
            print(f"{linha + 1}: ", end=" ")
            for conteudo in self.grafo[linha]:
                print(f"{conteudo} -> ", end=" ")
            print()

    def inserirArestaDirecionadaComPeso(self, u: Any, v: Any, peso: Any) -> None:
        """
        Insere aresta direcionada
        :param u:
        :param v:
        :return:
        """
        self.grafo[u - 1].append([v, peso])

    def removeEspecifico(self, posicao: int) -> None:
        print("Grafo antes da remocao: ")
        print(self.grafo)
        for indice in range(posicao, len(self.grafo) - 1):
            self.grafo[indice] = self.grafo[indice + 1]
        self.grafo.pop()
        print("Grafo apos a remocao: ")
        print(self.grafo)

    def removeRapidamente(self, posicao: int) -> None:
        print("Grafo antes da remocao: ")
        print(self.grafo)
        del self.grafo[posicao]
        print("Grafo apos a remocao: ")
        print(self.grafo)



"""
Representacao por matrizes:
"""
class GrafoRepresentacaoMatrizes:
    # vantagem -> melhor tempo em buscas (ideal para grafos pequenos)
    # desvantagens -> usa o dobro de memória da listas de adjacências (por isso, em alguns casos, armazena-se so a
    # parte de cima da diagonal)
    def __init__(self, vertice: Any) -> None:
        """
        Quantidade de vértices
        :param vertice:
        """
        self.__vertice = vertice
        self.grafo = []
        self.matriz = [self.grafo.append([0] * self.vertice) for i in range(self.vertice)]

    @property
    def vertice(self) -> Any:
        return self.__vertice

    def exibirMatrizDeAdjacencia(self) -> None:
        print("Matriz de adjacência")
        for i in range(len(self.grafo)):
            print("|", end="")
            for j in range(len(self.grafo)):
                print(self.grafo[i][j], end="")
            print("|",end="")
            print()

    def exibirMatrizDeAdjacenciaComPeso(self) -> None:
        print("Matriz de adjacência")
        tam: int = len(self.grafo)
        for i in range(len(self.grafo)):
            print(self.grafo[i], end=" " * tam)
            print()

    def inserirArestaDirecionada(self, u: Any, v: Any) -> None:
        ### grafo simples
        self.grafo[u - 1][v - 1] = 1

    def inserirArestaNaoDirecionadaMultiGrafo(self, u: Any, v: Any) -> None:
        # multigrafos
        self.grafo[u - 1][v - 1] += 1

    def inserirArestaNaoDirecionada(self, u: Any, v: Any) -> None:
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def inserirArestaDirecionadaComPeso(self, u: Any, v: Any, peso: int or float = 1) -> None:
        self.grafo[u - 1][v - 1] = peso

    def removeValorMatriz(self, line: int, column: int) -> None:
        self.grafo[line][column] = 0

    def automatizacaoDeInsercaoNaMatriz(self) -> None:
        valor = True
        while valor:
            print("Digite ctrl-c para finalizar a inserção")
            try:
                u: Any = int(input("u: "))
                v: Any = int(input("v: "))
                peso: int or float = int(input("peso: "))
                self.inserirArestaDirecionadaComPeso(u, v, peso)
            except KeyboardInterrupt:
                self.exibirMatrizDeAdjacenciaComPeso()
                valor = False
            except  ValueError:
                self.exibirMatrizDeAdjacenciaComPeso()
                valor = False


if __name__ == '__main__':
    grafo = GrafoRepresentacaoLista(5)
    #grafo.inserirArestaNaoDirecionada(1, 2)
    #grafo.inserirArestaNaoDirecionada(1, 3)
    #grafo.inserirArestaNaoDirecionada(2, 1)
    #grafo.inserirArestaNaoDirecionada(3, 1)
    #grafo.inserirArestaNaoDirecionadaComPeso(1, 2, 5)
    #grafo.inserirArestaNaoDirecionadaComPeso(1, 3, 2)
    #grafo.inserirArestaNaoDirecionadaComPeso(2, 1, 5)
    #grafo.inserirArestaNaoDirecionadaComPeso(3, 1, 2)
    #grafo.exibirListaDeAdjacenciaNaoDirecionada()
    grafo.inserirArestaDirecionadaComPeso(1, 2, 4)
    grafo.inserirArestaDirecionadaComPeso(1, 3, 5)
    grafo.inserirArestaDirecionadaComPeso(2, 1, 4)
    grafo.exibirArestaDirecionada()
    # remocao
    #grafo.removeEspecifico(1)
    #grafo.removeRapidamente(1)

    grafo2 = GrafoRepresentacaoMatrizes(5)
    grafo2.inserirArestaDirecionadaComPeso(1, 2, 5)
    grafo2.inserirArestaDirecionadaComPeso(1, 3, 6)
    grafo2.exibirMatrizDeAdjacenciaComPeso()
    """
    i = int(input("insira a quantidade de vertices: "))
    grafo3 = GrafoRepresentacaoMatrizes(i)
    grafo3.automatizacaoDeInsercaoNaMatriz()
    """
    # remocao:
    print("REMOV")
    grafo2.removeValorMatriz(0, 2)
    grafo2.exibirMatrizDeAdjacenciaComPeso()
