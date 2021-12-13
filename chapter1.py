from chapter2 import chapter2
import time
def chapter1():
    print("Chapter 1:")
    time.sleep(2.5)
    print("It was a rainy day when a young boy had just come back from the farm and was told his mother is dying")
    time.sleep(1)
    print("in other to save your mother from dying, you have to journey to the dark forest to retrieve an orb")
    print("select one of the choice")
    print("A.start your journey to the dark forest")
    print("B.do not start your journey")
    Choice1 = input("Which do you choose? >>")
    if Choice1.upper() == "A":
        print("the young boy begins his journey to the dark forest")
        time.sleep(1)
        print("on his way to te forest he stops by the river for a drink of water")
        time.sleep(3)
        print("while stopping for a drink of water,the player is approached by bunch of petty thieves")
        print("make a choice")
        print("A.fight with the thieves")
        print("B.do not fight with the thieves")
        choiceB = input("Which do you choose? >>")
        if choiceB.upper() == "A":
            print("gets victorious but gets injured")
            print("finds a place to rest")
            time.sleep(2)
            print("when you wake up start chapter 2")
            chapter2()
        else:
            print("the player gets beaten up and is returned to the beginning")
            return
    elif Choice1 == "B":
        print("return to the main menu")
        return


def ch1(name):
    print()
    chapter1()


