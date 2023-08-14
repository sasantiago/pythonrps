class Game:
    def __init__(self):
        
        pass

    def play(self, player_choice, enemy_choice):
        if player_choice == enemy_choice:
            return "Tie"
        elif player_choice == "rock":
            return "Win" if enemy_choice =="scissors" else "Lose"
        elif player_choice == "paper":
            return "Win" if enemy_choice == "rock" else "Lose"
        elif player_choice == "scissors":
            return "Win" if enemy_choice =="paper" else "Lose"
