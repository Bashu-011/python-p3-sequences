#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = [0, 1]

    while len(fib_sequence) < length:
        
        number = (fib_sequence[-1] + fib_sequence[-2])

        fib_sequence.append(number)

    print(fib_sequence[:length])

print_fibonacci(9)