def song_maker(notes,position,start):
    song=[]
    length=len(notes)
    song.append(notes[start])        
    for pos in position:
        start+=pos  
        while start<0:
            start+=length
        while start>length:
            start-=length
        song.append(notes[start])        
    return song

notes=["do", "re", "mi", "fa", "sol"]
position=[1, -3, 4, 2]
start=2
rez=[]
rez=song_maker(notes,position,start)
print(rez)