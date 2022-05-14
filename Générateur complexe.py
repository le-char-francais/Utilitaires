## - INFORMATIONS DE FONCTIONNEMENT - ##
##
## - Lorsque le programme vous demande quel générateur vous souhaitez, spécifiez le chiffre associé au générateur choisi
## - Suivez les consignes qui s'affichent 

import random
import time

def init(composant):
    composant=list(composant)
    random.shuffle(composant)
    composant="".join(composant)
    return composant
    
def generateur(longueur):

    password = ""

    minuscules = "abcdefghijklmnopqrstuvwxyz"
    majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spéciaux = "&#{([-|_^@)]=}<>$£µ*!§/+"
    chiffres = "0123456789"
    ponctuation = "?,.;/!€"

    while longueur != 0:

        longueur-=1
        
        choix = random.randint(1, 5)

        if choix == 1:
            minuscules = init(minuscules)
            caractère = minuscules[random.randint(0, len(minuscules)-1)]
            password+=caractère

        if choix == 2:
            majuscules = init(majuscules)
            caractère = majuscules[random.randint(0, len(majuscules)-1)]
            password+=caractère

        if choix == 3:
            spéciaux = init(spéciaux)
            caractère = spéciaux[random.randint(0, len(spéciaux)-1)]
            password+=caractère

        if choix == 4:
            chiffres = init(chiffres)
            caractère = chiffres[random.randint(0, len(chiffres)-1)]
            password+=caractère

        if choix == 5:
            ponctuation = init(ponctuation)
            caractère = ponctuation[random.randint(0, len(ponctuation)-1)]
            password+=caractère

    return password

def cnil_gen(phrase):
    mot_de_passe = phrase[0]

    chiffres = "0123456789"

    for i in range(len(phrase)):

        if phrase[i]==" ":
            mot_de_passe+=phrase[i+1]
            
        if phrase[i] in chiffres and phrase[i+1] !=" ":
            mot_de_passe+=phrase[i+1]
    
    return mot_de_passe

def chiffrage(mot):
    
    password=""
    minuscules = "abcdefghijklmnopqrstuvwxyz"
    majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(mot)):
        if mot[i] in minuscules:
            for o in range(len(minuscules)):
                if minuscules[o]==mot[i]:
                    password+=str(o+1)+"."
        if mot[i] in majuscules:
            for o in range(len(majuscules)):
                if minuscules[o]==mot[i]:
                    password+=str(o+1)+"."

    return password         

def générateur_complexe():

    print("\n Voici les générateurs disponibles : \n\n 1 - Aléatoire \n 2 - CNIL \n 3 - Conversion")
    time.sleep(1)
    choix=int(input("\n Quel générateur choisis-tu ? : "))

    if choix==1:
        longueur=int(input("\n De quelle longueur doit être votre mot de passe ? : "))
        time.sleep(1)
        print("\n Votre mot de passe : ",generateur(longueur),"\n")
        
    if choix==2:
        phrase=str(input("\n Choisisez une phrase facilement mémorable : "))
        time.sleep(1)
        print("\n Votre mot de passe : ",cnil_gen(phrase),"\n")

    if choix==3:
        mot=str(input("\n Choisisez un mot facilement mémorable : "))
        time.sleep(1)
        print("\n Votre mot de passe : ",chiffrage(mot),"\n")

générateur_complexe()

# 62 lignes