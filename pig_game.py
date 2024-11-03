import random


MAX_SCORE = 50
MAX_PLAYERS = 4
MIN_PLAYERS = 2


def roll():
    return random.randint(1, 6)

# Get a valid number of players
def get_number_of_players():
    while True:
        players = input("Choose number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if MIN_PLAYERS <= players <= MAX_PLAYERS:
                return players
            else:
                print(f"Choose a number between {MIN_PLAYERS} - {MAX_PLAYERS}")
        else:
            print("Choose a valid number!")

# Initialize player scores
def initialize_scores(number_of_players):
    return {player_id: 0 for player_id in range(1, number_of_players + 1)}

# Game loop
def play_game(players_scores):
    while max(players_scores.values()) < MAX_SCORE:
        for player in players_scores.keys():
            print(f"\nPlayer {player}'s turn")
            print(f"Player {player} starts with {players_scores[player]}")

            current_score = 0
            while True:
                should_roll = input("Would you like to roll? (y/n): ").lower()
                if should_roll != "y":
                    break

                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled: {value}")
                    print(f"Your current score for this turn is: {current_score}")

            players_scores[player] += current_score
            print(f"Player {player} ends with {players_scores[player]}")

print(f"The value of __name__ in pig_game is: {__name__}")

# Main execution
if __name__ == "__main__":
    print(f"The value of __name__ in pig_game is: {__name__}")  # Add this line
    num_players = get_number_of_players()
    players_scores = initialize_scores(num_players)
    play_game(players_scores)

    winner = max(players_scores, key=players_scores.get)
    print(f"Player {winner} wins with a score of {players_scores[winner]}!")
