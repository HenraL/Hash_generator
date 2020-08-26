"Random Hash generator"
from random import *
import os
import datetime
import platform
f=open("hash.txt","a")
date=datetime.datetime.now()
DATE="{}/{}/{}".format(date.day,date.month,date.year)
TIME="{}:{}:{}".format(date.hour,date.minute,date.second)
a="============ Data Collection of the: {}/{}/{} ============\nPath:{}\nTIME:\nos: {}\nCreeated By Henry Letellier\n============ End of data Collection ============\n============ hash created ============".format(DATE,os.getcwd(),TIME,platform.system()))
def pause():
    pause=input("Press enter to continue...")
Hash=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Message=["OK","Failed","Rebooted","404","Renamed","Deleted","Exported","Extracted","Blocked","Acces Denied"]
message=input("Please enter a number between 0 and {} (enter list for the list of options, enter r for a random option):".format(len(Message)))
Lendott=input("Maximum length for the hash line (from 5 onwards, default number 10):")
how=input("How many Hash files do you whant to generate? (enter 1 or higher, enter inf to endlessly generate files)")
separate=input("Do you whant to create a file for each hash? [(y)es/(n)o]")
if separate=="y" or separate=="Y":
    separate="seperate"
    hashline=input("Do you whant to write the hash line in its own file? [(y)es/(n)o]")
    if hashline=="y" or hashline=="Y":
        haashline="yes"
    else:
        haashline="no"
else:
    separate="not"

try:
    how=int(how)
    J=0
    Increase="yes"
except:
    how=5
    J=0
    Increase="no"

dot=30+Lendott
M=str(message)
if M.isnumeric==True:
    message=int(message)
elif message=="list" or message=="List" or message=="lIst" or message=="liSt" or message=="lisT" or message=="LIst" or message=="LiSt" or message=="LisT":
    for I in range(len(Message)):
        print("For message={} --> {}   For message={} --> {}   For message={} --> {}   For message={} -->{}".format(I,Message[I],I+1,Message[I+1],I+2,Message[I+2],I+3,Message[I+3]))
        I+=3
elif message=="r" or message=="R":
    message="random"
else:
    print ("Please enter either a didgit or a lowercase word or a lowercase r\n You have entered: {}".format(message))
    pause()
    continue

def rand_hash(Lendott,Alphabet,Hash):
    haSh=""
    for i in range(Lendott):
        haSh+="{}".format(Message[random.randint(0,len(Hash))])
    return haSh

def mezzage(Message,message):
    if message=="random":
        message=random.randint(0,len(Message))
    else:
        message=message
    return message

def dott(dot,haSh):
    dot-=len(haSh)
    for i in range(dot):
        Dott+="."
    return Dott


while J!=how:
    Zhash=rand_hash(Lendott,Alphabet,Hash)
    P="{}{}[{}]".format(Zhash,dott(dot,haSh),mezzage(Message,message))
    f=open("hash.txt","a")
    f.write(P)
    f.close()
    print(P)
    if seperate=="seperate":
        g=open("{}.txt","a")
        if haashline=="yes":
            g.write(P)
        else:
            haashline="no"
        g.write("Created by Henry Letellier")
    else:
        g.close()

    else:beta=0
    if increase=="yes":
        J+=1
    else:
        J=0