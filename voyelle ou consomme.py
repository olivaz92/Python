


v="aeiouy"#liste des voyelles
cpt=0# compteur pour savoir si la lettre saisie correspond à la liste des voyelles
n=""
p=1

while p==1:
    l= input("veuillez saisirune lettre : ")
    for i in range(len(v)):
        if l != v[i]:
            cpt= cpt 
        if l == v[i]:
            cpt= cpt + 1
            
    if cpt != 1:
        print("consonne", l.upper())
        
    if cpt == 1:
        print("voyelle", l.upper())
        
    print("voulez vous vérifier une autre lettre?! y/n")
    n= input("")
    while n!= "y" and n!= "n" and n!="":
        print("veuillez suivre les instructions une lettre entre y et n")
        print("voulez vous vérifier une autre lettre?! y/n")
        n= input("")
        
    if n=="y":
        p= 1
    if n=="n":
        p= p - 1
    

        
