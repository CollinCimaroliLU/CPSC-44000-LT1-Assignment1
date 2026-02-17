"""
Title: Looking for Fermat's Last Theorem Near Misses
Filename: fermat_near_miss.py
External files needed to run: None
External files created by this program: None
Programmers: Collin Cimaroli
Emails: collinpcimaroli@lewisu.edu
Course: CPSC-44000-LT1
Date completed/submitted: 2/17/2026

Program description:
    This Python program searches for "near misses" to Fermat's Last Theorem.
    Given an exponent n (with 2 < n < 12) and an upper bound k (k >= 10), it 
    examines integer pairs (x, y) with 10 <= x <= k and 10 <= y <= k. For each pair, it computes
    s = x^n + y^n and identifies the integer z such that z^n < s < (z+1)^n. The program then
    computes the absolute miss (the smaller of s - z^n and (z+1)^n - s) and the relative miss
    (absolute miss divided by s). It tracks and prints any new smallest relative miss discovered
    during the search, including the associated (x, y, z), absolute miss, and relative miss.
    When the search completes, the smallest relative miss found is the last result shown.

Resources used:
    - Python standard library documentation for syntax and reference.
    - W3Schools for Python code examples and documentation.
"""

from math import isclose


def integer_nth_root(value: int, n: int) -> int:
    """Return the floor of the n-th root of value.

    Arguments:
        value: The non-negative integer whose n-th root is taken.
        n: The root degree (n ≥ 2).
    Returns:
        The largest integer r such that r^n ≤ value.
    """

    # Handle small/edge cases explicitly
    if value <= 1:
        return value

    # Finds a search range on [low, high]
    low, high = 0, 1

    # Expand high until high^n > value quickly
    while pow(high, n) <= value:
        high *= 2

    # Binary search within the [low, high] range to determine the integer's root
    while low + 1 < high:
        mid = (low + high) // 2
        mid_pow = pow(mid, n)
        if mid_pow == value:
            return mid
        if mid_pow < value:
            low = mid
        else:
            high = mid
    return low


def validate_inputs(n: int, k: int) -> None:
    """Validates the user-provided n and k per our constraints.

    Provides a ValueError if the constraints are not met.
    """

    if not (3 <= n <= 11):
        raise ValueError("n must be an integer such that: 2 < n < 12 (3 through 11).")
    if k < 10:
        raise ValueError("k must be ≥ 10.")


def find_near_misses(n: int, k: int) -> None:
    """Search for near misses for the given n and k and print the results.

    For each (x, y) with 10 ≤ x ≤ k and 10 ≤ y ≤ k, compute s = x^n + y^n.
    Let z = floor(s ^ (1/n)) computed robustly via integer_nth_root. Identify which
    of z^n or (z+1)^n is closer to s. The absolute miss is the smaller difference, and
    the relative miss is absolute_miss / s.

    Any time a new smallest relative miss is found, print a labeled line with the details.
    """

    # Smallest near miss trackers
    best_rel_miss = None  
    best_record = None    

    # Outer loop over x values
    for x in range(10, k + 1):

        # Inner loop over y values
        for y in range(10, k + 1):

            # Compute s = x^n + y^n
            s = pow(x, n) + pow(y, n)

            # Find z such that z^n ≤ s < (z+1)^n
            z = integer_nth_root(s, n)

            # Compute neighbors' powers
            z_n = pow(z, n)
            zp1_n = pow(z + 1, n)

            # For n ≥ 3 and integer x,y, Fermat's Last Theorem implies s != perfect n-th power
            # But due to integer arithmetic, we still guard against equality.
            if s == z_n or s == zp1_n:

                # In this rare case, the absolute miss is 0; skip since it's not a near miss.
                continue

            # Compute absolute miss as the smaller difference
            miss_below = s - z_n
            miss_above = zp1_n - s
            abs_miss = miss_below if miss_below <= miss_above else miss_above

            # Compute relative miss
            rel_miss = abs_miss / s

            # If a new best/smaller near miss is found, record and print the values
            if best_rel_miss is None or rel_miss < best_rel_miss:
                best_rel_miss = rel_miss

                # Choose the closer z to report (the one producing abs_miss)
                chosen_z = z if abs_miss == miss_below else (z + 1)
                best_record = (x, y, chosen_z, abs_miss, rel_miss)

                # Print the label with all relevant information
                print(
                    f"New best near miss found: x={x}, y={y}, z={chosen_z} | "
                    f"absolute miss = {abs_miss} | relative miss = {rel_miss:.12f} ({rel_miss:.6%})"
                )

    # Final summary
    print("Search complete.")
    if best_record is not None:
        x, y, z, abs_miss, rel_miss = best_record
        print("Smallest relative miss found:")
        print(
            f"  x={x}, y={y}, z={z}"
            f"  absolute miss = {abs_miss}"
            f"  relative miss = {rel_miss:.12f} ({rel_miss:.6%})"
        )
    else:
        print("  No near misses recorded (this is unexpected for the given search space).")


def main() -> None:
    """Main entry: prompt for inputs, validate, run the search, then pause before exiting the IDE."""
    print("Collin's Fermat Near Miss Search: ")

    # Input prompts with validation and a loop to retry the inputs if an error occurs
    while True:
        try:
            n_str = input("Enter the value for exponent n (2 < n < 12): ").strip()
            k_str = input("Enter the value for the upper bound k (k ≥ 10): ").strip()
            n = int(n_str)
            k = int(k_str)
            validate_inputs(n, k)
            break
        except ValueError as ve:
            print(f"Input error: {ve}. Please try again.")

    print(f"Searching for near misses with n={n}, x,y in [10, {k}] ...")

    find_near_misses(n, k)

    # Pause so the user can review the output before the IDE automatically closes
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()

