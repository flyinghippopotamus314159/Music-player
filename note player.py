"""
Start of sequence= bpm,sum of all values
Rest of sequence=note:0-11,octave:0-3,length(beats);
"""
import re, winsound, math
sequence=input("Please enter note sequence to play:")
sequenceList=re.split(";",sequence)
for i in range(len(sequenceList)):
    sequenceList[i]=re.split(",",sequenceList[i])
bpm=int(sequenceList[0][0])
beatLen=(60/bpm)*1000
for i in range(len(sequenceList)-1):
    notes = [110, 116.541, 123.471, 130.813, 138.591, 146.832, 155.563, 164.814, 174.614, 184.997, 195.998,207.652]  # Hz values A2-Ab3
    pitch=notes[int(sequenceList[i+1][0])]
    octave=float(2^int(sequenceList[i+1][1]))
    pitch=pitch*octave
    noteLen=beatLen*float(sequenceList[i+1][2])
    winsound.Beep(math.floor(pitch),math.floor(noteLen))

