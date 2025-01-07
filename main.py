from password_generator import PasswordGenerator
from password_tester import PasswordTester
from passphrase_generator import PassphraseGenerator

def main():
    print("Bienvenue dans l'outil de génération et de test de mots de passe !\n")
    
    while True:
        print("Choisissez une option :")
        print("1. Générer un mot de passe")
        print("2. Tester la force d’un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")
        
        choice = input("Votre choix : ").strip()
        
        if choice == "1":
            # Génération de mot de passe
            print("\n--- Génération de mot de passe ---")
            min_length = int(input("Nombre de caractères minuscules : "))
            maj_length = int(input("Nombre de caractères majuscules : "))
            digit_length = int(input("Nombre de chiffres : "))
            special_length = int(input("Nombre de caractères spéciaux : "))
            
            generator = PasswordGenerator() # Création d'une instance de PasswordGenerator
            password = generator.generate_password(min_length, maj_length, digit_length, special_length) # Génération du mot de passe
            entropie = generator.calculate_entropy(password) # Calcul de l'entropie
            strength = PasswordTester.determine_strength(entropie) # Détermination de la force du mot de passe
            
            print(f"Mot de passe généré : {password}")
            print(f"Entropie : {entropie:.2f} bits")
            print(f"Force : {strength}\n")
        
        elif choice == "2":
            # Test de la force d'un mot de passe
            print("\n--- Test de force de mot de passe ---")
            password = input("Entrez le mot de passe à tester : ")
            tester = PasswordTester()
            entropie = tester.calculate_entropy(password)
            strength = tester.determine_strength(entropie)
            
            print(f"Entropie : {entropie:.2f} bits")
            print(f"Force : {strength}\n")
        
        elif choice == "3":
            # Génération de passphrase
            print("\n--- Génération de passphrase ---")
            num_words = int(input("Nombre de mots dans la passphrase : "))
            passphrase_gen = PassphraseGenerator()
            passphrase = passphrase_gen.generate_passphrase(num_words)
            
            print(f"Passphrase générée : {passphrase}\n")
        
        elif choice == "4":
            # Quitter le programme
            print("Au revoir !")
            break
        
        else:
            # Gestion des choix invalides
            print("Choix invalide, veuillez réessayer.\n")

if __name__ == "__main__":
    main()
