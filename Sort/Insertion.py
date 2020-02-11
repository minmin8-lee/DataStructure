
class Insertion:
    """
    Insertion sort
        ~ for python3 list ~
        tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm
    """

    def __init__(self, data):
        self._data = data

    def mount(self,data):
        self._data = data

    def _swap(self, i):
        temp = self._data[i]
        self._data[i] = self._data[i+1]
        self._data[i+1] = temp
        return self._data[i]

    def sort(self):
        for i in range(len(self._data)-1):
            # 지정위치와 다음위치의 크기를 비교하여 다음 것이 더 작으면 자리바꿈
            if self._data[i] > self._data[i+1]:
                target = self._swap(i)
                # 바뀌어서 넘어온 자리를 i로 지정
                hole = i
                while hole > 0 and self._data[hole-1] > target:
                    # 1개씩 찾아보면서 넘어온 값이 들어갈 자리를 찾는다
                    # 바뀌어서 넘어온 원소 > 이미 정렬된 배열의 원소 : 그 자리는 아님
                    self._data[hole] = self._data[hole-1]
                    hole -= 1
                # 바뀌어서 넘어온 원소 < 이미 정렬된 배열의 원소인 첫번째 자리가 들어갈 자리
                self._data[hole] = target
        return self._data
