def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Check if a number is prime")
        print("2. Generate prime numbers in a range")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            num = int(input("Enter a number: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")

        elif choice == "2":
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            primes = generate_primes(start, end)
            print(f"Prime numbers between {start} and {end}: {primes}")

        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
