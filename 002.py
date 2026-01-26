"""
Charles Gauthier
407
exercice de classe 2
"""
import random
from dataclasses import dataclass

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

class NPC:
    def __init__(self, nom, race, espece, profession):
        self.stats = NPCstats()
        self.armur = random.randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.vie = random.randint(1, 20)
        self.profession = profession

    def caract(self):
        print(self.stats)
        print(f"armur: {self.armur}")
        print(f"nom: {self.nom}")
        print(f"race: {self.race}")
        print(f"espece: {self.espece}")
        print(f"vie: {self.vie}")
        print(f"profession: {self.profession}")


kanye = NPC("shivank", "terreste", "humaine", "medecin")
kanye.caract()


class Kobold(NPC):
    def __init__(self, nom, espece="monstre", profession="kobold"):
        super().__init__(nom, "Kanye East", espece, profession)

    def attaquer(self, target):
        print(f"{self.nom} attaque {target.nom} !")
        valeur_attack = random.randint(1, 20)
        if valeur_attack == 1:
            print("Diddybop rate son attaque.")
        elif valeur_attack >= target.armur:
            print("Diddybop touche sa cible !")
            dommage = random.randint(1, 6)
            target.subir_dommage(dommage)
        else:
            print("Diddybop n'arrive pas à percer l'armure.")

    def subir_dommage(self, dommage):
        self.vie -= dommage
        print(f"{self.nom} subit {dommage} points de dommage. Vie restante: {self.vie}")

class Hero(NPC):
    def __init__(self, nom, race, espece, profession="Héros"):
        super().__init__(nom, race, espece, profession)

    def attaquer(self, target):
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

    print("\n--- Début du combat ---")
    hero.attaquer(kobold)
    kobold.attaquer(hero)


