from chapter4 import chapter4
import time
def chapter3():
    print("chapter 3:")
    print("player comes across a broken bridge")
    print("make a choice")
    print("A.Try to walk on the broken bridge")
    print("B.Look for a plank to put on the bridge")
    chapter3complete = False

    while chapter3complete == False:
        optionA = input("Which do you choose? >>")
        if optionA.upper() == "A":
            print("the player falls down and gets killed")
            print("loop back to the beginning of the bridge")
            time.sleep(5)

        elif optionA.upper() == "B":
            chapter3complete = True
            print("player crosses the bridge safely")
            print("move to the next chapter")
            chapter4()
            time.sleep(5)
        else:
            print("Error. Invalid input.")

def ch3(name):
    print()
    chapter3()

#chapter3()