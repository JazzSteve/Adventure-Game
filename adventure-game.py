import time
import random


def play_game():
    items = []
    enemy_list = ["six foot wolf man", "witch", "vampire", "ogre", "troll"]
    enemy = random.choice(enemy_list)
    get_enemy()
    intro(enemy)
    choose_path(items, enemy)


def get_enemy():
    enemy_list = ["six foot wolf man", "witch", "vampire", "ogre", "troll"]
    enemy = random.choice(enemy_list)


get_enemy()


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1="1", option2="2", yes="y", no="n"):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif yes in response:
            break
        elif no in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


# Introduction
def intro(enemy):
    print_pause("You’ve heard the stories your whole childhood.")
    print("About how every decade a", enemy, "comes to "
          "destroy the cattle in your town.")
    time.sleep(2)
    print_pause("So with this being the year, you decide to do "
                "something about it.")
    print_pause("One night, on foot and alone, you set out on a "
                "mission to find it.")
    print_pause("While you're walking through the woods, you see "
                "the path you're on split into two directions.")
    print_pause("The path on the right is overgrown and full of "
                "plants with thorns.")
    print_pause("The path on the left is clear and has "
                "beautifully grown flowers.")


# Going down the right path with or w/o sword
def right_path(items, enemy):
    print_pause("You walk down the path on the right.")

    if "sword" in items:
        print_pause("You see the same crate you took the "
                    "sword out of, nothing new.")
        print_pause("You walk back to the center of the two paths.")
    else:
        print_pause("It turns out the thorns weren't thorns at "
                    "all, and they are actually quite soft.")
        print_pause("The overgrown plants come to a quick end and "
                    "you’re able to see a crate tucked behind a tree.")
        print_pause("You look in the crate and behold!")
        print_pause("You found a sword!")
        items.append("sword")
        print_pause("You walk back to the center of the two paths.")
    choose_path(items, enemy)


# Going down the left path
def left_path(items, enemy):
    print_pause("You walk down the path on the left")
    print_pause("You come to a field with tall and pretty flowers, "
                "and walk through it.")
    print_pause("You hear a shuffling through the grass")
    print("Oh no it's the", enemy, "!")
    time.sleep(2)

    if "sword" in items:
        while True:
            choice = valid_input("Would you like to (1) fight or"
                                 "(2) run away?\n (Please enter 1 or 2.)\n")

            if choice == '1':
                print("The", enemy, "charges towards you, but you bring "
                      "out your sword.")
                time.sleep(2)
                print_pause("You proudly hold it, getting ready to use it.")
                print_pause("Swish! It happens so fast.")
                print("You’ve defeated the", enemy, "!")
                time.sleep(2)
                print_pause("Your town will be very happy.")
                play_again(items, enemy)
            elif choice == '2':
                print_pause("You run back to the center of the two paths. "
                            "Looks like it doesn’t know where you are.")
                choose_path(items, enemy)
    else:
        print_pause("It charges you and knocks you to the ground.")
        print_pause("You see a sharp but thin stick on the ground.")
        while True:
            choice = valid_input("Would you like to (1) fight or "
                                 "(2) run away?\n (Please enter 1 or 2.)\n")

            if choice == '1':
                print_pause("You pick up the stick and fight.")
                print_pause("But the thin stick breaks when you swing it.")
                print_pause("You have been defeated!")
                play_again(items, enemy)
            elif choice == '2':
                print_pause("You run back to the center of the two paths. "
                            "Looks like it doesn’t know where you are.")
                choose_path(items, enemy)


def choose_path(items, enemy):
    print_pause("Enter 1 to walk down the path on the right.")
    print_pause("Enter 2 to walk down the path on the left.")
    path = valid_input("Which path do you want to walk down?\n"
                       "(Please enter 1 or 2.)\n")
    if path == '1':
        right_path(items, enemy)
    elif path == '2':
        left_path(items, enemy)


def play_again(items, enemy):
    again = valid_input("Would you like to play again? (y/n)\n")

    if again == 'y':
        print_pause("Excellent! Restarting the game…")
        get_enemy()
        play_game()
    elif again == 'n':
        print("Thanks for playing! See you next time.")
        exit()


play_game()