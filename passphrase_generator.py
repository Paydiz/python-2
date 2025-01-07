import random

class PassphraseGenerator: # Classe pour générer des passphrases
    def __init__(self):
        self.word_list = self.load_word_list() # Chargement de la liste de mots
    
    def load_word_list(self): # Charge la liste de mots depuis le fichier wordlist
        with open("eff_large_wordlist.txt", "r") as f:
            return {line.split()[0]: line.split()[1] for line in f}
    
    def generate_passphrase(self, num_words): # Génère une passphrase en sélectionnant des mots aléatoires
        passphrase = []
        for _ in range(num_words):
            roll = ''.join(str(random.randint(1, 6)) for _ in range(5))  # Simuler un lancer de 5 dés
            passphrase.append(self.word_list[roll])
        return ' '.join(passphrase)
