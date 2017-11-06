Work through the practice problems provided in this repository.

Exercise 1: 
Write a program that asks the user to enter his or her name. The program should
respond with a message that says hello to the user, using his or her name.


Exercise 2:
Write a program that asks the user to enter the width and length of a room. Once the values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating point numbers. Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.

Exercise 3: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and always displays exactly two decimal places.

Exercise 4: 
In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.

Exercise 5: 
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.

Exercise 6: 
Write a Python program to construct the following pattern, using a nested for loop.

    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    *

Exercise 7: 
This exercise examines the process of identifying the maximum value in a collection of integers. Each of the integers will be randomly selected from the numbers between 1 and 100. The collection of integers may contain duplicate values, and some of the
integers between 1 and 100 may not be present. Create a list of randomly generated integers that is 10 items long. Then find the greatest number in that list without using the max() built in function.

Take a moment and think about how you would handle this problem on paper.

Many people would check each integer in sequence and ask themself if the number that they are currently considering is larger than the largest number that they have seen previously. If it is, then they forget the previous maximum number and remember the current number as the new maximum number. This is a reasonable approach, and will result in the correct answer when the process is performed carefully. If you were performing this task, how many times would you expect to need to update the maximum value and remember a new number? Hint: from random import randrange

Exercise 8:
Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

Exercise 9: 
A prime number is an integer greater than 1 that is only divisible by one and itself. Write a program that goes from 1-100 and determines whether or not a number is prime, printing "Prime" if it is, and the number otherwise.

Exercise 10: Multiplication Table
In this exercise you will create a program that displays a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10. Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10. It should also include labels down the left side consisting of the numbers 1 through 10. 
When completing this exercise you will probably find it helpful to be able to print out a value without moving down to the next line. This can be accomplished by added end="" as the last parameter to your print statement. For example, print("A") will display the letter A and then move down to the next line. The statement print("A", end="") will display the letter A without moving down to the next line, causing the next print statement to display its result on the same line as the letter A.

Exercise 11:
A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.

Exercise 1. Avoiding Duplicates.
Avoiding Duplicates In this exercise, you will create a program that reads words from the user until the user enters “quit”. After the user enters a blank line your program should dis- play each word entered by the user exactly once. The words should be displayed in the same order that they were entered. For example, if the user enters:
      first 
      second 
      first
      third 
      second
then your program should display:
      first 
      second 
      third


Exercise 2. Shuffling a Deck of Cards.
A standard deck of playing cards contains 52 cards. Each card has one of four suits along with a value. The suits are normally spades, hearts, diamonds and clubs while the values are 2 through 10, Jack, Queen, King and Ace. Each playing card can be represented using two characters. The first character is the value of the card, with the values 2 through 9 being represented directly. The characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack, Queen, King and Ace respectively. The second character is used to represent the suit of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for clubs. The following table provides several examples of cards and their two-character representations.

      Card               Abbreviation
      Jack of spades     Js
      Two of clubs       2c
      Ten of diamonds    Td
      Ace of hearts      Ah 
      Nine of spades     9s

Write your code to take this list of cards and shuffle them. One technique that can be used to shuffle the cards is to visit each element in the list and swap it with another random element in the list; do this shuffle a random amount of times. You must write your own loop for shuffling the cards. You cannot make use of Python’s built-in shuffle function.
