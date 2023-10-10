def aparitie(sir):
    sir=sir.lower()
    letter_counter={}
    for letter in sir:
      if letter!=' ':
        if letter in letter_counter:
            letter_counter[letter]+=1
        else:
            letter_counter[letter]=1
    common_letter=max(letter_counter,key=letter_counter.get)
    return common_letter

sir="an apple is not a tomato"
print(aparitie(sir))