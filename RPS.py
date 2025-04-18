import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Keep last 5 moves for pattern recognition
    if len(opponent_history) < 5:
        return "R"

    # Create a dictionary of next move frequencies after a given sequence
    guess_patterns = {}
    seq = "".join(opponent_history[-5:])
    for i in range(len(opponent_history) - 5):
        key = "".join(opponent_history[i:i+5])
        next_move = opponent_history[i+5]
        if key == seq:
            if next_move in guess_patterns:
                guess_patterns[next_move] += 1
            else:
                guess_patterns[next_move] = 1

    # Predict opponent's next move
    if guess_patterns:
        prediction = max(guess_patterns, key=guess_patterns.get)
    else:
        prediction = random.choice(["R", "P", "S"])

    # Choose the move that beats the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[prediction]