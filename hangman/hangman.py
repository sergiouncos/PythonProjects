import random
import hangman_logo



word_list = ["manzana", "pera", "banana"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6


print(hangman_logo)
print(f"The word is {chosen_word}")

# fill with blank spaces or _
display = []
for _ in chosen_word:
    display += "_"

player_won = False
while not player_won:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"The current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -= 1
        print (hangman_logo.stages[lives])
        if lives == 0:
            player_won = True
            print("You lose.")
            
    print(f"{' '.join(display)}")

    if "_" not in display:
        player_won = True
        print("You Win.")
        
#It can be improved the UX experience giving better inputs or output at each
#entry as well as adding more words imported from another file.

