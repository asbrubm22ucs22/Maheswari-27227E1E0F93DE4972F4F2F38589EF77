class Player:
  def play(self):
    print("the player is playing cricket")
class Batesman(Player): 
  def play(self):
    print("the batesman is batting")
class Boweller(Player):
  def play(self):
    print("the boweller is bowelling")
batesmen=Batesman()
boweller=Boweller()
batesmen.play()
boweller.play()