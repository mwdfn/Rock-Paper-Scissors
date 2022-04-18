from models.player import *

class Game:
    def __init__(self, input_player_1, input_player_2):
        self.player_1 = input_player_1
        self.player_2 = input_player_2

    def play_game(self, player1_move, player2_move):
        if player1_move == player2_move:
            return "It's a draw!"
        elif player1_move == "rock":
            if player2_move == "scissors":
                return "Rock smashes scissors! Player 1 wins!"
            else:
                return "Paper covers rock! Player 2 wins!"
        elif player1_move == "paper":
            if player2_move == "rock":
                return "Paper covers rock! Player 1 wins!"
            else:
                return "Scissors cuts paper! Player 2 wins!"
        elif player1_move == "scissors":
            if player2_move == "paper":
                return "Scissors cuts paper! Player 1 wins!"
            else:
                return "Rock smashes scissors! Player 2 wins!"


    # def play_game(self, player1_move, player2_move):
    #     if player1_move == "Rock" and player2_move == "Scissors":
    #         return "Rock smashes Scissors! Player 1 Wins!"
            
    #     elif player1_move == "Scissors" and player2_move == "Paper":
    #         return "Scissors cut Paper! Player 1 Wins!"
            
    #     elif player1_move == "Paper" and player2_move == "Rock":
    #         return "Paper covers Rock! Player 1 Wins!"

    #     elif player2_move == "Rock" and player1_move == "Scissors":
    #         return "Rock smashes Scissors! Player 2 Wins!"
            
    #     elif player2_move == "Scissors" and player1_move == "Paper":
    #         return "Scissors cut Paper! Player 2 Wins!"
            
    #     elif player2_move == "Paper" and player1_move == "Rock":
    #         return "Paper covers Rock! Player 2 Wins!"

    #     else:
    #         player1_move == player2_move
    #         return "It's a draw!" 