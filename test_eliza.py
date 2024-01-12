from el2 import*

class TestEliza:
    def __init__(self, eliza_instance, output_file):
        self.eliza = eliza_instance
        self.output_file = output_file
        # Liste des phrases de test en anglais
        self.test_phrases = [
            "Hello Eliza",
            "I am feeling sad today",
            "Let's talk about my family",
            "I have problems at work",
            "I am worried about my future",
            "I often argue with my friends",
            "I can't sleep at night",
            "I often think about school",
            "I feel lonely",
            "I am afraid of failure",
            "I don't know what to do with my life",
            "Sometimes, I feel depressed",
            "I am happy to be here",
            "I am stressed about my exams",
            "I argue with my parents",
            "I get nervous when speaking in public",
            "I think too much about what others think of me",
            "I often feel anxious",
            "What should I do now?",
            "I lack self-confidence",
            "I find it hard to be patient when waiting for results.",
            "How can I learn to be more patient with my team?",
            "I want to be more productive during my workday.",
            "How can I stop procrastinating and be more productive?",
            " I am confused about aced",
            "Sometimes life feels overwhelming."
"I often question my life choices.",
"Dealing with uncertainty is a constant struggle.",
"I feel disconnected from my friends and family.",
"Navigating through daily challenges is tough.",
"I worry about what the future holds.",
"Finding a balance in life seems impossible.",
"I am constantly second-guessing myself.","Stress has become a regular part of life.",
"I struggle to find meaning in my work.",
"It's difficult to stay optimistic.",
"I am often plagued by self-doubt.",
"Facing new challenges is always daunting.",
"I feel like I'm stuck in a rut.",
"It's hard to be confident in decision-making.",
"I am not sure how to handle my emotions.",
"Feeling underappreciated is disheartening.",
"I have difficulty coping with change.",
"Achieving personal goals feels out of reach.",
"I am afraid of being left behind.",
"Struggling with self-esteem is a daily battle.",
"I am not sure where my career is heading.",
"Life's pressures seem to be mounting.",
"I feel like I'm always under stress.",
"Finding time for self-care is challenging.",

        ]

    def run_tests(self):
        with open(self.output_file, 'w') as file:
            for phrase in self.test_phrases:
                response = self.eliza.respond(phrase)
                file.write(f"Phrase: {phrase}\nRéponse d'Eliza: {response}\n\n")



# Assurez-vous que votre instance d'Eliza est correctement initialisée ici
eliza_instance = Eliza()
eliza_instance.load('doctor.txt')  # Ou 'doctorbis.txt'

# Nom du fichier de sortie pour les résultats des tests
output_file = "eliza_test_results.txt"

# Créer une instance de TestEliza et exécuter les tests
test_eliza = TestEliza(eliza_instance, output_file)
test_eliza.run_tests()
