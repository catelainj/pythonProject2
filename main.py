#Exercice POO partie 2
#Jules Catelain
#groupe 403
#14 Décembre 2023

import random

class NPC:


    def __init__ (self, nom, race, espece, profession):
          self.force = self.nombre_alléatoire()
          self.agilité = self.nombre_alléatoire()
          self.constitution = self.nombre_alléatoire()
          self.intelligence = self.nombre_alléatoire()
          self.sagesse = self.nombre_alléatoire()
          self.charisme = self.nombre_alléatoire()
          self.armure = random.randint(1, 12)
          self.nom = nom
          self.race = race
          self.espece = espece
          self.point_de_vie = random.randint(1, 20)
          self.profession = profession



    def nombre_alléatoire(self):
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        de3 = random.randint(1, 6)
        de4 = random.randint(1, 6)

        if de1 < de4 and de1 < de2 and de1 < de3:
            return de4 + de2 +de3

        elif de2 < de1 and de2 < de3 and de2 < de4:
            return de1 + de3 + de4

        elif de3 < de1 and de3< de2 and de3 < de4:
            return de1 + de3 + de4

        elif de4 < de1 and de4 < de2 and de4 < de3:
            return de1 + de2 + de3

    def afficher_caracteristiques(self):
        print('force', self.force)
        print('agilité',self.agilité)
        print('constitution', self.constitution)
        print('intelligence', self.intelligence)
        print('sagesse', self.sagesse)
        print('charisme', self.charisme)
        print('armure', self.armure)
        print('nom', self.nom)
        print('race', self.race)
        print('espece', self.espece)
        print('point_de_vie', self.point_de_vie)
        print('profession', self.profession)

class kobold(NPC):
    def attaquer(self, cible):
        de5 = random.randint(1, 20)

        if de5 == 20:
            print("Tu fais 8 degats a l'ennemie")
            cible.subir_dégats(random.randint(1,8))

        elif de5 == 1:
            print("attaque manqué")

        else:
            if de5 > cible.armure:
                print("Tu fais 8 dégats au Kobold")
                cible.subir_dégats(random.randint(1, 6))
            else:
                print("attaque manqué")





    def subir_dégats(self, qté_dommages):
        self.point_de_vie - qté_dommages


class Héro(NPC):
    def attaquer(self, cible):
        de5 = random.randint(1, 20)

        if de5 == 20:
            print("Tu fais 8 degats a l'ennemie")
            cible.subir_dégats(random.randint(1, 8))

        elif de5 == 1:
            print("attaque manqué")

        else:
            if de5 > cible.armure:
                print("tu fais 6 dégats au Héro")
                cible.subir_dégats(random.randint(1, 6))
            else:
                print("attaque manqué")

    def subir_dégats(self, qté_dommages):
        self.point_de_vie -= qté_dommages















