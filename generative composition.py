"""
bpm;beat increase[beatVal increase-beatTime=m.floor(beatTine)];start note;multiplier(of Hz val);range(8ves)
"""
import  winsound
import math as maths
def init():
    bpm=int(input("Please enter bpm"))
    startBeat=float(input("Please enter a number between 1 and 2"))
    startNote=int(input("Please enter the start note in Hz"))
    multiplier=float(input("Please enter a multiplier between 1 and 2"))
    mMultiplier=float(input("Please enter a second multiplier between 1 and 2"))
    minHz=int(input("Please enter MIN Hz:"))
    maxHz=int(input("Please enter MAZ Hz:"))
    run(bpm,startBeat,startNote,multiplier,mMultiplier,minHz,maxHz)
def makePointFive(number):
    if number<=0.5:
        return(0.5)
    elif number<=1:
        return(1)
    elif number<=1.5:
        return(1.5)
    return(2)
def run(bpm,startBeat,startNote,multiplier,mMultiplier,minHz,maxHz):
    print(startBeat,"    ",startNote)
    bps=bpm/60
    beatVal=makePointFive(1/bps)
    hold=startBeat*beatVal
    hold=hold*1000
    winsound.Beep(maths.floor(hold),maths.floor(startNote))
    nextBeat=startBeat*startBeat
    while nextBeat>2:
        nextBeat=nextBeat-1
        print("AAAAAA",nextBeat)
    nextNote=startNote*multiplier
    while nextNote>maxHz:
        nextNote=nextNote-maxHz
        print("BIG!!!",nextNote)
 ##   else:
   ##     break
    if nextNote<minHz:
        nextNote=nextNote+minHz
    nextMultiplier=multiplier*mMultiplier
    if nextMultiplier>2:
        nextMultiplier=nextMultiplier-1
        print(nextBeat,nextNote)
    run(bpm,nextBeat,nextNote,nextMultiplier,mMultiplier,minHz,maxHz)
init()