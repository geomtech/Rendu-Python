# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 1.0.0
# Date : 12/11/2020
# Explication : Affiche à l'utilisateur le prix initial, le taux de réduction, la réduction et le prix soldé au client.

import math

# On demande le prix initial de l'article
prix_initial = float(input("Prix de l'article ? "))
# On demande le pourcentage de réduction
taux_reduction = int(input("Pourcentage de réduction ? "))

# On fait nos calculs
reduction = prix_initial * taux_reduction / 100
reduction = int(reduction * 100) / 100
prix_solde = prix_initial - reduction
prix_solde = int(prix_solde * 100) / 100

# On affiche le résultat
print(f"""Pour un article à un prix initial de {prix_initial} € et soldé à {taux_reduction} % :
Le montant de la réduction est de {reduction} €.
Le prix soldé est de {prix_solde} €.""")
