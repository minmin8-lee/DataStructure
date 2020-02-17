

class BinarySearch:
    """
    Binary Search
        ~ for python3 list
        tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm
    """
    def __init__(self, data=None):
        self._data = data
        self._is_sorted = False
        self.__sort_test__()

    def mount(self, data):
        self._data = data
        self.__sort_test__()

    def __sort_test__(self):
        if self._data is None:
            print("warning : empty data")
            return -1

        for i in range(len(self._data)-1):
            if self._data[i+1] < self._data[i]:
                self._is_sorted = False
                print("warning : data unsorted")
                return -1
            i += 1
        self._is_sorted = True

    def search(self, target):
        if self._is_sorted:
            #  step 1. set initial values
            cnt = 0
            low_bound = 0
            upp_bound = len(self._data)-1
            check = False

            #  step 2. loop while lower < upper
            while check is False:
                if low_bound > upp_bound:
                    print("not found")
                    return -1

                median = low_bound + int((upp_bound - low_bound) / 2)

                if self._data[median] < target:
                    low_bound = median+1

                elif self._data[median] > target:
                    upp_bound = median-1

                else:
                    check = True
                    print(cnt)
                    return median
                cnt += 1
        else:
            print("works only for sorted list")
            return -1
