#                  Task - 04  ("Hangman Game ")

import random
from man_stages import stage

word_list= ["alphabet","black","white","read","green","blue","aqua","orange","pink","yellow","magenta"]
word_to_guess = random.choice(word_list)

attempts=6
dashes= ['_']*len(word_to_guess)
word_guessed= ''
guessed=False

def find(word, ltr):
    index_list=[]
    for i, j in enumerate(word):
        if j==ltr:
            index_list.append(i)
    return index_list

print('Lets play the hangman...')
print(' '.join(dashes))

while attempts>0 and not guessed:
    letter = input('Guess a letter: ')
    if letter in word_guessed:
        print("Aready guessed, try another :")
        print(' '.join(dashes))
    elif letter in word_to_guess:
        indices= find(word_to_guess, letter)
        for index in indices:
            dashes[index]=letter
        word_guessed=''.join(dashes)
        print(' '.join(dashes))
    elif letter not in word_to_guess:
        attempts-=1
        print('Letter not found in word, try again!\nOnly {} attempts left'.format(attempts))
        print(stage(attempts))

        

    else:
        print("Invalid input")

    if word_guessed==word_to_guess:
        guessed=True

if guessed:
    print('you won!')
else:
    print("You lost!")
