# Day 14 Challenge:
# Write a program to print the first n numbers of a Fibonacci sequence.

def fibonacci(n):

    fib_sequence = []

    for i in range(0,n):

        if i <= 1:
            fib_sequence.append(i)
        else:
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    print(fib_sequence)

while True:

    try:
        n = int(input("How many values of the Fibonnaci sequence would you like to see? "))
        
        fibonacci(n)
        
        break

    except ValueError:
        print("Please enter your choice as a digit.")
        continue