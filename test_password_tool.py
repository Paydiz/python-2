import unittest
from password_generator import PasswordGenerator
from password_tester import PasswordTester

# Classe de tests unitaires pour valider les fonctionnalités de génération et de test de mot de passe
class TestPasswordTool(unittest.TestCase):
    # Test pour vérifier que l'entropie d'un mot de passe généré est toujours positive
    def test_password_entropy(self):
        # Générer un mot de passe avec des paramètres spécifiques
        generator = PasswordGenerator()
        password = generator.generate_password(2, 2, 2, 2)
        entropy = generator.calculate_entropy(password)
        self.assertGreater(entropy, 0)

# Test pour vérifier que la force d'un mot de passe est correctement déterminée
    def test_password_strength(self):
        self.assertEqual(PasswordTester.determine_strength(20), "Très faible")
        self.assertEqual(PasswordTester.determine_strength(50), "Moyenne")

# Point d'entrée pour exécuter les tests unitaires
if __name__ == "__main__":
    unittest.main()
