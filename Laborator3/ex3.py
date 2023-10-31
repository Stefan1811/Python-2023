def dict_comp(dictonary1,dictonary2):
    if not isinstance(dictonary1,dict) or not isinstance(dictonary2,dict):
        return False
    if set(dictonary1.keys())!=set(dictonary2.keys()):
        return False
    for key in dictonary1:
        val1=dictonary1[key]
        val2=dictonary2[key]
        if isinstance(val1,dict) and isinstance(val2,dict):
            if not dict_comp(val1,val2):
                return False
        else:
            if val1!=val2:
                return False
    return True

dictonary1 = {
    'a': 1,
    'b': [2, 3,{'t':2,'i':0}],
    'c': {'x': 4, 'y': 6}
}

dictonary2 = {
    'a': 1,
    'b': [2, 3,{'t':2,'i':8}],
    'c': {'x': 4, 'y': 6}
}

rez=dict_comp(dictonary1,dictonary2)
print(rez)