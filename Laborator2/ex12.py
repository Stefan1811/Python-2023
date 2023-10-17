def get_rhyme(words):
    rhyme = {}
    for word in words:
        last_letters = word[-2:]
        if last_letters not in rhyme:
            rhyme[last_letters] = []
        rhyme[last_letters].append(word)
    rez = []
    for keys in rhyme:
        rez.append(rhyme[keys])
    return rez


print(get_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))