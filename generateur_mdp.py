import random
import string
import math

class GenerateurDeMotDePasse:

    def generer_mot_de_passe(self, nb_min, nb_maj, nb_chiffres, nb_speciaux):
        # Génération de caractères selon les critères
        minuscules = random.choices(string.ascii_lowercase, k=nb_min)  # Liste des lettres minuscules
        majuscules = random.choices(string.ascii_uppercase, k=nb_maj)  # Liste des lettres majuscules
        chiffres = random.choices(string.digits, k=nb_chiffres)  # Liste des chiffres
        speciaux = random.choices("!@#$%^&*()-_=+[]{}|;:,.<>?", k=nb_speciaux)  # Liste des caractères spéciaux
        
        # Combinaison des caractères et mélange
        tous_les_caracteres = minuscules + majuscules + chiffres + speciaux
        random.shuffle(tous_les_caracteres)
        
        return ''.join(tous_les_caracteres)
    
    def calculer_entropie(self, mot_de_passe):
        # Calcul de l'entropie du mot de passe
        taille_du_pool = 0
        # Déterminer les types de caractères utilisés
        if any(c.islower() for c in mot_de_passe):
            taille_du_pool += 26
        if any(c.isupper() for c in mot_de_passe):
            taille_du_pool += 26
        if any(c.isdigit() for c in mot_de_passe):
            taille_du_pool += 10
        if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in mot_de_passe):
            taille_du_pool += 32
        
        # Calcul de l'entropie
        return len(mot_de_passe) * math.log2(taille_du_pool)
