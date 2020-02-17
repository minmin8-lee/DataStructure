
class LinearSearch:
    """
    Linear Search
        ~ for python3 list
        tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm
    """
    def __init__(self, data):
        self._data = data

    def mount(self, data):
        self._data = data

    def search(self, target):
        for i in range(len(self._data)):
            if self._data[i] == target:
                print(i)
                return i
            i += 1
        print("not found")

