import random

class QGridWalker(object):
  def __init__(self):
    self.gamma = 0.9
    self.eps = 0.9
    self.learningRate = 0.1
    self.grid = [[[0, 0, 0, 0] for row in range(15)] for col in range(15)]
    self.maxEps = 1000

  def greedy_nbr(self, row, col):
    q_max = 99999.99
    max_q_move = list()
    possible_moves = list()
    print row, col
    if row > 0:
      possible_moves.append(0)
      if q_max < self.grid[row][col][0]:
        q_max = self.grid[row][col][0]
        max_q_move = [0]
        print max_q_move 
        print "############"
      elif q_max == self.grid[row][col][0]:
        max_q_move.append(0)
        print max_q_move
        print "***********"
    print max_q_move
    if row < 14:
      possible_moves.append(1)
      if q_max < self.grid[row][col][1]:
        q_max = self.grid[row][col][1]
        max_q_move = [1]
      elif q_max == self.grid[row][col][1]:
        max_q_move.append(1)
    if col > 0:
      possible_moves.append(3)
      if q_max < self.grid[row][col][3]:
        q_max = self.grid[row][col][3]
        max_q_move = [3]
    if col < 14:
      possible_moves.append(2)
      if q_max < self.grid[row][col][2]:
        q_max = self.grid[row][col][2]
        max_q_move = [2]
      elif q_max == self.grid[row][col][2]:
        max_q_move.append(2)
    print max_q_move
    print "- - - - - - - -"
    expl_prob = random.randint(1, 10)
    if expl_prob / 10.0 > self.eps:
      for ii in max_q_move:
        possible_moves.remove(ii)
  
      if not possible_moves:
        return [random.choice(max_q_move), q_max]

      random_move = random.choice(possible_moves)

      if random_move == 0:
        q_value = self.grid[row][col][0]
      elif random_move == 1:
        q_value = self.grid[row][col][1]
      elif random_move == 2:
        q_value = self.grid[row][col][2]
      else:
        q_value = self.grid[row][col][3]
      return [random_move, q_value]
    print max_q_move
    return [random.choice(max_q_move), q_max]

  def eps_greedy_learner(self):
    ep = 1
    while ep <= self.maxEps:
      row = 1
      col = 1
      steps = 0
      while True:
        nextState = self.greedy_nbr(row, col)
        print nextState
        steps += 1
        if nextState[0] == 0:
          new_row = row - 1
          new_col = col
        elif nextState[0] == 1:
          new_row = row + 1
          new_col = col
        elif nextState[0] == 2:
          new_col = col + 1
          new_row = row
        else:
          new_col = col - 1
          new_row = row

        if new_row < 0 or new_row > 14 or new_col < 0 or new_col > 14:
          self.grid[row][col][nextState[0]] += self.learningRate * -2
        else:
          if new_row == 14 and new_col == 14:
            self.grid[row][col][nextState[0]] += self.learningRate * (10 - self.grid[row][col][nextState[0]])
            break
          future_move = self.greedy_nbr(new_row, new_col)
          self.grid[row][col][nextState[0]] += self.learningRate * (-1 + (self.gamma * future_move[1]) - self.grid[row][col][nextState[0]])
          row = new_row
          col = new_col
      print steps
      ep += 1

def main():
  learner = QGridWalker()
  learner.eps_greedy_learner()
  print learner.grid 
         
if __name__ == "__main__":
  main()
