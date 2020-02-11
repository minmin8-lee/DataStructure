
class Merge:
    """
    Merge Sort
        ~ for python3 list ~
        tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm
    """
    def __init__(self, data=None):
        self._data = data

    def mount(self, data):
        self._data = data

    def sort(self, divider=None):
        if divider is None:
            divider = self._data

        if len(divider) < 2:
            return divider

        half = int(len(divider) / 2)

        first_half = divider[:half]
        last_half = divider[half:]

        first_half = self.sort(first_half)
        last_half = self.sort(last_half)

        return self._merge(first_half, last_half)

    @staticmethod
    def _is_in(data):

        # no element -> False
        if len(data) < 1:
            return False

        # at least an element -> True
        else:
            return True

    def _merge(self, first_half, last_half):

        result = []
        while self._is_in(first_half) and self._is_in(last_half):
            # 어느 한 쪽이 텅 빌때까지 작은쪽을 비복원추출하여 새로운 배열에 추가해 나간다
            if first_half[0] > last_half[0]:
                result.append(last_half.pop(0))
            else:
                result.append(first_half.pop(0))

        # 남은 원소를 전부 순서대로 추출하여 결과 배열에 추가해 나간다.
        # 텅 빈 쪽은 이미 정렬되어 있기 때문에 순서대로 뽑아 넣으면 정렬된 결과가 됨
        while len(first_half) > 0:
            result.append(first_half.pop(0))

        while len(last_half) > 0:
            result.append(last_half.pop(0))

        return result






