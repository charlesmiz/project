def get_valid_guess(min_num, max_num,attempts,max_attempts ):
    while True: 
        try:
         guess = int(input(f"Attempt {attempts+1}/{max_attempts} — Enter your guess: "))
         if  guess < min_num or guess > max_num :
             print("Number is out of range")
         else:
             return guess
        except ValueError:
            print("Please enter a valid number.")
       

        
def choose_difficulty() :
    
    difficulties = {
        "1":(1,50,10,"Easy"),
        "2":(1,100,7,"Medium"),
        "3":(1,200,5,"Hard")
    }
    
    while True:
        choice = (input("Select difficulty:[1] Easy  [2] Medium  [3] Hard \n = ").strip())             
        if choice in difficulties:
            return difficulties[choice]
        else:
            print("Enter correct value [1]or[2]or[3]\n")
        

def score_calculator(max_attempts,attempts_used):
    attempts_remaining = max_attempts - attempts_used +1
    score = round((attempts_remaining / max_attempts ) * 100)
    
    return score

# print(score_calculator(5,2))
# settings = choose_difficulty()
# print(settings)
