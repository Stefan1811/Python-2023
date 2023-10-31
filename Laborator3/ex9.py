def count_arg(*args_numbers,**args_valnumbers):
    valnumbers=set(args_valnumbers.values())
    count=0
    for arg in args_numbers:
        if arg in valnumbers:
            count+=1
    return count

print(count_arg(1, 2, 3, 4, x=1, y=2, z=3, w=5))