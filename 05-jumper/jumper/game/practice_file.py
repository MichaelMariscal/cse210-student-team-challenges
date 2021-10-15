from random import random


random_word = ["shark"]
blanks = ['_','_','_','_','_']
guess = "r"
store_letters = []

for letter in random_word:
    for char in letter:
        store_letters.append(char)
    print(store_letters)

indexed_number = store_letters.index(guess)
print(indexed_number)
blanks[indexed_number] = guess

for piece in blanks:
    print(piece, end=" ")

    #if guess in store_letters:
     #   print(guess)

