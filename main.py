import random

def tekening(p):
    lijst = [  """
                   --------
                   |      |
                   |      O
                   |     \ /
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \ /
                   |      |
                   |     / 
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \ /
                   |      |
                   |     
                   -
                   """,
                   """
                  --------
                   |      |
                   |      O
                   |     \ /
                   |      
                   |      
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return lijst[p]

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

def SpeelSpel():
    pogingen=start()
    WoordenLijst=['informatica', 'informatiekunde', 'spelletje','aardigheidje', 'scholier', 'fotografie','waardebepaling', 'specialiteit','verzekering', 'universiteit']
    list1,list2=WillekeurigWoord(WoordenLijst)
    ToonWoord(list2)

    while pogingen > 0:
        letter = input("raad een letter:\n")
        if letter in list1:
            print('goed geraden!')
            index=-1
            for i in list1:
                index+=1
                if i==letter:
                    list2[index]=letter
        elif letter not in list1:
            print("%s"%(tekening(pogingen-1)))
            pogingen-=1
            if pogingen==0:
                print("jammer, je hangt!")
                print('het woord was:')
                ToonWoord(list1)
            elif pogingen>0:
                print("verkeerd geraden!, je mag nog %s keer fout raden"%(pogingen))
        ToonWoord(list2)
        if "_" not in list2:
            print("je hebt het woord geraden!")
            break
SpeelSpel()