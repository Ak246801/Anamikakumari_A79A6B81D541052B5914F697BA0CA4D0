'''Implement a class called Player that represents a cricket player.
method called play() which prints "The player is playing cricket.
Derive two classes, Batsman and
The Player class should have a Bowler, from the Player class. Override the play() method in each program to create objects of both 
the derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a
Batsman and Bowler classes and call the play() method for each object.'''
class Player:
  def play(self):
     print("The player is playing cricket.")
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")
class Bowler (Player):
  def play(self):
    print("The bowler is bowling.")
batsman = Batsman() 
bowler = Bowler()
batsman.play()
bowler.play()