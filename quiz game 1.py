print("welcome to my computer quiz ")
playing = input("Do you want to play?" )
if playing !="yes":
    quit()
print("ok lets play:")
score = 0
answer = input("what does cpu means?" )
if answer ==  "central processing unit":
    print("corret")
    score += 1    
else:
    print("incorrect")
answer = input("what does cpu means?" )
if answer ==  "central processing unit":
    print("corret")
    score += 1  
else:
    print("incorrect")
answer = input("what does USA means for?" )
if answer == "united states of america":
    print("correct")
    score += 1  
else:
    print("incorrect")
answer = input("what does nakba means? ")
if answer != "great catostrophe":
    print("incorrect")
    score += 1  
else:
    print("correct")
print("welcome to my quiz")
playing = input("do yoy want to play? ")
if playing != "yes":
    quit()
print("ok lets play:")
answer = input("who is the founder of zionism?")
if answer == "theoder herzel":
    print("correct")
    score += 1  
else:
    print("incorrect")
print("you got" +str(score) + "question correct!")