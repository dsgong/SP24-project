import librosa
import soundfile as sf
from scipy import signal
import numpy as np

class Daw:
    def __init__(self):
        self.tracklist = [[] for i in range(16)]
        self.menulist = ["load", "filter", "save", "exit"]
        self.filterlist = ["lpf", "hpf"]
        self.sr = 48000


    def menu(self):
        while(True):
            print("Main Menu")
            print("load\tfilter\tsave")
            s = input(">>").lower()
            if(s in self.menulist):
                if s == ("load"):
                    self.load()
                elif(s == 'filter'):
                    self.filter()
                elif(s == 'save'):
                    self.save()
                elif(s == "exit" or s == "exit()"):
                    return
    
        

    def load(self):
        print("Track Number")

        while(True):
            s = input(">>").lower()
            try: 
                s = int(s)
            except:
                print("Invalid Track Number")
                continue

            if (s >= 1 and s <= 16):
                print("File path")
                while True:
                    s1 = input(">>")
                    try:
                        y, sr = librosa.load(s1, sr=self.sr)
                        self.tracklist[s-1] = y
                        return
                    except:
                        print("Invalid File Path")
                        continue
            else:
                print("Invalid Track Number")

    def filter(self):
        print("Track Number")

        while(True):
            s = input(">>").lower()
            try: 
                s = int(s)
            except:
                print("Invalid Track Number")
                continue

            if (s >= 1 and s <= 16):
                print("Filter Type")
                while True:
                    s1 = input(">>")
                    if s1 in self.filterlist:
                        break
                    else:
                        print("Invalid Filter")
                if(s1 == 'lpf'):
                    self.lpf(s-1)
                elif(s1 == 'hpf'):
                    self.hpf(s-1)
                return
            else:
                print("Invalid Track Number")

    def lpf(self, tracknum):
        while True:
            print("Cutoff Frequency")
            s = input(">>")
            try:
                s = float(s)
                b, a = signal.butter(4, s, 'low', fs=self.sr)
                self.tracklist[tracknum] = signal.lfilter(b, a, self.tracklist[tracknum])
                return
            except:
                print("Invalid Cutoff Frequency")

    def hpf(self, tracknum):
        while True:
            print("Cutoff Frequency")
            s = input(">>")
            try:
                s = float(s)
                b, a = signal.butter(4, s, 'high', fs=self.sr)
                self.tracklist[tracknum] = signal.lfilter(b, a, self.tracklist[tracknum])
                return
            except:
                print("Invalid Cutoff Frequency")

    def save(self):
        print("Track Number")

        while(True):
            s = input(">>").lower()
            try: 
                s = int(s)
            except:
                print("Invalid Track Number")
                continue

            if (s >= 1 and s <= 16):
                print("File path")
                while True:
                    s1 = input(">>")
                    try:
                        sf.write(s1, self.tracklist[s-1], self.sr, 'PCM_24')
                        return
                    except:
                        print("Invalid File Path")
                        continue
            else:
                print("Invalid Track Number")