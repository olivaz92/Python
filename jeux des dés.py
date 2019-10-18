from random import *
#import pygame#bibliothèque de son
#from pygame.locals import *

#exercice sur le dées
#on lance un dée a 6 faces 10 fois, si la somme des dées est paire le joueur gagne 1points
#si la somme est impaire l'utilisateur perd 2points
#comment modifier l'algo pour que le jeux s'arrete à 5 parties.
#le joueur démarre la partie avec 10points et s'arrete lorsque la cagnotte est null

nbrt=0#
score=0#
smd=0#
play=""# On initialise les valeurs à zéro pour facilement
start=""#les utiliser dans le programme
son= ""#
colere=3#

print("")
print("")
print("          *********************************     ")
print("          *Welcome dans notre jeux des dés*     "                          )
print("          *********************************     ")
print("")
print(" les règles sont simples, on lance un dé a 6 faces 10 fois,")
print(" si la somme des dés est paire le joueur gagne 1points,")
print(" si la somme est impaire le joueur perd 2points")
print(" le jeux débute avec 10 points et s'arrete si le score ")
print(" devient inférieur à o ou lorsque le nombre de tour s'arrete")
print("")


#La condition ici est mise pour vérifier si le joueur respecte les
#conditions y/n
while start !="y" and start!="n" and colere!=0:
    start=input("      Voulez vous commencer votre partie?!y/n: ")
    print("")
    print("")
    if start=="y":#si l'utilisateur répond "y", le nombre de tour et le score s'initialise
           nbrt= nbrt + 5
           score= score + 10
    if start=="n":
        print("aurevoir à la prochaine")
        print("")
    elif start !="y" and start!="n":
        colere= colere -1
        print("il faut suivre les instructions")
        print("")
    if colere==1:
        print("Vous abusez de notre patience")
        print("")
    
if colere<=0:
               print("vous êtes un cas perdu, bye")
while nbrt>0 and score==10:#la première condition "while" est mise pour vérifier si le nombre de tour et le score est >0 pour recommencer le jeux
    while nbrt>0:# cette condition est mise pour commencer le jeux
    
         for i in range(1,10):#La boucle for ici est mise pour lancé le dé 10fois
            smd= smd + randint(1,6)# la somme des dés va s'additionner 
        
         if smd%2==0:
             score=score+1
             print("la somme est paire")
             print("vous avez ganez 1 point, votre score est:",score)
             print("")
         
         elif smd%2==1:
            score=score-2
            print("la somme est impaire")
            print("vous perdez 2 points, votre score est:",score)
        
         nbrt=nbrt-1
        
         print("")
         print("il vous reste",nbrt," partie de jeux")
         print("")
        
    if score>0 :   
          print("")
          print("")
          print("      ***********************************    ")
          print("      Félicitation!!! votre score est:",score)
          print("      ***********************************     ")
          print("")
          print("")
          play=input("vous voulez rejouer?y/n: ")
      
    if score<0:
          print("Pas de chance pour vous, dommage")
          print("")
        
    if play=="y":
        nbrt= nbrt+5
        score= score - score
        score= score+10
    if play=="n":
        print("aurevoir à la prochaine")
        
    if play!="y" and play!="n":
        while play!="y" and play!="n" and colere>0:
            colere= colere -1
            print("Veuillez suivre les instructions")
           
            print("")
            play=input("souhaitez vous tenter votre chance?y/n: ")
            print("")
            if colere<=2 and play!="y" and play!="n":
                print("Vous abusez de notre patience")
                print("")
        if colere<1:
            print("Vous abusez!")
            print("Aurevoir")
