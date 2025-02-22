import random

user_wins = 0
comp_wins = 0
rounds_played = 0

options = ["rock", "paper", "scissors"]

# Add ASCII art for visual appeal
ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Initialize game history
game_history = []

print("Welcome to Rock, Paper, Scissors!")
max_rounds = int(input("How many rounds would you like to play? "))

while rounds_played < max_rounds:
    rounds_played += 1
    print(f"\nRound {rounds_played} of {max_rounds}")
    
    user_choice = input("Enter a choice (Rock/ Paper/ Scissors/ Q to quit): ").lower()
    if user_choice == "q":
        break
    
    if user_choice not in options:
        print("Invalid choice! Please try again.")
        rounds_played -= 1
        continue

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    
    # Display ASCII art choices
    print(f"\nYou chose:\n{ascii_art[user_choice]}")
    print(f"Computer chose:\n{ascii_art[computer_choice]}")
    
    # Determine winner and store result
    result = "tie"
    if user_choice == "rock" and computer_choice == "scissors":
        print("You won :)")
        user_wins += 1
        result = "win"
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won :)")
        user_wins += 1
        result = "win"
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won :)")
        user_wins += 1
        result = "win"
    elif user_choice == computer_choice:
        print("It was a tie!")
    else:
        print("You lost :(")
        comp_wins += 1
        result = "lose"
    
    # Record game history
    game_history.append({
        'round': rounds_played,
        'player': user_choice,
        'computer': computer_choice,
        'result': result
    })

# Game summary
print("\n=== Game Summary ===")
print(f"You won {user_wins} times")
print(f"Computer won {comp_wins} times")
print(f"\nGame History:")
for game in game_history:
    print(f"Round {game['round']}: You chose {game['player']}, Computer chose {game['computer']} - {game['result'].upper()}")

print("\nGoodbye!")