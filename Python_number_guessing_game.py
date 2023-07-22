from random import randint
import sys
correct_answer = randint(int(sys.argv[1]), int(sys.argv[2]))
while True:
    try:  
        guess = input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  ')
        guess = int(guess)
        if 0 < guess < 11:
                    print("All good")
                    if guess == correct_answer:
                        print("You are correct! Good Guess!")
                        break
                    else:
                          print("Wrong answer, try again")

    except ValueError:
          print("Please enter a valid number within 1 to 10")
          continue

        