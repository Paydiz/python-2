# Projet Générateur et Testeur de Mots de Passe

Ce projet est un outil pour gérer des mots de passe sécurisés. Il inclut les fonctionnalités suivantes :
- Génération de mots de passe aléatoires en fonction de critères définis par l'utilisateur.
- Test de la force d'un mot de passe en fonction de son entropie.
- Génération de passphrases sécurisées basées sur la méthode Diceware.


## Fonctionnalités principales

1. Génération de mots de passe :
   - Vous pouvez définir le nombre de lettres majuscules, minuscules, chiffres, et caractères spéciaux.
   - Le programme génère un mot de passe aléatoire respectant vos critères.
   - Il calcule et affiche également l'entropie et la force du mot de passe.

2. Test de la force d'un mot de passe :
   - Entrez un mot de passe existant pour connaître son entropie (en bits).
   - Le programme indique si la force du mot de passe est "Très faible", "Faible", "Moyenne", "Forte", ou "Très forte".

3. Génération de passphrases :
   - Chaque mot de la passphrase est généré à partir d'un lancer simulé de dés.
   - Vous pouvez définir le nombre de mots dans la passphrase.


## Organisation des fichiers

- main.py : Point d'entrée du programme, gère les interactions avec l'utilisateur.
- generateur_mdp.py : Classe pour générer des mots de passe et calculer leur entropie.
- testeur_mdp.py : Classe pour tester la force d'un mot de passe.
- generateur_passphrase.py : Classe pour générer des passphrases sécurisées.
- testeur_unitaire.py : Tests unitaires pour valider les fonctionnalités du programme.


## Instructions pour exécuter le programme

1. Clonez le projet depuis GitLab ou placez les fichiers dans un même répertoire.
2. Lancez le programme avec la commande suivante :
   python3 main.py

