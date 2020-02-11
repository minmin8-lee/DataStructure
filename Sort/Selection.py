
class Selection:
    """
    Selection Sort
        ~ for python3 list ~
        tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm
    """
    def __init__(self, data=None):
        self._data = data

    def mount(self, data):
        self._data = data

    def _swap(self,i ,j ):
        temp = self._data[j]
        self._data[j] = self._data[i]
        self._data[i] = temp

    def sort(self):
        for i in range(len(self._data)-1):
            # 반복자 번째 원소가 최소값이라 가정.
            # 0부터 시작하므로, 반복자 이전 원소는 모두 정렬된 상태
            minimum = self._data[i]
            target = None
            changed = False

            for j in range(i+1, len(self._data)):
                # 정렬되지않은 원소들을 끝까지 뒤져가면서 최소값을 업데이트
                if minimum > self._data[j]:
                    minimum = self._data[j]
                    changed = True
                    target = j
            if changed:
                # 최소값이 변경된 경우, 반복자의 자리 <-> 최소값의 자리 원소위치변경
                self._swap(i, target)

        return self._data
