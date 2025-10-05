print("--------------WELCOME IN MY QUIZ GAME----------------")
ans=input("Do you want to start the game?").upper()
if ans=="YES":
    score=0
    print("let's begin")
    q1=input("what is 3+9?").lower()
    if q1=="12" or q1=="twelve":
        print("correct")
        score+=1
    else:
        print("not correct")
        score=score-0.25
    q2=input("what is color of sky?").lower()
    if q2=="blue":
        print("correct")
        score+=1
    else:
        print("not correct")
        score-=0.25
    
else:
    print("okay bye")
print("score is : ",score)
