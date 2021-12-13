from chapter3 import chapter3
import time
def chapter2():
    print("chapter 2:")
    print("wake up from resting")
    time.sleep(5)
    print("go on a hunt for food")
    time.sleep(2)
    print("encounters a bear")
    print("make a choice")
    print("A.either fight and kill the bear")
    print("B.let the bear kill you")
    validchoice = False
    while validchoice == False:
        choiceC = input("What do you select? >>")
        if choiceC.upper() == 'A':
            validchoice = True
            print("kill the bear")
            print("receive a token")
            time.sleep(2)
            chapter3()

        elif choiceC == 'B':
            validchoice = True
            print("mission failed")
            print("go back to the previous chapter")
            import chapter1
            chapter1.chapter1()
            #at this point in the game, the player loops back to the beginning of the chapter since he died in the fight against the bear
        else:
            print("invalid choice")
def ch2(name):
    print()
    chapter2()








