from flask import render_template
from app import app
from models.game import Game
from models.player import Player


@app.route('/home/')
def events_list():
    return render_template('index.html', title='Home')

@app.route('/<player1_move>/<player2_move>')
def play_game(player1_move, player2_move):
    player_1 = Player("Player 1", player1_move)
    player_2 = Player("Player 2", player2_move)
    game = Game(player_1, player_2)
    winner = game.play_game(player1_move, player2_move)
    return render_template("game_over.html", winner = winner)
