import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_img = [rock, paper, scissors]

while True:
    user_choice = int(
        input("What do you choose?\n0 for rock\n1 for paper\n2 for scissors.\n")
    )
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, so you lose.")
    else:
        print(game_img[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_img[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif user_choice == 2 and computer_choice == 0:
            print("Computer wins!")
        elif computer_choice > user_choice:
            print("Computer wins!")
        elif user_choice > computer_choice:
            print("You win!")
        elif user_choice == computer_choice:
            print("It's a tie")

    continue_playing = input(
        "Do you want to play again? Type 'yes' to continue, or anything else to exit: "
    ).lower()
    if continue_playing != "yes":
        print("Thanks for playing!")
        break
