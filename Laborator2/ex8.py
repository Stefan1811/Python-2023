def ascii_filter(x=1,words=[],flag=True):
    ascii_lists=[]
    for word in words:
        ascii_chars=[]
        for letter in word:
            if flag is True:
                if ord(letter) % x == 0:
                    ascii_chars.append(letter)
            else:
                if ord(letter) % x != 0:
                    ascii_chars.append(letter)
        ascii_lists.append(ascii_chars)
    return ascii_lists

x=2
flag=False
strings = ["test", "hello", "lab002"]
rez=ascii_filter(x,strings,flag)
print(rez)
