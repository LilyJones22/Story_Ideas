import random

characters = ["a", "b", "c", "d"] # all main characters
arcs = ["A", "B", "C", "D"] # different plot arcs

def random_arc(): # random plot arc
    choice = random.choice(arcs)
    print(f"Plot arc: {choice}")

def random_char(): # random character
    choice = random.choice(characters)
    print(f"Character: {choice}")

def random_char_arc(): # random character and random plot arc
    plot = random.choice(arcs)
    char = random.choice(characters)
    print(f"Plot Arc: {plot}")
    print(f"Character: {char}")

def random_multi_char(): # selects multiple characters
    chars = []
    while True:
        num = int(input("How many characters total?: "))

        if num < 2 or num > len(characters):
            print("Not an accepted number. Please try again.")
            continue
        break

    while len(chars) < num:
        char = random.choice(characters)

        if char not in chars:
            chars.append(char)

    print("Characters:", end=" ")

    for char in chars:
        print(f"{char}", end= " ")
        



def menu(): # menu of all avaliable options
    print("\n1: A random plot arc")
    print("2: A random character")
    print("3: A random plot arc with a random character")
    print("4: Multiple characters")
    print("X: End program")

while True:
    try:
        menu()
        choice = input()

        if choice == "1":
            random_arc()
        elif choice == "2":
            random_char()
        elif choice == "3":
            random_char_arc()
        elif choice == "4":
            random_multi_char()
        elif choice.upper() == "X":
            break
        else:
            raise ValueError


    except ValueError:
        print("Not an accepted input. Please try again.")
        choice = input()

print("Goodbye")