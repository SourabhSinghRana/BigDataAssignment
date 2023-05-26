



Q1. Why do we call Python as a general purpose and high-level programming language?

Ans: Python is a general-purpose programming language because it can be used for various applications such as web development, game development, scientific computing, data analysis, artificial intelligence, etc. It is called a high-level programming language because it is designed to be easy to read and write, with a syntax that is closer to human language than to machine language.




Q2. Why is Python called a dynamically typed language?

Ans: Python is called a dynamically typed language because the data type of a variable is determined at runtime instead of compile time. This means that you don't have to declare the data type of a variable explicitly, and it can be changed during the execution of the program.




Q3. List some pros and cons of Python programming language?

Ans:
Pros of Python:
Easy to learn and read
Rich library support for various tasks
Cross-platform compatibility
Interactive interpreter for testing and prototyping
Large community support and resources available
Supports multiple programming paradigms
Cons of Python:
Slower than low-level languages like C or C++
Not suited for high-performance computing or low-level system programming
GIL (Global Interpreter Lock) limits multithreading performance
Limited support for mobile app development




Q4. In what all domains can we use Python?

Ans: Python can be used in various domains, including:
Web development (Django, Flask)
Scientific computing (NumPy, SciPy)
Data analysis and visualization (Pandas, Matplotlib)
Artificial Intelligence and Machine Learning (TensorFlow, PyTorch)
Game development (Pygame)
Automation and scripting (Bash scripting, Selenium)
Desktop applications (PyQt, Tkinter)
Network programming (Twisted)




Q5. What are variables and how can we declare them?

Ans: Variables are containers that hold values in a program. In Python, we can declare a variable by assigning a value to it using the = operator. For example:
x = 10
In this example, the variable x is declared and assigned the value 10. We can also assign a value to multiple variables at once, like this:
x, y, z = 10, 20, 30
In this example, the variables x, y, and z are declared and assigned the values 10, 20, and 30, respectively.




Q6. How can we take input from the user in Python?

Ans: We can take input from the user in Python using the input() function. The input() function reads a line of text from the user and returns it as a string. For example:
name = input("Enter your name: ")
In this example, the input() function prompts the user to enter their name, and the value entered by the user is stored in the variable name.




Q7. What is the default data type of the value that has been taken as an input using input() function?

Ans: The default data type of the value that has been taken as an input using input() function is a string.




Q8. What is type casting?

Ans: Type casting is the process of converting a value from one data type to another. In Python, we can use the built-in functions int(), float(), str(), etc. to cast a value to a different data type. For example:
x = "10"
y = int(x)
In this example, the string "10" is cast to an integer using the int() function and stored in the variable y.




Q9. Can we take more than one input from the user using a single input() function? If yes, how? If no, why?

Ans: Yes, we can take more than one input from the user using a single input() function by separating the values with a space or any other separator. For example:
x, y = input("Enter two numbers: ").split()
In this example, the input() function prompts the user to enter two numbers, and the values entered by the user are separated by a space. The split() function is used to split the input string into two separate strings, which are then assigned to the variables x and y.




Q10. What are keywords?

Ans: Keywords are reserved words in Python that have a special meaning and cannot be used as variable names or function names. Keywords are used to define the syntax and structure of the Python language, and they are used to perform specific operations or actions. Some examples of keywords in Python are if, else, while, for, def, and class.




Q11. Can we use keywords as a variable? Support your answer with reason.

Ans: No, we cannot use keywords as a variable because keywords have a special meaning in Python and are used to define the syntax and structure of the language. Using a keyword as a variable name would result in a syntax error because the interpreter would not know how to interpret the code. For example, the following code would result in a syntax error:
if = 10




Q12. What is indentation? What's the use of indentation in Python?

Ans: Indentation is the spacing at the beginning of a line of code in Python. In Python, indentation is used to indicate the grouping of statements and to define the scope of functions, loops, and conditional statements. The use of indentation makes the code easier to read and understand, and it helps to avoid errors in the code.




Q13. How can we throw some output in Python?

Ans: We can output data in Python using the print() function. The print() function takes one or more arguments and prints them to the console or output window. For example:
print("Hello, world!")
In this example, the print() function outputs the string "Hello, world!" to the console.




Q14. What are operators in Python?

Ans: Operators in Python are symbols or keywords that perform various operations on operands, such as variables, values, or expressions. Python supports various types of operators, including arithmetic operators (+, -, *, /), assignment operators (=, +=, -=, *=), comparison operators (==, !=, <, >), logical operators (and, or, not), bitwise operators (&, |, ^), and more.




Q15. What is the difference between / and // operators?

Ans: The / operator performs floating-point division, which means that it returns a float value even if the operands are integers. For example, 5/2 would return 2.5.
The // operator performs integer division, which means that it returns an integer value by rounding down to the nearest integer. For example, 5//2 would return 2.
So, the main difference between / and // operators is that / returns a float value, while // returns an integer value.




Q16. Write a code that gives following as an output.

Ans. Here's the code that gives the required output:
word = "Neuron"
print("i" + word * 4)
Output:
iNeuroniNeuroniNeuroniNeuron




Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

Ans. Here's the code that takes a number as an input from the user and checks if the number is odd or even:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")




Q18. What are boolean operators?

Ans. Boolean operators are operators that return either True or False. In Python, the three boolean operators are and, or, and not.




Q19. What will the output of the following?

1 or 0
0 and 0
True and False and True
1 or 0 or 0
Ans. The output of the following expressions will be:
1
0
False
1




Q20. What are conditional statements in Python?

Ans. Conditional statements in Python are used to make decisions based on certain conditions. These statements allow the program to execute different code depending on whether a condition is true or false.




Q21. What is the use of 'if', 'elif', and 'else' keywords?

Ans. The if, elif, and else keywords are used to create conditional statements in Python. if is used to specify a block of code to be executed if a condition is true. elif is used to specify a new condition to test if the previous condition(s) were false. else is used to specify a block of code to be executed if all the previous conditions were false.




Q22. Write a code to take the age of a person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

Ans. Here's the code that takes the age of a person as an input and displays whether the person can vote or not:
age = int(input("Enter your age: "))
if age >= 18:
    print("I can vote")
else:
    print("I can't vote")




Q23. Write a code that displays the sum of all the even numbers from the given list.

Ans. Here's the code that displays the sum of all the even numbers from the given list:
numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0
for num in numbers:
    if num % 2 == 0:
        sum += num
print("Sum of even numbers in the list is:", sum)




Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

Ans.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print("The greatest number is: ", a)
elif b > a and b > c:
    print("The greatest number is: ", b)
else:
    print("The greatest number is: ", c)




Q25. Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
Ans.
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0:
        if num > 150:
            continue
        elif num > 500:
            break
        else:
            print(num)




Q26. What is a string? How can we declare string in Python?

Ans. A string is a sequence of characters. In Python, we can declare a string by enclosing the characters within single quotes (' ') or double quotes (" ").
Example:
name = 'John'
address = "123 Main Street"




Q27. How can we access the string using its index?

Ans. We can access individual characters in a string using their index. The index starts from 0 for the first character, and goes up to n-1 for the nth character, where n is the length of the string.
Example:
string = "Hello, World!"
print(string[0])   # Output: H
print(string[6])   # Output: ,
print(string[-1])  # Output: !




Q28. Write a code to get the desired output of the following

string = "Big Data iNeuron"
desired_output = "iNeuron"
Ans.
string = "Big Data iNeuron"
desired_output = string[-7:]
print(desired_output)




Q29. Write a code to get the desired output of the following

string = "Big Data iNeuron"
desired_output = "norueNi"
Ans.
string = "Big Data iNeuron"
desired_output = string[-8:-14:-1]
print(desired_output)




Q30. Reverse the string given in the above question.

Ans.
string = "Big Data iNeuron"
reverse_string = string[::-1]
print(reverse_string)




Q31. How can you delete entire string at once?

Ans. In Python, we cannot delete the entire string at once because strings are immutable. We can only assign a new value to the variable containing the string to replace the old value.
Example:
string = "Hello, World!"
string = ""  # This will empty the string




Q32. What is escape sequence?

Ans: Escape sequence refers to a sequence of characters that begins with a backslash character '' and is used to represent a special character in a string. For example, '\n' represents a newline character, '\t' represents a tab character, '\b' represents a backspace character, and so on.




Q33. How can you print the below string?

'iNeuron's Big Data Course'
Ans: There are different ways to print the given string in Python. One way is to use double quotes to enclose the string so that the single quote inside the string does not cause a syntax error. Here's an example:
print("iNeuron's Big Data Course")
Output:
iNeuron's Big Data Course




Q34. What is a list in Python?

Ans: A list is a collection of items that are ordered and mutable in Python. It is one of the most commonly used data structures in Python. Lists can contain any type of data, such as integers, strings, floats, and other objects, and they can be nested to represent more complex data structures.




Q35. How can you create a list in Python?

Ans: In Python, we can create a list by enclosing a comma-separated sequence of items in square brackets []. Here's an example:
my_list = [1, 2, "Hello", 3.5, [4, 5]]
This creates a list called my_list that contains five items of different data types.




Q36. How can we access the elements in a list?

Ans: We can access the elements in a list by using their index, which starts from 0 for the first element and goes up to n-1 for the nth element, where n is the length of the list. We can use the square bracket notation [] to access an element at a particular index. Here's an example:
my_list = [1, 2, "Hello", 3.5, [4, 5]]
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: Hello
print(my_list[4][0])  # Output: 4




Q37. Write a code to access the word "iNeuron" from the given list.

lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
Ans:
We can access the word "iNeuron" from the given list by using the index of the list and the index of the element in the nested list. Here's an example:
my_list = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(my_list[4][2])  # Output: iNeuron




Q38. Take a list as an input from the user and find the length of the list.

Ans:
We can use the input() function to take a list as an input from the user, and the len() function to find the length of the list. Here's an example:
my_list = input("Enter a list of elements separated by commas: ").split(",")
print("The length of the list is:", len(my_list))
In this example, we first take the input from the user as a string of comma-separated values using the input() function. We then split the string into a list using the split() function, and finally find the length of the list using the len() function.




Q39. Here's the code to add the word "Big" in the 3rd index of the given list:

lst = ["Welcome", "to", "Data", "course"]
lst.insert(2, "Big")
print(lst)
Output:
['Welcome', 'to', 'Big', 'Data', 'course']




Q40. What is a tuple? How is it different from list?

In Python, a tuple is a collection of ordered, immutable elements enclosed within parentheses, while a list is a collection of ordered, mutable elements enclosed within square brackets. The main difference between a tuple and a list is that the elements of a tuple cannot be modified once the tuple is created, whereas the elements of a list can be modified.




Q41. How can you create a tuple in Python?

A tuple can be created by enclosing a sequence of elements within parentheses () and separating them by commas.
Here's an example:
my_tuple = (1, 2, 3, "hello", "world")




Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

No, we cannot add or modify elements in a tuple once it is created because tuples are immutable. If we try to add or modify elements in a tuple, it will result in a TypeError.




Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

No, we cannot append one tuple to another tuple directly. Tuples are immutable and their contents cannot be modified once they are created. However, we can concatenate two tuples using the + operator to create a new tuple that contains all the elements of both tuples.
Here's an example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple)
Output:
(1, 2, 3, 4, 5, 6)




Q44. Take a tuple as an input and print the count of elements in it.

We can use the len() function to get the count of elements in a tuple.
Here's an example:
my_tuple = (1, 2, 3, "hello", "world")
print(len(my_tuple))
Output:
5




Q45. What are sets in Python?

In Python, a set is an unordered collection of unique elements enclosed within curly braces {} or created using the set() function. Sets are mainly used for performing mathematical operations such as union, intersection, and difference.




Q46. How can you create a set?

A set can be created by enclosing a sequence of elements within curly braces {} or by using the set() function.
Here's an example:
my_set = {1, 2, 3, "hello", "world"}




Q47. Create a set and add "iNeuron" in your set.

We can use the add() method to add an element to a set.
Here's an example:
my_set = {1, 2, 3, "hello", "world"}
my_set.add("iNeuron")
print(my_set)
Output:
{1, 2, 3, 'iNeuron', 'world', 'hello'}




Q49. How is update() different from add()?

Both add() and update() are used to add elements to a set, but there is a difference between them.
add() method is used to add only one element at a time to a set. If we try to add multiple elements to the set using this method, it will result in a TypeError.
update() method is used to add multiple elements to the set at once. We can pass any iterable object (e.g., list, tuple, set, dictionary keys) to this method, and it will add all the elements of that object to the set.
Example:
# add() example
s = {1, 2, 3}
s.add(4)
print(s)    # Output: {1, 2, 3, 4}
# update() example
s = {1, 2, 3}
s.update([4, 5, 6])
print(s)    # Output: {1, 2, 3, 4, 5, 6}




Q50. What is clear() in sets?

The clear() method is used to remove all the elements from a set. After calling this method, the set will become empty.
Example:
s = {1, 2, 3}
s.clear()
print(s)    # Output: set()




Q51. What is frozen set?

A frozen set is an immutable set in Python. Once a frozen set is created, we cannot modify it (add or remove elements). The elements of a frozen set are also immutable.
Example:
fs = frozenset([1, 2, 3])
print(fs)   # Output: frozenset({1, 2, 3})




Q52. How is frozen set different from set?

The key difference between a set and a frozen set is that a set is mutable (can be modified) whereas a frozen set is immutable (cannot be modified).
A set can be modified by adding or removing elements from it, whereas a frozen set cannot be modified. Once a frozen set is created, we cannot add or remove elements from it.
Example:
s = {1, 2, 3}
s.add(4)
print(s)   # Output: {1, 2, 3, 4}
fs = frozenset([1, 2, 3])
fs.add(4)  # This will result in an AttributeError since frozenset object does not support item assignment




Q53. What is union() in sets? Explain via code.

union() is a set method that returns a new set containing all the unique elements from two or more sets. It takes an iterable object as an argument and returns a set containing all the unique elements from all the sets.
Example:
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
# Using union() method
s4 = s1.union(s2, s3)
print(s4)   # Output: {1, 2, 3, 4, 5, 6, 7}




Q54. What is intersection() in sets? Explain via code.

In Python, the intersection() method is used to get the intersection of two or more sets. It returns a new set containing only the elements that are present in all the given sets.
Here is an example:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print(intersection_set)   # Output: {4, 5}
In the above example, we have two sets set1 and set2. We are finding the intersection of these two sets using the intersection() method, and storing the result in a new set called intersection_set. The output shows that only the elements 4 and 5 are common in both sets, hence those are the only elements present in the intersection_set.




Q55. What is dictionary in Python?

A dictionary in Python is an unordered collection of key-value pairs, where each key is unique. It is also known as an associative array or a hash table. The keys in a dictionary can be of any hashable data type, such as integers, floats, strings, or tuples, whereas the values can be of any data type. Dictionaries are mutable, which means you can change their values.




Q56. How is dictionary different from all other data structures?

A dictionary is different from other data structures in Python because it uses a key-value pair to store data instead of an index or sequence. It is a mutable data type, which means that you can add, remove, or modify elements in a dictionary after it has been created. Additionally, dictionaries are unordered, which means that the elements are not stored in any specific order.




Q57. How can we declare a dictionary in Python?

In Python, we can declare a dictionary using curly braces {} or by using the dict() constructor. Here is an example of both:
# Using curly braces
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Using dict() constructor
my_dict = dict(name='John', age=25, city='New York')
In the above examples, we are creating a dictionary called my_dict with three key-value pairs. The first example uses curly braces, where each key-value pair is separated by a colon, and the pairs are separated by a comma. The second example uses the dict() constructor, where each key-value pair is passed as an argument to the constructor.




Q58. What will the output of the following?

var = {}
print(type(var))
The output of the above code will be:
<class 'dict'>
In the above code, we are creating an empty dictionary called var using curly braces {}. We are then using the type() function to print the type of the variable var. Since var is a dictionary, the output will be <class 'dict'>.




Q59. How can we add an element in a dictionary?

To add a new key-value pair to a dictionary, we can simply use the square bracket notation and assign a value to the new key. Here's an example:
my_dict = {'name': 'John', 'age': 25}
# Adding a new key-value pair
my_dict['city'] = 'New York'
print(my_dict)   # Output: {'name': 'John', 'age': 25, 'city': 'New York'}
In the above example, we have a dictionary called my_dict




Q60. Here is an example of creating a dictionary and accessing all its values using a for loop:

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
# Accessing all the values using a for loop
for value in my_dict.values():
    print(value)
Output:
John
30
New York




Q61. Here is an example of creating a nested dictionary and accessing all the elements in the inner dictionary:

# Creating a nested dictionary
my_dict = {"person1": {"name": "John", "age": 30}, "person2": {"name": "Mary", "age": 25}}
# Accessing all the elements in the inner dictionary
print(my_dict["person1"]["name"])
print(my_dict["person1"]["age"])
print(my_dict["person2"]["name"])
print(my_dict["person2"]["age"])
Output:
John
30
Mary
25




Q62. The get() function is used to retrieve the value of a specified key in a dictionary. It takes one required argument, which is the key to be searched, and one optional argument, which is the default value to be returned if the key is not found. Here's an example:

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
# Retrieving the value of a specified key using get()
print(my_dict.get("name"))
print(my_dict.get("gender", "Unknown"))
Output:
John
Unknown




Q63. The items() function is used to return a list of key-value pairs in a dictionary. Each key-value pair is returned as a tuple. Here's an example:

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
# Retrieving a list of key-value pairs using items()
print(my_dict.items())
Output:
dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])




Q64. The pop() function is used to remove a specified key-value pair from a dictionary and return its value. It takes one required argument, which is the key to be removed. Here's an example:

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
# Removing a specified key-value pair using pop()
age = my_dict.pop("age")
print(age)
print(my_dict)
Output:
30
{'name': 'John', 'city': 'New York'}




Q65. The popitems() function is used to remove and return an arbitrary key-value pair from a dictionary. It takes no arguments. Here's an example:

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
# Removing an arbitrary key-value pair using popitem()
item = my_dict.popitem()
print(item)
print(my_dict)
Output:
('city', 'New York')
{'name': 'John', 'age': 30}




Q66. In Python, the keys() function is used to return a list of all the keys present in a dictionary.

For example, consider the following dictionary:
my_dict = {"apple": 1, "banana": 2, "orange": 3}
If we call the keys() function on this dictionary, like this:
print(my_dict.keys())
The output will be:
dict_keys(['apple', 'banana', 'orange'])
This function is useful when we want to iterate over all the keys of a dictionary.




Q67. In Python, the values() function is used to return a list of all the values present in a dictionary.

For example, consider the following dictionary:
my_dict = {"apple": 1, "banana": 2, "orange": 3}
If we call the values() function on this dictionary, like this:
print(my_dict.values())
The output will be:
dict_values([1, 2, 3])
This function is useful when we want to iterate over all the values of a dictionary.




Q68. In programming, loops are used to execute a set of statements repeatedly until a certain condition is met. In Python, there are two types of loops: for loops and while loops.





Q69. In Python, there are two types of loops: for loops and while loops.





Q70. The main difference between for and while loops is that for loops are used when we know the number of times we want to execute a block of code, while while loops are used when we don't know the number of times we want to execute a block of code, but we know the condition that needs to be met for the loop to terminate.





Q71. In Python, the continue statement is used to skip the current iteration of a loop and move on to the next iteration.

For example, consider the following loop:
for i in range(10):
    if i == 5:
        continue
    print(i)
In this loop, when i is equal to 5, the continue statement is executed and the loop skips the rest of the code in that iteration. As a result, the output of this loop will be:
0
1
2
3
4
6
7
8
9




Q72. In Python, the break statement is used to exit a loop prematurely. When a break statement is encountered inside a loop, the loop is immediately terminated and the program execution moves on to the next statement after the loop.

For example, consider the following loop:
for i in range(10):
    if i == 5:
        break
    print(i)
In this loop, when i is equal to 5, the break statement is executed and the loop is terminated. As a result, the output of this loop will be:
0
1
2
3
4




Q73. In Python, the pass statement is used as a placeholder when a statement is required syntactically, but no code needs to be executed. It is often used as a placeholder for code that has not yet been implemented.

For example, consider the following function:
def my_function():
    pass
In this function, the pass statement is used to indicate that the function body is empty and no code needs to be executed.




Q76. Write a Python program to find the factorial of a given number.

Solution:
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial doesn't exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("Factorial of",num,"is",factorial)
Output:
mathematica
Enter a number: 5
Factorial of 5 is 120




Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100

Solution:
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
si = (p * r * t) / 100
print("Simple Interest = ", si)
Output:
yaml
Enter the principal amount: 10000
Enter the rate of interest: 8
Enter the time period: 2.5
Simple Interest =  2000.0




Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

Solution:
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
ci = p * (pow((1 + r / 100), t))
print("Compound Interest = ", round(ci, 2))
Output:
mathematica
Enter the principal amount: 10000
Enter the rate of interest: 8
Enter the time period: 2.5
Compound Interest =  11970.59




Q79. Write a Python program to check if a number is prime or not.

Solution:
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
Output:
Enter a number: 17
17 is a prime number




Q80. Write a Python program to check Armstrong Number.

Solution:
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
Output:
csharp
Enter a number: 153
153 is an Armstrong number




Q81. Write a Python program to find the n-th Fibonacci Number.

Solution:
n = int(input("Enter a number: "))
if n <= 0:
    print("Please enter a positive integer")
else:
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        print(b)
Output:
Enter a number: 




Q82. Write a Python program to interchange the first and last element in a list.

To interchange the first and last element in a list, we can swap the values of the first and last index of the list using indexing. Here's the Python program to interchange the first and last element in a list:
def interchange_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
# example
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
interchanged_list = interchange_first_last(my_list)
print("Interchanged List:", interchanged_list)
Output:
Original List: [1, 2, 3, 4, 5]
Interchanged List: [5, 2, 3, 4, 1]




Q83. Write a Python program to swap two elements in a list.

To swap two elements in a list, we can use the index of the two elements and assign them with each other.
Here's an example code:
my_list = [1, 2, 3, 4, 5]
# Swap the 2nd and 4th elements in the list
temp = my_list[1]
my_list[1] = my_list[3]
my_list[3] = temp
print(my_list)   # Output: [1, 4, 3, 2, 5]




Q84. Write a Python program to find N largest element from a list.

To find the N largest elements from a list, we can sort the list in descending order and then select the first N elements.
Here's an example code:
my_list = [5, 2, 8, 3, 1, 9, 4]
n = 3
sorted_list = sorted(my_list, reverse=True)
n_largest_elements = sorted_list[:n]
print(n_largest_elements)  # Output: [9, 8, 5]




Q85. Write a Python program to find cumulative sum of a list.

To find the cumulative sum of a list, we can iterate through the list and add each element to a running total.
Here's an example code:
my_list = [1, 2, 3, 4, 5]
cumulative_sum = 0
cumulative_list = []
for i in my_list:
    cumulative_sum += i
    cumulative_list.append(cumulative_sum)
print(cumulative_list)  # Output: [1, 3, 6, 10, 15]




Q86. Write a Python program to check if a string is palindrome or not.

To check if a string is palindrome or not, we can reverse the string and check if it is the same as the original string.
Here's an example code:
my_string = "racecar"
if my_string == my_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




Q87. Write a Python program to remove i'th element from a string.

Solution:
We cannot remove an element from a string directly as it is an immutable data type in Python. Instead, we can create a new string by removing the i'th element.
Here is the Python code to remove the i'th element from a string:
def remove_char(str, i):
    if i < 0 or i >= len(str):
        return str
    else:
        return str[:i] + str[i+1:]
# test the function
str = "Hello World"
i = 6
print("Original String:", str)
new_str = remove_char(str, i)
print("String after removing i'th character:", new_str)
Output:
Original String: Hello World
String after removing i'th character: Hello orld




Q88. Write a Python program to check if a substring is present in a given string.

Solution:
We can use the in keyword or the find() method to check if a substring is present in a string. Here is the Python code to check if a substring is present in a given string:
def is_substring(str, sub):
    if sub in str:
        return True
    else:
        return False
# test the function
str = "Hello World"
sub = "World"
if is_substring(str, sub):
    print("Substring found!")
else:
    print("Substring not found!")
Output:
Substring found!




Q89. Write a Python program to find words which are greater than given length k.

Solution:
We can split the given string into words and then loop through each word to check if its length is greater than the given length k.
Here is the Python code to find words which are greater than given length k:
def find_long_words(str, k):
    words = str.split()
    long_words = []
    for word in words:
        if len(word) > k:
            long_words.append(word)
    return long_words
# test the function
str = "Hello World, how are you doing today?"
k = 4
long_words = find_long_words(str, k)
print("Words longer than", k, "are:", long_words)
Output:
Words longer than 4 are: ['Hello', 'World,', 'doing', 'today?']




Q90. Write a Python program to extract unique dictionary values.

Solution:
We can use a set to extract unique dictionary values. Here is the Python code to extract unique dictionary values:
def extract_unique_values(dict):
    unique_values = set()
    for key in dict:
        unique_values.add(dict[key])
    return unique_values
# test the function
dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
unique_values = extract_unique_values(dict)
print("Unique dictionary values:", unique_values)
Output:
Unique dictionary values: {1, 2, 3}




Q91. Write a Python program to merge two dictionaries.

Solution:
We can use the update() method to merge two dictionaries. Here is the Python code to merge two dictionaries:
def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1
# test the function
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict




Q92. Write a Python program to convert a list of tuples into dictionary.

Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
lst = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
result = dict(lst)
print(result)
Output:
{'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}




Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.

Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
lst = [9, 5, 6]
result = [(x, x**3) for x in lst]
print(result)
Output:
[(9, 729), (5, 125), (6, 216)]




Q94. Write a Python program to get all combinations of 2 tuples.

Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
from itertools import product
test_tuple1 = (7, 2)
test_tuple2 = (7, 8)
result = list(product(test_tuple1, test_tuple2))
print(result)
Output:
[(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]




Q95. Write a Python program to sort a list of tuples by second item.

Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)]
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
result = sorted(lst, key=lambda x: x[1])
print(result)
Output:
[('Geeks', 8), ('for', 24), ('Geeks', 30)]




Q96. Write a python program to print below pattern.

Solution:
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
Output:
markdown
* 
* * 
* * * 
* * * * 
* * * * * 




Q97. Write a python program to print below pattern.

markdown
*
**
Solution:
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
Output:
markdown
    *
   **
  ***
 ****
*****




Q98. Write a python program to print below pattern.

markdown
* 
*
Solution:
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
Output:
markdown
    * 
   * * 
  * * * 
 * * * * 
* * * * * 




Q99. Write a python program to print below pattern.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Solution:
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end=" ")
    print()
Output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 




Q100. Write a python program to print below pattern.

A
B B
C C C
D D D D
E E E E E
Solution:
n = 5
for i in range(n):
    print((chr(65+i)+" ")*(i+1))