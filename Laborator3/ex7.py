def op_sets(*sets):
    dictionary={}
    for number1,set1 in enumerate(sets):
        for number2,set2 in enumerate(sets):
            if number1==number2:
                continue
            key=f"{set1}|{set2}"
            dictionary[key]=set1|set2
            key=f"{set1}&{set2}"
            dictionary[key]=set1&set2
            key=f"{set1}-{set2}"
            dictionary[key]=set1-set2
            key=f"{set2}-{set1}"
            dictionary[key]=set2-set1
    return dictionary

set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}

rez = op_sets(set1,set2,set3)
for key, value in rez.items():
    if value == set():
        print(f"{key}: {None}")
    else:
        print(f"{key}: {value}")
    

