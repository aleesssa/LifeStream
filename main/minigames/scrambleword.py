import random

print(" 🎮 Welcome to Word Scramble! 🎮 ".center(50,"*"))
print("\nHere are the instructions:")
print("\n1.You must complete all 3 levels:")
print("• Easy [Basic Word] \n• Intermediate [Moderate Difficulty] \n• Hard [Medical Terms]")
print("\n2.The game will show you a scrambled word related to blood donation.")
print("\n3.You have 3 attempts to guess the correct word.")
print("\n4.If you fail all attempts, the game ends and shows the correct word.")
print("\nComplete all levels to unlock the hint! Good luck! 🚀✨")

def load_words():
    level_1 = ["Donor", "Nurse", "Hospital", "Emergency","Doctor","Vein"]
    level_2 = ["Plasma", "Surgeon", "Diagnosis", "Anemia","Antibodies", "Vessel"]
    level_3 = ["Blood Bank", "Platelets","Oxygenation","Transfusion", "Hemoglobin", "Hematology"]

    return level_1, level_2, level_3

# Scramble the word
def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def play_level(level, words):
    print(f"\nLevel {level} - Unscramble the Word!")
    word = random.choice(words)
    scrambled = scramble_word(word)

    print("🔀 Scrambled Word:", scrambled)
    attempts = 3

    while attempts > 0:
        guess = input("🤔 Guess the word: ").lower().strip()
        if guess == word.lower().strip():
            print("🎉 Correct! Moving to the next level!")
            return True
        else:
            attempts -= 1
            print(f"❌ Wrong! {attempts} attempts left.")

    print(f"\n💀 You’re out of attempts! The correct word was: {word}")

def play_game():
    level_1, level_2, level_3 = load_words()
    levels = [(1, level_1), (2, level_2), (3, level_3)]

    for level, words in levels:
        if not play_level(level, words):
            print("\n⚠️  Game Over! You won't be getting any hints for now.")
            return False 

    print("\n🎁 Congratulations! You manage to guess all of the words!")
    return True

play_game()
