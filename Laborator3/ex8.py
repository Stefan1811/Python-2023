def loop_dictionary(mapping):
    visited=[]
    current_key='start'
    rez=[]
    while current_key in mapping and current_key not in visited:
        visited.append(current_key)
        rez.append(mapping[current_key])
        current_key=mapping[current_key]
    if rez:
        rez.pop()
    return rez


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
rez=loop_dictionary(mapping)
print(rez)