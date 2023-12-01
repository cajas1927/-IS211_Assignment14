# Part I: Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Part II: Euclidâ€™s GCD Algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Part III: String Comparison
def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])

# Test the functions
if __name__ == "__main__":
    # Part I: Fibonacci Sequence
    print(f"Fibonacci(6): {fibonacci(6)}")

    # Part II: Euclidâ€™s GCD Algorithm
    print(f"GCD(48, 18): {gcd(48, 18)}")

    # Part III: String Comparison
    print(f'CompareTo("apple", "banana"): {compareTo("apple", "banana")}')
    print(f'CompareTo("banana", "apple"): {compareTo("banana", "apple")}')
    print(f'CompareTo("apple", "apple"): {compareTo("apple", "apple")}')
