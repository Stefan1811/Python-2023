def palindrom(number):
    copy_number=number
    palindrom=0
    while copy_number!=0:
        palindrom=palindrom*10+copy_number%10
        copy_number//=10
    if number==palindrom:
        return True
    else:
        return False

def palindrom_tuple(array):
    max_palindrom=0
    counter=0
    for i in array:
        if palindrom(i)==True:
            counter+=1
            if i>max_palindrom:
                max_palindrom=i
    return counter,max_palindrom

array=[1221,323,45654,34,55,78,908]
print(palindrom_tuple(array))
