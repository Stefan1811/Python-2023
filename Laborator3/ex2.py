def dictionary(str):
    sting_letter={}
    for letter in str:
        if letter != ' ':
            if letter in sting_letter:
                sting_letter[letter]+=1
            else:
                sting_letter[letter]=1
    return sting_letter

string="Ana has apples"
rez=dictionary(string)
print(rez)
#{'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} 