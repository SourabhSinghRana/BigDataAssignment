## Assignment Part-1




Q1. Why do we call Python as a general-purpose and high-level programming language?

Ans: Python is called a general-purpose programming language because it can be used to solve a wide range of problems across various domains, such as web development, data analysis, artificial intelligence, scientific computing, and more. Python is also a high-level programming language, which means it provides an abstraction over low-level details such as memory management, which makes it easier to write and read code.




Q2. Why is Python called a dynamically typed language?

Ans: Python is called a dynamically typed language because the data types of variables are determined at runtime rather than compile time. This means that the type of a variable can change during the execution of a program, based on the value that is assigned to it.




Q3. List some pros and cons of the Python programming language.

Ans:
Pros:
Easy to learn and read
Large standard library
Cross-platform support
Wide range of applications
Dynamically typed
Cons:
Slow performance compared to compiled languages
GIL (Global Interpreter Lock) limits parallelism
Weak in mobile application development




Q4. In what all domains can we use Python?

Ans: Python can be used in a wide range of domains, including web development, data analysis, machine learning, artificial intelligence, scientific computing, game development, and more.




Q5. What are variables, and how can we declare them?

Ans: Variables are used to store values in a program, such as numbers, strings, or Boolean values. In Python, we can declare a variable by assigning a value to it using the assignment operator (=). For example, we can declare a variable named "x" and assign it the value 10 as follows:
    x=10




Q6. How can we take input from the user in Python?

Ans: We can take input from the user in Python using the input() function. For example, the following code asks the user to enter their name and then displays a greeting message:
    name = input("Enter your name: ")
    print("Hello, " + name + "!")




Q7. What is the default data type of the value that has been taken as input using the input() function?

Ans: The default data type of the value that has been taken as input using the input() function is a string.




Q8. What is typecasting?

Ans: Typecasting is the process of converting a value from one data type to another. In Python, we can use built-in functions like int(), float(), str(), and bool() to perform typecasting.




Q9. Can we take more than one input from the user using a single input() function? If yes, how? If no, why?

Ans: No, we cannot take more than one input from the user using a single input() function. We need to call the input() function separately for each input that we want to take.




Q10. What are keywords?

Ans: Keywords are reserved words in Python that have a specific meaning and cannot be used as variable names or function names. Examples of keywords in Python include if, else, for, while, and def.




Q11. Can we use keywords as a variable? Support your answer with reason.

Ans: No, we cannot use keywords as variable names because keywords have a specific meaning in Python, and using them as variable names can cause syntax errors.




Q12. What is indentation? What is the use of indentation in Python?

Ans: Indentation refers to the spaces or tabs that are used at the beginning of a line in Python code. In Python, indentation is used to define the scope of code.




Q13. How can we throw some output in Python?

Ans. We can use the print() function to throw some output in Python. For example, to print the text "Hello World", we can use the following code:
print("Hello World")




Q14. What are operators in Python?

Ans. Operators in Python are special symbols that are used to perform operations on variables and values. Python has various types of operators such as arithmetic operators, comparison operators, logical operators, bitwise operators, etc.




Q15. What is the difference between / and // operators?

Ans. The / operator performs floating-point division, whereas the // operator performs integer division. For example:
7 / 2   # Output: 3.5
7 // 2  # Output: 3




Q16. Write a code that gives the following as an output.

iNeuroniNeuroniNeuroniNeuron
Ans. Here is the code that gives the desired output:
print("iNeuron" * 4 + "Neuron")




Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

Ans. Here is the code to take a number as input from the user and check if the number is odd or even:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")




Q18. What are boolean operators?

Ans. Boolean operators are operators that operate on boolean values (True or False). The most commonly used boolean operators in Python are 'and', 'or', and 'not'.




Q19. What will be the output of the following?

1 or 0
0 and 0
True and False and True
1 or 0 or 0
Ans. The output of the above expressions would be:
1
0
False
1




Q20. What are conditional statements in Python?

Ans. Conditional statements are used in Python to execute different statements based on different conditions. The two most commonly used conditional statements in Python are 'if' and 'if-else'.




Q21. What is the use of 'if', 'elif' and 'else' keywords?

Ans. 'if', 'elif' and 'else' are conditional statements in Python. 'if' is used to test a condition, and if the condition is true, then it executes a block of code. 'elif' is used for multiple conditions, and if any of the conditions are true, it executes the corresponding block of code. 'else' is used for any other condition that is not covered by 'if' or 'elif'.




Q22. Write a code to take the age of a person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

Ans. Here is the code to take the age of a person as an input and display whether the person can vote or not:
age = int(input("Enter your age: "))
if age >= 18:
    print("I can vote")
else:
    print("I can't vote")




Q23. Here's the code that displays the sum of all the even numbers from the given list:

numbers = [12, 75, 150, 180, 145, 525, 50]
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
print("Sum of all even numbers in the list:", sum_even)




Q24. Here's the code to take 3 numbers as an input from the user and display the greatest number as output:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)




Q25. Here's the program that displays only those numbers from a list that satisfy the following conditions:

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0:
        if num > 150:
            continue
        elif num > 500:
            break
        else:
            print(num)
Output:
75
150
50