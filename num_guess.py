#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Dec 2021
# This program checks if there is over 30 students


import constants


def main():
    # this function checks if there is over 30 students

    # input
    guess_number = int(input("Enter your number: "))
    print("")

    # process & output
    if guess_number == constants.CORRECT:
        print("You guessed correctly!")
        
    if guess_number != constants.CORRECT:
        print ("you guessed incorrectly!")


if __name__ == "__main__":
    main() 