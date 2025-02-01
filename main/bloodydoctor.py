from minigames.crossword import CrosswordPuzzle


class Player:
    def __init__(self, name, xp, level, hearts):
        self.name = name
        self.xp = xp
        self.level = level
        self.hearts = hearts
        
    def printStatus(self):
        print(f'Hearts = {self.hearts}')
        print(f'Level = {self.level}')
        print(f'XP = {self.xp}')

    # convert player data to json to save progress
    def to_dict(self):
        pass
    # convert saved json file to object
    def from_dict(self):
        pass
    
class Patient:
    # Instantiating object
    def __init__(self, name, age, condition, blood_type, allergy, isRevealedAge = False, isRevealedCondition = False, isRevealedBloodType = False, isRevealedAllergy = False):
        self.name = name
        self.age = age
        self.condition = condition
        self.blood_type = blood_type
        self.allergy = allergy    
        
        # Keep track of infos that have been revealed to player
        self.isRevealed = {
        'age' : isRevealedAge,
        'condition' : isRevealedCondition,
        'blood_type' : isRevealedBloodType,
        'allergy' : isRevealedAllergy
        }

    # convert patient's state to json
    def to_dict(self):
        pass
    # convert saved json file to object
    def from_dict(self):
        pass

    # Print patient's profile
    def printProfile(self):
        print(self.name)
        print(f'Age : {self.age if self.isRevealed['age'] else '?????????'}')
        print(f'Condition : {self.condition if self.isRevealed['condition'] else '?????????'}')
        print(f'Blood type : {self.blood_type if self.isRevealed['blood_type'] else '?????????'}')
        print(f'Allergy : {self.allergy if self.isRevealed['allergy'] else '?????????'}')

class Quiz:
    def __init__(self, questionSet, xp):
        self.questionSet = questionSet
        self.xp = xp

    # Print question and answer choices
    def printQuiz(self, n):
        answerChoices = self.questionSet[n]['answerChoices']
        
        # Print question
        print(self.questionSet[n]['question'])
        
        # Print answer choices
        for i, answer in enumerate(answerChoices):
            print(f'{Quiz.intToLetter(i)}. {answer}')
        
    def getHint(self, n):
        return self.questionSet[n]['hint']
        
    def checkAnswer(self, n, answer):
        if answer.lower() == self.questionSet[n]['answer'].lower():
            return True
        else:
            return False

    # Method to return corresponding letter to an integer. 
    @staticmethod
    def intToLetter(i):
        letters = ['A', 'B', 'C', 'D']
        
        return letters[i]

class Game:
    games = ['Word search', 'Crossword', 'TicTacToe']
    def printGameOptions():
        print(Game.games)

    def executeGame(game):
        pass

# Function to print intro
def printIntro(name):
    print(f'''
Hurry, Dr. {name}! 
The hospital is bustling with patients. 
You currently have 5 patients under your care.
Treat your patients by answering questions related to them.
You can play minigames to acquire hint that will help you answer the question.
Answering correctly will gain you XP that will help you level up!
However, if you answer the question wrong, 1 heart will be deducted from your 5 hearts.
Reaching zero hearts will kill your patient.
Here comes your first patient~
''')

# Function to print course and students info
def printInfo():
    print("""
# ***********************************************************************************************************************************************************************
# Program: bloodydoctor.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC4L
# Trimester: 2430
# Names: ALEESSA BATRISYIA BINTI AZWAN | NUR ALYA IMAN BINTI MOHD PAZLI YUSOF | NUR DAMIA' BATRISYIA BINTI MOHAMMAD DENEE ROSDI | QAISARAH BINTI SHAMSUL AZRAN
# IDs: 
# Emails: 
# ************************************************************************************************************************************************************************  
    """)
    


# Create Patient instances   
patient1 = Patient('Moana binti Drake', 12, 'Anaemic', 'A', 'peanut butter')
patient2 = Patient('Jaehyun bin Jamal', 27, 'Iron deficiency', 'B', 'Roses')
patient3 = Patient('Baby Boss', 1, 'Fell from bed', 'O', 'Eggs')
patient4 = Patient('Suka binti Dessert', 45, 'Diabetes', 'B', 'None')
patient5 = Patient('Bob', 60, 'Backache', 'AB', 'None')
            
patients = [patient1, patient2, patient3, patient4, patient5]

# Quiz section
questionSet1 = [
    {
        'question' : "What is your patient's age?",
        'answer' : 'A',
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    },
    {
        'question' : "What illness does your patient have?",
        'answer' : 'C',
        'answerChoices' : ['Diabetes', 'Heart attack', 'Anaemic', 'Heat stroke'],
        'hint' : 'She lacks red'
    },
    {
        'question' : "What is your patient's age?",
        'answer' : 'A',
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    },
    {
        'question' : "What is your patient's age?",
        'answer' : 'A',
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    },
    {
        'question' : "What is your patient's age?",
        'answer' : 'A',
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    }
]
questionSet2 = [
    {
        'question' : "What is your patient's age?",
        'answer' : 12,
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    }
]
questionSet3 = [
    {
        'question' : "What is your patient's age?",
        'answer' : 12,
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    }
]
questionSet4 = [
    {
        'question' : "What is your patient's age?",
        'answer' : 12,
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    }
]
questionSet5 = [
    {
        'question' : "What is your patient's age?",
        'answer' : 12,
        'answerChoices' : [12, 30, 50, 100],
        'hint' : 'Kids this age usually start going through puberty.'
    }
]
    
quiz1 = Quiz(questionSet1, 10)

# Print students info
printInfo()


# GAME STARTS

# Get player's name and create player instance
name = input("Hi there! Mind telling us your name? : ").capitalize()
player = Player(name, 0, 1, 5)

printIntro(player.name) # INTRO

patient1.printProfile() # Print patient's profile

for i in questionSet1:
    
    quiz1.printQuiz(i)
    
    hint = input("Would you like to play minigame and get a hint?[y/n] : ")
    
    if hint == "y":
        print(quiz1.getHint(i))
        # Execute minigames

    answer = input("Answer : ")
    if quiz1.checkAnswer(i, answer):
        print("Correct!")
        player.xp += quiz1.xp
    else:
        print("Incorrect.. don't you know your own patient?")
        player.hearts -= 1

    
    
player.printStatus()