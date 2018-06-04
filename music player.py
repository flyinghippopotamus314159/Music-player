import winsound, time
tune=input("Enter a beat code:")
##step_size=int(input("Enter step size:"))
##bpm=int(input("Enter bpm:"))
##bps=bpm/60
##sps=bps/step_size
for i in range (len(tune)):
    sound=str(tune[i])
    winsound.PlaySound(sound, winsound.SND_FILENAME)
##    time.sleep(sps)
