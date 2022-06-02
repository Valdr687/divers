#--importation bibliothèque csv
import csv
import re
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


#-----------------------------------------------------------------

#Variable de test

pattern = "^[A-Za-z_-èéàÑñÜüäáĩĨïîÎÏöӦ ÊÎÔÛÄËçÏÖÜÀÆæÇÉÈŒœÙ]*$"
pattern_chiffre = "^[0-9999999999]*$"
#-------------------------Tkinter---------------------------------

#Informations
infos = []

#Ajouter les informations dans la liste
def Ajt():
    global infos
    infos.append([Nom.get(),Prénom.get(),Numéro.get()])
    maj()

#Supprimer les informations dans la liste
def Suppr():
    del infos[int(listeagenda.curselection()[0])]
    maj()

# Maj de la liste
def maj():
    listeagenda.delete(0,END)
    for n in infos:
        listeagenda.insert(END,n)

#Définition des Commandes

#Création de l'interface
root = tk.Tk()
frame = Frame()
frame.pack(pady=10)

Nom = StringVar()
Prénom = StringVar()
Numéro = StringVar()

root.title("Agenda Python")
root.geometry("800x500")
#Input utilisateur pour le Contact
tk.Label(root,text="Nom",width=20).place(x=350,y=50)
tk.Label(root,text="Prénom",width=20).place(x=350,y=100)
tk.Label(root,text="Téléphone",width=20).place(x=350,y=150)
e1=tk.Entry(root,width=30,textvariable = Nom)
e2=tk.Entry(root,width=30,textvariable = Prénom)
e3=tk.Entry(root,width=30,textvariable = Numéro)
e1.place(x=500,y=50)
e2.place(x=500,y=100)
e3.place(x=500,y=150)

#Définition de La liste
listeagenda = Listbox(root,height=25,width=50)
listeagenda.place(x=50,y=25)
#Ajout d'une scrollbar à la liste
scrollbar = Scrollbar(root)
scrollbar.pack(fill=BOTH,side=LEFT)
listeagenda.config(yscrollcommand = scrollbar.set) #
scrollbar.config(command = listeagenda.yview) #
#Style des Boutons [Ajouter/Modifier/Supprimer]:

style = Style()
style.configure('W.TButton', font =
			('calibri', 10, 'bold'),
				foreground = 'black')

#Style du bouton "Quit:

style1 = Style()
style1.configure('TButton',font =
            ('Impact',12),
                foreground = 'red')

#Ensemble des boutons

ButtonQuit=Button(root, text="Quitter",style = 'TButton',command=quit)
ButtonQuit.place(x=147, y=470)

Ajouter=Button(root, text="Ajouter",style = 'W.TButton',command=Ajt)
Ajouter.place(x=50, y=429)

Modifier=Button(root, text="Modifier",style = 'W.TButton')
Modifier.place(x=160, y=429)

Supprimer=Button(root, text="Supprimer",style = 'W.TButton',command=Suppr)
Supprimer.place(x=268, y=429)

#Tests


root.mainloop()



#Définitions des fonctions :

#Imporation des données
def import_csv(fichier):
    agenda = csv.DictReader(open(fichier + '.csv','r'))
    return [dict(ligne) for ligne in agenda]

agenda=import_csv('agenda')

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


#Affichage de l'agenda
def affichage(répertoire) :
    #Test : l’agenda est-il vide ?
    print("Affichage de l'agenda :")
    nombre=0
    for element in répertoire  :
        nombre+=1
    #Affichage
    if (nombre==0) :
        print("Votre agenda est vide")
    else :
        a=0
        #singulier
        if nombre==0 :
            print(f"Il y a {nombre} personne dans l'agenda")
        #pluriel
        else :
            print(f"Il y a {nombre} personnes dans l'agenda :")
            Table=""
            critere=""
            decroit=False
            attribut=""
            def tri(Table, attribut, decroit=False):
                def critere(ligne):
                    return ligne[attribut]
                return sorted(Table, key=critere, reverse=decroit)
            tri(Table,attribut)
            agenda_affichage = tri(répertoire, 'nom')
            a=0
            for element in agenda_affichage  :
                a+=1
                print(f"{a} : {element.get('nom')} {element.get('prenom')} - Tel : {element.get('tel')}")




#Ajouter une personne :
def AddPers() :
    print("Ajout d'une personne")
    #Obtention des variables + tests
    #Nom
    Nom=""
    test_Nom = bool(re.match(pattern, Nom))
    while (test_Nom == False) or Nom =="" :
        Nom=input("Nom ? ")
        test_Nom = bool(re.match(pattern, Nom))
    #Prenom
    Prenom=""
    test_Prenom = bool(re.match(pattern, Prenom))
    while (test_Prenom == False) or Prenom =="" :
        Prenom=input("Prénom ? ")
        test_Prenom = bool(re.match(pattern, Prenom))
    #Numéro de tel
    Tel=""
    test_Tel = bool(re.match(pattern_chiffre, Tel))
    while (test_Tel == False) or Tel =="" :
        Tel=input("Numéro de téléphone ? ")
        test_Tel = bool(re.match(pattern_chiffre, Tel))

    #Ajout
    agenda.append({'nom':Nom,'prenom':Prenom,'tel':Tel})
    affichage()

#Supprimer une personne :
def SupprPers() :
    indice="a"
    #Obtention de l'indice - Test
    tab_test=[]
    for i in range(len(agenda)) :
        tab_test.append(str(i+1))  #Les indices seront dans le tableau
    while indice not in tab_test : #Est ce que l'indice correspond bien à une personne ?
        print("Merci d'enter l'indice de la personne que vous souhaitez supprimer")
        indice=input(f"L'indice doit être compris entre o et {len(agenda)} : ")
    #Suppression
    indice=int(indice)-1
    del agenda[indice]
    affichage()

#Modifier une personne
def ModPers() :
    indice="a"
    #Obtention de l'indice - Test
    tab_test=[]
    for i in range(len(agenda)) :
        tab_test.append(str(i+1))  #Les indices seront dans le tableau
    while indice not in tab_test : #Est ce que l'indice correspond bien à une personne ?
        print("Merci d'enter l'indice de la personne dont vous souhaitez modifier les informations")
        indice=input(f"L'indice doit être compris entre o et {len(agenda)} : ")

    #Obtention de l'information
        #Test
    num=""
    while num not in [1,2,3] :
        print("Merci d'entrer quelle information vous souhaitez modifier : le nom(1), le prenom(2) ou le numéro de téléphone(3)")
        num=int(input("Le numéro doit être 1,2 ou 3 : "))

    #Modification
    indice=int(indice)-1
    if (num==1) :
        Nom=""
        test_Nom = bool(re.match(pattern, Nom))
        while (test_Nom == False) or Nom =="" :
            Nom=input("Nom ? ")
            test_Nom = bool(re.match(pattern, Nom))
        agenda[indice].update({'nom': Nom})
    elif (num==2) :
        Prenom=""
        test_Prenom = bool(re.match(pattern, Prenom))
        while (test_Prenom == False) or Prenom =="" :
            Prenom=input("Prénom ? ")
            test_Prenom = bool(re.match(pattern, Prenom))
        agenda[indice].update({'Prenom': Prenom})
    else :
        Tel=""
        test_Tel = bool(re.match(pattern_chiffre, Tel))
        while (test_Tel == False) or Tel =="" :
            Tel=input("Numéro de téléphone ? ")
            test_Tel = bool(re.match(pattern_chiffre, Tel))
        agenda[indice].update({'tel': Tel})
    affichage()



def Menu():
    #Menu
    #Affiche de la Partie Commande
    print("_______________________________","\n|Commandes:                   |")
    print("|1- Ajouter Personne          |")
    print("|2- Modifier Personne         |")
    print("|3- Supprimer une personne    |")
    print("|0- Quitter le programme      |")
    print("|_____________________________|")



run= True
indice1=""
Menu()
affichage()
while run== True:
    indice1=input("Veulliez choisir l'action que vous voulez faire :")
    if indice1 in ['quitter','Quitter','QUITTER',"0"] :
        verification = input("Etes vous sûr de vouloir quitter le programme?")
        while verification not in ['oui','Oui','OUi','OUI','ouI','oUI''non','Non','nON','nON','noN']:
            print("Merci d'entrer une valeur valide")
            verification=input("La valeur doit etre égale a oui ou non")
        if verification in ['non','Non','Non','nON','nON','noN']:
            run=True
        if verification in ['oui','Oui','OUi','OUI','ouI','oUI']:
            export_csv('agenda',['nom','prenom','tel'])
            print("exit")
            exit()
    if indice1 in ['ajouter','Ajouter','AJOUTER',"1"]:
        AddPers()
        export_csv('agenda',['nom','prenom','tel'])
    if indice1 in ['modifier','Modifier','MODIFIER',"2"]:
        ModPers()
        export_csv('agenda',['nom','prenom','tel'])
    if indice1 in ['supprimer','Supprimer','SUPPRIMER',"3"]:
        SupprPers()
        export_csv('agenda',['nom','prenom','tel'])
    else:
        indice1=input("Veuillez rentrer un valeur correcte s'il vous plait")
affichage()







