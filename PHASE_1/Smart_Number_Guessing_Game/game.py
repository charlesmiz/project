import random
from utils import get_valid_guess, choose_difficulty,score_calculator

def play_game():
    
    min_num, max_num,max_attempts,multiplier = choose_difficulty()
    
    print(f"you have {max_attempts} attempts, you should pick numbers between {min_num,max_num}")
    print()
    secret_number = random.randint(min_num,max_num)
    
    attempts = 0
    won = False
    while attempts < max_attempts and not won :
        guess = get_valid_guess(min_num,max_num)
        attempts +=1
        if guess == secret_number :
            won = True
            print (f"Correct guess! you got it in {attempts} attempts")
        elif guess < secret_number:
            # won = False
            print ("Guess too low,Try higher")
        else:
            # won = False
            print ("Guess too high,Try lower")
    score = (score_calculator(max_attempts,attempts))
    if not won :
        print()
        print(f"You've used all {max_attempts} attempts.")
        print(f"The correct number is {secret_number}")
        print ("Your Score is 0 of possible 100 ")
    else :
        print (f"Your Score is {score} of possible 100 ")
        
        
def main():
    while True:
        play_game()
        Answer = (input("Do you want to play again? (y/n)")).lower()
        
        if Answer != "y":
            print("Thanks for playing!")
            break
    
if __name__ == "__main__":
    main()
    
