print ("This programs helps two players play 'Rock, Paper, Scissors'")
j=input("Player One plays: \n")
while j!="exit":
  k=input("Player Two plays: \n")
  while k!= "exit":
    if j == "rock":
      if k == "rock":
        print ("Players draw")
      elif k=="paper":
        print ("Player Two WINS !!!")
      elif k=="scissors":
        print ("PLayer One Wins !!!")
      else:
        print ("Invalid (you can only pick between rock, paper, or scissors (Beware, use Lower caps only as Python is case sensitive)")
    elif j == "paper":
      if k == "rock":
        print ("Player One WINS !!!")
      elif k=="paper":
        print ("Players draw")
      elif k=="scissors":
        print ("PLayer Two Wins !!!")
      else:
        print ("Invalid (you can only pick between rock, paper, or scissors (Beware, use Lower caps only as Python is case sensitive)")     
    elif j=="scissors":
      if k== "rock":
        print ("Player Two WINS !!!")
      elif k=="paper":
        print ("Player One WINS !!!")
      elif k=="scissors":
        print ("PLayers draw")
      else:
        print ("Invalid (you can only pick between rock, paper, or scissors (Beware, use Lower caps only as Python is case sensitive)")
    else:
      print ("Invalid (you can only pick between rock, paper, or scissors (Beware, use Lower caps only as Python is case sensitive)")
    j=input("Player One plays: \n")
    if j=="exit":
      break
    k=input("Player Two plays: \n")
    if k=="exit":
      break

  break
print("Goodbye")

