#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program gets 10 random numbers then finds the average using an array

import random


def main():
    # This function gets random numbers then finds the average using an array

    # Array
    list_array = []

    # Process
    for repeater in range(10):
        number = random.randint(1, 100)
        print("Random number " + str(repeater) + " is " + str(number))
        list_array.append(number)

    average = sum(list_array)/10

    # Output
    print("The average of the numbers is: " + str(average))


if __name__ == "__main__":
    main()
