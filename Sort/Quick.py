
class Quick:
    """
    Quick Sort
        ~ for python3 list ~
        tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm
    """
    def __init__(self, data=None):
        self._data = data

    def mount(self, data):
        self._data = data

    def _swap(self, pos1, pos2):
        temp = self._data[pos1]
        self._data[pos1] = self._data[pos2]
        self._data[pos2] = temp

    def _pivot(self, pivot, left, right):
        while True:
            while self._data[left] < self._data[pivot]:
                left += 1
            while self._data[right] >= self._data[pivot] and right > 0:
                right -= 1
            if left >= right:
                break
            # elif self._data[left] == self._data[right]:
            #     break
            else:
                self._swap(left, right)

        self._swap(left, pivot)
        return left

    def _quick_sort(self, left, right):

        if right <= left:
            return
        else:
            pivot = right
            boundary = self._pivot(pivot, left, right-1)
            self._quick_sort(left, boundary-1)
            self._quick_sort(boundary+1, right)

    def sort(self):
        self._quick_sort(0, len(self._data)-1)
        return self._data
