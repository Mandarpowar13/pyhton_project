print("wwlcome To Quizz game!!")
playing = input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("okay lets play!!")
score=0
answer=input("what dose CPU stands for? ")
guess_count=0
guess_limit=3
out_of_guess=False
while answer.lower() != "central processing unit" and not(out_of_guess):
      if guess_count < guess_limit:
        answer = input("Your answer is wrong!you got another guess : ")
        guess_count += 1
      else:
        out_of_guess = True


if out_of_guess:
    print("You are out of guess! Next question")
else:
    print("Correct!")
    score +=1  

answer1=input("which city is capital of India? ")
guess_count=0
guess_limit=3
out_of_guess=False
while answer1.lower() != "delhi" and not (out_of_guess):
        if guess_count < guess_limit:
         answer1 = input("Your answer is WRONG!! You got another guess : ")
         guess_count += 1
        else:
         out_of_guess = True


if out_of_guess:
    print("You are out of guess!! Next question")
else:
    print("Correct!")
    score += 1


answer2=input("which is popular programming launguge? ")
guess_count=0
guess_limit=3
out_of_guess=False
while answer2.lower() != "python" and not (out_of_guess):
    if guess_count < guess_limit:
         answer1 = input("Your answer is wrong!you got another guess : ")
         guess_count += 1
    else:
         out_of_guess = True


if out_of_guess:
    print("You are out of guess! Next question")
else:
    print("Correct!")
    score += 1

print("YOU GOT "+ str(score)+" ANSWER CORRECT!!")

  

