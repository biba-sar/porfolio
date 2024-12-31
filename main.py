print("******Bienvenue dans notre Boutique BIBAAAAAACisco******")
prenom = input("Veuillez entrer votre Prenom: ").capitalize()
nom = input("Veuillez entrer votre Nom: ").upper()
liste_commandes = []
prix_total = 0
while True:
    commandes = input("ajouter votre commande ou taper <q> pour arreter votre commande: ").lower()
    if commandes == "q":
        break
    liste_commandes.append(commandes)
    prix = float(input("Donnez le prix: "))
    tct = 0.18 * prix
    tva = prix + tct
    prix_total += prix
montant = int(input("Taper votre montant: "))
monnaie = montant - prix_total
print('Prenom: ', prenom)
print("nom: ", nom)
print('Vos commandes: ',liste_commandes)
print("prix_total: ",prix_total,"Fcf")
print("Votre monnaie: ", monnaie,"Fcfa")
print("******Merci beaucoup a la prochaine*******")



    