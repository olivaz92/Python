from math import *
print("")
print("")
print("***********************************")
print("*********CONVERTISSEUR*************")
print("*BINAIRE DECIMAL ; Décimal binaire*")
print("***********************************")
print("")
print("")
def binaire():
    print("veuillez rentrer votre binaire à convertir en décimal") 
    b= int(input("=>"))
    cb= str(b)#on convertit l'entier en chaine caractère
    lcb= len(cb)#on récupère la longueur de la chaine carcatère
    rd=0#La variable mise pour le resultat en décimal
    for i in range(lcb):
        rd= int(cb[i]) *2**(lcb-1-i)+ rd
    print("La forme décimale de ",b," est :",rd)
    print("")
    print("1) retour au menu          2) Recommencer")
    slct=int(input("=>"))
    while slct != 1 and slct != 2:
            print("1) retour au menu")
            slct=int(input("=>"))
    if  slct==1:
                choisir()
    if  slct==2:
                binaire()
    

def decimal():
    print("veuillez rentrer votre décimal à convertir en binaire") 
    d= int("=>")
    rd=""
    while d/2!=0:
        rb= str(d%2) + rb
        d=str(d//2)
    rb= d + rb
    print("")
    print("La forme binaire de ",d," est :",rb)
    print("")
    print("1) retour au menu        2) Recommencer")
    slct=int(input("=>"))
    while slct != 1 and slct != 2:
            print("1) retour au menu")
            slct=int(input("=>"))
    if  slct==1:
                choisir()
    if  slct==2:
                decimal()
    
    
#la fonction choisir du menu
def choisir():
        print("       *Menu*")
        print("1) Binaire décimal")
        print("2) Décimal Binaire")
        slct=int(input("=>"))
        while slct != 1 and slct != 2:
            print("veuillez suivre les instructions")
            print("*le menu*")
            print("")
            print("1) Binaire décimal")
            print("2) Décimal Binaire")
            slct=int(input("=>"))
        if  slct==1:
                 binaire()
        if  slct==2:
                 decimal()
        
#fin fonction choisir
    
#la fonction main qui sert à exécuter les fonctions du dessus
if __name__ == '__main__':
        choisir()
