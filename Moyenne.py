## - INFORMATIONS DE FONCTIONNEMENT - ##
##
## - Lorsque le programme vous demande le nombre de notes que vous voulez entrer, spécifiez un seul chiffre
## - Lorsqu'il vous demande votre note avec le coefficient, rentrez votre note, laissez un espace puis rentrer le coefficient

def moyenne():
    notes={}
    total=0
    coefficient=0
    for i in range(int(input("\n Combien de notes voulez-vous entrer ? : "))):
        valeurs=input("\n Entrez les notes et leurs coefficients : ")

        form = valeurs.split()
        notes[form[0]] = form[1]

    for clé in notes:

        total+=int(clé)*int(notes[clé])
        coefficient+=int(notes[clé])
        
    print("\n Voici ta moyenne :",total/coefficient,"\n")

moyenne()  