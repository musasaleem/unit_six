# Name: Musa Saleem
# Date : 10/25/2018
# Last Modified : 10/25/18
# Comments: This program is about making prime numbers from the first prime number, 2 up until whichever number the user
# wants to pick. The number can not be less than two, however, or else, the prime number list will be blank. Used code
# for lists. The goal which was accomplished: having short line of code that repeats no matter which number user chooses


def main():
    """
The main function, where I get user number and run all prime numbers from the first prime number (2), up until the users 
number they picked. For example, if user picked the number 24, computer will spit out prime numbers from 2 until 23
    :return: 
    """
    number = int(input("Choose any number, it must be greater than or equal to two"))
    listofnumbers = []
    for x in range(2, number):
        listofnumbers.append(x)
    primenumbers = []
    while len(listofnumbers) > 0:
        first = listofnumbers[0]
        primenumbers.append(first) # first number is always prime, add it to the prime list
        for prime in listofnumbers:
            if prime % first == 0:
                listofnumbers.remove(prime)
    print(primenumbers)


main()
