def no_of_1(number):
    counter=0
    base2=bin(number)[2:]
    base2=int(base2)
    while base2!=0:
        if base2%10==1:
           counter+=1
        base2//=10
    return counter

print(no_of_1(24))
