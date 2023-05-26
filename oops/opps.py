



Q1. What is the purpose of Python's OOP?

A1. The purpose of Python's Object-Oriented Programming (OOP) is to model real-world objects, entities or concepts as classes, and provide a way to interact with them using objects. OOP allows encapsulating data and behavior, abstracting implementation details, and enabling code reusability and modularity.




Q2. Where does an inheritance search look for an attribute?

A2. In Python, when an attribute is accessed on an object, the interpreter searches for it in the object's class, and then in its superclass(es) according to the method resolution order (MRO), until it is found or an AttributeError is raised.




Q3. How do you distinguish between a class object and an instance object?

A3. In Python, a class object is an instance of type, whereas an instance object is an instance of a class. A class object defines a blueprint for creating objects, while an instance object is a concrete realization of that blueprint, with its own state and identity.




Q4. What makes the first argument in a class’s method function special?

A4. In Python, the first argument in a class's method function is conventionally called "self" and refers to the instance object that the method is called on. This argument is used to access and modify the instance's attributes, and to call other instance methods.




Q5. What is the purpose of the init method?

A5. The purpose of the "init" method in Python is to initialize the attributes of a newly created instance object. It is called automatically when an instance is created, and can take arguments to set initial values for the object's attributes.




Q6. What is the process for creating a class instance?

A6. In Python, a class instance is created by calling the class object as if it were a function, with any arguments to the "init" method provided in parentheses. The result is a new instance object with its own namespace, attributes, and reference to its class.




Q7. What is the process for creating a class?

A7. In Python, a class is created using the "class" keyword followed by the class name, and an optional list of base classes in parentheses. The body of the class contains its attributes, which can include data members and methods.




Q8. How would you define the superclasses of a class?

A8. In Python, the superclasses of a class are the classes that it inherits from, either directly or indirectly. The superclasses can be accessed through the "bases" attribute of the class object, which returns a tuple of the base classes in the order of their occurrence in the MRO.




Q9. What is the relationship between classes and modules?

A9. In Python, a module is a file that contains Python code, while a class is a construct that defines a type of object with its own attributes and behavior. Modules can contain classes as well as other code, and classes can be defined in a module or imported from other modules.




Q10. How do you make instances and classes?

A10. In Python, instances are created by calling a class object, while classes are defined using the "class" keyword followed by the class name and body of attributes. Instances and classes can also be created dynamically using metaclasses or the "type" function.




Q11. Where and how should be class attributes created?

A11. In Python, class attributes should be created inside the class body as variables or methods that are shared by all instances of the class. Class attributes can also be created dynamically at runtime using the "setattr" method or by assigning values directly to the class object.




Q12. Where and how are instance attributes created?

Ans. Instance attributes are created inside a class's methods, either through assignment statements using the self parameter or by modifying an existing attribute on self. Instance attributes can also be created outside of class methods by assigning to them directly on the instance object.




Q13. What does the term "self" in a Python class mean?

Ans. "self" is a reference to the instance of the class that is being operated on. It is a conventional name and the first parameter of any method in a class. When a method is called on an instance, "self" refers to that instance, allowing access to its attributes and methods.




Q14. How does a Python class handle operator overloading?

Ans. Python classes can overload operators using special methods that correspond to each operator. These methods have predefined names, such as "add" for the "+" operator, and allow instances of a class to behave like built-in types when used in expressions with those operators.




Q15. When do you consider allowing operator overloading of your classes?

Ans. Operator overloading should be considered when it improves the readability and intuitiveness of the code. Overloading should be used sparingly and only when it makes the code more concise and readable. Overloading should also adhere to established conventions and not change the expected behavior of the overloaded operator.




Q16. What is the most popular form of operator overloading?

Ans. The most popular form of operator overloading is probably arithmetic operator overloading, which allows instances of a class to behave like built-in types in arithmetic expressions. This is achieved by implementing special methods such as "add", "sub", "mul", etc.




Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

Ans. The two most important concepts to grasp in order to comprehend Python OOP code are classes and objects. Classes define the structure and behavior of objects, while objects are instances of classes that have attributes and methods.




Q18. Describe three applications for exception processing.

Ans. Three applications for exception processing are error handling, program termination, and event notification. Exception processing allows for graceful handling of errors, exiting programs when necessary, and triggering events when certain conditions are met.




Q19. What happens if you don't do something extra to treat an exception?

Ans. If an exception is not handled, it will propagate up the call stack until it is caught by an exception handler or it reaches the top level of the program, causing the program to terminate.




Q20. What are your options for recovering from an exception in your script?

Ans. Options for recovering from an exception in a script include catching the exception and taking appropriate action, such as retrying an operation, reverting to a previous state, or logging the error. Another option is to raise a new exception with additional information or context.




Q21. Describe two methods for triggering exceptions in your script.

Ans. Two methods for triggering exceptions in a script are using the "raise" statement to explicitly raise an exception, and using built-in functions or methods that raise exceptions, such as "assert", "open", or "int".




Q22. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.

Ans. Two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists, are using the "finally" clause in a "try-except-finally" block and using the "atexit" module to register functions to be called at program exit.




Q23. What is the purpose of the try statement?

Ans. The purpose of the try statement is to handle exceptions in Python. The try statement allows a block of code to be executed, and if an exception is raised, it provides a mechanism to catch the exception and take appropriate action.




Q24. What are the two most popular try statement variations?

Ans. The two most popular try statement variations are the "try-except" block, which catches and handles exceptions, and the "try-finally" block, which ensures that a block of code is executed regardless of whether or not an exception is raised.




Q25. What is the purpose of the raise statement?

Ans. The purpose of the raise statement is to raise an exception in Python. The raise statement is used to signal that an error or exceptional condition has occurred and to provide information about the error or condition.




Q26. What does the assert statement do, and what other statement is it like?

Ans. The assert statement is used to check for a condition that should be true, and raise an AssertionError if the condition is false. It is similar to the if statement, but is typically used for debugging purposes and to ensure that assumptions about the state of the program are correct.




Q27. What is the purpose of the with/as argument, and what other statement is it like?

Ans. The with/as argument is used in Python to manage resources such as files, network connections, and locks. It is similar to the try/finally statement, but provides a more concise and readable way to manage resources and ensure that they are properly cleaned up when they are no longer needed.




Q28. What are *args, **kwargs?

Ans. *args and **kwargs are special syntax in Python for passing a variable number of arguments to a function. *args is used to pass a variable number of positional arguments, while **kwargs is used to pass a variable number of keyword arguments.




Q29. How can I pass optional or keyword parameters from one function to another?

Ans. Optional or keyword parameters can be passed from one function to another using *args and **kwargs. *args is used to pass a variable number of positional arguments, while **kwargs is used to pass a variable number of keyword arguments.




Q30. What are Lambda Functions?

Ans. Lambda functions are anonymous functions in Python that can be defined on a single line. They are typically used for simple operations and as arguments to higher-order functions.




Q31. Explain Inheritance in Python with an example?

Ans. Inheritance is a mechanism in Python that allows a subclass to inherit properties and methods from a parent or superclass. For example, if we have a class Animal, we can create a subclass Dog that inherits properties and methods from Animal, such as bark() and run(). The subclass Dog can also define its own properties and methods, such as breed().




Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?

Ans. It depends on the method resolution order (MRO) of class C. The MRO determines the order in which the methods of the base classes are searched when a method is called from an object of the derived class. By default, Python uses a depth-first search algorithm to determine the MRO. In this case, if the method func() is not defined in class C, Python will search for it in class A first, then in class B. The first matching method it finds will be invoked.




Q33. Which methods/functions do we use to determine the type of instance and inheritance?

Ans. The built-in functions type() and isinstance() can be used to determine the type of an instance and its inheritance. The type() function returns the class or type of an object, while the isinstance() function checks if an object is an instance of a specific class or its subclass.




Q34. Explain the use of the 'nonlocal' keyword in Python.

Ans. The 'nonlocal' keyword is used to access and modify a variable in the closest enclosing scope that is not the global scope. It is used within a nested function, where a variable with the same name as a variable in the enclosing function is defined. Without the 'nonlocal' keyword, the variable in the nested function would be considered as a new variable, separate from the variable in the enclosing function.




Q35. What is the global keyword?

Ans. The 'global' keyword is used to indicate that a variable is a global variable, and should be accessed from the global scope. If a variable is defined within a function and the 'global' keyword is used before it, any changes made to the variable within the function will be reflected in the global variable. If the 'global' keyword is not used, the variable will be considered a local variable within the function, and any changes made to it will not affect the global variable.