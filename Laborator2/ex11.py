def sort_tuple_list(tuples):
    tuples.sort(key= lambda x:x[1][2])
    return tuples

print(sort_tuple_list([('abc', 'bcd'), ('abc', 'zza')]))