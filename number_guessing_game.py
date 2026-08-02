import random

while True:
    print("")
    print("Please Select Difficulty Level: ", "            Type 'exit' whenever you want to leave the game")
    print("Easy(1) => 10 attempts")
    print("Medium(2) => 7 attempts")
    print("Hard(3) => 5 attempts")
    user_mode = input("Final Decision: ").strip()
    print("")

    if user_mode == "1" or user_mode.lower() == "easy":
        Secret = random.randint(1, 100)
        total_attempts = 10
        low = 1
        high = 100
        while total_attempts > 0:
            try:
                raw_input = input(f"Enter a number between {low} and {high}: ").strip()

                if raw_input.lower() == "exit":
                    print("Thank you for playing! Hope you enjoyed it!")
                    exit()

                user_input = int(raw_input)
                total_attempts = total_attempts - 1

                if user_input == Secret:
                    print("🎉 You guessed the number! You won!\n")
                    break
                if user_input < Secret:
                    if user_input > low:
                        low = user_input
                    print(f"Higher ↑  You've {total_attempts} attempts left", "\n")
                if user_input > Secret:
                    if user_input < high:
                        high = user_input
                    print(f"Lower ↓  You've {total_attempts} attempts left", "\n")
                if total_attempts == 0:
                    print(f"You lost! You've run out of attempts! Secret was: {Secret}\n")

            except ValueError:
                print("Please enter a single whole number only!", "\n")
                continue

        while True:
            user_continue = input("Let's Play Another Game? Yes(1) / No(2): ").strip()
            if user_continue == "1" or user_continue.lower() == "yes":
                break
            elif user_continue == "2" or user_continue.lower() == "no":
                print("Thank you for playing! Hope you enjoyed it!")
                exit()
            else:
                print("Pick 1 / 2 only!\n")
                continue

    elif user_mode == "2" or user_mode.lower() == "medium":
        Secret = random.randint(1, 100)
        total_attempts = 7
        low = 1
        high = 100

        while total_attempts > 0:
            try:
                raw_input = input(f"Enter a number between {low} and {high}: ").strip()

                if raw_input.lower() == "exit":
                    print("Thank you for playing! Hope you enjoyed it!")
                    exit()

                user_input = int(raw_input)
                total_attempts = total_attempts - 1

                if user_input == Secret:
                    print("🎉 You guessed the number! You won!\n")
                    break

                if user_input < Secret:
                    if user_input > low:
                        low = user_input
                    print(f"Higher ↑  You've {total_attempts} attempts left", "\n")

                if user_input > Secret:
                    if user_input < high:
                        high = user_input
                    print(f"Lower ↓  You've {total_attempts} attempts left", "\n")

                if total_attempts == 0:
                    print(f"You lost! You've run out of attempts! Secret was: {Secret}\n")

            except ValueError:
                print("Please enter a single whole number only!", "\n")
                continue

        while True:
            user_continue = input("Let's Play Another Game? Yes(1) / No(2): ").strip()
            if user_continue == "1" or user_continue.lower() == "yes":
                break
            elif user_continue == "2" or user_continue.lower() == "no":
                print("Thank you for playing! Hope you enjoyed it!")
                exit()
            else:
                print("Pick 1 / 2 only!\n")
                continue

    elif user_mode == "3" or user_mode.lower() == "hard":
        Secret = random.randint(1, 100)
        total_attempts = 5
        low = 1
        high = 100

        while total_attempts > 0:
            try:
                raw_input = input(f"Enter a number between {low} and {high}: ").strip()

                if raw_input.lower() == "exit":
                    print("Thank you for playing! Hope you enjoyed it!")
                    exit()

                user_input = int(raw_input)
                total_attempts = total_attempts - 1

                if user_input == Secret:
                    print("🎉 You guessed the number! You won!\n")
                    break

                if user_input < Secret:
                    if user_input > low:
                        low = user_input
                    print(f"Higher ↑  You've {total_attempts} attempts left", "\n")

                if user_input > Secret:
                    if user_input < high:
                        high = user_input
                    print(f"Lower ↓  You've {total_attempts} attempts left", "\n")

                if total_attempts == 0:
                    print(f"You lost! You've run out of attempts! Secret was: {Secret}\n")

            except ValueError:
                print("Please enter a single whole number only!", "\n")
                continue

        while True:
            user_continue = input("Let's Play Another Game? Yes(1) / No(2): ").strip()
            if user_continue == "1" or user_continue.lower() == "yes":
                break
            elif user_continue == "2" or user_continue.lower() == "no":
                print("Thank you for playing! Hope you enjoyed it!")
                exit()
            else:
                print("Pick 1 / 2 only!\n")
                continue

    elif user_mode.lower() == "exit":
        print("Thank you for playing! Hope you enjoyed it!")
        break
    else:
        print("You can pick 1 / 2 / 3 Only\n")
