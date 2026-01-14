"""
Druhý projekt Projekt: Bulls & Cows do Engeto Online Python Akademie
author: Květoslav Leidorf
email: k.leidorf@gmail.com
discord: kvetos_95684
"""

import random
import time
from typing import Tuple

SEPARATOR = "-" * 47
DIGITS_COUNT = 4

def generate_secret_number(length: int) -> str:
    """Generuje unikátní n-místné číslo, které nezačíná nulou."""
    digits = list("0123456789")
    while True:
        random.shuffle(digits)
        secret = digits[:length]
        if secret[0] != "0":
            return "".join(secret)

def validate_input(user_input: str, length: int) -> Tuple[bool, str]:
    """Validuje vstup uživatele na délku, unikátnost, číslice a nulu na začátku."""
    if not user_input.isdigit():
        return False, "Input must contain digits only."
    if len(user_input) != length:
        return False, f"Input must have exactly {length} digits."
    if user_input.startswith("0"):
        return False, "Number cannot start with zero."
    if len(set(user_input)) != length:
        return False, "Digits must be unique (no duplicates)."
    return True, ""

def evaluate_guess(secret: str, guess: str) -> Tuple[int, int]:
    """Vypočítá počet bulls (shoda pozice i čísla) a cows (shoda čísla)."""
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def get_label(count: int, label: str) -> str:
    """Vrací správné jednotné nebo množné číslo pro bull/cow."""
    return f"{count} {label}" if count == 1 else f"{count} {label}s"

def play_game() -> None:
    """Hlavní smyčka hry Bulls & Cows."""
    print("Hi there!", SEPARATOR, 
          "I've generated a random 4 digit number for you.",
          "Let's play a bulls and cows game.", SEPARATOR, sep="\n")
    
    secret_number = generate_secret_number(DIGITS_COUNT)
    attempts = 0
    start_time = time.time()

    while True:
        print("Enter a number:")
        print(SEPARATOR)
        guess = input(">>> ").strip()
        attempts += 1

        is_valid, message = validate_input(guess, DIGITS_COUNT)
        if not is_valid:
            print(message, SEPARATOR, sep="\n")
            continue

        if guess == secret_number:
            elapsed_time = round(time.time() - start_time, 2)
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!",
                  SEPARATOR, "That's amazing!", f"Time spent: {elapsed_time}s", sep="\n")
            break

        bulls, cows = evaluate_guess(secret_number, guess)
        print(f"{get_label(bulls, 'bull')}, {get_label(cows, 'cow')}")
        print(SEPARATOR)

# Spuštění hlavní smyčky hry
if __name__ == "__main__":
    play_game()
