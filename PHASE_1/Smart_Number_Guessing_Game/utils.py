def get_valid_guess(min_num, max_num):
    while True: 
        try:
         guess = int(input("Please pick a valid number: "))
         if  guess < min_num or guess > max_num :
             print("Number is out of range")
         else:
             return guess
        except ValueError:
            print("Please enter a valid number.")
       

        
def choose_difficulty() :
    
    # difficulties = {
    #     "1":(1,50,10),
    #     "2":(1,100,7),
    #     "3":(1,200,5)
    # }
    
    while True:
        print("1. Easy")
        print("2. Medium")        
        print("3. Hard")
    
        try:
            choice = input("choose difficulty: ").strip()
            
            if choice == 1:
                return (1,50,10)
                
            elif choice == 2:
                return(1,100,7)
            elif choice == 3:
                return(1,200,5)
            else:
                print("Pick between 1-3")
                print()
        except ValueError:
            print("Enter correct value")
            print()
             

def score_calculator(max_attempts,attempts_used):
    attempts_remaining = max_attempts - attempts_used +1
    score = round((attempts_remaining / max_attempts ) * 100)
    
    return score

# print(score_calculator(5,2))
# settings = choose_difficulty()
# print(settings)
