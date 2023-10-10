def no_spaces_string(sir):
    new_sir=sir.split(" ")
    counter=0
    for word in new_sir:
        if word!='':
            counter+=1
    return counter

sir="Ma numesc Vatamanu Petru"
print(no_spaces_string(sir))
