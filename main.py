import random
 
from bke import start, MLAgent, is_winner, opponent, load, RandomAgent, train_and_plot, EvaluationAgent

class MyRandomAgent(EvaluationAgent):
    def evaluate (self, board, y_symbol, opponent_symbol):
     return random.randint(1, 500)


class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    

def play():    
  start()


def randomAgent():   
  my_random_agent = MyRandomAgent()
  start(player_o=my_random_agent)


def smartOpponent():
  my_agent = MyAgent()
  start(player_x=my_agent)
  
def trainAndPlot():
  my_agent = MyAgent(alpha=0.8, epsilon=0.2)
  
  my_agent = MyAgent()
  random_agent = RandomAgent()
   
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=20,
      trainings=50,
      validations=1000)

def undefeatable ():
  my_agent = MyAgent()
  my_agent = load('MyAgent_3000')
  my_agent.learning = False
  start(player_x=my_agent)

print("Kies uit de volgende opties wat voor spel u zou willen spelen!")
print("   ")
print("1. Medespeler! Speel tegen je kamaraat en kom erachter wie de sterkste speler is!")
print("2. Beginner! Leer de beste tactieken te gebruiken zonder te hard ten onder te gaan..")
print("3. Expert! Kan jij de echte gevaren van dit spel al aan?")
print("4. Train, valideer en plot: kijk welke vooruitgangen je maakt!")
print("5. Eindbaas! Niemand heeft deze ooit weten te verslaan...")

i = input()
if i == "1":
  play()
elif i == "2":
  randomAgent()
elif i == "3":
  smartOpponent()
elif i == "4":
  trainAndPlot()

elif i == "5" :
  undefeatable ()
  