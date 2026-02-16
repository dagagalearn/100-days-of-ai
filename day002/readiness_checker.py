# Starting conversation with the user 
name = input("> Hello, what should I call you? ")
print(f"Alright {name}, I calculate how ready you are to become an AI Engineer!\n")

# taking inputs from a user
hours = float(input("> How many hours do you study a day? "))
mathl = float(input("> How do you rate your math(1-10)? "))
progr_conf = float(input("> How about your confidence in programming(1-10)? "))
days_studied = int(input("> How many days do you study per week? "))

# calculating score and presenting it
if (mathl<=10 and mathl>=1) and (progr_conf<=10 and progr_conf>=1) and (hours<=24 and hours>=0) and (days_studied<=7 and days_studied>=1):
  score = (hours * 2) + mathl + progr_conf + (days_studied * 1.5)
  message = ""
  if score<20:
    message="You are just warmin up. Stay Consistent"
  elif score>=20 and score<=35:
    message="Solid foundations. Keep building"
  elif score >= 36 and score<=50:
    message="You are becoming dangerous :)"
  elif score>50:
    message="AI Engineering in making!"
  else:
    print("Something went wrong, check your inputs again")
  # outputing score to a user
  print(f"Well, {name}, here is your result: {score} that means: {message}")
else:
    print("Check the inputs, please!")
