#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
moves = [ROCK, PAPER, SCISSORS]

"""The Player class is the parent class for all of the Players
in this game"""


def print_and_pause(message):
    print(message)
    time.sleep(0.8)


class Player:
    def move(self):
        return ROCK

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    valid_moves = {'r', ROCK, 'p', PAPER, 's', SCISSORS}

    move_map = {
        'r': ROCK, ROCK: ROCK,
        'p': PAPER, PAPER: PAPER,
        's': SCISSORS, SCISSORS: SCISSORS
    }

    def move(self):
        human_move = input("Make your move(r/rock or p/paper or s/scissors)")
        while human_move not in self.valid_moves:
            print_and_pause("Invalid move")
            human_move = input(
                "Make your move(r/rock or p/paper or s/scissors)"
            )

        return self.move_map[human_move]


class ReflectPlayer(Player):

    def __init__(self):
        self.next_move = random.choice(moves)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(Player):

    def __init__(self):
        self.next_move = ROCK

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        if my_move == ROCK:
            self.next_move = PAPER
        elif my_move == PAPER:
            self.next_move = SCISSORS
        else:
            self.next_move = ROCK


def beats(one, two):
    return ((one == ROCK and two == SCISSORS) or
            (one == SCISSORS and two == PAPER) or
            (one == PAPER and two == ROCK))


class Game:
    def __init__(self, p1, p2):
        self.p1_wins = 0
        self.p2_wins = 0
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        while move1 == move2:
            print_and_pause(f"Player 1: {move1}  Player 2: {move2}")
            print_and_pause("It is a tie. Try again.")
            move1 = self.p1.move()
            move2 = self.p2.move()
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)

        print_and_pause(f"Player 1: {move1}  Player 2: {move2}")
        player_one_won = beats(move1, move2)
        if player_one_won:
            player_won = '1'
            self.p1_wins += 1
        else:
            player_won = '2'
            self.p2_wins += 1
        print_and_pause(f"Player {player_won} won this round.")

    def play_game(self):
        print_and_pause("Game start!")
        for round in range(3):
            print_and_pause(f"Round {round + 1}:")
            self.play_round()
            print_and_pause(
                f"The score is\nPlayer 1: "
                f"{self.p1_wins}\nPlayer 2: {self.p2_wins}"
            )
            if (self.p1_wins == 2) or (self.p2_wins == 2):
                break

        print_and_pause(
            f"The final score is\nPlayer 1: "
            f"{self.p1_wins}\nPlayer 2: {self.p2_wins}"
        )
        winner = '1' if self.p1_wins > self.p2_wins else '2'
        print_and_pause(f"Incredible! Player {winner} won!!! Game over!")


if __name__ == '__main__':
    strategies = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()
    }

    initial_input_request = (
        "Select the player strategy "
        "you want to play against"
        "1- Rock Player"
        "2- Random Player"
        "3- Cycle Player"
        "4- Reflect Player"
    )

    user_input = input(initial_input_request)
    while user_input not in {'1', '2', '3', '4'}:
        user_input = input(initial_input_request)

    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
