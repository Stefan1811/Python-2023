def order_tuples(*lists):
    max_length_list=0
    rez=[]
    for list in lists:
        if len(list)>max_length_list:
            max_length_list=len(list)
    for i in range(max_length_list):
        tuple=()
        for list in lists:
            if i<len(list):
                tuple+=(list[i],)
            else:
                tuple+=(None,)
        rez.append(tuple)
    return rez


rez=order_tuples([1,2,3], [5,6,7], ["a", "b", "c","d"] )
print(rez)