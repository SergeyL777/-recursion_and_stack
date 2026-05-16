#  Рекурсивная функция для вычисления факториала числа n
def factorial(n):
    # Базовый случай: факториал 0 и 1 равен 1
    if n == 0 or n == 1:
        return 1
    # Рекурсивный случай: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Пример использования
print(factorial(5))  # Вывод: 120
print(factorial(0))  # Вывод: 1
