import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value , max_value)
    
    return roll
while True:
    player = input("Enter the number of player(2-4)" )
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("must be between 2 - 4 players!")
    else:
        print("invalid try again!")
        
max_score = 50
player_score = [0 for _ in range(player)]
while max(player_score) < max_score:
    for player_idx in range(player):
        print("\nplayer number" , player_idx + 1 ,"turn has just started!")
        print("your total score is", player_score[player_idx], "\n")
        current_score = 0
        
        while True:
            should_role = input("would you like to roll (y)? ")
            if should_role.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("you rolled a 1! turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a:", value)
                
            print("your score is",current_score)
            
            
        player_score[player_idx] += current_score
        print("your total score is:", player_score[player_idx])
        
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("player number",winning_idx + 1,"is winner with score of:" ,max_score)
                