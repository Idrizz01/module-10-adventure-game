#idris adeyemi
#12/3/21
def intro():
    print("**  Game created by Idris Adeyemi   **")
    print("**  the game takes place in an ancient mystic world  ")
    print("**  the mission is to retrieve an orb from the dark forest to save your mother  **")
    print("**  along the game the player will explore his powers and how to use them  **")

def main():
    print(" provide a name you want to use in the game")
    user = input("[username: ]")
    intro()
    answer = input("\n start the game ?(y/n): ")
    answer = answer.upper()
    if answer == 'Y':
        print("start,chapter 1")
        import chapter1
        chapter1.chapter1()

    elif answer == 'n':
        print(" No. ")

main()

