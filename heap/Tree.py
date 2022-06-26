from queue import Queue

from Node import Node


class Tree:
    def __init__(self, root=None) -> None:
        """
        Árvore heap é uma árvore binária que possui as seguintes características:
        1) O maior valor está sempre na raíz
        2) possui boa eficiencia na inserção e remocao O(logn)
        3) alternativa à fila de prioridade
        4) podem ser representadas como array (resultado do percurso em largura)
        5) adição é feita sempre na próxima posição livre
        6) remoção é sempre do maior, ou seja, pela raíz.
        7) heapify é um método que compara qual o maior de 3 nós e o coloca na raíz
        9) de acordo com o indice do array, os metodos left, right, parent são implementados
        10) esquerda de um no de indice i => 2i + 1
        11) direita de um nó de indice i => 2(i + 1)
        12) raiz de um nó de indice i => (i - 1) / 2
        """
        self.root = root
        self.values = [100, 19, 36, 17, 3, 25, 1, 2, 7]
        self.heap_ = []  # heap é uma lista
        self.node = 0  # quantidade de nós
        ...

    def preOrder(self, node) -> None:
        if node is None:
            pass
        else:
            print(node.value, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def posOrder(self, node) -> None:
        if node is None:
            pass
        else:
            self.preOrder(node.left)
            self.preOrder(node.right)
            print(node.value, end=" ")

    def inOrder(self, node) -> None:
        if node is None:
            pass
        else:
            self.preOrder(node.left)
            print(node.value, end=" ")
            self.preOrder(node.right)

    def deepInsert(self, node=None, c=0, root=None) -> None:
        if c < 8:
            i = int(input('insert: '))
            c += 1
            if root is None:
                root = Node(i)
                node = root
            if i <= root.value:
                node.left = Node(i)
                self.deepInsert(node.left, c, root)
            else:
                node.right = Node(i)
                self.deepInsert(node.right, c, root)
        else:
            self.inOrder(root)

    def largeInsertion(self):
        """
        Inserção em largura
        :return:
        """

        if self.root is None:
            self.root = Node(self.values[0])
        fila = Queue()
        fila.put(self.root)
        index = 1
        fila2 = Queue()
        fila2.put(self.root)
        while index < len(self.values):
            node = fila.get()
            node.left = Node(self.values[index])
            node.right = Node(self.values[index + 1])
            fila.put(node.left)
            fila.put(node.right)
            index += 2
        #self.preOrder(self.root)
        return self.root

    def allocHeap(self, parent, left=None, right=None) :
        """
        faz com que o nó pai de sub árvores sempre seja o maior
        :param parent:
        :param left:
        :param right:
        :return:
        """

        #print("\nIN")
        #print(f"{parent.value} {left.value} {right.value}", end=" ")
        if left is not None:
            if parent <= left:
                aux = parent
                parent = left
                left = aux
        if right is not None:
            if parent <= right:
                aux = parent
                parent = right
                right = aux
        #print("\nOUT")
        #print(f"{parent.value} {left.value} {right.value}", end=" ")

        return parent, left, right

    def heap(self) -> list:
        """
        Ordena conforme o heap
        :return:
        """
        nodes = []
        root = self.largeInsertion()
        queue = Queue()
        queue.put(root)
        left = ''
        right = ''
        c = len(self.values) / 3
        while c > 0:
            node = queue.get()
            if node.left is not None and node.right is not None:
                node, left, right = self.allocHeap(node, node.left, node.right)
            if node.left is None and node.right is not None:
                node, left, right = self.allocHeap(node, None, node.right)
            if node.left is not None and node.right is  None:
                node, left, right = self.allocHeap(node, node.left)
            nodes.append([node, left, right])
            queue.put(left)
            queue.put(right)
            c -= 1
        return nodes

    def maxHeapAdd(self, node):
        """
        Implementacao real
        :return:
        """
        self.heap_.append(node)
        self.node += 1
        son = self.node
        while True:
            if son == 1:
                # significa que é a raíz,portanto:
                break
            father = son // 2 # resultado inteiro da divisao
            if self.heap_[son - 1] >= self.heap_[father - 1]: # se o no filho for maior que o pai, inverte
                self.heap_[son - 1], self.heap_[father - 1] = self.heap_[father - 1], self.heap_[son - 1]
                son = father
            else:
                break

    def maxHeapRemove(self):
        """
        A remoção consite em pegar e remover a raíz.No lugar dela
        acrescenta-se o último nó e monta a estrutura heap novamente
        :return:
        """
        self.heap_[0] = self.heap_.pop()
        index = 1
        self.node -= 1
        while True:
            left_son = 2 * index # 2x
            right_son = left_son + 1  # 2x + 1
            if left_son > self.node:  # se a esquerda for maior que o total de nós, então, não existe
                break
            # se o filho da direita for maior que a esquerda:
            if right_son <= self.node:
                if self.heap_[right_son - 1] > self.heap_[left_son - 1]:
                    left_son = 0
            if left_son == 0:
                if self.heap_[index - 1] < self.heap_[right_son - 1]:
                    self.heap_[index - 1], self.heap_[right_son - 1] = self.heap_[right_son - 1], self.heap_[index - 1]
            else:
                if self.heap_[index - 1] < self.heap_[left_son - 1]:
                    self.heap_[index - 1], self.heap_[left_son - 1] = self.heap_[left_son - 1], self.heap_[index - 1]
            print(self.heap_)
            index += 1

    def __len__(self):
        return self.node

    def maior(self):
        return self.heap_[0]


# [36, 17, 25, 7, 3, 19, 1, 2]
if __name__ == '__main__':
    value = [17, 36, 25, 7, 3, 100, 1, 2, 19]
    j = Node(value[8])
    i = Node(value[7])
    g = Node(value[6])
    f = Node(value[5], i, j)
    e = Node(value[4])
    d = Node(value[3])
    c = Node(value[2], f, g)
    b = Node(value[1], d, e)
    a = Node(value[0], b, c)
    tree = Tree()
    # tree.deepInsert()
    # tree.preOrder(a)
    # node_heap = tree.heap()
    for item in value:
        tree.maxHeapAdd(item)
    tree.maxHeapRemove()
    print(tree.heap_)


