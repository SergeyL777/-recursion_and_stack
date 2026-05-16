# Класс Stack с основными операциями
class Stack:
    def __init__(self):
        """Инициализация пустого стека"""
        self.items = []

    def push(self, item):
        """Добавление элемента на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удаление и возврат элемента с вершины стека
        Вызывает IndexError, если стек пуст"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        """Проверка, пуст ли стек"""
        return len(self.items) == 0

    def peek(self):
        """Возврат элемента с вершины стека без удаления
        Вызывает IndexError, если стек пуст"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Возвращает количество элементов в стеке"""
        return len(self.items)

# Пример использования
stack = Stack()
print(stack.is_empty())  # Вывод: True

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())        # Вывод: 3
print(stack.pop())         # Вывод: 3
print(stack.size())       # Вывод: 2
print(stack.is_empty())   # Вывод: False
