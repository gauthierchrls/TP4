"""
Charles Gauthier
407
exercice de classe 3
"""


import random
from dataclasses import dataclass
import enum


class Alignement(enum.Enum):
    LOYAL_BON = "Loyal Bon"
    NEUTRE_BON = "Neutre Bon"
    CHAOTIQUE_BON = "Chaotique Bon"
    LOYAL_NEUTRE = "Loyal Neutre"
    NEUTRE = "Neutre"
    CHAOTIQUE_NEUTRE = "Chaotique Neutre"
    LOYAL_MAUVAIS = "Loyal Mauvais"
    NEUTRE_MAUVAIS = "Neutre Mauvais"
    CHAOTIQUE_MAUVAIS = "Chaotique Mauvais"
    NON_DEFINI = "Non défini"




def dee():
    lancers_dee = [random.randint(1, 6) for _ in range(4)]
    lancers_dee.sort(reverse=True)
    lancers_dee.pop()
    return sum(lancers_dee)






@dataclass
class NPCstats:
    force: int = dee()
    agilite: int = dee()
    constitution: int = dee()
    intelligence: int = dee()
    sagesse: int = dee()
    charisme: int = dee()





@dataclass
class Item:
    quantite: int
    nom: str



class SacADos:
    def __init__(self):
        self.liste_items = []


    def ajouter_item(self, item: Item):
        for i in self.liste_items:
            if i.nom == item.nom:
                i.quantite += item.quantite
                return
        self.liste_items.append(item)


    def retirer_item(self, nom_item, quantite):
        for i in self.liste_items:
            if i.nom == nom_item:
                if quantite > i.quantite:
                    print("Erreur : quantité à retirer trop grande.")
                    return
                i.quantite -= quantite
                if i.quantite == 0:
                    self.liste_items.remove(i)
                return
        print("Erreur : item non présent dans le sac.")


    def voir_contenu(self):
        if not self.liste_items:
            print("Le sac est vide.")
        else:
            print("Contenu du sac :")
            for item in self.liste_items:
                print(f"- {item.nom} x{item.quantite}")


class NPC:
    def __init__(self, nom, race, espece, profession, alignement=Alignement.NON_DEFINI):
        self.stats = NPCstats()
        self.armur = random.randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.vie = random.randint(10, 20)
        self.profession = profession
        self.alignement = alignement


    def caract(self):
        print(self.stats)
        print(f"armur: {self.armur}")
        print(f"nom: {self.nom}")
        print(f"race: {self.race}")
        print(f"espece: {self.espece}")
        print(f"vie: {self.vie}")
        print(f"profession: {self.profession}")
        print(f"alignement: {self.alignement.value}")


    def est_vivant(self):
        return self.vie > 0


class Kobold(NPC):
    def __init__(self, nom, espece="monstre", profession="kobold"):
        super().__init__(nom, "Kobold", espece, profession, Alignement.CHAOTIQUE_MAUVAIS)


    def attaquer(self, target):
        if not self.est_vivant():
            print(f"{self.nom} est mort et ne peut pas attaquer.")
            return


        print(f"{self.nom} attaque {target.nom} !")
        valeur_attack = random.randint(1, 20)


        if valeur_attack == 1:
            print(f"{self.nom} rate son attaque.")
        elif valeur_attack >= target.armur:
            print(f"{self.nom} touche sa cible !")
            dommage = random.randint(1, 6)
            target.subir_dommage(dommage)
        else:
            print(f"{self.nom} n'arrive pas à percer l'armure.")


    def subir_dommage(self, dommage):
        self.vie -= dommage
        print(f"{self.nom} subit {dommage} points de dommage. Vie restante: {self.vie}")



class Hero(NPC):
    def __init__(self, nom, race, espece, profession="Héros"):
        super().__init__(nom, race, espece, profession, Alignement.LOYAL_BON)
        self.sac = SacADos()


    def attaquer(self, target):
        if not self.est_vivant():
            print(f"{self.nom} est mort et ne peut pas attaquer.")
            return


        print(f"{self.nom} attaque {target.nom} !")
        valeur_attack = random.randint(1, 20)


        if valeur_attack == 1:
            print("Attaque ratée !")
        elif valeur_attack == 20:
            print("Coup critique !")
            dommage = random.randint(1, 8)
            target.subir_dommage(dommage)
        elif valeur_attack >= target.armur:
            print("Attaque réussie !")
            dommage = random.randint(1, 6)
            target.subir_dommage(dommage)
        else:
            print("Le coup n'a pas fonctionné.")


    def subir_dommage(self, dommage):
        self.vie -= dommage
        print(f"{self.nom} subit {dommage} points de dommage. Vie restante: {self.vie}")



if __name__ == "__main__":
    hero = Hero("Kanye East", "Humain", "Terrestre", "Guerrier")
    kobold = Kobold("Diddybop")


    hero.caract()
    kobold.caract()


    print("\nCombat!")
    hero.attaquer(kobold)
    kobold.attaquer(hero)


    print("\nSac à dos->")
    hero.sac.ajouter_item(Item(2, "Potion"))
    hero.sac.ajouter_item(Item(1, "Épée"))
    hero.sac.ajouter_item(Item(3, "Potion"))
    hero.sac.voir_contenu()
    hero.sac.retirer_item("Potion", 4)
    hero.sac.voir_contenu()
