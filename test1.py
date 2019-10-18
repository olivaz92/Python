from random import *

sd=0
np=5
sc=10

if np<5 and sc>10:
    
    while sc>=1:
        
        for i in range(0,10):
            sd = sd + randint(1,6)

            if sd%2==0:
                sc= sc + 1
                print("vous avez gané 1 points")
            else:
                sc = sc -2
                print("vous perdez 2 points")
        np= np-1
        if sc==0:
            print("vous avez perdu et votre score est:",sc)
        
    print("vous avez gagnez et votre est:",sc)
