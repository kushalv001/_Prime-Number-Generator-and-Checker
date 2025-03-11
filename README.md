# _Prime-Number-Generator-and-Checker

# Prime Number Generator and Checker

## Introduction
This Python program allows users to check whether a number is prime and generate a list of prime numbers within a specified range. It provides a simple CLI-based interface to interact with the functionality.

## Features
- Check if a given number is prime.
- Generate a list of prime numbers within a specified range.
- User-friendly command-line interface.

## Installation
1. Clone this repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd Prime-Checker
   ```
3. Run the script:
   ```sh
   python prime_checker.py
   ```

## Usage
1. Run the program, and it will prompt you with options:
   - `1`: Check if a number is prime.
   - `2`: Generate prime numbers in a given range.
   - `3`: Exit the program.
2. Follow the on-screen instructions to enter numbers and receive results.

## Code Structure
- `is_prime(n)`: Checks whether a number is prime.
- `generate_primes(start, end)`: Generates a list of prime numbers within a range.
- The script runs an interactive loop allowing users to choose functionalities.

## Example
```
Options:
1. Check if a number is prime
2. Generate prime numbers in a range
3. Exit
Enter your choice (1/2/3): 1
Enter a number: 17
17 is a prime number.
```
