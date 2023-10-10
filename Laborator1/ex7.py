def find_number(sir):
    number=0
    for letter in sir:
        if letter.isdigit():
            number+=int(letter)
            number*=10
    number//=10
    return number
        
print(find_number("abc123abc"))