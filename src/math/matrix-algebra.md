tags `math` `matrix` `algebra`

# matrix algebra

# multiplication

$$
AB=
\begin{bmatrix}
1&0\\
2&3\\
\end{bmatrix}

\begin{bmatrix}
a&b\\
c&d\\
\end{bmatrix}
$$

### dot product

$$
AB=
\begin{bmatrix}
1&0\\
2&3\\
\end{bmatrix}

\begin{bmatrix}
a&b\\
c&d\\
\end{bmatrix}=
\begin{bmatrix}
1a+0c & 1b+0d\\
2a+3c & 2b+3d\\
\end{bmatrix}
$$

### by columns

$$
AB=
\begin{bmatrix}
1&0\\
2&3\\
\end{bmatrix}

\begin{bmatrix}
a&b\\
c&d\\
\end{bmatrix}=
\begin{bmatrix}
a\begin{bmatrix} 1\\2\end{bmatrix}+c\begin{bmatrix} 0\\3\end{bmatrix}&,& b\begin{bmatrix} 1\\2\end{bmatrix}+d\begin{bmatrix} 0\\3\end{bmatrix}\\
\end{bmatrix}
$$

### by row

$$
AB=
\begin{bmatrix}
1&0\\
2&3\\
\end{bmatrix}

\begin{bmatrix}
a&b\\
c&d\\
\end{bmatrix}=
 \begin{bmatrix}
1\begin{bmatrix} a & b\end{bmatrix}+0\begin{bmatrix} c&d \end{bmatrix}\\
2\begin{bmatrix} a & b\end{bmatrix}+3\begin{bmatrix} c&d\end{bmatrix}\\
\end{bmatrix}
$$

### by block

$$
AB=
\begin{bmatrix}
1&0\\
2&3\\
\end{bmatrix}

\begin{bmatrix}
a&b\\
c&d\\
\end{bmatrix}=
\begin{bmatrix}
1\\2
\end{bmatrix}
\begin{bmatrix}
a&b
\end{bmatrix}
+
\begin{bmatrix}
0\\3
\end{bmatrix}
\begin{bmatrix}
c&d
\end{bmatrix}
$$

# matrix form of gaussian elimination

actually the row reduce from the [there](./linear-algebra.html#reduced-echelon-formgaussian-elimination) are matrix multiplication as well

Subtracting 2 times the $1^{st}$ row of A from the $2^{nd}$ row of A

$$
\{ EA \} \rightarrow A^+\\
\begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0\\
0 & 0 & 1\\
\end{bmatrix}
\begin{bmatrix}
x_{11} &x_{12} & x_{13}\\
x_{21} &x_{22} & x_{23}\\
x_{31} &x_{32} & x_{33}\\
\end{bmatrix} =
\begin{bmatrix}
x_{11} &x_{12} & x_{13}\\
x_{21}-2x_{11} &x_{22}-2x_{21} & x_{23}-2x_{13}\\
x_{31} &x_{32} & x_{33}\\
\end{bmatrix}\\
$$

## for example

$$
\begin{aligned}\\
\{ EA \} &\rightarrow A^+\\
\begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0\\
0 & 0 & 1\\
\end{bmatrix}
\begin{bmatrix}
2 & 1 & 1\\
4 & -6 & 0\\
-2 & 7 & 2\\
\end{bmatrix}&\rightarrow
\begin{bmatrix}
2 & 1 & 1\\
0 & -8 & -2\\
-2 & 7 & 2\\
\end{bmatrix}\\
\end{aligned}\\
$$

## revert U to A

$G,F,E $ are elimination operation matrix

$$
GFEA=U\\
E^{-1}F^{-1}G^{-1}U=A\\
\text{let } L=E^{-1}F^{-1}G^{-1}\\
LU=A\\
U=DU\\
LDU=A\\
$$

$$
\begin{aligned}\\
E^{-1} F^{-1} G^{-1}&=L\\

\begin{bmatrix}
1 & 0 & 0\\
l_{21} & 1 & 0\\
0 & 0 & 1\\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
l_{31} & 0 & 1\\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & l_{32} & 1\\
\end{bmatrix}
&=
\begin{bmatrix}
1 & 0 & 0\\
l_{21} & 1 & 0\\
l_{31} & l_{32} & 1\\
\end{bmatrix}\\
\begin{bmatrix}
1 & 0 & 0\\
l_{21} & 1 & 0\\
l_{31} & l_{32} & 1\\
\end{bmatrix}
&=L
\end{aligned}
$$

<!-- * $U$:Appears after forward elimination -->
<!-- * $U$: result of gaussian elimination -->
<!-- * $L$:Bring $U$ back to $A$ -->

$$
\begin{align}
Ax &= b \\
L^{-1}Ax &= L^{-1}b \\
Ux &= L^{-1}b \\
x &= U^{-1}L^{-1}b
\end{align}
$$
