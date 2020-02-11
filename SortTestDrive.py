from Sort.Bubble import Bubble
bubble = Bubble([12, 32768, 436, 457, 3, 564, 1, 2])
sorted_list = bubble.sort()
print(sorted_list)

bubble.mount([9, 8, 7, 6, 5, 4, 3, 2, 1])
sorted_list = bubble.sort()
print(sorted_list)


from Sort.Insertion import Insertion
insertion = Insertion([9,8,7,6,5])
sorted_list = insertion.sort()
print(sorted_list)

insertion.mount([14, 33, 27, 10, 35, 19, 42, 44])
sorted_list = insertion.sort()
print(sorted_list)


from Sort.Selection import Selection
selection = Selection([9, 8, 7, 6, 5])
sorted_list = selection.sort()
print(sorted_list)


selection.mount([14, 33, 27, 10, 35, 19, 42, 44])
sorted_list = selection.sort()
print(sorted_list)


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
