import random
from utils import get_valid_guess, choose_difficulty,score_calculator
from leaderboard import save_score, display_leaderboard
def play_game():
    player_name = input("Enter your name: ").strip()
    print(f"{player_name}, Welcome to the Guessing Game!")
    min_num, max_num,max_attempts,diffculty = choose_difficulty()
    
    print(f"I'm thinking of a number between {min_num} and {max_num}.You have {max_attempts} attempts.")
    print()
    secret_number = random.randint(min_num,max_num)
    
    attempts = 0
    won = False
    while attempts < max_attempts and not won :
        guess = get_valid_guess(min_num,max_num,attempts,max_attempts)
        attempts +=1
        if guess == secret_number :
            won = True
            score = score_calculator(max_attempts,attempts)
            save_score(player_name,score,diffculty)
            # print (f"Correct guess! you got it in {attempts} attempts")
        elif guess < secret_number:
            # won = False
            print ("📉 Too low! Try higher")
        else:
            # won = False
            print ("📈 Too high! Try lower.")
    # score = score_calculator(max_attempts,attempts)
    if not won :
        print()
        print(f"You've used all {max_attempts} attempts.")
        print(f"The correct number is {secret_number}\n")
        print ("Your Score is 0 of possible 100 \n")
    # else :
    #     print (f"Your Score is {score} of possible 100 ")
        
    display_leaderboard("leaderboard.txt")    
        
def main():
    while True:
        play_game()
        Answer = (input("Do you want to play again? (y/n) ")).lower()
        
        if Answer != "y":
            print("Thanks for playing!")
            break
    
if __name__ == "__main__":
    main()
    
