import random
name = input("Enter player's name: ")
print(f"Welcome  {name}!\n\tr - rock\n\tp - paper\n\ts - scissors\n\tq - quit")
score = {"win":0,"lose":0,"tie":0}

while True:
  cmd = input("What do you wanna play? ").lower()

  # Generate computer draws
  computer_guess = ""
  random_n = random.random()

  if random_n < 1/3:
    computer_guess = "r"
  elif random_n >= 1/3 and random_n < 2/3:
    computer_guess = "p"
  elif random_n >= 2/3 and random_n < 1:
    computer_guess = "s"
  else:
    print("Something went wrong!")

  # The game algorithm
  result = ""

  if cmd == computer_guess:
    result = "tie"
    score["tie"] += 1
  elif cmd == "s" and computer_guess == "p":
    result = "win"
    score["win"] += 1
  elif cmd == "r" and computer_guess == "s":
    result = "win"
    score["win"] += 1
  elif cmd == "p" and computer_guess == "r":
    result = "win"
    score["win"] += 1
  elif cmd == "q":
    break
  elif cmd not in ["p", "q", "r", "s"]:
    print("use only the p,q,r and s commands ")
    continue
  else:
    result = "lose"
    score["lose"] += 1

  print(f"You went for {cmd} and the computer went for {computer_guess}\n\tResult: {result.upper()}\n\tScore: Wins: {score['win']} Losses: {score['lose']} and Ties: {score['tie']}")

# Written by Dagaga A. Feb 19
