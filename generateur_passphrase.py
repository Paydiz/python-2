import random

class GenerateurDePassphrase:  # Classe pour générer des passphrases
    def __init__(self):
        self.liste_mots = self.charger_liste_mots()  # Chargement de la liste de mots
    
    def charger_liste_mots(self):  # Charge la liste de mots depuis le fichier wordlist
        with open("eff_large_wordlist.txt", "r") as fichier:
            return {ligne.split()[0]: ligne.split()[1] for ligne in fichier}
    
    def generer_passphrase(self, nombre_de_mots):  # Génère une passphrase en sélectionnant des mots aléatoires
        passphrase = []
        for _ in range(nombre_de_mots):
            lancer = ''.join(str(random.randint(1, 6)) for _ in range(5))  # Simuler un lancer de 5 dés
            passphrase.append(self.liste_mots[lancer])
        return ' '.join(passphrase)
