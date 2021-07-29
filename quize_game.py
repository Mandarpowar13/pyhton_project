print("wwlcome To Quizz game!!")
playing = input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("okay lets play!!")
score=0
answer=input("what dose CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score +=1
else:
    print("incorrect!")

answer=input("which city is capital of India? ")
if answer.lower() == "delhi":
    print("correct!")
    score +=1
else:
    print("incorrect!")

answer=input("which is popular programming launguge? ")
if answer.lower() == "python":
    print("correct!")
    score +=1
else:
    print("incorrect!")

print("you got "+ str(score)+" answer correct!!")

  

