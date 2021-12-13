from chapter5 import chapter5
import time
def chapter4():
    print("chapter 4:")
    print("player walks into the jungle after crossing the bridge")
    print("player looks for a place to sit while he eats")
    print("player finds a place to eat but the place is dark")
    time.sleep(3.5)
    print("the player is frightened as he hears a loud thunderstrike")
    print("few moments after the thunderstrike stops, a footstep could be heard outside")
    print("the player decides to check it out")
    time.sleep(2)
    print("the player finds it is a wizard")
    print("player also finds an outerworld monster")
    print("the player is then prompted with a choice")
    print("A.follow the wizard")
    print("B.fight the monster")
    Validchoice = False
    while Validchoice == False:
        choiceD = input("what was your choice? >>")
        if choiceD.upper() == "A":
            Validchoice = True
            print("follow the wizard")
            print("move to the next chapter")
            time.sleep(5)
            chapter5()


        elif choiceD == 'B':
            Validchoice = True
            print("player fights with the monster")
            print("player dies")
            print("go back to the previous chapter")
            import chapter3
            chapter3.chapter3()

        else:
            print("Invalid choice")

def ch4(name):
    print()
    chapter4()

#chapter4()



