def occurence(str1,str2):
    no_occur=0
    poz=0
    while poz<len(str1):
        poz=str1.find(str2,poz)
        if poz==-1:
            break
        no_occur+=1
        poz+=1
    print(no_occur)

str1=input("Introduceti primul sir: ")
str2=input("Introduceti al doilea sir: ")

occurence(str1,str2)