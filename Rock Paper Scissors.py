import random

def get_winner(user, comp):
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if user == comp:
        return "tie"
    elif rules[user] == comp:
        return "user"
    else:
        return "computer"

def play():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    rounds = 5

    print("🎮 Welcome to Rock Paper Scissors (Best of 5) 🎮\n")

    for round_no in range(1, rounds + 1):
        print(f"--- Round {round_no} ---")
        
        user = input("Choose rock/paper/scissors: ").lower()

        if user not in options:
            print("⚠ Invalid choice! Round skipped.\n")
            continue

        comp = random.choice(options)

        print(f"You ➜ {user}")
        print(f"Computer ➜ {comp}")

        result = get_winner(user, comp)

        if result == "tie":
            print("Result: It's a tie ")
        elif result == "user":
            print("Result: You win this round ")
            user_score += 1
        else:
            print("Result: Computer wins this round ")
            comp_score += 1

        print(f"Score ➜ You: {user_score} | Computer: {comp_score}\n")

    print(" Final Result ")
    if user_score > comp_score:
        print(" You are the overall winner!")
    elif user_score < comp_score:
        print(" Computer wins the game!")
    else:
        print(" Match Draw!")

# Run game
play()               