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
   WoordenLijst=['informatica', 'informatiekunde', 'spelletje','aardigheidje', 'scholier', 'fotografie','waardebepaling', 'specialiteit','verzekering', 'universiteit']
   p=5
   l=[]

   # Introductie spel
   print("Leuk, we gaan galgje spelen!")
   print("Je mag %s keer fout raden" %(p))
   
   # Tekening galge printen
   print("%s"%(tekening(p)))

   return(p,WoordenLijst,l)


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

def GeefLetter(AlGeprobeerd):
    letter = input("raad een letter:\n")
    while 'TRUE':
        if letter in AlGeprobeerd:
            letter = input("Die letter heb je eerder al geprobeerd, raad een letter die je niet al eerder hebt geprobeerd:\n")
        elif not (letter.isalpha() and len(letter)==1):
            letter = input("ongeldige input, probeer iets anders:\n")
        elif 'TRUE':
            break
    return letter

def SpeelSpel():
    pogingen,WoordenLijst, GeprobeerdeLetters=start()
    list1,list2=WillekeurigWoord(WoordenLijst)
    ToonWoord(list2)

    while pogingen > 0:
       # Toont geprobeerde letters aan
        print('je hebt de volgende letters al geprobeerd: %s'%(GeprobeerdeLetters))
        letter = GeefLetter(GeprobeerdeLetters)
        GeprobeerdeLetters.append(letter)
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
            
def game():
  again = input("Wil je opnieuw spelen? typ (ja/nee)")
  # game loop
  if again == "ja":
    SpeelSpel()
  else:
    print("THE END")

SpeelSpel()
game()