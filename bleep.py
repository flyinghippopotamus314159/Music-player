import winsound
tune=input("Enter tune code:")
x=0
while x<len(tune):
    note=int(str(tune[x])+str(tune[x+1])+str(tune[x+2]))
    if note<37:
        note=37
    winsound.Beep(note, 250)
    x=x+3
