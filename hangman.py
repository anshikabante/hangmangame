# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:43:22 2026

@author: Asus
"""

import random

words = ["python", "apple", "laptop", "college", "student"]

word = random.choice(words)
guessed = []
attempts = 6

display = ["_"] * len(word)

print("Welcome to Hangman Game")

while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    letter = input("Enter a letter: ").lower()

    if letter in guessed:
        print("You already guessed this letter")
        continue

    guessed.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in display:
    print("\nCongratulations! You guessed:", word)
else:
    print("\nGame Over! Word was:", word)