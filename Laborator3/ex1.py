def setopp(a,b):
    a=set(a)
    b=set(b)
    inter=a.intersection(b)
    union=a.union(b)
    diff_a=a.difference(b)
    diff_b=b.difference(a)
    return inter,union,diff_a,diff_b

a=[3,5,6,7]
b=[3,6,9,8,10]
rez=setopp(a,b)
print(rez)