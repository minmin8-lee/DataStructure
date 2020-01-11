from Array.Array import Array

a = Array([1,2,3,4,5])

a.traverse()

a.insertion(new_data=["A quick brown fox jumps over the lazy dog"])
a.insertion([1024,2048,4096],idx=2)
a.insertion(new_data=9999,idx=a.search(3))
a.traverse()

a.deletion()
a.deletion(1)

a.update(data=["1048576"], idx=1)
a.traverse()
