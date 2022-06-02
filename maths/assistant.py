# Cree par Thomas C           
from math import *
def menu() :
  print(" ____________________________ ")
  print("|1-Polynome de 2nd degres    |")
  print("|2-Division euclidienne      |")
  print("|3-Conversion deg / rad      |")
  print("|4-Geometrie analytique      |")
  print("|5-Changement de point de vue|")
  print("|0-Quitter le programme      |")
  print("|____________________________|")

menu()  
run=1
while run== 1:
    entree=input("Menu : ")
    while entree not in ["1","2","3","4","5","0"] :
        entree=input("Menu : ")
    if entree =="1" :
        print("Module de calcul des polynomes de second degre : Entree des valeurs ")
        #Entree des valeurs
        a=float(input("a = "))
        b=float(input("b = "))
        c=float(input("c = "))

        #Calcul de Alpha, Delta et Beta :
        alpha=-b/(2*a)
        delta=b**2-4*a*c
        beta=-delta/(4*a)

        #Affichage
        a=str(a)
        alpha=str(alpha)
        beta=str(beta)
        print(" ____________________________ ")
        print("|        Resultats :         |")
        print("f(x) =",a+"(x -"+alpha+")2+"+beta)  
        print("Alpha = ",alpha)
        print("Beta  = ",beta)
        print("Delta = ",delta)
        a=float(a)
        alpha=float(alpha)
        beta=float(beta)
        #Forme canonique  
        if delta <0 :
          print("Pas de solution")

        elif delta >0 :
          s1=(-b-sqrt(delta)/2*a)
          s2=(-b+sqrt(delta)/2*a)
          print("Il y a deux solutions :")
          print("s1 =",s1)
          print("s2 =",s2)

        elif (delta==0) :
          print("La solution est ",alpha)

        else :
          print("Erreur : code clem")
        #Tableau de signe
        print("|     Tableau de signe :     |") 
        if delta <0 :
          print("|x    |-inf              +inf|")
          if a<0 : 
            print("|f(x) |          -           |")
          else :
            print("|f(x) |          +           |")
            

        elif delta==0 :
          print("|x    |-inf     0        +inf|")
          if a<0 : 
            print("|f(x) |     -   |     -      |")
          else :
            print("|f(x) |     +   |     +      |")
        
        else :
          print("|x    |-i    s1      s2    +i|")
          if a<0 : 
            print("|f(x) |  -   0   +    0   -  |")
          else :
            print("|f(x) |  +   0   -    0   +  |")
        print("|____________________________|")  
    elif entree == "2" :
        print(" ____________________________ ")
        print("|  Division euclidienne :    |")
        x=int(input("Nombre a diviser : "))
        a=int(input("Diviseur : "))
        print("Quotien",x//a,"; Reste",x%a)
        print("|____________________________|") 
    elif entree == "3" :
        print("Deg vers rad / rad vers deg")
        print("Choix 1 / 2 : ")
        x="N"
        while x not in ["1","2"] :
            x=input("1, 2 : ")
        if x =="1" :
            a=int(input("Valeur en degres : "))
            if a==180 :
              print("pi rad")
            elif a==360 :
              print("2 pi rad")
            elif a==90 :
              print("pi/2 rad")
            elif a==45 :
              print("pi/4 rad")
            elif a==30 :
              print("pi/6 rad")
            else :
              print((pi/180)*a,"rad")
        else :
            a=input("Valeur en radians : ")
            if a=="2pi" :
              print("360 deg")
            elif a=="pi" :
              print("180 deg")
            elif a=="pi/2" :
              print("90 deg")
            elif a=="pi/4" :
              print("45 deg")
            elif a=="pi/6" :
              print("30 deg")
            else :
              a=int(a)
              print((180/pi)*a,"deg")
    elif entree=="4" :
        print(" ____________________________ ")
        print("|Test de colinearite         |")
        print("|et d'orthogonalite          |")
        print("|des vecteurs u et v         |")
        x=int(input("u : x = ? "))
        y=int(input("u : y = ? "))
        xx=int(input("v : x = ? "))
        yy=int(input("v : y = ? "))
        print("det(u;v)=",x*yy-xx*y)
        if x*yy-xx*y==0 :
          print("|u et v sont colineaires     |")
        else :
          print("|u et v non pas colineaires  |")
        scalaire=x*xx+y*yy
        print("u.v=",x*xx+y*yy)
        if x*xx+y*yy==0 :
          print("|u et v sont orthogonaux.    |")
        else :
          print("|u et v non orthogonaux.     |")
        print("|____________________________|")
    elif entree=="5" :
        x="N"
        print(" ____________________________ ")
        print("|1-Vect directeur vers pente |")
        print("|2-Pente vers vect directeur |")
        print("|3-Vect dir vers vect normal |")
        print("|4-Vect normal vers vect dic |")
        print("|5-Equation donnee /vect norm|")
        print("|6-Quitter                   |")
        print("|____________________________|")
        while x not in ["1","2","3","4","5","6"] :
          x=input("Choix : ")
        if x=="1" :
          print("Soit le vecteur v(x;y) :")
          xv=int(input("x = "))
          yv=int(input("y = "))
          print("c = ",xv/yv)
        elif x=="2" :
          pente=int(input("Valeur de la pente : "))
          print("Un vecteur est v(",pente,";1)")
        elif x=="3" :
          print("Soit le vecteur v(x;y) :")
          xv=int(input("x = "))
          yv=int(input("y = "))
          print("Le vecteur normal est n(",-1*yv,";",xv,")")
          print("ou n'(",yv,";",-1*xv,")")
        elif x=="4" :
          print("Soit le vecteur normal n(x;y) :")
          xn=int(input("x = "))
          yn=int(input("y = "))
          print("Soit v(",-1*yn,";",xn,")")
          print("ou v'(",yn,";",-1*xn,")")
        elif x=="5" :
          print("Soit le vecteur normal n(x;y) :")
          xn=int(input("x = "))
          yn=int(input("y = "))
          print("Soit le point R sur la droite :")
          xr=int(input("x = "))
          yr=int(input("y = "))
          print(xn,"x + ",yn,"y"," = ",xr*xn," + ",yn*yr)
        elif x=="6" :
            break
        else :
          print("Erreur : code mel")
    else :
        print("Vous quittez l'assistant realise par Thomas Casanova")
        run=0


