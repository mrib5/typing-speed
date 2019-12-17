from random import randint
import time
import re

f = open('english2.txt')
lines = f.readlines()
wordsToType = 50
randomNumbers = []
listOfWordsToType = []

def speedTestSetup():
    for j in range(wordsToType):
        number = randint(0,65198)
        randomNumbers.append(number)
    for i in randomNumbers:
        listOfWordsToType.append(lines[i][:-1])
    #print(' '.join(listOfWordsToType))
def typingSpeedTest():
    print("[*] Words required to be re-written are displayed below:\n")
    print(' '.join(listOfWordsToType))
    print("\n")
    ready = input("[*] When you are ready to start please press Enter.")
    start = time.time()
    userWords = input("[*] Type in the words you see above:\n")
    end = time.time()
    wordsInputted = re.split(r'[^0-9A-Za-z]+',userWords)
    timeTakenS = (end-start)
    timeTakenM = timeTakenS/60
    wordsPerMinute = len(wordsInputted)/timeTakenM
    print("[*] That is roughly "+str(wordsPerMinute)+" words per minute")
speedTestSetup()
typingSpeedTest()
