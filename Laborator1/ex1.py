import math

def cmmdc(array):
    if len(array) < 2:
        return "Trebuie introduse doua numere"
    rez=array[0]
    for i in array[1:]:
        rez=math.gcd(rez,i)
    return rez

array=[]
while True:
    try:
        number=int(input("Introduceti un numar pentru a calcula cmmdc"))
        if number==0:
            break
        array.append(number)
    except ValueError:
        print("Input ul nu este valid")

rez=cmmdc(array)
print(rez)