from math import *
# coding: utf-8
import sqlite3#bibliothèque de la bdd en local


#######################################################################
#Programme qui sert à un enseignant de rentrer le nombre d'étudiants, noms, prenoms           #
#et leurs notes afin de lister ceux qui ont la moyenne avec mention et ceux qui ne l'ont pas   #
######################################################################

#fonctionnalités
#bdd(), qui sert à se connecter à la BDD SQLITE
#saisir(), qui sert à enregistrer les étudiants et leurs notes
#mention(), qui sert à donner la mention de l'étudiant en fonction de la moyenne
#moyenne(), qui sert à calculer la moyenne de l'étudiatnt en fonction de sa note de test et l'examen
#liste_admis(), qui sert à lister les étudiants qui ont une moyenne >= 10 et qui donne leur mention
#liste_echoues(), qui sert à lister les étudiants qui ont une moyenne< 10
#liste_etudiant(), qui sert à lister tous les étudiants enregistrés
#choisir(), crée pour gérer le menu de navigation


for i in range(2):
        print("")
print("****************************")
print("* Programme de session d'examen *")
print(" ***************************")
print("")
print("")


#connection  la base de donnée 
def  bdd():          
        try:
            conn = sqlite3.connect('bdd.db')
            cursor = conn.cursor()
            cursor.execute("""
        CREATE TABLE etudiants(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            nom TEXT,
            prenom TEXT,
            note_test INTERGER,
            note_exam INTERGER,
            moyenne INTERGER,
            mention TEXT     
        )
        """)
            conn.commit()
        except sqlite3.OperationalError:
            print('Vous pouvez utiliser la bdd')
        except Exception as e:
            print("Erreur")
            conn.rollback()
            # raise e
       
#fin  base de donnée


#la fonction la_moyenne
def  la_moyenne( note_test, note_exam):
        moyenne= (note_test + note_exam) /2
        return moyenne
#fin contion la_moyenne

    
#la fonction mention
def  la_mention( moyenne):
    
        if moyenne<10:
                mention="échoué"
                print(mention)
                return mention
        if moyenne >=10 and  moyenne<=11:
                mention="passable"
                print(mention)
                return mention
        if moyenne >11 and moyenne <=13:
                mention="assez bien"
                print(mention)
                return mention
        if moyenne >=14:
                mention="très bien"
                print(mention)
                return mention

# fin fonction mention


#la fonction liste des admis
def liste_admis():
        print("       *Liste des admis*")
        print("")
        cpt=1
        conn = sqlite3.connect('etudiants.db')
        cursor = conn.cursor()
        cursor.execute("select nom, prenom, moyenne,mention  from etudiants where moyenne >=10 ORDER BY nom DESC")
        rows= cursor.fetchall()
        for row in rows:
             print(cpt,")", row)
             cpt=cpt+1
        cursor.close()
        print("")
        print("1) retour au menu")
        slct=int(input("=>"))
        while slct != 1:
            print("1) retour au menu")
            slct=int(input("=>"))
        if  slct==1:
                choisir()
#fin fonction admis

                
#la fonction échoué
def liste_echoues():
        print("       *Liste des échoués*")
        print("")
        cpt=1
        conn = sqlite3.connect('etudiants.db')
        cursor = conn.cursor()
        cursor.execute("select nom, prenom, moyenne from etudiants where moyenne <10 order by nom DESC")
        rows= cursor.fetchall()
        for row in rows:
             print(cpt,")", row)
             cpt=cpt+1
        cursor.close()
        print("")
        print("1) retour au menu")
        slct=int(input("=>"))
        while slct != 1:
            print("1) retour au menu")
            slct=int(input("=>"))
        if  slct==1:
                choisir()
#fin fonction échoué
                

#la fonction liste des étudiants
def liste_etudiant():
        print("       *Liste des échoués*")
        print("")
        cpt=1
        conn = sqlite3.connect('etudiants.db')
        cursor = conn.cursor()
        cursor.execute("select * from etudiants order by nom DESC")
        rows= cursor.fetchall()
        for row in rows:
             print(cpt,")", row)
             cpt=cpt+1
        cursor.close()
        print("")
        print("1) retour au menu")
        slct=int(input("=>"))
        while slct != 1:
            print("1) retour au menu")
            slct=int(input("=>"))
        if  slct==1:
                choisir()
#fin liste des étudiants

                
#la fontion saisir
def saisir():
        print("       *Enregistrer vos étudiants*")
        print("")
        print("entrer le nombre d'etudiant:")
        nbr_etudiant=int(input("=>"))
        nom=""
        prenom=""
        note_test=0
        note_exam=0
        etudiants=[]
        cpt= nbr_etudiant
        moyenne=0
        mention=""
        conn = sqlite3.connect('etudiants.db')
        cursor = conn.cursor()
        for i in range(nbr_etudiant):
                print("nombre etudiant a enregistrer: ", cpt,"/", nbr_etudiant)
                print("entrer le nom de l'etudiant")
                nom=input("=>")
                print("entrer le prenom de l'etudiant")
                prenom=input("=>")
                print("entrer la note du test de l'etudiant")
                note_test=int(input("=>"))
                if note_test<0:
                    while note_test<0 :
                         print("la note ne repond pas aux normes")
                         print("entrer la note du test de l'etudiant")
                         note_test=int(input("=>"))
                if note_test>20:
                    while note_test>20 :
                        print("la note ne repond pas aux normes")
                        print("entrer la note du test de l'etudiant")
                        note_test=int(input("=> "))
                print("entrer la note de l'exam de l'etudiant")
                note_exam=int(input("=>"))
                if note_exam<0:
                    while note_exam<0 :
                         print("entrer la note de l'exam de l'etudiant")
                         print("la note ne repond pas aux normes")
                         note_exam=int(input("note exam: "))
                if note_exam>20:
                    while note_exam>20 :
                        print("la note ne repond pas aux normes")
                        print("entrer la note de l'exam de l'etudiant")
                        note_test=int(input("=>"))
                moyenne= la_moyenne(note_test, note_exam)
                mention=  la_mention( moyenne)
                etudiants.append(nom)
                etudiants.append(prenom)
                etudiants.append(note_test)
                etudiants.append(note_exam)
                etudiants.append(moyenne)
                etudiants.append(mention)
                cpt=cpt-1
                print(etudiants)
                #ici on fait la sauvegarde de l'étudiant apres avoir donné ses infos un par un
                conn = sqlite3.connect('etudiants.db')
                cursor = conn.cursor()
                cursor.execute("insert into etudiants  values (Null, ?, ?, ?, ?, ?, ?)", etudiants)
                cursor.close()
                conn.commit()
        print("vous avez bien enregistré vos étudiant")
        print("")
        print("1) retour au menu")
        slct=int(input("=>"))
        while slct != 1:
            print("1) retour au menu")
            slct=int(input("=>"))
        if  slct==1:
                choisir()
#fin fonction saisir
        
                                    
#la fonction choisir du menu
def choisir():
        print("            *menu*")
        print("1) enregistrer les etudiant et leurs notes")
        print("2) la liste des admis")
        print("3) la liste des échoués")
        print("4) la liste des etudiants")
        print("")
        slct=int(input("=>"))
        while slct != 1 and slct != 2 and slct != 3 and slct !=4:
            print("veuillez suivre les instructions")
            print("*le menu*")
            print("")
            print("1) Enregistrer vos Etudiants")
            print("2) la liste des admis")
            print("3) la liste des échoués")
            print("4) la liste des etudiants")
            print("")
            slct=int(input("=>"))
        if  slct==1:
                 saisir()
        if  slct==2:
                 liste_admis()
        if  slct==3:
                 liste_echoues()
        if  slct==4:          
                 liste_etudiant()
#fin fonction choisir
    
#la fonction main qui sert à exécuter les fonctions du dessus
if __name__ == '__main__':
        bdd()
        choisir()




    
        
