import secrets #omitted using random for "cryptographic reasons"

secret="c3JlZWhhcmlfc3BpZDNyX2NvbW1vbl9jcnlwdG8gLy9wbGVhc2UgbGV0IG1lIGluIQ=="
PRIME = 2**127 - 1  # safe smallish prime

def generate_polynomial(secret, degree):
    return [secret] + [secrets.randbelow(PRIME) for _ in range(degree)]

def evaluate_polynomial(poly, x):
    result = 0
    for coeff in reversed(poly):
        result = (result * x + coeff) % PRIME
    return result

def generate_shares(secret, threshold, num_shares):
    if threshold > num_shares:
        raise ValueError("Threshold cannot be greater than the number of shares.")
    poly = generate_polynomial(secret, threshold - 1)
    shares = [(x, evaluate_polynomial(poly, x)) for x in range(1, num_shares + 1)]
    return shares


def mod_inverse(a, p):
    a = a% p
    if a == 0:
        raise ValueError("No modular inverse for 0")
    old_r, r = a, p
    old_s, s = 1,0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    if old_r != 1:
        raise ValueError("No modular inverse exists")  # a and p are not coprime
    return old_s % p

def reconstruct_secret(shares):
    secret = 0
    for i, (xi, yi) in enumerate(shares):
        num,den=1,1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                num = (num * -xj) % PRIME
                den = (den * (xi - xj)) % PRIME
        lagrange_coeff = (num * mod_inverse(den, PRIME)) % PRIME
        secret = (secret + yi * lagrange_coeff) % PRIME
    return secret

def main():
    print("- - - Polynomial vault! - - -")
    print("Shamir's Secret Sharing using Python\n")

    try:
        secret = int(input(f"Enter your secret number (less than {PRIME}): "))
        n = int(input("Enter total number of shares to generate(n): "))
        k = int(input("Enter threshold (minimum shares to reconstruct)(k): "))
        if k == 1:
            print("Alert ! - - > in this case, the share will be the same as the secret!!!!")
    except ValueError:
        print("Please enter valid integers.")
        return
    try:
        shares = generate_shares(secret, k, n)
    except ValueError as e:
        print(e)
        return

    print("\n Generated Shares:")
    for i in range(len(shares)):
        x, y = shares[i]
        print(f"Share {i + 1}: (x={x}, y={y})")

    print("\n--- Reconstruct Secret ---\nExample-")
    print("Enter x for Share #1: 2 (*generally smaller than y)" )
    print("Enter y for Share #1: 7661854 (the value of share)\n")
    selected = []
    for i in range(k):
        try:
            x = int(input(f"Enter x for Share #{i+1}: "))
            y = int(input(f"Enter y for Share #{i+1}: "))
            selected.append((x, y))
        except ValueError:
            print(" Invalid input. Please enter integers.")
            return

    recovered = reconstruct_secret(selected)
    print("\n Recovered Secret:", recovered)
    if recovered == secret:
        print(" Success!")
    else:
        print(" Failed !") #why

if __name__ == "__main__":
    main()
