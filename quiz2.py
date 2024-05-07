print("Welcome to my quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
else:
    print("Okay. Let's play!")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct")
else:
    print("Wrong answer. The correct answer is central processing unit.")

answer2 = input("What year did we move to Ireland: ")

if answer2 == 2013:
    print("Correct")
else:
    print("Wrong answer. The correct answer is 2013.")
                

