name = input("Entrer votre nom svp: ")
print("***Bienvenue Dans notre jeux", name, " I hope you will win****")
print("Bonne chance a vous!!!")
print("TOP C'EST PARTIE!!!")
question = input("Vous vous trouver dans un village abandonné, vous avez deux choix soit tourner a gauche ou  a droite, sinon vous etes mort!!!: ").lower()
if question == "gauche":
    question = input("Tu as choisi gauche,humm maintenant vous voyez une passerelle,soit vous montez ou vous traversez la route!!!: ")
    if question == "monter":
        question = input("Vous voyez une vielle vilaine femme ressemblant a une monstre assis par terre sur la passerelle, allez-vous la saluer oui ou non: ")
        if question == "oui":
            print("La vielle vous donne une livre contenant le bon chemin pour arriver dans la bonne destination, vous avez gagné*****CONGATULATION")
        else:
            print("La dame vous capture et vous emméne dans la foret,")
    elif question == "traverser":
        question = input("vous avez decider de traverser et vous voila devant des bandits armés,allez-vous vous <battre> et ou <fuir>")  
        if question=="battre":
            print('Tu est un guerrier, vous avez battu et gagné les bandits, et poursuivez le reste de votre chemin sans probléme')
            question = input("Vous avez traversé la route, maintenant vous aves devant vous 2chats qui se bagarrent, voulez-vous les <separer> ou les <laisser> pour continuer votre chemin: ")
            if question == "separer":
                print("Les deux chats vous guide le chemin a suivre en étant satisfait de vous,CONGRATULATION! vous avez gagné")
            elif question == "laisser":
                print("les deux chats vous battent,et vous torture tellement mal,")
            else:
                print("Choisi une chemin donné ou quitter le jeux")
        elif question=="fuir":
            print("Oppps vous avez heurté une voiture, Votre aventure s'arréte la!!")
        else:
             print("Choisi une chemin donné ou quitter le jeux")               
    else:
        print("Choisi une chemin donné ou quitter le jeux")               
         
elif question == "droite":
    question = input("vous avez choisi la droite,il y'a que la mer devant vous allez vous <nager> ou <prendre le pirogue>, taper nager ou progue ")
    if question == "nager":
        print("Vous avez été mangé par un requin, desole a vous, votre aventure s'arréte la, buy!!!!!")
    elif question == "pirogue":
        print("Vous avez pris la pirogue, bravos a vous, CONGRATULATION, vous etes arriver a destination, vous aves gagner.")
else:
    print("Choisi une cemin donné ou quitter le jeux")

    