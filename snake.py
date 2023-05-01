def snake_ladder():
    import random

    class Board:
        def __init__(self):
            self.snakes = {
                16: 6,
                47: 26,
                49: 11,
                56: 53,
                62: 19,
                64: 60,
                87: 24,
                93: 73,
                95: 75,
                98: 78
            }
            self.ladders = {
                1: 38,
                4: 14,
                9: 31,
                21: 42,
                28: 84,
                36: 44,
                51: 67,
                71: 91,
                80: 100
            }
            self.num_squares = 100

    class Player:
        def __init__(self, name):
            self.name = name
            self.position = 0
       
        def __str__(self):
            return f"{self.name} is at position {self.position}"
       
        def move(self, roll):
            self.position += roll

    class Die:
        def roll(self):
            return random.randint(1, 6)

    class SnakeAndLadder:
        def __init__(self, num_players):
            self.board = Board()
            self.players = [Player(f"Player {i+1}") for i in range(num_players)]
            self.die = Die()
       
        def play(self):
            while True:
               
               
                for player in self.players:
                    print("\n" + str(player))
                    input("Press enter to roll the die.")
                    roll = self.die.roll()
                    print(f"You rolled a {roll}!")
                    player.move(roll)
                    if player.position in self.board.snakes:
                        print(f"Oh no! You landed on a snake. You slide down to position {self.board.snakes[player.position]}.")
                        player.position = self.board.snakes[player.position]
                    elif player.position in self.board.ladders:
                        print(f"Wow! You landed on a ladder. You climb up to position {self.board.ladders[player.position]}.")
                        player.position = self.board.ladders[player.position]
                   
                    if player.position >= self.board.num_squares:
                        print(f"\nCongratulations, {player.name}! You won!")
                        return
    game = SnakeAndLadder(2)
    game.play()
snake_ladder() 