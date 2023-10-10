import re
def cc_to_lc(sir):
    rezultat=[]
    for letter in sir:
        if letter.isupper():
            rezultat+="_"
        rezultat+=letter.lower()
    if(rezultat[0]=='_'):
        rezultat=rezultat[1:]
    return ''.join(rezultat)


sir = input("Introduceti fraza: ")
print(cc_to_lc(sir))
