# Polynomial vault
# Shamir's Secret Sharing in Python

This is a Python implementation of **Shamir's Secret Sharing (SSS)** scheme, a cryptographic algorithm for splitting a secret into multiple parts, called shares. The original secret can only be reconstructed when a sufficient number of shares (a "threshold") are combined.

## Algorithm

The core idea is based on a mathematical property of polynomials: a unique polynomial of degree $k-1$ can be defined by any $k$ points on it.

1.  **Initialization**: We start with a secret, which must be a number. All calculations are performed within a large prime finite field ($\text{mod } p$) to ensure security and mathematical consistency. In this code, $p = 2^{127} - 1$.

2.  **Polynomial Generation**:
    * A random polynomial of degree $k-1$ is generated, where $k$ is the minimum number of shares needed for reconstruction (the threshold).
    * The secret number is set as the y-intercept of this polynomial (the constant term, $a_0$).
    * The polynomial looks like this: $f(x) = a_0 + a_1x + a_2x^2 + \dots + a_{k-1}x^{k-1}$, where $a_0$ is the secret.

3.  **Share Distribution**:
    * Shares are created by taking different points $(x, f(x))$ on the polynomial.
    * The program generates $n$ shares, where $n$ is the total number of shares to be distributed. Each share is a tuple `(x, y)`.

4.  **Secret Reconstruction**:
    * To recover the secret, at least $k$ shares must be gathered.
    * Using these $k$ points, the original polynomial is reconstructed using **Lagrange Interpolation**.
    * The reconstructed secret is the y-intercept of the interpolated polynomial (i.e., the value of the polynomial at $x=0$), which is our original constant term, $a_0$.

---

## Run the Program

1.  Save the code as a Python file (e.g., `sss.py`).
2.  Run it from your terminal:
3. 
    ```
    python sss.py
    ```
4.  Follow the interactive prompts:
    * Enter your secret number.
    * Enter the total number of shares (`n`) you want to create.
    * Enter the threshold of shares (`k`) required to reconstruct the secret.
5.  The program will display the generated shares.
6.  To test the reconstruction, you will be prompted to enter `k` number of shares.

### Example

```
- - - Polynomial vault! - - -
Shamir's Secret Sharing using Python

Enter your secret number (less than 170141183460469231731687303715884105727): 911
Enter total number of shares to generate(n): 3
Enter threshold (minimum shares to reconstruct)(k): 3

 Generated Shares:
Share 1: (x=1, y=5243766420449181159521539591435246649)
Share 2: (x=2, y=139714245825479877388666467235015779834)
Share 3: (x=3, y=63129071294153625224060175498973389012)

--- Reconstruct Secret ---
Enter x for Share #1: 2 (*generally smaller than y)
Enter y for Share #1: 7661854 (the value of share)

Enter x for Share #1: 1
Enter y for Share #1: 5243766420449181159521539591435246649
Enter x for Share #2: 2
Enter y for Share #2: 139714245825479877388666467235015779834
Enter x for Share #3: 3
Enter y for Share #3: 63129071294153625224060175498973389012

 Recovered Secret: 911
 Success!

Process finished with exit code 0
```

---

## Functions breakdown


- **`generate_polynomial(secret, degree)`**  
  Builds a random polynomial where the secret is the constant term. Used to hide the secret in math.
- **`evaluate_polynomial(poly, x)`**  
  Evaluates the polynomial at `x` using modular arithmetic. Gives you one point (share).
- **`generate_shares(secret, threshold, num_shares)`**  
  Splits the secret into `num_shares`. Any `threshold` of them can recover the secret.
- **`mod_inverse(a, p)`**  
  Finds the modular inverse of `a` mod `p`. Needed for clean division during interpolation.
- **`reconstruct_secret(shares)`**  
  Rebuilds the original secret using Lagrange interpolation with `k` valid shares.

