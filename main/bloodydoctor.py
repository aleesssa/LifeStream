hearts = 5
xp = 0
level = 0

# Patient(name, age, condition, blood_type, allergy)
class Patient:

    # Instantiating object
    def __init__(self, name, age, condition, blood_type, allergy):
        self.name = name
        self.age = age
        self.condition = condition
        self.blood_type = blood_type
        self.allergy = allergy    
        
        # Keep track of infos that have been revealed to player
        self.isRevealed = {
        'age' : False,
        'condition' : False,
        'blood_type' : False,
        'allergy' : False
        }

    # Print patient's profile
    def printProfile(self):
        print(self.name)
        print(f'Age : {self.age if self.isRevealed['age'] else '?????????'}')
        print(f'Condition : {self.condition if self.isRevealed['condition'] else '?????????'}')
        print(f'Blood type : {self.blood_type if self.isRevealed['blood_type'] else '?????????'}')
        print(f'allergy : {self.allergy if self.isRevealed['allergy'] else '?????????'}')

  
patient1 = Patient('Moana binti Drake', 12, 'Anaemic', 'A', 'peanut butter')
patient2 = Patient('Jaehyun bin Jamal', 27, 'Iron deficiency', 'B', 'Roses')
patient3 = Patient('Baby Boss', 1, 'Fell from bed', 'O', 'Eggs')
patient4 = Patient('Suka binti Dessert', 45, 'Diabetes', 'B', 'None')
patient5 = Patient('Bob', 60, 'Backache', 'AB', 'None')
            
patients = [patient1, patient2, patient3, patient4, patient5]
for patient in patients:
    patient.printProfile()
    print('*************************************************************')

# Quiz(question, answer, hint, exp) 

# INFO
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
