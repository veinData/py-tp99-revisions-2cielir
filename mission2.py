# =====================================================
#  Mission 2 - Construire et afficher la matrice
# =====================================================
# 1. Construire une matrice TAILLE x TAILLE remplie de 0, avec des boucles.
# 2. L'afficher : "# " pour une LED allumee, ". " pour une LED eteinte,
#    une ligne de la matrice = une ligne affichee.
# 3. Allumer les LED (2, 3) et (5, 5), afficher une ligne vide,
#    puis reafficher la matrice.
#
# ATTENTION : matrice = [[0] * 8] * 8 ne fonctionne PAS (voir RAPPELS-PYTHON.md).

TAILLE = 8

# --- 1. construction de la matrice eteinte ---
matrice = []
# TODO : pour chaque ligne, construire une liste de TAILLE zeros
#        puis l'ajouter a matrice avec .append()
for i in range(TAILLE):
    matrice.append([])
    for j in range(TAILLE):
        matrice[i].append(".")



# --- 2. affichage ---
# TODO : deux boucles imbriquees ; on construit une chaine texte pour
#        la ligne courante, puis on l'affiche avec print(texte)

for i in range(TAILLE):
    for j in range(TAILLE):
        print(matrice[i][j],end=" ")
    print()


# --- 3. allumage de deux LED puis nouvel affichage ---
# TODO

matrice[0][0]='#'
matrice[TAILLE-1][TAILLE-1]='#'


for i in range(TAILLE):
    for j in range(TAILLE):
        print(matrice[i][j],end=" ")
    print()