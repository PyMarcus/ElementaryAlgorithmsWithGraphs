class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.__value = value
        self.__left = left
        self.__right = right

    @property
    def value(self):
        return self.__value

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @value.setter
    def value(self, value):
        self.value = value

    @left.setter
    def left(self, node):
        self.__left = node

    @right.setter
    def right(self, node):
        self.__right = node

    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return str(self.value)
