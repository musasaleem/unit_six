# Name: Musa Saleem
# Date : 10/25/2018
# Last Modified : 10/25/18
# Comments: This program is about making prime numbers from the first prime number, 2 up until whichever number the user
# wants to pick. The number can not be less than two, however, or else, the prime number list will be blank. Used code
# for lists.The goal which was accomplished: having short line of code that repeats no matter which number user chooses.
# I get user number and run all prime numbers from the first prime number (2), up until the users number they picked.
# For example, if user picked the number 24, computer will spit out prime numbers from 2 until 23.


def main():
    number = int(input("Choose any number, it must be greater than or equal to two"))  # asks user for number they want
    listofnumbers = []  # Symbol for list of numbers
    for x in range(2, number):  # What the range of numbers varies from. 2- the number student chooses
        listofnumbers.append(x)  # Adds the number the user chooses
    primenumbers = []  # Symbol for prime numbers
    while len(listofnumbers) > 0:  # Giving a while loop as to when the number is greater than 2
        first = listofnumbers[0]  # giving the first number in the listofnumber's function be equal to the word first
        primenumbers.append(first)  # first number is always prime, add it to the prime list
        for prime in listofnumbers:  # Function for finding prime
            if prime % first == 0:  # Finding out if a number is prime
                listofnumbers.remove(prime)  # Removing all the numbers that are not prime
    print(primenumbers)  # printing of the prime numbers


main()
