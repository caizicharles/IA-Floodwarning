from floodsystem.utils import sorted_by_key

a = [(1,300),(2,200),(3,100)]
b = sorted_by_key(a,1,reverse=True)
print(b)