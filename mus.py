from os import listdir
from os.path import isfile, join
import os
from playsound import playsound

def main():

    cd = str(input("Directory"))
    i = 0
    songs = []
    for file in os.listdir(cd):
        print("{} | {}".format(i,file))
        songs.append("{}\{}".format(cd,file))
        i += 1
    sng = int(input("Song Selection: "))
    playsound(songs[sng].replace("\\","/"))