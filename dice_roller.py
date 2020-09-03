import random

def main():
  rolls = 2
  
  for i in range(0,rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print("You rolled a {0}! Critical Fail".format(roll))
    elif roll == 6:
      print("You rolled a {0}! Critical Success!".format(roll))
    else:
      print("You rolled a {0}".format(roll))
  print("You have rolled a total of {0}".format(dice_sum))
if __name__== "__main__":
  main()