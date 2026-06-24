import random
choices=['rock','paper','scissor']
user_wins=0
computer_wins=0
tie=0
while True:
    play=input("do you want to play rock paper scissor (yes / no): ")
    if play == "no":
        print("thanks for playing","goodbye")
        print("user wins",user_wins)
        print("computer wins",computer_wins)
        print("ties",tie)
        with open("scores.txt","w") as f:
           f.write(f"User wins: {user_wins}\n")
           f.write(f"Computer wins: {computer_wins}\n")
           f.write(f"Ties: {tie}\n")
        print("Scores have been saved to scores.txt")
        break
    elif play == "yes":
        user_choice=input("enter rock or paper or scissor:").lower()
    if user_choice not in choices:
        print("invalid input! please try again.")
        continue
    computer_choice=random.choice(choices)
    print("computer choose:",computer_choice)

    if user_choice==computer_choice:
        print("its tie")
        tie+=1
    elif (user_choice=="rock" and computer_choice=="scissor") or (user_choice=="scissor"and computer_choice=='paper')or (user_choice=="paper"and computer_choice=="rock"):
        print("user wins")
        user_wins+=1
    else:
        print("computer wins")
        computer_wins+=1
else:
        print("please enter a valid input (yes or no).")
        
