# Python Reading Reflections

---

## Chapter 1: The Way of the Program

**One Thing I Knew:**

I already knew that a *program* is a sequence of instructions that tells the computer what to do — including things like math operations, input/output, conditionals, and repetition. I was also familiar with Python’s `print()` statement and basic arithmetic operators like `+`, `-`, `*`, and `/`.

**One Thing I Did Not Know:**

I didn’t realize that typing a number like `1,000,000` in Python would actually be interpreted as a tuple `(1, 0, 0)` — I had assumed it would just be a number with commas for readability. Also, I wasn’t aware that the caret symbol `^` in Python represents the XOR bitwise operator, rather than exponentiation like in some other languages.

---

## Chapter 3: Functions

**One Thing I Knew:**

I already knew how to define and call basic functions using the `def` keyword, as well as how to pass arguments to functions. I was also familiar with built-in functions like `print()` and `type()`, and the idea of returning values from a function.

**One Thing I Did Not Know:**

I didn’t know that if you call a fruitful function in a script without using or saving the return value, the result is lost. Also, I found the explanation of stack diagrams and local variable scope particularly helpful — especially how parameters and variables only exist within the function frame that called them.

---

## Chapter 5: Conditionals and Recursion

**One Thing I Knew:**

I already knew how to use basic `if`, `else`, and `elif` statements to control the flow of a program based on conditions. I also knew how to use comparison operators like `==`, `<`, and `>=`, and how boolean logic works in conditionals.

**One Thing I Did Not Know:**

I didn’t know about Python’s floor division operator `//` and how it’s useful for integer division when working with units like hours and minutes. I also found the section on recursion insightful — especially how Python uses a stack of frames to manage recursive calls, and how forgetting a base case can lead to infinite recursion errors.

---

## Chapter 10: Lists

**One Thing I Knew:**

I already knew how to create lists using square brackets and access elements using indexing. I also knew that lists are mutable and could be modified using indexing, loops, and methods like `append()` or `remove()`.

**One Thing I Did Not Know:**

I didn’t know that many list methods like `sort()` return `None` and directly modify the original list, unlike string methods which return a new string. I also didn’t realize how aliasing works with lists — that assigning one list variable to another makes them point to the same object, and how modifying one affects the other. That distinction between modifying the original vs. returning a new list is super important for debugging.
