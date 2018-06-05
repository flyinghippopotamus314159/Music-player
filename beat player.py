import winsound, time
tune=input("Enter a beat code:")
for i in range (len(tune)):
    sound=str(tune[i])
    winsound.PlaySound(sound, winsound.SND_FILENAME)
