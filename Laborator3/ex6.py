def idem_tuple(list):
    elemnt_dictionary={}
    for el in list:
            if el in elemnt_dictionary:
                elemnt_dictionary[el]+=1
            else:
                elemnt_dictionary[el]=1
    duplicate=set()

    unique=set()
    for key in elemnt_dictionary:
        if elemnt_dictionary[key]!=1:
            duplicate.add(key)
        else:
            unique.add(key)
    return len(unique),len(duplicate)

list = [1,2,2,2,3,4,4,5,6,7,7,8,9,9]
print(idem_tuple(list))