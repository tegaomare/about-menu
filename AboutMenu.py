# Author: Tega Omarejedje
# Project: Recursive Functions Menu
# Date: 06/21/2025

import turtle

# Recursive factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive Fibonacci function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive fractal pattern (tree)
def draw_fractal_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Display the menu and handle choices
def about_menu():
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            num = input("Enter a positive integer to find its factorial: ")
            if num.isdigit() and int(num) >= 0:
                result = factorial(int(num))
                print(f"The factorial of {num} is {result}.")
            else:
                print("Please enter a valid non-negative integer.")

        elif choice == "2":
            num = input("Enter the position (non-negative integer) of the Fibonacci number: ")
            if num.isdigit() and int(num) >= 0:
                result = fibonacci(int(num))
                print(f"The {num}th Fibonacci number is {result}.")
            else:
                print("Please enter a valid non-negative integer.")

        elif choice == "3":
            print("Drawing a recursive fractal tree... Close the window to return to the menu.")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.left(90)
            t.color("green")
            t.speed("fastest")
            draw_fractal_tree(100, t)
            screen.mainloop()

        elif choice == "4":
            print("Goodbye! Thanks for exploring recursion!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Run the menu
about_menu()
