import math

class PasswordTester:
    @staticmethod
    def calculate_entropy(password): # Calculer l'entropie du mot de passe
        pool_size = 0
        if any(c.islower() for c in password):
            pool_size += 26
        if any(c.isupper() for c in password):
            pool_size += 26
        if any(c.isdigit() for c in password):
            pool_size += 10
        if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password):
            pool_size += 32
        
        return len(password) * math.log2(pool_size)
    
    @staticmethod
    def determine_strength(entropy): # Déterminer la force du mot de passe
        if entropy < 28:
            return "Très faible"
        elif entropy < 36:
            return "Faible"
        elif entropy < 60:
            return "Moyenne"
        elif entropy < 128:
            return "Forte"
        else:
            return "Très forte"
