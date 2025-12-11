import random

def separator():
    print("-" * 30)

def get_user_input(request: str) -> int:

    while True:
        user_input = input(request).strip()
        try:
            user_input = int(user_input)
            if user_input <= 0:
                print("Please, type a number larger than 0 next time.")
                continue
            return user_input
        except ValueError:
            print("Please, type a number next time.")

def play_round(random_number: int) -> bool:
    user_guess = get_user_input("Make a guess: ")

    if user_guess == random_number:
        separator()
        print("You got it!")
        return True
    elif user_guess < random_number:
        print("You were below the number!")
    elif user_guess > random_number:
        print("You were above the number!")
    return False

def get_hidden_number() -> int:
    top_of_range = get_user_input("Type a number: ")
    random_number = random.randint(1, top_of_range)
    return random_number

def main() -> None:
    print("Hello, Welcome to my game!")
    separator()

    random_number = get_hidden_number()
    guesses = 0

    while True:
        guesses += 1
        if play_round(random_number):
            break

    print(f"You got it in {guesses} guesses.")
    return

if __name__ == "__main__":
    main()