from Search.Binary import BinarySearch


class InterpolationSearch(BinarySearch):
    def __init__(self, data):
        super().__init__(data)

    def search(self, target):
        if self._is_sorted:
            #  step 1. set initial values
            cnt = 0
            low_bound = 0
            upp_bound = len(self._data) - 1
            check = False

            #  step 2. loop while lower < upper and A[lower] != A[upper]
            while check is False:
                if low_bound > upp_bound and self._data[low_bound] != self._data[upp_bound]:
                    print("not found")
                    return -1

                fore = (upp_bound - low_bound) / (self._data[upp_bound] - self._data[low_bound])
                multi = target - self._data[low_bound]

                median = low_bound + int(fore*multi)

                if self._data[median] < target:
                    low_bound = median + 1

                elif self._data[median] > target:
                    upp_bound = median - 1

                else:
                    check = True
                    print(cnt)
                    return median
                cnt += 1

        else:
            print("works only for sorted list")
            return -1
