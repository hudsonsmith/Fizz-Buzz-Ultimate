from time import sleep
from os import system, name


i: int = 0
points: int = 0
lives: int = 5


def custom_banner(line1: str = "", line2: str = "") -> str:
    banner = f"""
          \\  '  ,
        . ' \\ ' , . ,
          \\  . ' /
             ,
  \033[0;34m________\033[0;32m./B|\033[0;34m_
 \033[0;34m/             \\
/\033[0;31m^^^^^^^^^^^^^^^\033[0;34m\\
\033[0;31m|   \033[0m_________   \033[0;31m|
|   \033[0mFizz Buzz   \033[0;31m|\033[0;32m{line1}
\033[0;31m|   \033[0m^^^^^^^^^   \033[0;31m|\033[0;32m{line2}
\033[0;31m|               |
|               |
|               |
|               |
|_______________|\033[0m
\033[0;34m\\,,,,,,,,,,,,,,,/
 \\_____________/\033[0m
"""

    return banner


def clear() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")


def play_again() -> bool:
    while True:
        try:
            clear()
            print(
                custom_banner("      YOU ARE DEAD.", f"   {points} FizzBuzz's Drank!")
            )

            answer = input(
                "\033[0;32mWould you like to play again?\n\033[0;34m[y]es/[n]o/[r]age_quit: \033[0m"
            )

            if "y" in answer:
                return True

            elif "n" in answer or "r" in answer:
                return False

        except KeyboardInterrupt:
            continue


# Display the title screen.
clear()
try:
    input(custom_banner("     Press [ENTER]", "       To Start"))

except KeyboardInterrupt:
    print("\n\033[36mGoodbye!\033[0m")
    exit()

while True:
    clear()
    print(
        custom_banner(f"     {points} FizzBuzz's Drank!", f"        {lives} Lives Left")
    )
    i += 1

    if (i % 3 == 0) and (i % 5 == 0):
        try:
            print("\033[36mFizz\033[0m\033[31mBuzz\033[0m")
            sleep(0.3)

        except KeyboardInterrupt:
            points += 3

    elif i % 3 == 0:
        try:
            print("\033[36mFizz\033[0m")
            sleep(0.3)

        except KeyboardInterrupt:
            points += 1

    elif i % 5 == 0:
        try:
            print("\033[31mBuzz\033[0m")
            sleep(0.3)

        except KeyboardInterrupt:
            points += 1

    else:
        try:
            print(i)
            sleep(0.3)

        except KeyboardInterrupt:
            lives -= 1

            if lives <= 0:
                if play_again() is True:
                    i = 0
                    points = 0
                    lives = 5
                else:
                    print("\n\033[36mGoodbye!\033[0m")
                    exit()
