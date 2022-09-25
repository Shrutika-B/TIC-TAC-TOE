import random
from colorama import Fore

class Coord:

  def __init__(self):
    self.state = [
      [" "," "," "],
      [" "," "," "],
      [" "," "," "]
    ]
    self.position = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
    self.taken = []
    self.win_states = [(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9)]

  def __str__(self):
    str = ""
    for i,row in enumerate(self.state):
      c1,c2,c3 = self.get_colored(row)
      part1 = Fore.YELLOW + f" {c1} | {c2} | {c3}  \n"
      part2 = "---|---|---\n"
      str += part1
      if i != 2:
        str += part2
    return str

  def get_colored(self,row):
    c_row = []
    for val in row:
      if val == "X":
        c_row.append(Fore.RED + val + Fore.YELLOW)
      elif val == "O":
        c_row.append(Fore.GREEN + val + Fore.YELLOW)
      else:
        c_row.append(val)
    return tuple(c_row)
        
      

  def update(self,pos,sign):
    if pos not in self.taken:
      x,y = self.position[pos]
      self.state[x][y] = sign
      self.taken.append(pos)
    else:
      raise SyntaxError()

  def get(self,pos):
    x,y = self.position[pos]
    return self.state[x][y]

  def check_win(self):
    for p1,p2,p3 in self.win_states:
      v1,v2,v3 = (self.get(p1),self.get(p2),self.get(p3))
      if v1 != " " and v1 == v2 == v3:
        self._winner = v1
        return True
    return False

  def get_winner(self):
    return self._winner



class Game_agent:

  def __init__(self,sign):
    self.score = 0
    self.sign = sign

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self,S):
    self._score = S

class Comp(Game_agent):

  def __init__(self,sign):
    super().__init__(sign)

  def choose(self,taken_list):
    choice = random.randint(1,9)
    while choice in taken_list:
      choice = random.randint(1,9)
    return choice

class User(Game_agent):

  def __init__(self,name,sign=None):
    super().__init__(sign)
    self.name = name
      
class Game:

  def __init__(self):
    sign = {'X':'O','O':'X'}
    
    print("======== TIC-TAC-TOE GAME ========")
    self.coord = Coord()
    self.user = User(input(Fore.BLUE + "Enter ur name: " + Fore.GREEN))
    while True:
      try:
        self.user.sign = input(Fore.BLUE + "Enter ur sign('X'/'O'): " + Fore.GREEN).strip().upper()
        self.comp = Comp(sign[self.user.sign])
        break
      except:
        print(Fore.RED + "INVALID CHOICE")
      
      
    
  def start(self):
    
    while not self.won():
      print(self.coord)
      try: 
        user_choice = int(input(Fore.CYAN + "Enter ur choice(1-9): " + Fore.GREEN))
        self.coord.update(user_choice,self.user.sign)
      except SyntaxError:
        print(Fore.RED + "Position already taken :(")
        continue
      except:
        print(Fore.RED + "INVALID VALUE")
        continue
        
      if self.won():
        break
        
      if len(self.coord.taken) == 9:
        break

      comp_choice = self.comp.choose(self.coord.taken)
      self.coord.update(comp_choice,self.comp.sign)
      
    
      
    cont = input(Fore.MAGENTA + "DO U WANT TO CONTINUE(Y/N): " + Fore.RED).strip().lower()
    if cont == "y":
      self.restart()
      
  def restart(self):
    self.coord = Coord()
    self.start()

    
  def won(self):
    w = self.coord.check_win()
    if w:
      if self.coord.get_winner() == self.user.sign:
        print(Fore.GREEN + f"{self.user.name} won\n")
        self.user.score += 1
      else:
        print(Fore.RED + "Computer won\n")
        self.comp.score += 1
      print(self.coord)
      print(Fore.WHITE + f"{self.user.name}:{self.user.score} | Computer:{self.comp.score}")
      
    elif len(self.coord.taken) == 9:
      print(Fore.LIGHTRED_EX + "GAME TIED\n")
      
    return w
    
if __name__ == "__main__":
  Game().start()





