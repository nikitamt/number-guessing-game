import random

def separator():
    print("-" * 30)

def user_input(request) -> int:
    temp = input(request)
    while not temp.isdigit():
        print("Please, type a number next time.")
        temp = input(request)
    temp = int(temp)
    while temp <= 0:
        print("Please, type a number larger then 0 next time.")
        temp = int(input(request))
    return temp

def play_round(random_number) -> bool:
    user_guess = user_input("Make a guess: ")

    if user_guess == random_number:
        separator()
        print("You got it!")
        return True
    elif user_guess < random_number:
        print("You were above the number!")
    elif user_guess > random_number:
        print("You were below the number!")
    return False


def main() -> None:
    print("Hello, Welcome to the my game!")
    separator()

    top_of_range = user_input("Type a number: ")

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        if play_round(random_number):
            break

    print(f"You got it in {guesses} guesses.")
    return

if __name__ == "__main__":
    main()