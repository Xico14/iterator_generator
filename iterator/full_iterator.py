class FlatIterator:
    """
    Итератор, который принимает список списков и возвращает их плоское представление,
    т. е. последовательность, состоящую из вложенных элементов.
    """

    def __init__(self, list_of_list):
        """
        Инициализирует итератор.

        :param list_of_list: список списков
        """
        self.flatten_list = self.flatten(list_of_list)
        self.index = 0

    def __iter__(self):
        """
        Возвращает сам объект в качестве итератора.
        """
        return self

    def __next__(self):
        """
        Возвращает следующий элемент плоского списка.

        :return: следующий элемент
        :raises StopIteration: если достигнут конец списка
        """
        if self.index < len(self.flatten_list):
            item = self.flatten_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def flatten(self, lst):
        """
        Рекурсивно уплощает список.

        :param lst: входной список
        :return: уплощенный список
        """
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()