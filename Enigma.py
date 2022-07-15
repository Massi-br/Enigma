from tkinter import *
import random
from tkinter import ttk
from turtle import color

Réflecteur = [+25,+23,+21,19,17,15,13,11,9,7,5,3,1,-1,-3,-5,-7,-9,-11,-13,-15,-17,-19,-21,-23,-25 ]
Rotor1Up=[ [17,4,19,21,7,11,3,-5,7,9,-10,9,17,6,-6,-2,-4,-7,-12,-5,3,4,-21,-16,-2,-21 ] , 
[10,21,5,-17,21,-4,12,16,6,-3,7,-7,4,2,5,-7,-11,-17,-9,-6,-9,-19,2,-3,-21,-4] ] 
Rotor2Up= [ [25,7,17,-3,13,19,12,3,-1,11,5,-5,-7,10,-2,1,-2,4,-17,-8,-16,-18,-9,-1,-22,-16],
 [3,17,22,18,16,7,5,1,-7,+16,-3,8,2,9,2,-5,-1,-13,-12,-17,-11,-4,1,-10,-19,-25 ] ]
Rotor3Up = [ [12,-1,+23,+10,2,14,5,-5,9,-2,-13,+10,-2,-8,10,-6,6,-16,2,-1,-17,-5,-14,-9,-20,10],
 [1,16,5,17,20,8,-2,+2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23] ]

i=0
c=0
z=0
Bool=FALSE
def click1():
    global i,z,c,Bool
    configureAlpha()
    configureRéf()
    Rotor_entrer=clicked_Rotor.get()
    coté_choisi=clicked_cote.get()
    Rotor_entrer1=clicked_Rotor1.get()
    coté_choisi1=clicked_cote1.get()
    Rotor_entrer2=clicked_Rotor2.get()
    coté_choisi2=clicked_cote2.get()
    
    
    if (c<=26) and (Bool==TRUE): 
        if Rotor_entrer=='R1':
           if coté_choisi=='D':
               decalage_un_rangDR1(z)
               configureR2()
               configureR3()

           else :
            decalage_un_rangGR1(z)
            configureR2()
            configureR3()
        elif Rotor_entrer=='R2':
               if coté_choisi=='D':
                  decalage_un_rangDR2(z)
                  configureR1()
                  configureR3()
               else :
                 decalage_un_rangGR2(z)
                 configureR1()
                 configureR3()
        elif Rotor_entrer=='R3':
               if coté_choisi=='D':
                 decalage_un_rangDR3(z)
                 configureR1()
                 configureR2() 
               else :
                 decalage_un_rangGR3(z)
                 configureR1()
                 configureR2()
        z=1
        c=+1
        i+=1   

    elif (c>26) and (c<=52) and (Bool==TRUE):  
        if Rotor_entrer1=='R1':
           if coté_choisi1=='D':
               decalage_un_rangDR1(z)
               configureR2()
               configureR3()
           else :
            decalage_un_rangGR1(z)
            configureR2()
            configureR3()
        elif Rotor_entrer1=='R2':
               if coté_choisi1=='D':
                  decalage_un_rangDR2(z)
                  configureR1()
                  configureR3()
               else :
                 decalage_un_rangGR2(z)
                 configureR1()
                 configureR3()
        elif Rotor_entrer1=='R3':
               if coté_choisi1=='D':
                 decalage_un_rangDR3(z)
                 configureR1()
                 configureR2()
               else :
                 decalage_un_rangGR3(z)
                 configureR1()
                 configureR2()
        z=1
        c=+1
        i+=1 

    elif (c>52) and (c<=78) and (Bool==TRUE) :
        if Rotor_entrer2=='R1':
           if coté_choisi2=='D':
               decalage_un_rangDR1(z)
           else :
            decalage_un_rangGR1(z)
        elif Rotor_entrer2=='R2':
               if coté_choisi2=='D':
                  decalage_un_rangDR2(z)
               else :
                 decalage_un_rangGR2(z)
        elif Rotor_entrer2=='R3':
               if coté_choisi2=='D':
                 decalage_un_rangDR3(z)
               else :
                 decalage_un_rangGR3(z)
        z=1
        c=+1
        i+=1          
    if(c==78): 
           c=0
           
     
    Bool=FALSE 
    
 
      

def click():
  
  global i,z
  a=True
  while a==True :
    encrypter()
    z=1
    a=False

def clickD():
  global i,z
  a=True
  while a==True :
    dycrypter()
    z=1
    a=False
     
global valeur

 #------------------Fonctions de Décalage d'un rang ------------------------------------------#
def decalage_un_rangGR1(z):
    global Rotor1
    for j in range(0,z):
        for k in range (len(Rotor1)):
            save=Rotor1[k][0]
            for i in range(0,len(Rotor1[k])-1):
                Rotor1[k][i]=Rotor1[k][i+1]
            Rotor1[k][len(Rotor1[k])-1]=save
    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame12,  text=Rotor1[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)

def decalage_un_rangGR2(z):
    global Rotor2
    for j in range(0,z):
        for k in range (len(Rotor2)):
            save=Rotor2[k][0]
            for i in range(0,len(Rotor2[k])-1):
                Rotor2[k][i]=Rotor2[k][i+1]
            Rotor2[k][len(Rotor2[k])-1]=save
    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame11,  text=Rotor2[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)   

def decalage_un_rangGR3(z):
    global Rotor3
    for j in range(0,z):
        for k in range (len(Rotor3)):
            save=Rotor3[k][0]
            for i in range(0,len(Rotor3[k])-1):
                Rotor3[k][i]=Rotor3[k][i+1]
            Rotor3[k][len(Rotor3[k])-1]=save
    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame1,  text=Rotor3[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)  


def decalage_un_rangDR1(z):
     global Rotor1
     for j in range(0,z):
        for k in range(len(Rotor1)):
            save=Rotor1[k][len(Rotor1[k])-1]
            for i in range(len(Rotor1[k])-1,0,-1):
                Rotor1[k][i]=Rotor1[k][i-1]
            Rotor1[k][0]=save
     for row in range(2):
      for column in range(26):
        label11=Label(Enigma.Frame12,  text=Rotor1[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)     

def decalage_un_rangDR2(z):
     global Rotor2
     for j in range(0,z):
        for k in range(len(Rotor2)):
            save=Rotor2[k][len(Rotor2[k])-1]
            for i in range(len(Rotor2[k])-1,0,-1):
                Rotor2[k][i]=Rotor2[k][i-1]
            Rotor2[k][0]=save
     for row in range(2):
      for column in range(26):
        label11=Label(Enigma.Frame11,  text=Rotor2[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)  

def decalage_un_rangDR3(z):
     global Rotor3
     for j in range(0,z):
        for k in range(len(Rotor3)):
            save=Rotor3[k][len(Rotor3[k])-1]
            for i in range(len(Rotor3[k])-1,0,-1):
                Rotor3[k][i]=Rotor3[k][i-1]
            Rotor3[k][0]=save
     for row in range(2):
      for column in range(26):
        label11=Label(Enigma.Frame1,  text=Rotor3[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)  


 #------------------Fonctions de Décalage d'un rang ------------------------------------------#                                

  #------------------Fonctions de Décalage de n rang ------------------------------------------#
    
def toLeft(valeur):
    global Rotor1
    Rotor1=[ [17,4,19,21,7,11,3,-5,7,9,-10,9,17,6,-6,-2,-4,-7,-12,-5,3,4,-21,-16,-2,-21 ] , 
[10,21,5,-17,21,-4,12,16,6,-3,7,-7,4,2,5,-7,-11,-17,-9,-6,-9,-19,2,-3,-21,-4] ]  

    for j in range(0,valeur):
        for k in range (len(Rotor1)):
            save=Rotor1[k][0]
            for i in range(0,len(Rotor1[k])-1):
                Rotor1[k][i]=Rotor1[k][i+1]
            Rotor1[k][len(Rotor1[k])-1]=save
    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame12,  text=Rotor1[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)
    
        

def toLeft1(valeur):
    global Rotor2
    Rotor2= [ [25,7,17,-3,13,19,12,3,-1,11,5,-5,-7,10,-2,1,-2,4,-17,-8,-16,-18,-9,-1,-22,-16],
 [3,17,22,18,16,7,5,1,-7,+16,-3,8,2,9,2,-5,-1,-13,-12,-17,-11,-4,1,-10,-19,-25 ] ]

    for j in range(0,valeur):
        for k in range (len(Rotor2)):
            save=Rotor2[k][0]
            for i in range(0,len(Rotor2[k])-1):
                Rotor2[k][i]=Rotor2[k][i+1]
            Rotor2[k][len(Rotor2[k])-1]=save
    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame11,  text=Rotor2[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)         


def toLeft2(valeur):
    global Rotor3
    Rotor3 = [ [12,-1,+23,+10,2,14,5,-5,9,-2,-13,+10,-2,-8,10,-6,6,-16,2,-1,-17,-5,-14,-9,-20,10],
 [1,16,5,17,20,8,-2,+2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23] ]
    column=0
    row=0
    for j in range(0,valeur):
        for k in range (len(Rotor3)):
            save=Rotor3[k][0]
            for i in range(0,len(Rotor3[k])-1):
                Rotor3[k][i]=Rotor3[k][i+1]
            Rotor3[k][len(Rotor3[k])-1]=save
    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame1,  text=Rotor3[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1) 


def toRight(valeur):
    global Rotor1
    Rotor1=[ [17,4,19,21,7,11,3,-5,7,9,-10,9,17,6,-6,-2,-4,-7,-12,-5,3,4,-21,-16,-2,-21 ] , 
[10,21,5,-17,21,-4,12,16,6,-3,7,-7,4,2,5,-7,-11,-17,-9,-6,-9,-19,2,-3,-21,-4] ]
    row=0
    column=0
    
    for j in range(valeur):
        for k in range(len(Rotor1)):
            save=Rotor1[k][len(Rotor1[k])-1]
            for i in range(len(Rotor1[k])-1,0,-1):
                Rotor1[k][i]=Rotor1[k][i-1]
            Rotor1[k][0]=save
    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame12,  text=Rotor1[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)  

def toRight1(valeur):
    global Rotor2
    Rotor2= [ [25,7,17,-3,13,19,12,3,-1,11,5,-5,-7,10,-2,1,-2,4,-17,-8,-16,-18,-9,-1,-22,-16],
 [3,17,22,18,16,7,5,1,-7,+16,-3,8,2,9,2,-5,-1,-13,-12,-17,-11,-4,1,-10,-19,-25 ] ]
    row=0
    column=0
    
    for j in range(valeur):
        for k in range(len(Rotor2)):
            save=Rotor2[k][len(Rotor2[k])-1]
            for i in range(len(Rotor2[k])-1,0,-1):
                Rotor2[k][i]=Rotor2[k][i-1]
            Rotor2[k][0]=save

    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame11,  text=Rotor2[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)  

def toRight2(valeur):
    global Rotor3
    Rotor3 = [ [12,-1,+23,+10,2,14,5,-5,9,-2,-13,+10,-2,-8,10,-6,6,-16,2,-1,-17,-5,-14,-9,-20,10],
 [1,16,5,17,20,8,-2,+2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23] ]
    row=0
    column=0
    
    for j in range(valeur):
        for k in range(len(Rotor3)):
            save=Rotor3[k][len(Rotor3[k])-1]
            for i in range(len(Rotor3[k])-1,0,-1):
                Rotor3[k][i]=Rotor3[k][i-1]
            Rotor3[k][0]=save

    for row in range(2):
     for column in range(26):
        label11=Label(Enigma.Frame1,  text=Rotor3[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        label11.grid(row=row ,column=column ,padx=1,pady=1)


def configureR1():
 for row in range(2):
    for column in range(26):
        Enigma.Frame12.label12=Label(Enigma.Frame12,  text=Rotor1Up[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        Enigma.Frame12.label12.grid(row=row ,column=column ,padx=1,pady=1)
   

def configureR2():
 for row in range(2):
    for column in range(26):
     Enigma.Frame11.label11=Label(Enigma.Frame11,  text=Rotor2Up [row][column] , background='silver',padx=10 ,pady=3 , width=2 )
     Enigma.Frame11.label11.grid(row=row ,column=column ,padx=1,pady=1) 

def configureR3(): 
 for row in range(2):
    for column in range(26):
        Enigma.Frame1.label13=Label(Enigma.Frame1,  text=Rotor3Up[row][column] ,background='silver',padx=10 ,pady=3 ,width=2  )
        Enigma.Frame1.label13.grid(row=row ,column=column ,padx=1,pady=1)   

def configureRéf() :
    for row in range(1):
     for column in range(26):
        Enigma.Frame0.labelR=Label(Enigma.Frame0,  text=Réflecteur[column],background='silver' ,padx=10 ,pady=3 ,width=2 )
        Enigma.Frame0.labelR.grid(row=row ,column=column ,padx=1,pady=1)

def configureAlpha():
    Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for row in range(1):
      for column in range(26):
        Enigma.Frame0A.labelA=Label(Enigma.Frame0A,  text=Alphabet[column],background='silver' ,padx=10 ,pady=3  )
        Enigma.Frame0A.labelA.grid(row=row ,column=column ,padx=1,pady=1)


#------------------Fonctions de Décalage de n rang ------------------------------------------#


#la fonction de décalage---------------------------------------------------------------------------------------------#
def Decalage():
    global i 
    i=0
    Rotor_entrer=clicked_Rotor.get()
    #coté_choisi=clicked_cote.get()
    valeur=(int(entree1.get()))
    if Rotor_entrer == 'R1' :
        if valeur>0 :
          toRight(valeur)
        else :
            toLeft(abs(valeur))  
    elif Rotor_entrer == 'R2':
        if valeur>0 :
          toRight1(valeur)
        else :
             toLeft1(abs(valeur))   
    else:
        if valeur>0 :
          toRight2(valeur)
        else :
             toLeft2(abs(valeur))   
    
    Rotor_entrer1=clicked_Rotor1.get()
    #coté_choisi1=clicked_cote1.get()
    valeur1=(int(entree5.get()))
    if Rotor_entrer1 == 'R1' :
        if valeur1>0 :
          toRight(valeur1)
        else :
             toLeft(abs(valeur1))  
    elif Rotor_entrer1 == 'R2':
        if valeur1>0 :
            toRight1(valeur1)
        else :
            toLeft1(abs(valeur1))
    else:
        if valeur1>0:
            toRight2(valeur1)
        else :
             toLeft2(abs(valeur1)) 

    configureAlpha()
    configureRéf()

    Rotor_entrer2=clicked_Rotor2.get()
    #coté_choisi2=clicked_cote2.get()
    valeur2=(int(entree4.get()))
    if Rotor_entrer2 == 'R1' :
        if valeur2>0 :
          toRight(valeur2)
        else :
             toLeft(abs(valeur2))  
    elif Rotor_entrer2 == 'R2':
        if valeur2>0:
          toRight1(valeur2)
        else :
             toLeft1(abs(valeur2))
    else:
        if valeur2>0:
          toRight2(valeur2)
        else :
             toLeft2(abs(valeur2))

    #la fonction de décalage---------------------------------------------------------------------------------------------#

#--------------------------------------------------------Décrypter----------------------------------------------#
def dycrypter() : 
    S=recuperC().upper()
    print(S)
    global i,Bool
    message=''
    
    if i<len(S) : 
     if S[i]==' ':
         i=i+1
         message=message+' '
     char=S[i]
     valeur=lettre_en_nombre(char)
     colorierAlphaM(valeur)
     print(valeur)
     colorerRotor(valeur) 
     print('rotor1 ') 
     



     colorierLabelR1M(valeur)
     valeur=(valeur+passage_dans_rotor(Rotor1, valeur))%26
     
     colorierLabelR2M(valeur)
     colorerRotor(valeur)
     print('rotor2')
     valeur=(valeur+passage_dans_rotor(Rotor2, valeur))%26
     colorierLabelR3M(valeur)
     colorerRotor(valeur)
     print('rotor3')
     valeur=(valeur+passage_dans_rotor(Rotor3, valeur))%26
     colorerRotor(valeur)
     colorierLabelRef(valeur)
     print('reflecteur 1ere fois')
     print(valeur)
     valeur=(valeur+passage_dans_reflecteur(valeur))%26
     print(passage_dans_reflecteur(valeur))
     colorerRotor(valeur)
     colorierLabelR3D(valeur)
     colorierLabelRefD(valeur)
     print('refelcteur 2eme fois')
     # valeur =passage_dans_rotor(Rotor1Up,0)%26
     print(valeur)
     print('rotor 3 ')
       #jusque la tout marche à merveille! 
     
     valeur=(valeur+ passage_dans_rotor_down(Rotor3,valeur))%26
     colorierLabelR2D(valeur)
     colorerRotor(valeur) 
     print('rotor2')
     valeur=(valeur+ passage_dans_rotor_down(Rotor2,valeur))%26
     colorerRotor(valeur)
     colorierLabelR1D(valeur)
     print('rotor1')
     valeur=(valeur+ passage_dans_rotor_down(Rotor1,valeur))%26
     colorerRotor(valeur)
     colorierAlphaD(valeur)
     print('place alphabet')
     azul = passage_inverse_rotor(valeur)
     print(valeur)
     print(azul)
     message=message+azul
     
    Bool=TRUE
    afficherD(message)

    #--------------------------------------------------------Décrypter----------------------------------------------#


#--------------------------------------------------------Encrypter----------------------------------------------#

def encrypter() : 
    Rotor_entrer=clicked_Rotor.get()
    coté_choisi=clicked_cote.get()
    Rotor_entrer1=clicked_Rotor1.get()
    coté_choisi1=clicked_cote1.get()
    Rotor_entrer2=clicked_Rotor2.get()
    coté_choisi2=clicked_cote2.get()
    cpt=0
    S=recuper().upper()
    
    global i,Bool
    message=''
    
    if i<len(S) : 
     if S[i]==' ':
         i=i+1
         message=message+' '
     char=S[i]
     valeur=lettre_en_nombre(char)
     colorierAlphaM(valeur)
     print(valeur)
     colorerRotor(valeur) 
     print('rotor1 ') 
     



     colorierLabelR1M(valeur)
     valeur=(valeur+passage_dans_rotor(Rotor1, valeur))%26
     
     colorierLabelR2M(valeur)
     colorerRotor(valeur)
     print('rotor2')
     valeur=(valeur+passage_dans_rotor(Rotor2, valeur))%26
     colorierLabelR3M(valeur)
     colorerRotor(valeur)
     print('rotor3')
     valeur=(valeur+passage_dans_rotor(Rotor3, valeur))%26
     colorerRotor(valeur)
     colorierLabelRef(valeur)
     print('reflecteur 1ere fois')
     print(valeur)
     valeur=(valeur+passage_dans_reflecteur(valeur))%26
     print(passage_dans_reflecteur(valeur))
     colorerRotor(valeur)
     colorierLabelR3D(valeur)
     colorierLabelRefD(valeur)
     print('refelcteur 2eme fois')
     # valeur =passage_dans_rotor(Rotor1Up,0)%26
     print(valeur)
     print('rotor 3 ')
       #jusque la tout marche à merveille! 
     
     valeur=(valeur+ passage_dans_rotor_down(Rotor3,valeur))%26
     colorierLabelR2D(valeur)
     colorerRotor(valeur) 
     print('rotor2')
     valeur=(valeur+ passage_dans_rotor_down(Rotor2,valeur))%26
     colorerRotor(valeur)
     colorierLabelR1D(valeur)
     print('rotor1')
     valeur=(valeur+ passage_dans_rotor_down(Rotor1,valeur))%26
     colorerRotor(valeur)
     colorierAlphaD(valeur)
     print('place alphabet')
     azul = passage_inverse_rotor(valeur)
     print(valeur)
     print(azul)
     message=message+azul
     
    Bool=TRUE
    afficher(message)

 #--------------------------------------------------------Encrypter----------------------------------------------#   

def colorerRotor(valeur): 
    print('la case',valeur,'est coloré')
     

def recuperC():
 return entree.get()

def afficherD(message) : 
    entree3.insert(END,message) 


def recuper():
 return entree3.get()

def afficher(message) : 
    entree.insert(END,message)    
    

def lettre_en_nombre(lettre) :

    return Alphabet.index(lettre)


def passage_inverse_rotor(valeur):
    return Alphabet[valeur]    


def passage_dans_rotor(rotor, valeur):
 return rotor[1][valeur]

def passage_dans_rotor_down(rotor, valeur):
 return rotor[0][valeur]

def passage_dans_reflecteur(valeur):
 return Réflecteur[valeur]    



           
#Programe principale--------------------------------------------------------------------------------#

Enigma=Tk()

Enigma.title('Enigma')
Enigma.iconbitmap()
Enigma.geometry('900x680')
# Enigma.iconbitmap('enigmaaa.ico')

FrameRéf=Frame(Enigma) 
FrameRéf.pack()    #Frame principale 


Enigma.Frame0 = Frame(Enigma)   #Frame du réflécteur 
Enigma.Frame0.pack(pady=10)

FrameRot3=Frame(Enigma)  #Frame du rotor3  
FrameRot3.pack()
Enigma.Frame1 = ttk.Frame(Enigma)
Enigma.Frame1.pack(pady=10)

FrameRot2=Frame(Enigma)
FrameRot2.pack()               #Frame du rotor2
Enigma.Frame11 = ttk.Frame(Enigma)
Enigma.Frame11.pack(pady=10) 
      
FrameRot1=Frame(Enigma)
FrameRot1.pack()                 #Frame du rotor1
Enigma.Frame12 = ttk.Frame(Enigma)
Enigma.Frame12.pack(pady=10)

Enigma.Frame0A = Frame(Enigma)  #Frame Alphabét
Enigma.Frame0A.pack(pady=10)

sp = ttk.Separator(Enigma, orient='horizontal')
sp.pack(fill='x',pady=10)

Frame2 = Frame(Enigma)   #Frame pour Zone de Clé
Frame2.pack(pady=15)

sp = ttk.Separator(Enigma, orient='horizontal')
sp.pack(fill='x',pady=10)

Frame3 = Frame(Enigma)   #Frame pour encrypter ou Résultat Décryptage
Frame3.pack(pady=20)

Frame4 = Frame(Enigma)   #Frame des boutons
Frame4.pack(pady=20)

sp = ttk.Separator(Enigma, orient='horizontal')
sp.pack(fill='x',pady=5)

Frame5 = Frame(Enigma)  #Frame pour décrypter ou Résultat Cryptage
Frame5.pack(pady=20)


for row in range(1):
    for column in range(26):
        Enigma.Frame0.labelR=Label(Enigma.Frame0,  text=Réflecteur[column],background='silver' ,padx=10 ,pady=3 ,width=2 )
        Enigma.Frame0.labelR.grid(row=row ,column=column ,padx=1,pady=1)

for row in range(2):
    for column in range(26):
        Enigma.Frame1.label13=Label(Enigma.Frame1,  text=Rotor3Up[row][column] ,background='silver',padx=10 ,pady=3 ,width=2  )
        Enigma.Frame1.label13.grid(row=row ,column=column ,padx=1,pady=1)

for row in range(2):
    for column in range(26):
       
        Enigma.Frame11.label11=Label(Enigma.Frame11,  text=Rotor2Up [row][column] , background='silver',padx=10 ,pady=3 , width=2 )
        Enigma.Frame11.label11.grid(row=row ,column=column ,padx=1,pady=1)
  
for row in range(2):
    for column in range(26):
        Enigma.Frame12.label12=Label(Enigma.Frame12,  text=Rotor1Up[row][column] ,background='silver',padx=10 ,pady=3, width=2  )
        Enigma.Frame12.label12.grid(row=row ,column=column ,padx=1,pady=1)

Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for row in range(1):
    for column in range(26):
        Enigma.Frame0A.labelA=Label(Enigma.Frame0A,  text=Alphabet[column],background='silver' ,padx=10 ,pady=3  )
        Enigma.Frame0A.labelA.grid(row=row ,column=column ,padx=1,pady=1)
        
a= lettre_en_nombre('A') 
print(a) 

label = Label(FrameRéf, text="Réflécteur")
label.pack(side=RIGHT )
label = Label(FrameRot3, text="Rotor 3")
label.pack(side=RIGHT )
label = Label(FrameRot2, text="Rotor 2")
label.pack(side=RIGHT )
label = Label(FrameRot1, text="Rotor 1")
label.pack(side=RIGHT )


label = Label(Frame2, text="La clé est :")
label.pack(side=LEFT,padx=5 )

Frame2A=Frame(Frame2 )
Frame2A.pack(padx=10, side=LEFT)

Frame2B=Frame(Frame2 )
Frame2B.pack(padx=10, side=LEFT)

Frame2C=Frame(Frame2 )
Frame2C.pack(padx=10, side=LEFT)

clicked_Rotor=StringVar()
clicked_Rotor.set('R1')

clicked_Rotor1=StringVar()
clicked_Rotor1.set('R1')

clicked_Rotor2=StringVar()
clicked_Rotor2.set('R1')

clicked_cote=StringVar()
clicked_cote.set('G')

clicked_cote1=StringVar()
clicked_cote1.set('G')

clicked_cote2=StringVar()
clicked_cote2.set('G')
#--------------------------------------------------------------------------

# def Selection_Rotor(event):
#     my_lable=Label(Frame2A, text=clicked_Rotor.get()).pack()

# def Selection_Coté(event):
#     my_lable=Label(Frame2A, text=clicked_cote.get()).pack()


#--------------------------------------------------------------------------
liste_rotors=['R1','R2','R3']
liste_coté=['G','D']
#--------------------------------------------------------------------------
drop_rotor=OptionMenu(Frame2A,clicked_Rotor,*liste_rotors)
drop_rotor.pack(side=LEFT)
drop_coté=OptionMenu(Frame2A,clicked_cote,*liste_coté )  #command=Selection_Coté
drop_coté.pack(side=LEFT)
value = StringVar() 
entree1 = Entry(Frame2A, text=value, width=5)
entree1.pack(side=LEFT)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
drop=OptionMenu(Frame2B,clicked_Rotor1,'R1','R2','R3')
drop.pack(side=LEFT)
drop=OptionMenu(Frame2B,clicked_cote1,'G','D')
drop.pack(side=LEFT)

value = StringVar() 
entree5 = Entry(Frame2B ,text= value , width=5  )
entree5.pack(side=LEFT)
#--------------------------------------------------------------------------
drop=OptionMenu(Frame2C,clicked_Rotor2,'R1','R2','R3')
drop.pack(side=LEFT)
drop=OptionMenu(Frame2C,clicked_cote2,'G','D')
drop.pack(side=LEFT)
value = StringVar() 
entree4 = Entry(Frame2C ,text= value , width=5 )
entree4.pack(side=LEFT)

#--------------------------------------------------------------------------




label = Label(Frame3, text="Texte à Encrypter / Résultat Décryptage ")
label.pack(side=LEFT,padx=7 )

label = Label(Frame5, text="Texte à Décrypter /Résulat Cryptage : ")
label.pack(side=LEFT,padx=7 )


# value = StringVar() 
# entree2 = Entry(Frame2, width=200 )
# entree2.pack()

value = StringVar() 
entree3 = Entry(Frame3,  width=150 )
entree3.pack()


btn1 = Button(Frame4, command=Decalage, text="Configure rotors",padx=50)
btn1.grid(row=0,column=1,padx=20)
btn2 = Button(Frame4, text="Encrypter",padx=50,command=click)
btn2.grid(row=0,column=2,padx=20)
btn3 = Button(Frame4, text="Decrypter",padx=50,command=clickD)
btn3.grid(row=0,column=3,padx=20)
btn4 = Button(Frame4, text=" Etape suivante" ,padx=50,command=click1)
btn4.grid(row=0,column=4,padx=20)






value = StringVar() 
entree = Entry(Frame5, width=150 )
entree.pack()


#----------------------------------Coloriage -------------------------------------------------------------
#chaque rotor a sa fonction de coloriage car chacun se situe dans un Frame différent c'est pour cela ! 
def colorierLabelR1M(key): 
    Enigma.Frame12.labeltemp=Label(Enigma.Frame12,  text=Rotor1[1][key] ,background='silver',fg='red', )
    Enigma.Frame12.labeltemp.grid(row=1 ,column=key ,padx=1,pady=1)
def colorierLabelR2M(key): 
    Enigma.Frame11.labeltemp=Label(Enigma.Frame11,  text=Rotor2[1][key] ,background='silver',fg='red', )
    Enigma.Frame11.labeltemp.grid(row=1 ,column=key ,padx=1,pady=1)    
def colorierLabelR3M(key): 
    Enigma.Frame1.labeltemp=Label(Enigma.Frame1,  text=Rotor3[1][key] ,background='silver',fg='red', )
    Enigma.Frame1.labeltemp.grid(row=1 ,column=key ,padx=1,pady=1)
def colorierLabelRef(key): 
    Enigma.Frame0.labeltemp=Label(Enigma.Frame0,  text=Réflecteur[key] ,background='silver',fg='red', )
    Enigma.Frame0.labeltemp.grid(row=0 ,column=key ,padx=1,pady=1)
def colorierLabelRefD(key): 
    Enigma.Frame0.labeltemp=Label(Enigma.Frame0,  text=Réflecteur[key] ,background='silver',fg='blue', )
    Enigma.Frame0.labeltemp.grid(row=0 ,column=key ,padx=1,pady=1) 
def colorierLabelR1D(key): 
    Enigma.Frame12.labeltemp=Label(Enigma.Frame12,  text=Rotor1[0][key] ,background='silver',fg='blue', )
    Enigma.Frame12.labeltemp.grid(row=0 ,column=key ,padx=1,pady=1)
def colorierLabelR2D(key): 
    Enigma.Frame11.labeltemp=Label(Enigma.Frame11,  text=Rotor2[0][key] ,background='silver',fg='blue', )
    Enigma.Frame11.labeltemp.grid(row=0 ,column=key ,padx=1,pady=1)    
def colorierLabelR3D(key): 
    Enigma.Frame1.labeltemp=Label(Enigma.Frame1,  text=Rotor3[0][key] ,background='silver',fg='blue', )
    Enigma.Frame1.labeltemp.grid(row=0 ,column=key ,padx=1,pady=1)
def colorierAlphaD(key): 
    Enigma.Frame0A.labeltemp=Label(Enigma.Frame0A,  text=Alphabet[key] ,background='silver',fg='blue', )
    Enigma.Frame0A.labeltemp.grid(row=0 ,column=key ,padx=1,pady=1)  
def colorierAlphaM(key): 
    Enigma.Frame0A.labeltemp=Label(Enigma.Frame0A,  text=Alphabet[key] ,background='silver',fg='red', )
    Enigma.Frame0A.labeltemp.grid(row=0 ,column=key ,padx=1,pady=1) 

Enigma.mainloop()

#----------------------------------------------------------------------------------------------------------#
