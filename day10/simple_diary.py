import datetime
from pathlib import Path
while True:
  cmd = input("\n\tr - read a file\n\tw - write on a file\n\tq - quit\n").lower()
  if cmd=="r":
    file_name = input("What do you want to read? ")
    if Path(file_name).exists():
      with open(file_name,'r') as handle:
        print(handle.read())
    else:
      print("File not found!")
    
  elif cmd=="w":
    msg = input("Enter the message you want to add: ")
    file_name = input("To what file: ")
    date_time= datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
    with open(file_name,'a') as handle:
      handle.write(f"\nNotes on {date_time}: ")
      handle.write(f"\n=====================\n {msg} \n=====================\n")
      print("File written successfully!")
  else:
    break
    # The user might be confused how to leave the program, that's why!

# Written by Dagaga Addisu Feb 24
