# CPSC-44000-LT1-Assignment1

# Author

Collin Cimaroli

# Course

CPSC-44000-LT1

# Credits

- Python standard library documentation for syntax and reference
- W3Schools for code examples and Python documentation

# How the Program Works

This program searches for "near misses" to the equation
\(x^n + y^n = z^n\) for integers with constraints: 
- \(2 < n < 12\),
- \(10 ≤ x ≤ k\) and \(10 ≤ y ≤ k\), where \(k ≥ 10\).

A **near miss** is defined as a relatively small difference between \(x^n + y^n\) and the nearest \(n\)-th power \(z^n\). For each pair \((x, y)\), the program:
1. Computes \(s = x^n + y^n\),
2. Finds \(z\) such that \(z^n < s < (z+1)^n\),
3. Calculates the absolute miss as \\\min(s - z^n, (z+1)^n - s)\), and
4. Calculates the relative miss as \(	ext{absolute miss} / s\).

Whenever a new **smallest relative miss** is found, the program prints a labeled line with the
current \(x, y, z\), the absolute miss, and the relative miss (both as a fraction and percentage).
At the end of the search, it prints a summary of the smallest relative miss discovered.

## How to Run

1. Ensure you have Python installed.
2. In your terminal, navigate to the project directory and run the program:

python fermat_near_miss.py

   Or just open the .exe file to run the program.

3. Enter the values for n and k when prompted:
   - `n` as an integer from 3 to 11,
   - `k` as an integer ≥ 10.

4. Click enter once you have reviewed the findings to exit the session.
