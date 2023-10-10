def vocale(sir1):
    sir1=sir1.lower()
    voc="aeiou"
    count=0
    for letter in sir1:
        if letter in voc:
            count+=1
    print(count)

sir="a iesit soarele din nori"
vocale(sir)
