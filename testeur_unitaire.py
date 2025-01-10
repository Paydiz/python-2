import unittest
from generateur_mdp import GenerateurDeMotDePasse
from testeur_mdp import TesteurDeMotDePasse

# Classe de tests unitaires pour valider les fonctionnalités de génération et de test de mot de passe
class TestUnitaire(unittest.TestCase):
        # Test pour vérifier que l'entropie d'un mot de passe généré est toujours positive
    def test_entropie_mot_de_passe(self):
                # Générer un mot de passe avec des paramètres spécifiques
        generateur = GenerateurDeMotDePasse()
        mot_de_passe = generateur.generer_mot_de_passe(2, 2, 2, 2)
        entropie = generateur.calculer_entropie(mot_de_passe)
        self.assertGreater(entropie, 0)

    # Test pour vérifier que la force d'un mot de passe est correctement déterminée
    def test_force_mot_de_passe(self):
        self.assertEqual(TesteurDeMotDePasse.determiner_force(20), "Très faible")
        self.assertEqual(TesteurDeMotDePasse.determiner_force(50), "Moyenne")

# Point d'entrée pour exécuter les tests unitaires
if __name__ == "__main__":
    unittest.main()
