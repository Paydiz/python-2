from generateur_mdp import GenerateurDeMotDePasse
from testeur_mdp import TesteurDeMotDePasse
from generateur_passphrase import GenerateurDePassphrase

def main():
    print("Bienvenue dans l'outil de génération et de test de mots de passe !\n")
    
    while True:
        print("Choisissez une option :")
        print("1. Générer un mot de passe")
        print("2. Tester la force d’un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")
        
        choix = input("Votre choix : ").strip()
        
        if choix == "1":
            # Génération de mot de passe
            print("\n--- Génération de mot de passe ---")
            nb_min = int(input("Nombre de caractères minuscules : "))
            nb_maj = int(input("Nombre de caractères majuscules : "))
            nb_chiffres = int(input("Nombre de chiffres : "))
            nb_speciaux = int(input("Nombre de caractères spéciaux : "))
            
            generateur = GenerateurDeMotDePasse()  # Création d'une instance de GenerateurDeMotDePasse
            mot_de_passe = generateur.generer_mot_de_passe(nb_min, nb_maj, nb_chiffres, nb_speciaux)  # Génération du mot de passe
            entropie = generateur.calculer_entropie(mot_de_passe)  # Calcul de l'entropie
            force = TesteurDeMotDePasse.determiner_force(entropie)  # Détermination de la force du mot de passe
            
            print(f"Mot de passe généré : {mot_de_passe}")
            print(f"Entropie : {entropie:.2f} bits")
            print(f"Force : {force}\n")
        
        elif choix == "2":
            # Test de la force d'un mot de passe
            print("\n--- Test de force de mot de passe ---")
            mot_de_passe = input("Entrez le mot de passe à tester : ")
            testeur = TesteurDeMotDePasse()
            entropie = testeur.calculer_entropie(mot_de_passe)  # Calcul de l'entropie
            force = testeur.determiner_force(entropie)  # Détermination de la force
            
            print(f"Entropie : {entropie:.2f} bits")
            print(f"Force : {force}\n")
        
        elif choix == "3":
            # Génération de passphrase
            print("\n--- Génération de passphrase ---")
            nb_mots = int(input("Nombre de mots dans la passphrase : "))
            generateur_phrase = GenerateurDePassphrase()
            passphrase = generateur_phrase.generer_passphrase(nb_mots)
            
            print(f"Passphrase générée : {passphrase}\n")
        
        elif choix == "4":
            # Quitter le programme
            print("Au revoir !")
            break
        
        else:
            # Gestion des choix invalides
            print("Choix invalide, veuillez réessayer.\n")

if __name__ == "__main__":
    main()
