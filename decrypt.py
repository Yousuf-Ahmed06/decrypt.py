def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

try:
    public_key = int(input("Please enter a public key: "))
    if public_key <= 0:
        raise ValueError("Please enter a positive integer.")
except ValueError as e:
    print(e)
    exit()
print("-"*23)
print("Decrypting key.......")
result = prime_factors(public_key)
print("-"*23, "\n")

if len(result) == 1:
    print(f"{public_key} is a prime number.")
elif len(result) == 2:
    print(f"The private keys of {public_key} are: {result}")
else:
    print(f"{public_key} is not a product of two prime numbers but here are the prime factors regardless: {result}")
