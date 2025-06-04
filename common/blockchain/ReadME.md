Of course. Here is a README file for your assignment.

---

# Shamir's Secret Sharing in Python

This project is a Python implementation of **Shamir's Secret Sharing (SSS)** scheme, a cryptographic algorithm for splitting a secret into multiple parts, called shares. The original secret can only be reconstructed when a sufficient number of shares (a "threshold") are combined.

## 📜 How It Works: The Flow

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

## ⚙️ How to Run the Program

1.  Save the code as a Python file (e.g., `sss.py`).
2.  Run it from your terminal:
    ```bash
    python sss.py
    ```
3.  Follow the interactive prompts:
    * Enter your secret number.
    * Enter the total number of shares (`n`) you want to create.
    * Enter the threshold of shares (`k`) required to reconstruct the secret.
4.  The program will display the generated shares.
5.  To test the reconstruction, you will be prompted to enter `k` number of shares.

### Example

```
- - - Polynomial vault! - - -
Shamir's Secret Sharing using Python

Enter your secret number (less than ...): 12345
Enter total number of shares to generate: 5
Enter threshold (minimum shares to reconstruct): 3

Generated Shares:
Share 1: (x=1, y=...)
Share 2: (x=2, y=...)
Share 3: (x=3, y=...)
Share 4: (x=4, y=...)
Share 5: (x=5, y=...)

--- Reconstruct Secret ---
Enter any 3 shares to recover the secret.
Enter x for Share #1: 1
Enter y for Share #1: ...
Enter x for Share #2: 3
Enter y for Share #2: ...
Enter x for Share #3: 5
Enter y for Share #3: ...

Recovered Secret: 12345
Success!
```

---

## 🔬 Code Breakdown

* `generate_polynomial(secret, degree)`: Takes the secret and the threshold to create a polynomial list, with the secret as the first coefficient (the constant term).
* `evaluate_polynomial(poly, x)`: Evaluates the polynomial at a given point `x` to help generate a share.
* `generate_shares(secret, threshold, num_shares)`: The main function for creating the set of `n` shares from the secret.
* `mod_inverse(a, p)`: A crucial helper function that calculates the modular multiplicative inverse, which is required for the division step in Lagrange interpolation within a finite field.
* `reconstruct_secret(shares)`: Implements Lagrange interpolation to take `k` shares and calculate the original secret.
* `main()`: Handles all user interaction, calls the necessary functions, and displays the results.
