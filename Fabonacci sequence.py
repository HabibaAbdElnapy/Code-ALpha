def fibonacci_iterative(n):
    """Generate a list of Fibonacci numbers up to the nth number using the iterative method."""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def main():
    n = 10  # Number of Fibonacci numbers to generate

    # Using the iterative method
    print("Fibonacci sequence (iterative):", fibonacci_iterative(n))


if __name__ == "__main__":
    main()
