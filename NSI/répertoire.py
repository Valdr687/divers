# Créé par TCASANOV, le 26/11/2021 en Python 3.7
#------------------------------------------------------importation bibliothèques
#-----------CSV : gestion des bases de données
import csv
#-----------RE :  gestion des tests par comparaison avec un pattern
import re


#------------------------------------------------------Définitions et explication des variables

#--------------------Variable de test

pattern = "^[A-Za-z_-èéàÑñÜüäáĩĨïîÎÏöӦ ÊÎÔÛÄËçÏÖÜÀÆæÇÉÈŒœÙ]*$"
pattern_chiffre = "^[0-9999999999]*$"
tab_test=[] #Tout les indices correspondant à un dictionnaire de le répertoire seront rangées dans ce tableau / Utilisée pour tester si l'indice rentré par l'utilisateur est valide
tab_nom=[]  #Tout les indices noms de le répertoire seront rangées dans ce tableau / Utilisée pour tester si le nom rentré par l'utilisateur est valide


#------------------variables globales

répertoire=[]   #Contiendra le répertoire
run= True   #Le programme tourne tant que cette variable est True

#------------------variables utilisées dans les fonctions ( explications )

indice=""   #Correspond à l'indice de le répertoire, défini par l'utilisateur, lors de la suppression et la modification

num=""     #Variable définie par l'utilisateur lors de la modification / permet d'interagir avec le code

indice_menu=""  #Variable définie par l'utilisateur pour le menu / permet d'intéragir avec le code

dic={}      #Contiendra les dictionnaires lors de l'importation
ligne=""    #Représente les lignes du fichier csv lors de l'importation

nombre=""   #Nombre de personne dans le répertoire
num=""      #Correspond à l'indice du dictionnaire encours d'affichage

Nom=""      #Variable définie par l'utilisateur lors de l'ajout et de la modification
Prenom=""   #Variable définie par l'utilisateur lors de l'ajout et de la modification
Tel=""      #Variable définie par l'utilisateur lors de l'ajout et de la modification



#Importation des données
def import_csv(fichier):
    répertoire = csv.DictReader(open(fichier + '.csv','r'))
    return [dict(ligne) for ligne in répertoire]

répertoire=import_csv('répertoire')

#------------Fonction exportation dans un fichier CSV
def export_csv(nom,ordre):
    #ouverture du fichier en écriture 'w'
    with open(nom+'.csv','w') as fichier:
        #prépare l'écriture dans le fichier
        dic= csv.DictWriter(fichier,fieldnames=ordre)
        table= eval(nom)
        #---écriture de la 1ère ligne du fichier CSV : les attributs
        dic.writeheader()
        #---boucle pour chaque dictionnaire
        for ligne in table:
            #écriture de chaque dictionnaire dans une nouvelle ligne du fichier
            dic.writerow(ligne)
#fonction qui permet de trier par ordre alphabétique
def tri(table, attribut, decroit=False):
    def critere(ligne):
        return ligne[attribut]
    return sorted(table, key=critere, reverse=decroit)


#Affichage de le répertoire
def affichage(répertoire) :
    répertoire = tri(répertoire, 'nom')
    print("Affichage de le répertoire :")
    #Test : le répertoire est-il vide ?
    nombre=len(répertoire) #Nombre de personnes dans le répertoire
    #Affichage
    if (nombre==0) :
        print("Votre répertoire est vide")
    else :
        a=0 #Indice
        #singulier
        if nombre==1 :
            print(f"Il y a {nombre} personne dans le répertoire")
        #pluriel
        else :
            print(f"Il y a {nombre} personnes dans le répertoire :")
        #affichage du répertoire
        for element in répertoire  :
            a+=1
            print(f"{a} : {element.get('nom')} {element.get('prenom')} - Tel : {element.get('tel')}")


#Ajouter une personne :
def AddPers(répertoire) :
    print("Ajout d'une personne")
    #Obtention des variables + tests
    #Nom
    test_Nom = False
    while (test_Nom == False) or Nom =="" :
        Nom=input("Nom ? ")
        test_Nom = bool(re.match(pattern, Nom))
    #Prenom
    test_Prenom = False
    while (test_Prenom == False) or Prenom =="" :
        Prenom=input("Prénom ? ")
        test_Prenom = bool(re.match(pattern, Prenom))
    #Numéro de tel
    test_Tel = False
    while (test_Tel == False) or Tel =="" :
        Tel=input("Numéro de téléphone ( sans espaces ) ? ")
        test_Tel = bool(re.match(pattern_chiffre, Tel))

    #Ajout
    répertoire.append({'nom':Nom,'prenom':Prenom,'tel':Tel})
    affichage(répertoire)
    return(répertoire)

#Supprimer un personne :
def SupprPers(répertoire) :
    #le répertoire est il vide ?
    nombre=len(répertoire) #Nombre de personnes dans le répertoire
    #Affichage
    if (nombre==0) :
        print("Votre répertoire est vide")
    else :
        indice="a"    #Correspond à l'indice de le répertoire, défini par l'utilisateur, lors de la suppresion et la modification
        #Obtention de l'indice - Test
        tab_test=[]
        for i in range(len(répertoire)) :
            tab_test.append(str(i+1))  #Les indices seront dans le tableau
        while indice not in tab_test : #Est ce que l'indice correspond bien à une personne ( est'il dans le tableau ) ?
            print("Merci d'enter l'indice de la personne que vous souhaitez supprimer")
            indice=input(f"L'indice doit être compris entre 1 et {len(répertoire)} : ")
        #Suppression
        indice=int(indice)-1
        print(f"{répertoire[indice].get('nom')} {répertoire[indice].get('prenom')} a bien été supprimé du répertoire.")
        del répertoire[indice]
        affichage(répertoire)
    return(répertoire)


#Modifier une personne
def ModPers(répertoire) :
    indice="a" #Correspond à l'indice de le répertoire, défini par l'utilisateur, lors de la suppresion et la modification
    #Obtention de l'indice - Test
    tab_test=[]
    for i in range(len(répertoire)) :
        tab_test.append(str(i+1))  #Les indices seront dans le tableau
    while indice not in tab_test : #Est ce que l'indice correspond bien à une personne ?
        print("Merci d'enter l'indice de la personne dont vous souhaitez modifier les informations")
        indice=input(f"L'indice doit être compris entre 1 et {len(répertoire)} : ")

    #Obtention de l'information à modifier + test
    num="" #Variable définie par l'utilisateur lors de la modification / permet d'intéragir avec le code
    while num not in ["1","2","3"] :
        print("Merci d'entrer quelle information vous souhaitez modifier : le nom(1), le prenom(2) ou le numéro de téléphone(3)")
        num=input("Le numéro doit être 1,2 ou 3 : ")

    #Modification : obtention des données - tests - modification ( update )
    indice = int(indice)-1
    if (num=="1") :
        test_Nom = False
        while (test_Nom == False) or  Nom =="" :
            Nom=input("Nom ? ")
            test_Nom = bool(re.match(pattern, Nom))
        répertoire[indice].update({'nom': Nom})
    elif (num=="2") :
        test_Prenom = False
        while (test_Prenom == False) or Prenom =="" :
            Prenom=input("Prénom ? ")
            test_Prenom = bool(re.match(pattern, Prenom))
        répertoire[indice].update({'prenom': Prenom})
    else :
        test_Tel = False
        while (test_Tel == False) or Tel =="" :
            Tel=input("Numéro de téléphone ( sans espaces ) ? ")
            test_Tel = bool(re.match(pattern_chiffre, Tel))
        répertoire[indice].update({'tel': Tel})
    affichage(répertoire)
    return(répertoire)


def ModPersNom(répertoire) :
    #Obtention du nom + test de la validité des caractères:
    NomDansrépertoire= False #Entrée dans la boucle
    while NomDansrépertoire == False :
        #Tant que le nom n'est pas dans le répertoire on répète la boucle
        Mod_nom=input("Entrez le nom de la personne dont vous souhaitez modifier les informations : ")
        #Test de la validité de l'entrée : les caractères sont ils valables
        test_Mod_nom = bool(re.match(pattern, Mod_nom))
        while (test_Mod_nom == False) or Mod_nom =="" :
            Mod_nom=input("Entrez le nom de la personne dont vous souhaitez modifier les informations : ")
            test_Mod_nom = bool(re.match(pattern, Mod_nom))
        #Test : le nom est-il existant ?
        indice2=0
        while indice2 <=len(tab_nom) :
            if Mod_nom == répertoire[indice2].get('nom') :
                NomDansrépertoire = True
                break #Sortie de boucle dès que le nom est valide
            indice2+=1

        if NomDansrépertoire == False :
            print("Le nom que vous avez tapé n'est pas dans le répertoire, veuillez réessayer.")
    #Obtention de l'information a modifier + test
    num = "a" #Variable définie par l'utilisateur lors de la modification / permet d'intéragir avec le code
    while num not in ["1","2","3"] :
        print("Merci d'entrer quelle information vous souhaitez modifier : le nom(1), le prenom(2) ou le numéro de téléphone(3)")
        num=input("Le numéro doit être 1,2 ou 3 : ")

    #Modification

    if (num=="1") :
        test_Nom = False
        while (test_Nom == False) or Nom =="" :
            Nom=input("Nom ? ")
            test_Nom = bool(re.match(pattern, Nom))
        répertoire[indice2].update({'nom': Nom})
    elif (num=="2") :
        test_Prenom = False
        while (test_Prenom == False) or Prenom =="" :
            Prenom=input("Prénom ? ")
            test_Prenom = bool(re.match(pattern, Prenom))
        répertoire[indice2].update({'Prenom': Prenom})
    else :
        test_Tel = False
        while (test_Tel == False) or Tel =="" :
            Tel=input("Numéro de téléphone ( sans espaces ) ? ")
            test_Tel = bool(re.match(pattern_chiffre, Tel))
        répertoire[indice2].update({'tel': Tel})
    affichage(répertoire)
    return(répertoire)







def Menu():
    #Menu
    #Affiche de la Partie Commande
    print("__________________________________","\n|Commandes                       |")
    print("|1- Ajouter Personne             |")
    print("|2- Modifier Personne            |")
    print("|3- Supprimer une personne       |")
    print("|4- Modifier Personne par son nom|")
    print("|0- Quitter le programme         |")
    print("|________________________________|")
    affichage(répertoire)

def AppelFonction() :
    Menu()
    run=True
    indice_menu=""
    while run==True:
        indice_menu=input("Veuillez choisir l'action que vous voulez faire (0,1,2,3 ou 4) : ") #Variable définie par l'utilisateur pour intéragir avec le menu
        #Test
        while (indice_menu not in ["1","2","3","4","0"]) :
            indice_menu=input("Vous devez choisir une action valide (0,1,2,3 ou 4) : ")
            run=True
        if indice_menu=="0":
            verification = input("Etes vous sûr de vouloir quitter le programme ? ")
            while verification not in ['oui','Oui','OUi','OUI','ouI',"0",'oUI''non','Non','nON','nON','noN']:
                print("Merci d'entrer une valeur valide")
                verification=input("La valeur doit etre oui ou non : ")
            if verification in ['non','Non','Non','nON','nON','noN']:
                indice_menu=input("Quelle action voulez vous vraiment faire ? ")
                run=True
            if verification in ['oui','Oui','OUi','OUI','ouI','oUI','0']:
                export_csv('répertoire',['nom','prenom','tel'])
                run=False
                exit()
        if indice_menu=="1":
            AddPers(répertoire)
        if indice_menu=="2":
            ModPers(répertoire)
        if indice_menu=="3":
            SupprPers(répertoire)
        if indice_menu=="4" :
            ModPersNom(répertoire)








AppelFonction()










