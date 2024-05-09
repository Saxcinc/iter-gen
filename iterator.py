class FlatIterator:
    def __init__(self, list_of_list):
        self.list_ = list_of_list

    def __iter__(self):
        self.cursor = -1
        self.index = 0
        return self

    def __next__(self):
        self.cursor += 1
        self.index_list = self.list_[self.index]

        if self.cursor >= len(self.index_list):
            self.cursor = 0
            self.index += 1
            if self.index == len(self.list_):
                raise StopIteration
            self.index_list = self.list_[self.index]

        return self.index_list[self.cursor]

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