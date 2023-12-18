# NLA-Project-2023: Team-007
This was a project of some skoltech students, where the task was the implementation of a Block like Cholesky Matrix Factorization: https://doi.org/10.1002/nla.2497

In the paper, it is acknowledged that block algorithms are generally faster than other algorithms, and householder transformations are more stable. So the author proposes a method that tries to take advantage of the best of both worlds. In this repository, we implement from ground up (using only basic Numpy functions and matplotlib), the algorithms in the paper, specifically: algorithm 1, algorithm 2 and algorithm 3. Algorithm 3 is the grand result of the paper.

In each function we implemented, we have included a documentation for the user to know what type of matrices each function accepts as an input. We have also enabled the functions to give error where necessary as a guide to the user to edit the function inputs.

For the numerical analysis, we do both a stability check and speed check. For the speed check, we compare algortihm 3 to algorithm 1 and for the stability test we compare algorithm 3 to algorithm 2. For speed test we use the time module in Python, and for the stability test, we generate a random matrix with a given condition number, and we do relative loss of orthogonality check, as defined in the paper, but we use spectral norm. 
