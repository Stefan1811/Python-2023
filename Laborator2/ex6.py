def list_appearence(x, *lists):
    frequency = {}
    rez = []
    for list in lists:
        for element in list:
            if isinstance(element, int):
                if element not in frequency:
                    frequency[element] = 1
                else:
                    frequency[element] = frequency[element] + 1

    for key,value in frequency.items():
        value = frequency[key]
        if value == x:
            rez.append(key)
    return rez


print(list_appearence(2, [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))