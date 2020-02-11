
class Bubble:
    """
    Bubble Bobble Sort
        ~ for python3 list ~
        tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
    """

    def __init__(self,data):
        self._swapped = None
        self._data = data
        self._count = None

    def mount(self, data):
        self._data = data

    def _swap(self, idx):
        temp = self._data[idx]
        self._data[idx] = self._data[idx+1]
        self._data[idx+1] = temp
        self._swapped = True

    def sort(self):
        self._count = 0

        for i in range(len(self._data)):
            self._swapped = False

            # bubble sort
            for j in range(len(self._data)-1):
                if self._data[j] > self._data[j+1]:
                    self._swap(j)
                    self._add()

            # final test
            if self._swapped is False:
                print("operations: ", self._count)
                return self._data

    def _add(self):
        self._count += 1
