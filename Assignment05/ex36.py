from sys import exit

def bear_room():
    print("There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your leg off.")
        elif choice == "open door" and bear_moved:
            Clark_Lab()
        else:
            print("I got no idea what that means.")


def Janitor_Closet():
    print("You have found the Janitor Closet.\nWould you like to clean?.")

    choice = input("> ")

    if "yes" in choice:
        start()
    elif "no" in choice:
        dead("Well who's going to clean up the broken glass??!")
    else:
        Janitor_Closet

def Clark_Lab():
    print("This room is full of labitory equipment \nWhat do you want to take?")
    print(" 1) Microscope \n2) GC-FID\n3)Mystery Box")

    choice = input(">  ")
    if "1" in choice or "2" in choice or "3" in choice:
        Item = choice

        if Item = 1:
            print("Nice, you're not greedy, now get out!")
            exit(0)
        elif Item = 2:
            print("The GC-FID is too complicated and combersome to move.\nYou're caught by the police!")
            exit(0)
        elif Item = 3:
            print("You have found a mysterius golden key!")
    else:
        dead("Man, learn to type a Number.")

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You break into Washington State Universites Clark Hall.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input(">> ")

    if choice == "left":
        Clark_Lab()
    elif choice == "right":
        Janitor_Closet()
    else:
        dead("You stumble around the building until you are caught by police.")


start()
