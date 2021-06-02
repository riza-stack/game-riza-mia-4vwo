import random

WoordenLijst=['informatica', 'informatiekunde', 'spelletje','aardigheidje', 'scholier', 'fotografie','waardebepaling', 'specialiteit','verzekering', 'universiteit']

def start():
    p=5
    print("Leuk, we gaan galgje spelen!")
    print("Je mag %s keer fout raden" %(p))
    print("%s"%(tekening(p)))
    return(p)


def WillekeurigWoord(W):
    woord=random.choice(W)
    l1=[]
    l2=[]
    for i in woord:
        l1.append(i)
        l2.append('_')
    return(l1,l2)

def ToonWoord(l2):
    for i in l2:
        print(i, end=" ")
    print("")
