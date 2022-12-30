""" This is a program I am writing after many months of neglect"""

"""
Layout of the project

* Game object consisting of three games; guessing game, hangman and wordle.
* Game object of players keeping track of name and high score and arranging the leaderboard.

** Additional algorithm for searching
** Gui for interaction

"""

import random

class Player:

    players_id = {'computer': 'ai'}

    def __init__(self, name, username, score=0):
        self.name = name
        self.username = username
        self.score = score

class Game:

    games = ['guessing']
    players = {'ai': 1000}

    def __init__(self):
        name = input("What is your name? ")
        # print (name)
        # print ("flag")
        username =  input("What name would you like to use in this game? ")
        self.get_info(name, username)
        self.choose_game()

    def get_info(self, name, username):
        self.name = name
        self.username = username
        self.player_id = (self.name, self.username)
        self.get_score(Game, self.player_id)

    def get_score(self, cls, player_id):
        if player_id in Player.players_id:
            self.score = cls.players[self.player_id[1]]
        else:
            player_id = Player(self.name, self._username)

            cls.players[self.username] = player_id.score
            Player.players_id[self.name] = player_id.username

            self.score = player_id.score

            print (Player.players_id)
            print (cls.players)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        while not name:
            print ("Name cannot be empty")
            name = input("What is your name? ")
        self._name = name

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        while not username:
            print ("Username cannot be empty.")
            username = input("What name would you like to use in this game? ")

        while username in Game.players:
            print ("Username is taken. Please choose another name: ")
            username = input("What name would you like to use in this game? ")

        self._username = username

    def choose_game(self):
        if len(Game.games) == 1:
            det = 'is'
            plural = ''
        else:
            det = 'are'
            plural = 's'

        print (f"The game{plural} available {det}:")
        for i in Game.games:
            print (i.title())

        game = input("Which game would you like to play? ")
        if game.lower() in Game.games:
            print ("Start!")

            match game:
                case "guessing":
                    Guessing(self.name, self.username, self.score)
                case "hangman":
                    Hangman()

    def leaderboard(self):
        key_list = list(cls.players.item())
        value_list = list(cls.players.item())


        for i in sorted(value_list, reverse=True):
            position = value_list.index(i)
            print({key_list[position]: i})


class Guessing(Game):

    options = ['Human', 'Computer']

    def __init__(self, name, username, score):

        self.name = name
        self._username = username
        self.score = score

        self.guess = ''
        self.determiner(Game)

    def human_guess(self):
        hum_score = 1000
        guess = self.guess
        num = random.randint(1, 100)
        print ("Pick a number between 1 and 100!")
        while guess != num:
            try:
                guess = int(input("Guess: "))
                if guess > 0:
                    if guess < num:
                        print ("Too small!")
                    elif guess > num:
                        print ("Too large!")
                    else:
                        print ("Just right!")

                    hum_score = hum_score - 50

            except ValueError:
                pass

        Game.players[self.username] = hum_score
        print (f"Your score is {hum_score}. Good Job!")

    def computer_guess(self):
        comp_score = 1000

        num = int(input("What's your secret number? "))
        upper_limit = 100
        lower_limit = 0
        guess = int(100/2)
        print ("\nRespond with 'Too High' or 'H' if my guess is too high.", "Respond with 'Too Low' or 'L' if my guess is too low.", sep = '\n')
        print ("Respond with 'Just Right' or 'J' if my guess is correct.")

        while True:
            print (f"\nI choose the number {guess}")
            response = input("How's my guess? ").title()
            if response == 'Too High' or response == 'H':
                upper_limit = guess
            elif response == 'Too Low' or response == 'L':
                lower_limit = guess
            elif response == 'Just Right' or response == 'J':
                print ("\nGame over. Your secret number was: " + str(guess))
                break
            else:
                print ("Sorry, I didn't understand your response")
            guess = int((upper_limit + lower_limit) / 2)

            comp_score = comp_score - 50

        Game.players['ai'] = comp_score
        print (f"The computer's score is {comp_score}. AI isn't so bad")


    def determiner(self, cls):
        print ("Enter 'Human' to guess.", "Enter 'Computer' to prompt computer to guess.", sep = '\n')
        print ("Enter 'Random' to pick randomly.", "Enter 'Quit' to stop playing.", sep = '\n')
        turn = ''
        while turn != 'Quit':
            turn = input("\nWhose turn is it to play: ").title()
            if turn == 'Human':
                self.human_guess()
            elif turn == 'Computer':
                self.computer_guess()
            elif turn == 'Random':
                random.shuffle(cls.options)
                if options[0] == 'Human':
                    print ("\nIt's your turn to play.")
                    self.human_guess()
                elif options[0] == 'Computer':
                    print ("\nIt's the computer's turn to play.")
                    self.computer_guess()
            elif turn == 'Quit':
                print ("Thank you for playing with me.")
                break
            else:
                print ("Sorry, I didn't understand your response")


def main():
    print (Player.players_id)
    print (Game.players)
    Game()
    print (Player.players_id)
    print (Game.players)


main()
