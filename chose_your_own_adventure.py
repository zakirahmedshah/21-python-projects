name = input("type a name: ")
print("welcome",name,"to this adventue!")
answer = input("you are on a dirt road ,it has come to an end ,and you can go left or right which way would you like to go ").lower()
if answer == "left":
  answer = input("you come to a river,you can walk around it or swim across it ./type walk, to walk around it ,swim to swim across it: ")
  
  if answer ==  "swim":
    print("you swam across were eaten by a alligator")
    
  elif answer == "walk":
    print("you walked for many miles ,out of ran and you lost the game")
  else:
      print("not a valid answer")
      
elif answer == "right":
    asnwer = input("you come to a bridge its look woobly ,do you want to cross it or head back / cross /back. ")
    if  answer == "back":
      print("you go back andyou lose")
     
    elif answer == "cross":
      
      print("you talk to stranger and it gives you gold you win! ") 
        
    else:
       print("not a valid option")
else:
  print("yor answer is not valid")
