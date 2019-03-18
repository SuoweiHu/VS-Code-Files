# (a)
Prove the associative law for matrix multiplication A(BC) = (AB)C. (2 subpts)

---
To prove the equivalance of $A(BC)$ and $(AB)C$, it is required to show both $A(BC) -> (AB)C$ and $(AB)C -> A(BC)$.

---
Proving $(AB)C -> A(BC)$:

Let $A$ be a matrix of $m$ colu(m,n)s and $n$ rows, ($m*n$) matrix, according to the definition of matrix operation, $B$ must have $n$ coloums for the oeration $(AB)$ to be valid, thus let $B$ be a ($n*p$) matrix, also given by the definition of matrix operation, the product of $(AB)$ is a ($m*p$) matrix, similarly, let matrix $C$ be a ($p*q$) matrix. And teh name of the element is named after the lowcase letter of the matrix's name with its row and coloum number in the matrix, shown below:

$A = \begin{bmatrix} a(1,1) & a(1,2) & a(1,3) & ...& a1n\\  a(2,1) & a(2,2) & a(2,3) & ...& a2n\\ a(3,1) & a(3,2) & a(3,3) & ...& a3n\\ ...&...&...&...&...\\a(m,1) & a(m,2) & a(m,3) & ...& a(m,n)\\ \end{bmatrix}$$B = \begin{bmatrix} b(1,1) & b(1,2) & b(1,3) & ...& b(1,p)\\  b(2,1) & b(2,2) & b(2,3) & ...& b(2,p)\\ b(3,1) & b(3,2) & b(3,3) & ...& b(3,p)\\ ...&...&...&...&...\\b(n,1) & b(n,2) & b(n,3) & ...& b(n,p)\\ \end{bmatrix}$$C = \begin{bmatrix} c(1,1) & c(1,2) & c(1,3) & ...& c(1,q)\\  c(2,1) & c(2,2) & c(2,3) & ...& c(2,q)\\ c(3,1) & c(3,2) & c(3,3) & ...& c(3,q)\\ ...&...&...&...&...\\c(p,1) & c(p,2) & c(p,3) & ...& c(p,q)\\ \end{bmatrix}$

For the 1 row 1 column element in the (AB) matrix product:

$$(AB)(1,1)=\sum_{x=1}^{\infty} a(1,x)*b(x,1)$$

For the 1 row 2 column element in (AB) matrix product:

$$(AB)(1,2)=\sum_{x=1}^{\infty} a(1,x)*b(x,2)$$

For the 2 row 1 column element in (AB) matrix product:

$$(AB)(1,2)=\sum_{x=1}^{\infty} a(2,x)*b(x,1)$$

Therefore (AB) = $\begin{bmatrix} \sum_{x=1}^{\infty} a(1,x)*b(x,1) & \sum_{x=1}^{\infty} a(1,x)*b(x,2) & \sum_{x=1}^{\infty} a(1,x)*b(x,3) & ... & \sum_{x=1}^{\infty} a(1,x)*b(x,n) \\ \sum_{x=1}^{\infty} a(2,x)*b(x,1) & \sum_{x=1}^{\infty} a(1,x)*b(x,2) & \sum_{x=1}^{\infty} a(1,x)*b(x,3) & ... & \sum_{x=1}^{\infty} a(1,x)*b(x,n) \\ \sum_{x=1}^{\infty} a(3,x)*b(x,1) & \sum_{x=1}^{\infty} a(1,x)*b(x,2) & \sum_{x=1}^{\infty} a(1,x)*b(x,3) & ... & \sum_{x=1}^{\infty} a(1,x)*b(x,n) \\ ... &... & ... & ... \\ \sum_{x=1}^{\infty} a(m,x)*b(x,1) & \sum_{x=1}^{\infty} a(m,x)*b(x,2) & \sum_{x=1}^{\infty} a(m,x)*b(x,3) & ... & \sum_{x=1}^{\infty} a(m,x)*b(x,n) \\ \end{bmatrix}$


---
$A(BC) -> (AB)C$

Similar to the assumtion in previous prove, let $B$ be a ($m*n$) matrix, $C$ be a ($n*p$) matrix, $A$ be a ($q*m$) matrix.

