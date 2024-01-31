class FlatIterator:
    """
    Итератор, который преобразует список списков в одну последовательность вложенных элементов.
    """
    def __init__(self, list_of_list):
        """
        Инициализирует FlatIterator с списком списков.

        Аргументы:
        list_of_list (list): Список списков, который нужно преобразовать в плоскую последовательность.
        """
        self.list_of_list = list_of_list
        self.flatten_list = [item for sublist in list_of_list for item in sublist]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Возвращает следующий элемент в плоской последовательности.

        Возвращает:
        Следующий элемент в плоской последовательности.

        Вызывает:
        StopIteration: Если больше нет элементов для возврата.
        """
        if self.index < len(self.flatten_list):
            item = self.flatten_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()