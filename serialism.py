import winsound, random
import math as maths
ignorevar=input("Press enter to begin serialist generator")
notes=[110,116.541,123.471,130.813,138.591,146.832,155.563,164.814,174.614,184.997,195.998,207.652]       #Hz values A2-Ab3
while True:
    random.shuffle(notes)
    for i in range(12):
        noteLen=0
        while noteLen<0.1:
            noteLen=random.random()
        winsound.Beep((maths.floor((float(notes[i]))*random.randint(1,5))),maths.floor(100*(1/noteLen))) #disallow val<0.01 for this r.r() statement


