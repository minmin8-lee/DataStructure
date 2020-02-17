
from Sort.Merge import Merge
merge = Merge([9, 8, 7, 6, 5])
sorted_list = merge.sort()
print(sorted_list)

merge.mount([14, 33, 27, 10, 35, 19, 42, 44, 17])
sorted_list = merge.sort()
print(sorted_list)

from Sort.Quick import Quick
quick = Quick([9, 8, 7, 6, 5])
sorted_list = quick.sort()
print(sorted_list)

quick.mount([14, 33, 27, 10, 35, 19, 42, 44, 17])
sorted_list = quick.sort()
print(sorted_list)

from Search.Linear import LinearSearch
lin = LinearSearch(sorted_list)
lin.search(42)

from Search.Binary import BinarySearch
bin = BinarySearch(sorted_list)
bin.search(42)

from Search.Interpolation import InterpolationSearch
inter = InterpolationSearch(sorted_list)
inter.search(42)
