def find_number(sir):
    number=""
    ok=False
    for letter in sir:
        if letter.isdigit():
            number+=letter
            ok=True
        elif ok:
            break
    if number:
        return number
    else:
        return None
        
print(find_number("abbb1122ababab112abba1334"))