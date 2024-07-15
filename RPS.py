# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[], sequences={}):
  stride = 6

  
  if prev_play != '':
    opponent_history.append(prev_play)


  if len(opponent_history) <= stride:
    return "R"


  if len(opponent_history) > stride + 1:
    opponent_history.pop(0)


  seq = "".join(opponent_history)
  sequences[seq] = sequences.get(seq, 0) + 1


  seq     = "".join(opponent_history[-stride:])
  predict = max([seq+"R", seq+"P", seq+"S"],
                  key=lambda key: sequences.get(key,0))[-1]

  if predict == "R": return "P"
  if predict == "P": return "S"
  return "R"