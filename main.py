import random
from wordlist import word_list
from Hangman import logo
from Hangman import stages


# main code
end_of_game = False
print(logo)
lives = 6
guessed_list = []
random_word = random.choice(word_list)

# replacing the letters with "_"
Display = []
for _ in random_word:
    Display += "_"
print(Display)
# so now I have chosen now I have to do is to match the words enter by the user
while not end_of_game:
    # now we will see the to put the guessed number at the place
    guessed = input("Enter the letter you want to check").lower()
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guessed:
            Display[position] = letter

    # to check if the letter is present in the list or not
    if guessed in guessed_list:
        print(f"You have already guessed it {guessed}")
    guessed_list.append(guessed)

    if guessed not in random_word:
        lives -= 1
        print(f"You guessed {guessed} which is wrong, oh no u loose a life!")
        if lives == 0:
            end_of_game = True
            print("You lose")
        print(f"Number of lives {lives}")

    if "_" not in Display:
        end_of_game = True
        print("You won")

    print(Display)
    print(f"Number of lives {lives}")

    print(stages[lives])
