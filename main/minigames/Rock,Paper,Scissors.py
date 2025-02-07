import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "Ermmm it's a tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!YAYYY"
    else:
        return "Computer wins!"

def update_scoreboard(user_score, computer_score):
    print("\n--- SCOREBOARD ---")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("-------------------\n")

def play_game():
    print("Halo!This is Rock, Paper, Scissors game")
    print("Instructions : You need to choose either Rock, Paper, or Scissors and The Computer will also make a choice. The winner is determined based on the standard rules.")
    print("Here are the rules:")
    print("~ Rock beats Scissors")
    print("~ Scissors beats Paper")
    print("~ Paper beats Rock")
    print("The game will be played over multiple rounds, and the player with the highest score at the end wins!")
    print("Good luck! Do your best!\n")

    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds would you like to play? "))
    
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "You win!YAYYY" in result:
            user_score += 1
        elif "Computer wins!" in result:
            computer_score += 1
       
        update_scoreboard(user_score, computer_score)
        
        print(f"Current Score - You: {user_score}, Computer: {computer_score}\n")
    
    print("Game Over!")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game yahoo!")
    elif user_score < computer_score:
        print("Uh oh you did a great job! Better luck next time! The computer won the game hehe.")
    else:
        print("Well done! It's a draw weehee!")

if __name__ == "__main__":
    play_game()


