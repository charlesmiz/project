def save_score(name,score,difficulty):
    with open("leaderboard.txt", "a") as f:
        f.write( f"{name},{score},{difficulty}\n")
        
def load_scores():
    try:
        with open("leaderboard.txt", "r") as f:
            lines = f.readlines()
            records = []
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) !=3 :
                    continue
                name = parts[0]
                score = int(parts[1])
                difficulty = parts[2]
                records.append([name,score,difficulty])
            return records 
    except FileNotFoundError:
        print("file not found. start afresh or check file name again")
        return []

def display_leaderboard(file):
    print("         ===== LEADERBOARD =====")
    records = load_scores()
    
    if not records:
        print("No Scores yet")
    else:
        sorted_records = sorted(records,key = lambda record:record[1], reverse= True)
        top_10 = sorted_records[:10]
        # records = records.sort(key=lambda record:record[1] reverse=True) permanent modification of original list   
        for index,player in enumerate(top_10, start=1):
            print (f"{index}. {player[0]:<15}|{player[1]:^10}|{player[2]:>15}")
    

        
        
            