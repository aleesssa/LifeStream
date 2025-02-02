import random
from minigames.crossword import CrosswordPuzzle
from minigames.tictactoe import tictactoe
from minigames.wordsearch import WordSearchV2


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

    def xpToLevelUp(self):   
        xpToLevelUp = {
        1 : 50,
        2 : 125,
        3 : 225,
        4 : 350,
        5 : 500
         }
        return xpToLevelUp[self.level]

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
            intToLetter = lambda x: chr(ord("A") + i) # Convert int to letter for MCQ
            print(f'{intToLetter(i)}. {answer}')
        
    # def randomizeChoices(self, n):
    #     # randomize choices position 
    #     randomizedChoices = random.choices(self.questionSet[n]['answerChoices'])
        
    #     pass
        
    def getHint(self, n):
        return self.questionSet[n]['hint']
        
    def checkAnswer(self, n, answer):
        if answer.lower() == self.questionSet[n]['answer'].lower():
            return True
        else:
            return False
    
    def revealInfo(self, patient, index):
        patient.isRevealed[self.questionSet[index]['revealedInfo']] = True
        
    # choose question randomly
    def randomize(self):
        return random.randint(0, len(self.questionSet) - 1)

class Game:
    games = ['Word search', 'Crossword', 'TicTacToe']
    
    # Display game options
    @classmethod
    def printGameOptions(cls):
        for i, game in enumerate(cls.games):
            print(f'{i+1}. {game}')

    # Execute game based on user's input
    @classmethod
    def executeGame(cls, index):
        if 0 <= index <= len(cls.games):
            print(f'Playing {cls.games[index-1]}')
        else:
            print('Invalid choice.')
            
            
        if index == 1:
            WordSearchV2.execute()
        if index == 2:
            CrosswordPuzzle.execute()
        if index == 3:
            tictactoe.play_game()

# Function for each level
def startLevel(patient, quiz):
    patient.printProfile() # Print patient's profile

    # Loop through quiz set 1
    while len(quiz.questionSet) > 0: #makes sure player answers all the question correctly before proceeding to next patient
        index = quiz.randomize() # Choose random question from question set
        
        # Display question to player
        quiz.printQuiz(index)
        
        hint = input("Would you like to play minigame and get a hint?[y/n] : ")
        
        if hint == "y":
            Game.printGameOptions()
            index = int(input(f'Choose the minigame you would like to play![1 - {len(Game.games)}] :'))
            Game.executeGame(index)
            quiz.printQuiz(index)
            
        answer = input("Answer : ")
        if quiz.checkAnswer(index, answer):
            print("Correct!")
            quiz.revealInfo(patient1, index) # Reveal patient's info according to the question answered
            quiz.questionSet.pop(index) # Remove question from the list
            player.xp += quiz.xp
        else:
            print("Incorrect.. don't you know your own patient?")
            player.hearts -= 1
            print(f'You currently have {player.hearts} hearts')

        
        if player.xp >= player.xpToLevelUp():
            player.level += 1
            print("You've leveled up!")
    
        
        if player.hearts <= 0:
            lose()
            
            
        patient.printProfile()
        
# Execute when player loses (10 Hearts gone)
def lose():
    print("Your patient is dead. You should've paid more attention.")
    exit()

# Function to print intro
def printIntro(name):
    print(f'''
Hurry, Dr. {name}! 
The hospital is bustling with patients. 
You currently have 5 patients under your care.
Treat your patients by answering questions related to them.
You can play minigames to acquire hint that will help you answer the question.
Answering correctly will gain you XP that will help you level up!
However, if you answer the question wrong, 1 heart will be deducted from your 10 hearts.
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
        'answerChoices' : [12, 30, 50, 100],
        'answer' : 'A',
        'revealedInfo' : 'age',
        'hint' : 'Kids this age usually start going through puberty.'
    },
    {
        'question' : "What illness does your patient have?",
        'answerChoices' : ['Diabetes', 'Heart attack', 'Anaemic', 'Heat stroke'],
        'answer' : 'C',
        'revealedInfo' : 'condition',
        'hint' : 'She lacks red'
    },
    {
        'question' : "What is your patient's blood type?",
        'answer' : 'B',
        'answerChoices' : ['B', 'A', 'AB', 'O'],
        'revealedInfo' : 'blood_type',
        'hint' : 'This blood type is rare. Only 6% of population has it.'
    },
    {
        'question' : "Does your patient have any allergy?",
        'answer' : 'A',
        'answerChoices' : ['Peanut butter', 'Seafood', 'Dust', 'None'],
        'revealedInfo' : 'allergy',
        'hint' : 'Sweet.'
    },
    {
        'question' : "What is your patient's age?",
        'answer' : 'A',
        'answerChoices' : [12, 30, 50, 100],
        'revealedInfo' : 'age',
        'hint' : 'Kids this age usually start going through puberty.'
    }
]
questionSet2 = [
    {
        'question' : "What is your patient's age?",
        'answer' : 'A',
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
    
quiz1 = Quiz(questionSet1, xp=10)
quiz2 = Quiz(questionSet2, xp=15)
quiz3 = Quiz(questionSet3, xp=20)
quiz4 = Quiz(questionSet4, xp=25)
quiz5 = Quiz(questionSet5, xp=30)

# Print students info
printInfo()


# GAME STARTS

# Get player's name and create player instance
name = input("Hi there! Mind telling us your name? : ").capitalize()
player = Player(name, xp=0, level=1, hearts=10)
printIntro(player.name) # INTRO

# Start level 1
startLevel(patient1, quiz1)

# Start level 2
startLevel(patient2, quiz2)
        
# Start level 3
startLevel(patient3, quiz3)

# Start level 4
startLevel(patient4, quiz4)
    
# Start level 5
startLevel(patient5, quiz5)


player.printStatus()