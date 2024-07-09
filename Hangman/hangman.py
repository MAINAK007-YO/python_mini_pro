from hang_art import logo, stages
from hang_word import word_list
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

lives = 6
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose.")
            print(f"The correct word was: {chosen_word}")
            end_of_game = True

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    print(stages[lives])
