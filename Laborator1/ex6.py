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

a=int(input("Introduceti numarul: "))
print(palindrom(a))