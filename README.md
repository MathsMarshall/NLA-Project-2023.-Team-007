# NLA-Project-2023: Team-007
This was a project of some skoltech students, where the task was the implementation of a Block like Cholesky Matrix Factorization: https://doi.org/10.1002/nla.2497

In the paper, it is acknowledged that block algorithms are generally faster than other algorithms, and householder transformations are more stable. So the author proposes a method that tries to take advantage of the best of both worlds. In this repository, we implement from the ground up (using only basic Numpy functions, cholesky, lu functions in scipy.linalg, and matplotlib), the algorithms in the paper, specifically: algorithm 1, algorithm 2, and algorithm 3. Algorithm 3 is the grand result of the paper, for "tall skinny matrices."

## The Problem
We consider $m \geq n$ always.

Algorithm 1: Recursive Householder-based QR factorization of $A \in \mathbb{R}^{m \times n}$ with orthogonal factor in the form $Q = I - VSV^T$.

Input: $A \in \mathbb{R}^{m \times n}$

Output: $V,\ R \in \mathbb{R}^{m \times n}, \ S \in \mathbb{R}^{n \times n}$ representing the QR factor of $A$.

Algorithm 2:  Block Cholesky-LU-based QR factorization of $A$ with orthogonal factor in the form $Q = I − VSV^T$ (Please refer to the Jupyter notebook file for formulas as the LaTeX was not working well here)

Input: $A \in \mathbb{R}^{m \times n}$ (It must also permit LU factorisation without permutation).

Output: $V,\ R \in \mathbb{R}^{m \times n}, \ S, \ R_{□} \in \mathbb{R}^{n \times n}$ representing the QR factor of $A$.

Algorithm 3: It uses a user-defined parameter $k$ to decide when to shift from algorithm 1, which involves equal splits of columns, to the block method of algorithm 2.

The task is to show that overall, algorithm 3 is faster than Algorithm 1 and more stable than Algorithm 2. Of more interest would be to find the best k.

## Directions for use

In each function we implemented, we have included documentation for the user to know what type of matrices each function accepts as input. We have also enabled the functions to give errors where necessary as a guide to the user to edit the function inputs.

For the numerical analysis, we do both a stability check and a speed check. For the speed test, we compare algorithm 3 to algorithm 1 and for the stability test, we compare algorithm 3 to algorithm 2. For the speed test, we use the time module in Python, and for the stability test, we generate a random matrix with a given condition number, and we do a relative loss of orthogonality check, as defined in the paper, but we use spectral norm, whereas Frobenius norm was used in the paper.



## Team Members Contribution

Holdings Ogon -  Implemented algorithm 1 and helped with writing the condtion_number function

Joshua Udobang -  Did the plot graphing and observed the empirical results

Nwachukwu Mmesomachi - Implemented Algorithm 3 and verified the mathematical correctness. Wrote the README file

Okechukwu Okeke - Implemented algorithm 2 and modularised the code


## References

Le Borne S. A block Cholesky-LU-based QR factorization for rectangular matrices. Numer Linear Algebra Appl. 2023;30(5):e2497

Barlow J. Block modified Gram-Schmidt algorithms and their analysis. SIAM J Matrix Anal Appl. 2019;40:1257–90. 

Carson E, Lund K, Rozloznik M, Thomas S. Block Gram-Schmidt algorithms and their stability properties. Linear Algebra Appl. 2022;638:150–95. 

Terao T, Ozaki K, Ogita T. LU-Cholesky QR algorithms for thin QR decomposition. Parallel Comput. 2020;92:102571. https://doi.org/10. 1016/j.parco.2019.102571 4. 

Golub G, Van Loan C. Matrix computations. 3rd. ed. London: John Hopkins; 1996. 5.

Kressner D, Susnjara A. Fast QR decomposition of HODLR matrices, 2018. https://arxiv.org/abs/1809.10585 6. 
 
Le Borne S. Block computation and representation of a sparse nullspace basis of a rectangular matrix. Linear Algebra Appl. 2008;428:2455–67
![image](https://github.com/MathsMarshall/NLA-Project-2023.-Team-007/assets/54585664/e4e7952a-3346-4b22-9070-0f125a375c3f)


