from random import randint

def rps():
  options = ["ROCK", "PAPER", "SCISSORS"]

  message = {
    "tie": "Its a tie!",
    "won": "You won!",
    "lost": "you lost!",
  }

  def decide_winner(user_choice, computer_choice):
    print("You chose: %s" % user_choice)
    print("The computer chose: %s" % computer_choice)

    if user_choice == computer_choice:
      print(message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
      print(message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
      print(message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
      print(message["won"])
    else:
      print(message["lost"])

  def play_RPS():
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,2)]
    decide_winner(user_choice, computer_choice)

  play_RPS()

rps()

while True:
  rps()
