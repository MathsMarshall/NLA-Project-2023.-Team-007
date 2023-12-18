# NLA-Project-2023: Team-007
This was a project of some skoltech students, where the task was the implementation of a Block like Cholesky Matrix Factorization: https://doi.org/10.1002/nla.2497

In the paper, it is acknowledged that block algorithms are generally faster than other algorithms, and householder transformations are more stable. So the author proposes a method that tries to take advantage of the best of both worlds. In this repository, we implement from ground up (using only basic Numpy functions and matplotlib), the algorithms in the paper, specifically: algorithm 1, algorithm 2 and algorithm 3. Algorithm 3 is the grand result of the paper, for "tall skinny matrices."

## The Problem
We consider $m \geq n$ always.

Algorithm 1: Recursive Householder-based QR factorization of $A \in \mathbb{R}^{m \times n}$ with orthogonal factor in the form $Q = I - VSV^T$.

Input: $A \in \mathbb{R}^{m \times n}$

Output: $V,\ R \in \mathbb{R}^{m \times n}, \ S \in \mathbb{R}^{n \times n}$ representing the QR factor of $A$.

Algorithm 2:  Block Cholesky-LU-based QR factorization of $A$ with orthogonal factor in the form $Q = I − VSV^T$ (Please refer to the Jupyter notebook file for formulas as the LaTeX was not working well here)

Input: $A \in \mathbb{R}^{m \times n}$

Output: $V,\ R \in \mathbb{R}^{m \times n}, \ S, \ R_{□} \in \mathbb{R}^{n \times n}$ representing the QR factor of $A$.

Algorithm 3: It uses a user defined parameter $k$ to decide when to shift from algorithm 1, which involves equal splits of columns, to the block method of algorithm 2.

The task is to show that overall, algorithm 3 is faster than algorithm 1, and more stable than algorithm 2. Of more interest would be to find the best k.

## Directions for use

In each function we implemented, we have included a documentation for the user to know what type of matrices each function accepts as an input. We have also enabled the functions to give error where necessary as a guide to the user to edit the function inputs.

For the numerical analysis, we do both a stability check and speed check. For the speed test, we compare algortihm 3 to algorithm 1 and for the stability test we compare algorithm 3 to algorithm 2. For speed test we use the time module in Python, and for the stability test, we generate a random matrix with a given condition number, and we do relative loss of orthogonality check, as defined in the paper, but we use spectral norm, whereas Frobenius norm was used in the paper.



Team Memeber Contribution
Holdings Ogon -  Implemented algoriuthm 1 and helped with writing the condtion_number function
Joshua Udobang -  Did the plot graphing and observed the emprical results
Nwachukwu Mmesomachi - Implemented Algorithm 3 and verified the mathematical correctness. Wrote the README file
Okechukwu Okeke - Implemented algorithm 2 and modularised the code
