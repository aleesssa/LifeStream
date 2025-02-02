import random

def load_words():
    level_1 = ["Donor", "Nurse", "Hospital", "Emergency","Doctor","Vein"]

    level_2 = ["Plasma", "Surgeon", "Diagnosis", "Anemia","Antibodies", "Vessel"]

    level_3 = ["Blood Bank", "Platelets","Oxygenation", 
               "Transfusion", "Hemoglobin", "Hematology"]

    return level_1, level_2, level_3

# Scramble the word
def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Play the game
def play_game():
    level_1, level_2, level_3 = load_words()

    # Ask for level input and ensure valid input
    while True:
        print("Choose your level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        try:
            level = int(input("Enter level (1/2/3): "))
            if level in [1, 2, 3]:
                break  # Exit the loop if valid input
            else:
                print("❌ Invalid choice! Please choose 1, 2, or 3.")
        except ValueError:
            print("❌ Invalid input! Please enter a number (1, 2, or 3).")

    # Select words based on chosen level
    if level == 1:
        chosen_words = level_1
        attempts = 3
    elif level == 2:
        chosen_words = level_2
        attempts = 3
    elif level == 3:
        chosen_words = level_3
        attempts = 3

    # Choose a random word from the selected level
    word = random.choice(chosen_words)
    scrambled = scramble_word(word)

    print("🔀 Scrambled Word:", scrambled)

    while attempts > 0:
        guess = input("🤔 Guess the word: ").lower()
        if guess == word.lower():
            print("🎉 Correct! You guessed the word!")
            return
        else:
            attempts -= 1
            print(f"❌ Wrong! {attempts} attempts left.")

    print(f"💀 Game Over! The correct word was: {word}")

play_game()