print("******************************")
print("*Etude de chaine de caractères*")
print("*******************************")


mot=""
c=""
n=1
n_m=""

while n>=1:
    mot=input("rentrer un mot :")

    for i in range(len(mot)):
        c=c + mot[i] + "#"
    print(c)
    print("")
    n_m=input("voulez vous saisir un nouveau mot? y/n")
    if n_m != "y" and n_m != "n":
        while n_m != "y" and n_m != "n":
            print("veuillez suivre les instructions en choisissant entre Y et N")
            n_m=input("voulez vous saisir un nouveau mot? y/n")
    if n_m == "y":
        n= 1
    if n_m=="n":
        print("aurevoir")
        n=0
    
    
    
    
