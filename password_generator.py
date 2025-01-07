import random
import string
import math

class PasswordGenerator:

    def generate_password(self, min_length, maj_length, digit_length, special_length):
        # Génération de caractères selon les critères
        lowercase = random.choices(string.ascii_lowercase, k=min_length) # Liste des lettres minuscules
        uppercase = random.choices(string.ascii_uppercase, k=maj_length) # Liste des lettres majuscules
        digits = random.choices(string.digits, k=digit_length) # Liste des chiffres
        specials = random.choices("!@#$%^&*()-_=+[]{}|;:,.<>?", k=special_length) # Liste des caractères spéciaux
        
        # Combinaison des caractères et mélange
        all_chars = lowercase + uppercase + digits + specials
        random.shuffle(all_chars)
        
        return ''.join(all_chars)
    
    def calculate_entropy(self, password):
        # Calcul de l'entropie du mot de passe
        pool_size = 0
        # Déterminer les types de caractères utilisés
        if any(c.islower() for c in password):
            pool_size += 26
        if any(c.isupper() for c in password):
            pool_size += 26
        if any(c.isdigit() for c in password):
            pool_size += 10
        if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password):
            pool_size += 32
        
    
        return len(password) * math.log2(pool_size)
