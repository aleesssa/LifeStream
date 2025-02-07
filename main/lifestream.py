import os
import json
import random
import time

from rich.console import Console
from rich.console import group
from rich.table import Table
from rich.panel import Panel
from rich.text import Text


from minigames import CrosswordPuzzle
from minigames import tictactoe
from minigames import WordSearchV2
from minigames import SpeedQuiz
from minigames import scrambleword
from minigames import Decryptify
from minigames import rps

class Player:
    def __init__(self, name, level, xp, hearts):
        self.name = name
        self.level = level
        self.xp = xp
        self.hearts = hearts
        
    def printStatus(self):
        print(f'Hearts = {self.hearts}')
        print(f'Level = {self.level}')
        print(f'XP = {self.xp}')
        
    # Print patient's profile
    @group()
    def playerStatus(self):
        yield Panel(f'Level : {self.level}')
        yield Panel(f'XP : {self.xp}')
        yield Panel(f'Hearts : {self.hearts}')

    def printStatus(self):
        console.print(Panel(self.playerStatus(), title=self.name), justify='left', width=90)
        time.sleep(1)    

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
        return player.__dict__
    
    # convert saved json file to object
    @staticmethod
    def from_dict(player):
        name = player['name']
        level = player['level']
        xp = player['xp']
        hearts = player['hearts']
        return Player(name, level, xp, hearts)
    
class Patient:
    # Instantiating object
    def __init__(self, name, age, condition, symptom, blood_type, allergy, isRevealedAge = True, isRevealedCondition = False, isRevealedSymptom = False, isRevealedBloodType = False, isRevealedAllergy = False):
        self.name = name
        self.age = age
        self.condition = condition
        self.symptom = symptom
        self.blood_type = blood_type
        self.allergy = allergy    
        
        # Keep track of infos that have been revealed to player
        self.isRevealed = {
        'age' : isRevealedAge,
        'condition' : isRevealedCondition,
        'symptom' : isRevealedSymptom,
        'blood_type' : isRevealedBloodType,
        'allergy' : isRevealedAllergy
        }

    # return state of info(revealed or not) to be saved
    def to_dict(self):
        return self.__dict__
        
    # convert saved json file to object
    @staticmethod
    def from_dict(patient):
        name = patient['name']
        age = patient['age']
        condition = patient['condition']
        symptom = patient['symptom']
        blood_type = patient['blood_type']
        allergy = patient['allergy']
        isRevealed = patient['isRevealed']
        
        patient = Patient(name, age, condition, symptom, blood_type, allergy, isRevealed['age'], isRevealed['condition'], isRevealed['symptom'], isRevealed['blood_type'], isRevealed['allergy'])
        
        return patient
        
    # Print patient's profile
    @group()
    def patientProfile(self):
        yield Panel(f'Age : {self.age if self.isRevealed['age'] else '?????????'}')
        yield Panel(f'Condition : {self.condition if self.isRevealed['condition'] else '?????????'}')
        yield Panel(f'Symptom : {self.symptom if self.isRevealed['symptom'] else '?????????'}')
        yield Panel(f'Blood type : {self.blood_type if self.isRevealed['blood_type'] else '?????????'}')
        yield Panel(f'Allergy : {self.allergy if self.isRevealed['allergy'] else '?????????'}')

    def printProfile(self):
        console.print(Panel(self.patientProfile(), title=self.name), justify='left', width=90)
        time.sleep(1)

class Quiz:
    def __init__(self, questionSet, xp):
        self.questionSet = questionSet
        self.xp = xp

    # Print question and answer choices
    def printQuiz(self, n):
        answerChoices = self.questionSet[n]['answerChoices']
        
        # Print question
        print(self.questionSet[n]['question'])
        time.sleep(0.5)
        
        # Print answer choices
        for i, answer in enumerate(answerChoices):
            intToLetter = lambda x: chr(ord("A") + x) # Convert int to letter for MCQ
            print(f'{intToLetter(i)}. {answer}')
            time.sleep(0.5)
            
        print('\n')
        
        
    def getHint(self, n):
        return self.questionSet[n]['hint']
    
    @staticmethod
    def inputAnswer():
        answer = console.input('Enter your answer : ').lower()
        while answer not in ['a', 'b', 'c', 'd']:
            answer = console.input('Enter your answer [bold][A, B, C, D][/] : ').lower()
            
        return answer
        
    def checkAnswer(self, n, answer):
        if answer == self.questionSet[n]['answer'].lower():
            return True
        else:
            return False
    
    def revealInfo(self, patient, index):
        patient.isRevealed[self.questionSet[index]['revealedInfo']] = True        

    # choose question randomly
    def randomize(self):
        return random.randint(0, len(self.questionSet) - 1)

    # Return Quiz dict to be saved in a json file
    def to_dict(self):
        return self.__dict__

    # From dict to instance
    @staticmethod
    def from_dict(quiz):
        questionSet = quiz['questionSet']
        xp = quiz['xp']
        
        return Quiz(questionSet, xp)

class Game:
    games = ['Word search', 'Crossword', 'TicTacToe', 'Speed Quiz', 'Scramble Word', 'Decryptify', 'Rock, Paper, Scissor']
    
    # Display game options
    @classmethod
    def printGameOptions(cls):
        for i, game in enumerate(cls.games):
            print(f'{i+1}. {game}')

    # Execute game based on user's input
    @classmethod
    def executeGame(cls, index):
        win = False
        if index == 1:
            win = WordSearchV2.wsExecute()
        if index == 2:
            win = CrosswordPuzzle.cpExecute()
        if index == 3:
            win = tictactoe.play_game()
        if index == 4:
            win = SpeedQuiz.sqExecute()
        if index == 5:
            win = scrambleword.play_game()
        if index == 6:
            win = Decryptify.dExecute()
        if index == 7:
            win = rps.play_game()
            
        return win
            
    @staticmethod
    def saveGame(player, patients, quizzes):
        # Save player and patient data to their respective json files
        with open('player.json', 'w') as playerFile:
            json.dump(player.to_dict(), playerFile, indent = 4)
            
        # Save patient info to patients.json
        patients = [patient.to_dict() for patient in patients]        
        with open('patients.json', 'w') as patientFile:
            json.dump(patients, patientFile, indent = 4)
            
        # Save quizzes to quizzes.json
        quizzes = [quiz.to_dict() for quiz in quizzes] 
        with open('quizzes.json', 'w') as quizFile:
            json.dump(quizzes, quizFile, indent = 4)    

    # Load json files as python dictionaries and create player instance
    @staticmethod
    def loadPlayer():
        with open('player.json', 'r') as playerFile:
            playerData = json.load(playerFile) 
            player = Player.from_dict(playerData) # Player instance created from loaded dictionary
        return player    

    @staticmethod
    def loadPatient(n):
        with open('patients.json', 'r') as patientFile:
            patientData = json.load(patientFile)
            patient = Patient.from_dict(patientData[n])
            
        return patient
    
    @staticmethod
    def loadQuiz(n):
        with open('quizzes.json', 'r') as quizFile:
            quizData = json.load(quizFile)
            quiz = Quiz.from_dict(quizData[n])
            
        return quiz
    
# Validate user's inputs
def inputYesNo(string):
    user_input = console.input(f"{string} Enter [green bold]Yes[/] or [red bold]No[/] (or [green bold]y[/]/[red bold]n[/]): ").lower()

    while user_input not in ['yes', 'no', 'y', 'n']:
        user_input = console.input(f"{string} Please enter 'yes', 'no', 'y', or 'n': ").lower()

    if user_input in ['yes', 'y']:
        return True
    elif user_input in ['no', 'n']:
        return False
    
def inputInt(string, n):
    while True:
        try:
            user_input = int(input(f"{string} Please enter a number from 1 - {n}: "))
            if user_input < 1 or user_input > n:
                print(f'Number out of range! Please enter a number from 1 to {n}')
            else:
                return user_input
                
        except ValueError:
            console.print("Please enter an integer! :warning:")
            continue

    
# Function for each level
def startLevel(patient, quiz):


    # Loop through quiz set 1
    while len(quiz.questionSet) > 0: #makes sure player answers all the question correctly before proceeding to next patient
        patient.printProfile() # Print patient's profile
        question_index = 0
        
        # Display question to player
        quiz.printQuiz(question_index)
        
        # Give user option to gain hint
        hint = inputYesNo("Would you like to play minigame and get a hint? ")
        
        # If user wants hint
        if hint:
            Game.printGameOptions() # Display minigames options
            index = inputInt('Choose the minigame you would like to play!', len(Game.games)) # Get input for which minigame to play
            win = Game.executeGame(index) # Execute minigame and get boolean (True for win and False for lose)
            if win:
                time.sleep(1)
                console.print(f'\n[blue]Here\'s your hint![/]:bulb: [bold]{quiz.questionSet[0]['hint']}[/]\n') # Print hint
            else:
                time.sleep(1)
                console.print("[red]You won't be getting any hints..[/]")
                time.sleep(1)
                continue
            
            patient.printProfile()
            quiz.printQuiz(question_index)
            
        answer = Quiz.inputAnswer()
        if quiz.checkAnswer(question_index, answer):
            time.sleep(1)
            print("\nCorrect!\n")
            time.sleep(1)
            quiz.revealInfo(patient, question_index) # Reveal patient's info according to the question answered
            quiz.questionSet.pop(question_index) # Remove question from the list
            player.xp += quiz.xp
        else:
            console.print("\n[bold red]Incorrect..[/] don't you know your own patient?\n")
            time.sleep(1)
            player.hearts -= 1
            console.print(f'You currently have [bold red]{player.hearts} hearts[/]\n\n')        
            if player.hearts <= 0:
                lose()
                
            continue
        

            
        console.print("Moving on to the next question...\n")
        time.sleep(1)

            
        
# Execute when player loses (10 Hearts gone)
def lose():
    print("\nYour patient is [blood]dead[/]. You should've paid more attention :wilted_flower:")
    exit()

# Function to print intro
@group()
def introPanel(name):
    yield Text(f'Hurry, Dr. {name}!')
    yield Text('The hospital is bustling with patients. ')
    yield Text('You currently have 5 patients under your care.')
    yield Text('Treat your patients by answering questions related to them.')
    yield Text('You can play minigames to acquire hint that will help you answer the question.')
    yield Text('Answering correctly will gain you XP that will help you level up!')
    yield Text('However, if you answer the question wrong, 1 heart will be deducted from your 10 hearts.')
    yield Text('Reaching zero hearts will kill your patient.')
    yield Text('Here comes your first patient~')
    

def printIntro(name):
    console.print(Panel(introPanel(name), title='GAME RULE'), justify='left', width=90)
    print('\n')
    time.sleep(1)
    
    
# Function to print course and students info
def printInfo():
        
    tableInfo = Table(show_header=False, show_lines=True)
    tableInfo.add_column("Attribute")
    tableInfo.add_column("Value")
    
    tableInfo.add_row('[bold]PROGRAM[/]', 'lifestream.py')
    tableInfo.add_row('[bold]COURSE[/]', 'CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN')
    tableInfo.add_row('[bold]LECTURE / LAB SECTION[/]', 'TC4L')
    tableInfo.add_row('[bold]TRIMESTER[/]', '2430')
    
    
    tableStudents = Table(title="STUDENTS' INFO", show_lines=True)

    tableStudents.add_column("NAME", justify="center", style="cyan", no_wrap=False)
    tableStudents.add_column("STUDENT ID", style="magenta")
    tableStudents.add_column("EMAIL", justify="center", style="green")

    tableStudents.add_row("ALEESSA BATRISYIA BINTI AZWAN", "242FC243DD", "ALEESSA.BATRISYIA.AZWAN@student.mmu.edu.my")
    tableStudents.add_row("NUR ALYA IMAN BINTI MOHD PAZLI YUSOF", "242FC24352", "NUR.ALYA.IMAN@student.mmu.edu.my")
    tableStudents.add_row("NUR DAMIA' BATRISYIA BINTI MOHAMMAD DENEE ROSDI", "242FC243Y5", "NUR.DAMIA.BATRISYIA@student.mmu.edu.my")
    tableStudents.add_row("QAISARAH BINTI SHAMSUL AZRAN", "242FC243DY", "QAISARAH.SHAMSUL.AZRAN@student.mmu.edu.my")

    console.print(tableInfo)
    time.sleep(1)
    console.print(tableStudents)
    time.sleep(1)
    print('\n')
    
    console.rule()
    
    time.sleep(1)
    print('\n')

# Quiz section
questionSet1 = [
    {
        'question' : "How old is your patient?",
        'answerChoices' : [12, 30, 50, 100],
        'answer' : 'A',
        'revealedInfo' : 'age',
        'hint' : 'Kids this age usually start going through puberty.'
    },
    {
        'question' : "What condition does your patient have?",
        'answerChoices' : ['Diabetes', 'Heart attack', 'Anaemic', 'Heat stroke'],
        'answer' : 'C',
        'revealedInfo' : 'condition',
        'hint' : 'She lacks red'
    },
    {
        'question' : "What is your patient's blood type?",
        'answer' : 'C',
        'answerChoices' : ['B+', 'A-', 'AB-', 'O+'],
        'revealedInfo' : 'blood_type',
        'hint' : 'The rarest blood type.'
    },
    {
        'question' : "Does your patient have any allergy?",
        'answer' : 'A',
        'answerChoices' : ['Peanut butter', 'Seafood', 'Dust', 'None'],
        'revealedInfo' : 'allergy',
        'hint' : 'Sweet.'
    },
    {
        'question' : "What symptom does the patient primarily show?",
        'answer' : 'D',
        'answerChoices' : ['Swollen ankle', 'Irritated skin', 'High fever', 'Fatigue'],
        'revealedInfo' : 'symptom',
        'hint' : 'Tired.'
    }
]

questionSet2 = [
    {
        'question' : "What happened to Baby Boss?",
        'answer' : 'A',
        'answerChoices' : ['Fell off the bed', 'Choked on a food', 'Allergy reaction', 'Cried too much'],
        'revealedInfo' : 'condition',
        'hint' : 'Head concussion'
    },
    {
        'question' : "What symptom is the baby showing?",
        'answer' : 'B',
        'answerChoices' : ['Hyperactivity', 'Vomiting', 'Runny nose', 'High fever'],
        'revealedInfo' : 'symptom',
        'hint' : "Liquid"
    },
    {
        'question' : "From the symptom shown, what is the most immediate medical concern",
        'answer' : 'D',
        'answerChoices' : ['Fractured arm', 'Sprained ankle', 'Dehydration', 'Concussion'],
        'revealedInfo' : 'symptom',
        'hint' : ""
    },
    {
        'question' : "Who can donate blood to Baby Boss?",
        'answer' : 'B',
        'answerChoices' : ['A+ Donor', 'O- Donor', 'B- Donor', 'AB- Donor'],
        'revealedInfo' : 'blood_type',
        'hint' : 'Baby Boss has O+ type.'
    },
    {
        'question' : "Which food should you not feed to Baby Boss?",
        'answer' : 'C',
        'answerChoices' : ['A bowl of fresh fruit', 'A humidifier', 'A scented rose bouquet', 'A book and a cup of tea'],
        'revealedInfo' : 'condition',
        'hint' : 'Jaehyun enjoys nature but avoids certain flowers because they make him feel unwell.'
    }
]
questionSet3 = [
    {
        'question' : "Is Jaehyun eligible for blood donation?",
        'answer' : 'C',
        'answerChoices' : ['Yes, his condition does not affect his eligibility.', 'Yes, as long as he drinks enough water.' ,'No, he has low hemoglobin levels.', 'No, but taking iron supplements right before donation makes him eligible.'],
        'revealedInfo' : 'condition',
        'hint' : 'Jaehyun suffers from iron deficiency.'
    },
    {
        'question' : "Who can donate blood to Jaehyun?",
        'answer' : 'D',
        'answerChoices' : ['B+ donor', 'O+ donor', 'A- Donor', 'O- donor'],
        'revealedInfo' : 'blood_type',
        'hint' : "Jaehyun's blood type is B-"
    },
    {
        'question' : "What symptom does Jaehyun show?",
        'answer' : 'A',
        'answerChoices' : ['Pale skin.', 'High fever', 'Joint pain', 'Rash'],
        'revealedInfo' : 'symptom',
        'hint' : "This condition affects the body's ability to carry oxygen efficiently"
    },
    {
        'question' : "What is the best diet for Jaehyun",
        'answer' : 'B',
        'answerChoices' : ['Dairy products and white rice', 'Lean red meat and vitamin C-rich fruits', 'Fast food and sugary drinks', 'Seafood, whole grains and coffee'],
        'revealedInfo' : 'condition',
        'hint' : 'Jaehyun often feels tired and dizzy.'
    },
    {
        'question' : "As Jaehyun's doctor, what should you avoid placing in his hospital room?",
        'answer' : 'C',
        'answerChoices' : ['A bowl of fresh fruit', 'A humidifier', 'A scented rose bouquet', 'A book and a cup of tea'],
        'revealedInfo' : 'allergy',
        'hint' : 'Jaehyun enjoys nature but avoids certain flowers because they make him feel unwell.'
    }
]
questionSet4 = [
    {
        'question' : "How do you treat Sunghoon's condition?",
        'answer' : 'C',
        'answerChoices' : ['Administration of intravenous fluids and pain management', 'Antibiotic therapy', 'Surgical removal of the appendix', 'Adoption of a high-fiber diet and bed rest'],
        'revealedInfo' : 'condition',
        'hint' : "Sunghoon is facing acute appendicitis"
    },
    {
        'question' : "What causes Sunghoon's symptom?",
        'answer' : '',
        'answerChoices' : ['Physical blockage of the intestines', 'Inflammatory cytokine release', 'Excessive gastric acid secretion', 'Severe blood loss from the inflamed appendix'],
        'revealedInfo' : 'symptom',
        'hint' : "Sunghoon shows lack of appetite as the symptom"
    },
    {
        'question' : "Which is true about Sunghoon's blood type?",
        'answer' : '',
        'answerChoices' : ['They can donate red blood cells to patients of any blood type', 'They are universal recipients for red blood cell transfusions', 'Their plasma can be transfused to patients of all blood types', 'They can only receive red blood cells from O- donors.'],
        'revealedInfo' : 'blood_type',
        'hint' : 'Sunghoon has AB- blood type.'
    },
    {
        'question' : "What is the most appropriate diet for Sunghoon after appendix surgery?",
        'answer' : '',
        'answerChoices' : ['Plenty of fruits and vegetables', 'Clear liquids only, gradually advancing to soft foods', 'High-protein, low-carbohydrate diet', 'High-sugar diet for energy'],
        'revealedInfo' : 'condition',
        'hint' : 'After appendix surgery, patient needs foods that are balanced and easy to digest'
    },
    {
        'question' : "What is Sunghoon allergic to?",
        'answer' : '',
        'answerChoices' : ['Eggs', 'Peanut butter', 'Grapes', 'Nothing'],
        'revealedInfo' : 'allergy',
        'hint' : 'Sunghoon is not allergic to anything'
    }
]
questionSet5 = [
    {
        'question' : "Is Nisreen's conditionc contagious?",
        'answer' : 'C',
        'answerChoices' : ['Yes, it can spread through direct skin contact', 'No, it is not contagious', 'Yes, it is caused by bacteria and can be transmitted through the air', 'All of the above'],
        'revealedInfo' : 'condition',
        'hint' : "Nisreen has eczema"
    },
    {
        'question' : "What type of eczema does Nisreen have?",
        'answer' : 'A',
        'answerChoices' : ['Dyhrotic eczema', 'Atopic dermatitis', 'Contact dermatitis', 'Nummular Eczema'],
        'revealedInfo' : 'symptom',
        'hint' : "Nisreen has small, fluid-filled blisters on her hands"
    },
    {
        'question' : "In a scenario where Nisreen needs blood donation, which one of your previous patients is eligible and compatible to donate blood to Nisreen?",
        'answer' : 'E',
        'answerChoices' : ['Moana binti Drake', 'Baby Boss', 'Jaehyun bin Jamal', 'Sunghoon', 'None of the above'],
        'revealedInfo' : 'blood_type',
        'hint' : 'Nisreen has O- blood type.'
    },
    {
        'question' : "What is the best treatment for Nisreen?",
        'answer' : 'B',
        'answerChoices' : ['Scrubbing the blisters to remove dead skin and applying alcohol-based sanitizer', 'Applying a thick moisturizer, using mild steroid cream, and avoiding triggers', 'Popping the blisters to let the fluid drain and dry out the skin', 'Taking antibiotics immediately, even if there is no sign of infection'],
        'revealedInfo' : 'condition',
        'hint' : 'Treatments should focus on soothing the skin, reducing inflammation, and preventing infections'
    },
    {
        'question' : "Nisreen had an eczema flare up recently. What is the possible trigger for her flare up?",
        'answer' : 'C',
        'answerChoices' : ['Smoke', 'Pollen', 'Dust', 'Stress'],
        'revealedInfo' : 'allergy',
        'hint' : 'Nisreen was cleaning her fan the day before the flare up happened'
    }
]
    
# Create concole instance for rich
console = Console()
console.rule("[bold red]Life Stream")



# Print students info
printInfo()

# GAME STARTS

# Check for saved file
if os.path.exists('player.json'):
    loadFile = inputYesNo('Would you like to load your saved game?')
    
    if loadFile:
        console.print('\n[green]Loading saved game...[/]\n')
        time.sleep(2.5)
        
        # Create instances using saved data
        player = Game.loadPlayer()
        quizzes = []
        patients = []
        
        # Load patients and quizzes info and append instances to patients and quizzes list
        for i in range (player.level - 1, 5):
            patients.append(Game.loadPatient(i))
            quizzes.append(Game.loadQuiz(i))
 
        
        console.print(f'Welcome back, Dr. {player.name}! Ready to get back to work? Of course you are ! Let us continue!!!')
                
    else:       
        console.print('\n[green]Creating new game...[/]\n')
        time.sleep(2.5)
        
        # Create Patient instances using new data   
        patient1 = Patient('Moana binti Drake', 12, 'Anemia', 'Fatigue', 'AB-', 'peanut butter', isRevealedAge=False)
        patient2 = Patient('Baby Boss', 1, 'Head concussion', 'Vomiting', 'O+', 'Eggs')
        patient3 = Patient('Jaehyun bin Jamal', 27, 'Iron deficiency', 'Pale skin', 'B-', 'Roses')
        patient4 = Patient('Sunghoon', 45, 'Acute appendictitis', 'Lack of appetite', 'AB-', 'None')
        patient5 = Patient('Nisreen Athirah', 22, 'Eczema', 'Painful blisters on hands', 'O-', 'Dust')
        
        patients = [patient1, patient2, patient3, patient4, patient5]
        
        # Create Quiz instances using new data
        quiz1 = Quiz(questionSet1, xp=10)
        quiz2 = Quiz(questionSet2, xp=15)
        quiz3 = Quiz(questionSet3, xp=20)
        quiz4 = Quiz(questionSet4, xp=25)
        quiz5 = Quiz(questionSet5, xp=30)

        quizzes = [quiz1, quiz2,quiz3, quiz4, quiz5]
        
        # Get player's name and create player instance
        name = console.input("Hi there! Mind telling us your name? : ").capitalize()
        player = Player(name, xp=0, level=1, hearts=10)
        Game.saveGame(player, patients, quizzes)
        
        printIntro(player.name) # INTRO
else:
    # Create Patient instances using new data   
    patient1 = Patient('Moana binti Drake', 12, 'Anemia', 'Fatigue', 'AB-', 'peanut butter', isRevealedAge=False)
    patient2 = Patient('Baby Boss', 1, 'Head concussion', 'Vomiting', 'O+', 'Eggs')
    patient3 = Patient('Jaehyun bin Jamal', 27, 'Iron deficiency', 'Pale skin', 'B-', 'Roses')
    patient4 = Patient('Sunghoon', 45, 'Acute appendictitis', 'Lack of appetite', 'AB-', 'None')
    patient5 = Patient('Nisreen Athirah', 22, 'Eczema', 'Painful blisters on hands', 'O-', 'Dust')
    
    patients = [patient1, patient2, patient3, patient4, patient5]
    
    # Create Quiz instances using new data
    quiz1 = Quiz(questionSet1, xp=10)
    quiz2 = Quiz(questionSet2, xp=15)
    quiz3 = Quiz(questionSet3, xp=20)
    quiz4 = Quiz(questionSet4, xp=25)
    quiz5 = Quiz(questionSet5, xp=30)

    quizzes = [quiz1, quiz2,quiz3, quiz4, quiz5]
    
    # Get player's name and create player instance
    name = input("Hi there! Mind telling us your name? : ").title()
    player = Player(name, xp=0, level=1, hearts=10)
    printIntro(player.name) # INTRO

# Start level starting from current patient
for i in range(len(patients)):
    startLevel(patients[i], quizzes[i])   
         
    if player.xp >= player.xpToLevelUp():
        player.level += 1
        console.print("You've leveled up!")
        time.sleep(1.5)
        player.printStatus()
        time.sleep(1.5)
        console.print("Moving on to the next patient!")
    
    saveGame = inputYesNo('Would you like to save the game?')
    if saveGame:
        Game.saveGame(player, patients, quizzes)
    
    exitGame = inputYesNo('Would you like to exit the game?')
    if exitGame:
        console.print('[bold red]Exiting...[/]')
        time.sleep(2)
        exit()