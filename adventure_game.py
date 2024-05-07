"""
Adventure game tutorial by Tech with Tim, https://www.youtube.com/watch?v=NpmFbWO6HPU
"""


name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way do you go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or type swim to swim across. " )
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you die.")
    
elif answer == "right": 
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross or head back (cross/back)")
    if answer == "back":
        print("You go back to the main road. You die of dysentary")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?")
else:
    print("Not a valid option. You lose.")