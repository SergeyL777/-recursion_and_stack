# Рекурсивная функция для бинарного поиска элемента в отсортированном списке
def binary_search(arr, target, low=0, high=None):
    # Инициализация верхней границы при первом вызове
    if high is None:
        high = len(arr) - 1

    # Базовый случай: элемент не найден
    if low > high:
        return -1

    # Вычисление среднего индекса
    mid = (low + high) // 2

    # Элемент найден
    if arr[mid] == target:
        return mid
    # Поиск в левой половине
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # Поиск в правой половине
    else:
        return binary_search(arr, target, mid + 1, high)

# Пример использования
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(sorted_list, 7))   # Вывод: 3
print(binary_search(sorted_list, 4))   # Вывод: -1
print(binary_search(sorted_list, 1))   # Вывод: 0
