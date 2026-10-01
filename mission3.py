# =====================================================
#  Mission 3 - Le chenillard (barre de 8 LED)
# =====================================================
# On travaille ici sur une simple LISTE de 8 LED (une seule ligne).
# Une seule LED est allumee a la fois, et elle se deplace :
#   - aller  : de la LED 0 jusqu'a la LED 7   (8 affichages)
#   - retour : de la LED 6 jusqu'a la LED 1   (6 affichages)
# Chaque etape est affichee sur une ligne, comme en mission 2.

TAILLE = 8

# --- creation de la barre eteinte ---
barre = []

# TODO

for j in range(TAILLE):
    barre.append(".")





# --- aller ---
# TODO : pour chaque position, tout eteindre, allumer la bonne LED,
#        puis afficher la barre




# --- retour ---
# TODO : meme chose, mais avec un range() qui compte a l'envers

n=1
for i in range(TAILLE):
    for a in range(TAILLE):
            

            if j==n :
                barre[n] = '#'
                print(barre[j],end=" ")

            else : 
                print(barre[j],end=" ")

            n = n+1


    print()