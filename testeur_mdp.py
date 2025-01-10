import math

class TesteurDeMotDePasse:
    @staticmethod
    def calculer_entropie(mot_de_passe):  # Calculer l'entropie du mot de passe
        taille_du_pool = 0
        if any(c.islower() for c in mot_de_passe):
            taille_du_pool += 26
        if any(c.isupper() for c in mot_de_passe):
            taille_du_pool += 26
        if any(c.isdigit() for c in mot_de_passe):
            taille_du_pool += 10
        if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in mot_de_passe):
            taille_du_pool += 32
        
        return len(mot_de_passe) * math.log2(taille_du_pool)
    
    @staticmethod
    def determiner_force(entropie):  # Déterminer la force du mot de passe
        if entropie < 28:
            return "Très faible"
        elif entropie < 36:
            return "Faible"
        elif entropie < 60:
            return "Moyenne"
        elif entropie < 128:
            return "Forte"
        else:
            return "Très forte"
