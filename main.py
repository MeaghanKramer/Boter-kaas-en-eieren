import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    

random.seed(1)

def plot1():
def plot2():
def plot3():
def plot4():
def plot5():
  my_agent = MyAgent(alpha=0.8, epsilon=0.2)
  
  my_agent = MyAgent()
  random_agent = RandomAgent()
   
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=20,
      trainings=50,
      validations=1000)


print("1. speel tegen een medespeler")
print("2. speel tegen een beginner")
print("3. train je tegenstander")
print("4. speel tegen een expert")
print("5. train, valideer en plot")

i = input()
if i == "1":
  plot1()
elif i == "2":
  plot2()
elif i == "3":
  plot3()
elif i == "4":
  plot4()
elif i == "5":
  plot5()
  