tags `math` `linear` `algebra`

# linear algebra

## matrix

|      | Column 1 | Column 2 | Column 3 |
| ---- | -------- | -------- | -------- |
| Row1 | value    | value    | value    |
| Row2 | value    | value    | value    |
| Row3 | value    | value    | value    |

diagoua 對角
commtative law
associative law
distributive law

## sample

$$
    A=\begin{bmatrix}
    1&2\\
    3&4\\
    \end{bmatrix}
$$

$$
    B=\begin{bmatrix}
    1&-2\\
    2&-4\\
    \end{bmatrix}
$$

## 乘積

$$
    A=\begin{bmatrix}
    a&b\\
    c&d\\
    \end{bmatrix}
    \\
    B=\begin{bmatrix}
    1&2\\
    3&4\\
    \end{bmatrix}
    \\
    A*B=\begin{bmatrix}
    a*1+b*3 & a*2+b*4\\
    c*1+d*3& c*2+d*4\\
    \end{bmatrix}
    \\
    A=\begin{bmatrix}
    2&3\\
    1&-5\\
    \end{bmatrix}
    B=\begin{bmatrix}
    4&3&6\\
    1&-2&3\\
    \end{bmatrix}
    \\
    A*B=\begin{bmatrix}
    2*4+3*1 & 2*3+3*-2&2*6+3*3\\
    1*4+-5*1& 1*3+-5*-2 &1*6+-5*3\\
    \end{bmatrix}=
    \begin{bmatrix}
    11 & 0 &21\\
    -1& 13 &-9\\
    \end{bmatrix}\\
    \underset{[n\times m]}{A}*\underset{[m\times s]}{B}=\underset{[n\times s]}{C}
$$

## 反矩陣

$$
A=\begin{bmatrix}
        a&b\\
        c&d\\
    \end{bmatrix}\\
    {a*d-b*c=0} \;then\; not \;inverable\\
    A * A^{-1}=I  =\begin{bmatrix}
    1&0\\
    0&1\\
    \end{bmatrix}
    \\
    A^{-1}=\frac{1} {\begin{vmatrix}
    a&b\\
    c&d\\
    \end{vmatrix}} *\begin{bmatrix}
    d&-b\\
    -c&a\\
    \end{bmatrix}\\
    \text{high level matrix} \\
    \begin{bmatrix}
        A&I\\
    \end{bmatrix}=
    \begin{bmatrix}
        A*A^{-1}&I*A^{-1}\\
    \end{bmatrix}=
    \begin{bmatrix}
        I&A^{-1}\\
    \end{bmatrix}\\
    \begin{bmatrix}
        1&0&0 &| & 1&0&0\\
        1&1&0 &| & 0&1&0\\
        1&1&1 &| & 0&0&1\\
    \end{bmatrix}=
    \begin{bmatrix}
        1&0&0 &| & 1&0&0\\
        0&1&0 &| & -1&1&0\\
        0&0&1 &| & 0&-1&1\\
    \end{bmatrix}\\
    \begin{bmatrix}
        1&0&0 &| & 1&0&0\\
        1&1&0 &| & 0&1&0\\
        1&1&1 &| & 0&0&1\\
    \end{bmatrix}=
    \begin{bmatrix}
        1&0&0 &| & 1&0&0\\
        0&1&0 &| & -1&1&0\\
        0&0&1 &| & 0&-1&1\\
    \end{bmatrix}
$$

## indentity matrix

$$
    I=\begin{bmatrix}
        1&0&0\\
        0&1&0\\
        0&0&1\\
    \end{bmatrix}
$$

## transpose matrix

$$
    A=\begin{bmatrix}
        1&2\\
        3&4\\
    \end{bmatrix}\\
    A^{T}=\begin{bmatrix}
        1&3\\
        2&4\\
    \end{bmatrix}
$$

## innrchange (change row)

$$
    \begin{bmatrix}
        1&2\\
        3&4\\
        5&6\\
    \end{bmatrix} ==\begin{bmatrix}
        5&6\\
        3&4\\
        1&2\\
    \end{bmatrix}
$$

## math to matrix

$$
    \begin{cases}
        1*x_1&+&2*x_2&+&3*x_3=5\\
        2*x_1&+&3*x_2&+&4*x_3=7
    \end{cases}=
    \begin{bmatrix}
        1&2&3&5\\
        2&3&4&7\\
    \end{bmatrix}
$$

## reduced echelon form(gaussian elimination)

$$
    \begin{bmatrix}
        0& 3 &-6 &6 &4 &-5\\
        3& -7 &8 &-5 &8 &9\\
        3& -9 &12 &-9 &6 &15\\
    \end{bmatrix}==
    \begin{bmatrix}
        3& -9 &12 &-9 &6 &15\\
        3& -7 &8 &-5 &8 &9\\
        0& 3 &-6 &6 &4 &-5\\
    \end{bmatrix}=
    \begin{bmatrix}
        3& -9 &12 &-9 &6 &15\\
        0&  2 &-4 &4 &2 &-6\\
        0&  3 &-6 &6 &4 &-5\\
    \end{bmatrix}\\=
    \begin{bmatrix}
        3& -9 &12 &-9 &6 &15\\
        0&  2 &-4 &4 &2 &-6\\
        0&  3 &-6 &6 &4 &-5\\
    \end{bmatrix}=
     \begin{bmatrix}
        3& -9 &12 &-9 &6 &15\\
        0&  2 &-4 &4 &2 &-6\\
        0&  0 &0  &0 &1 &4\\
    \end{bmatrix}\\=
    \begin{bmatrix}
        3& -9 &12 &-9 &6 &15\\
        0&  1 &-2 &2 &1 &-3\\
        0&  0 &0  &0 &1 &4\\
    \end{bmatrix}=
    \begin{bmatrix}
        1& -3 &4 &-3 &2 &5\\
        0&  1 &-2 &2 &1 &-3\\
        0&  0 &0  &0 &1 &4\\
    \end{bmatrix}\\=
    \begin{bmatrix}
        1& -3 &4 &-3 &0 &-3\\
        0&  1 &-2 &2 &0 &-7\\
        0&  0 &0  &0 &1 &4\\
    \end{bmatrix}=
    \begin{bmatrix}
        1&  0 &-2 &-3 &0 &-24\\
        0&  1 &-2 &2 &0 &-7\\
        0&  0 &0  &0 &1 &4\\
    \end{bmatrix}\\=
    \begin{cases}
        1*x_1 -2*x_3 +-3*x_4 =24\\
        1*x_2 -2*x_3 +2*x_4 =-7\\
        x_5=4
    \end{cases}
$$

## vector equation and matrix equation

$$
    \begin{cases}
        &x_1   &+ &2x_2  &-&x_3 &=&3\\
        -&2x_1 &- &2x_2  &+&4x_3 &=&0\\
        & &  &2x_2  &+&2x_3 &=&6\\
    \end{cases}==\\
    x_1 \begin{bmatrix}
        1\\
        -2\\
        0\\
    \end{bmatrix}
    +x_2 \begin{bmatrix}
        2\\
        -2\\
        2\\
    \end{bmatrix}
    +x_3 \begin{bmatrix}
        -1\\
        4\\
        2\\
    \end{bmatrix}=
     \begin{bmatrix}
        3\\
        0\\
        6\\
    \end{bmatrix}\\
    A\begin{bmatrix}
        1&  2 &-1 \\
        -2&-2 &4 \\
        0&  2 &2  \\
    \end{bmatrix}
    *x\begin{bmatrix}
        x_1\\
        x_2\\
        x_3\\
    \end{bmatrix}
    =\begin{bmatrix}
        3\\
        0\\
        6\\
    \end{bmatrix}\\
    Ax=b\\
    A_{matrix}*x_{vector}=b_{vector}
$$

## span

$$
	v_1=\begin{bmatrix}
        1\\
        -2\\
        0\\
    \end{bmatrix}
	v_2=\begin{bmatrix}
        2\\
        -2\\
        2\\
    \end{bmatrix}
	v_3=\begin{bmatrix}
        -1\\
        4\\
        2\\
    \end{bmatrix}\\
  set\lbrace
  \begin{matrix}
	&v_1,&v_2,&v_3
  \end{matrix}
  \rbrace
   span
   \text{: mean all the combinenation vecter of can combine by }v_1、v_2、v_3 .\\
	\\
	set\lbrace
  \begin{matrix}
	&v_1,&v_2,&v_3
  \end{matrix}
  \rbrace
   span \ R^3
   \text{: mean all the vecter can be combine by }v_1、v_2、v_3 .\\
       \text{b are the all the vector} \\
    \text{x are the all the possible vector} \\
	example:\\
	if \lbrace
  \begin{matrix}
	&v_1,&v_2,&v_3
  \end{matrix}
  \rbrace
   span \ R^3 \ then \\
    A\begin{bmatrix}
	   	 1  &2  & -1 \\
        -2 &-2  & 4 \\
    	0  & 2  & 2 \\
	\end{bmatrix}
    *x\begin{bmatrix}
        x_1\\
        x_2\\
        x_3\\
    \end{bmatrix}
    =b\begin{bmatrix}
        b_1\\
        b_2\\
        b_3\\
    \end{bmatrix}\\
	\\
	and\begin{bmatrix}
	   	 1  &2  & -1 &0\\
        -2 &-2  & 4 &0\\
    	0  & 2  & 2 &0\\
	\end{bmatrix}
	\text{have pivot position in every row}\\
	but\begin{bmatrix}
	   	 1  &2  & -1 &b_1\\
        -2 &-2  & 4 &b_2\\
    	0  & 2  & 2 &b_3\\
	\end{bmatrix}=
	\begin{bmatrix}
	   	 1  &0  & -3 &b_1\\
        0  &1  & 1 &b_2\\
    	0  & 0  & 0 &b_3\\
	\end{bmatrix} \text{did not have pivot point in row3}\\
	So  \lbrace
  \begin{matrix}
	&v_1,&v_2,&v_3
  \end{matrix}
  \rbrace
   not \ span \ R^3
$$

## linear dependence

$$
if \lbrace
  \begin{matrix}
	v_1 ,& v_2 ,& v_3
  \end{matrix}
  \rbrace
  \text{
   linear dependence then at least one of vector is linear combination of another.}
$$

## linear depandence vs. span:

$$
    A_{matrix}*x_{vector}=b_{vector}\\
A\begin{bmatrix}
	   	  0  &2  & -2 \\
	   	  1  &1  & 1 \\
	   	 -2  &0  & -4 \\
	   	 1  &2  & 0 \\
	\end{bmatrix}x
    \begin{bmatrix}
	   	  x_1 \\
	   	  x_2 \\
	   	  x_3 \\
    \end{bmatrix}=
    b
    \begin{bmatrix}
	   	  b_1 \\
	   	  b_2 \\
	   	  b_3 \\
	   	  b_4 \\
    \end{bmatrix}
$$

## echelon form

$$
\begin{bmatrix}
      0  &2  & -2 &b_1 \\
      1  &1  & 1  &b_2\\
     -2  &0  & -4 &b_3\\
     1  &2  & 0   &b_4\\
\end{bmatrix}=
\begin{bmatrix}
      1  &1  & 1  &b_2\\
      0  &2  & -2 &b_1 \\
     -2  &0  & -4 &b_3\\
     1  &2  & 0   &b_4\\
\end{bmatrix}=
\begin{bmatrix}
      1  &1  & 1  &b_2\\
      0  &2  & -2 &b_1 \\
      0  &2  & -2 &2b_2+b_3\\
      0  &1  & -1   &-b_2+b_4\\
\end{bmatrix}=\\
\begin{bmatrix}
      1  &0  & 2  &b_2+\frac{-b_1}{2}\\
      0  &2  & -2 &b_1 \\
      0  &0  & 0 &2b_2+b_3-b_1 \\
      0  &0  & 0  &-b_2+b_4+\frac{-b_1}{2}\\
\end{bmatrix}
$$

## vector equation

$$
x_1\begin{bmatrix}
      1  \\
      0  \\
      0  \\
      0  \\
\end{bmatrix}+
x_2\begin{bmatrix}
      0  \\
      2 \\
      0  \\
      0  \\
\end{bmatrix}+
x_3\begin{bmatrix}
      2  \\
      -2 \\
      0  \\
      0  \\
\end{bmatrix}=
b\begin{bmatrix}
      b_2+\frac{-b_1}{2} \\
      b_1 \\
      2b_2+b_3-b_1  \\
      -b_2+b_4+\frac{-b_1}{2}\\
\end{bmatrix}
$$

## span R^4

NO,did not have pivot point in row3 and row4

## linear independence?

NO,did not have pivot point in column 3

# transform

## one-to-one

$$
T(x)= b \\
\text{for all b only have one x that T(x)=b}
$$

## onto

$$
T(x)= b \\
\text{for all b have atleast one x that T(x)=b}
$$

## linear transformation

$$
T(x)= b \\
\text{for all b have atleast one x that T(x)=b}\\
T(a+b)=T(a)+T(b)
$$

# vectorspace

$$
\text{If A is vectorspace then}\\
\begin{cases}
\text{the zero vector or zero matrix must be in side of A}\\
\text{if u and v is inside A then (u+v) should be inside A}\\
\text{if v is inside A then n} \in \text{R and n*v should be also inside A}\\
\end{cases}
$$

# child space

$$
x=\begin{bmatrix}
      2  & 2& 4 \\
      -2 & 2& 4 \\
      0  & 4& 8 \\
\end{bmatrix}
\xrightarrow[\text{}]{\text{rref}}
\begin{bmatrix}
      1 & 0& 0 \\
      0 & 1& 2 \\
      0 & 0& 0 \\
\end{bmatrix}
$$

$$
Col(A)=Row(A^T)\\
Col(A^T)=Row(A)\\
$$

## null svfvvvvbgvvvvnvfvbnmv

$$
\text{null space : all the solution make }  Ax=0.\\
\text{orth to columns space}\\
\text{Negative the not pivot columns }\\
\text{but if the row of not pivot columns have not pivot then value of that row is 1}\\
{\begin{cases}
    {\begin{bmatrix}
        -0\\
        -2\\
        1\\
    \end{bmatrix}}
\end{cases}}
$$

## columns space

$$
\text{columns space :all the  combinenation of columsn vector }\\
Ax=b\\
\text{The pivot columns of the origin columns.}\\
    {\begin{cases}
		\begin{bmatrix}
			2\\
			-2\\
			0\\
		 \end{bmatrix},
		\begin{bmatrix}
			2\\
			2\\
			4\\
		 \end{bmatrix}
    \end{cases}}
$$

## rows space

$$
\text{rows space :the space that is orth to columns space}\\
\text{the pivot row}\\
    {\begin{cases}
		\begin{bmatrix}
			2\\
			2\\
			4\\
		 \end{bmatrix},
		\begin{bmatrix}
			-2\\
			2\\
			4\\
		 \end{bmatrix}
    \end{cases}}or
	{\begin{cases}
		\begin{bmatrix}
			1\\
			0\\
			0\\
		 \end{bmatrix},
		\begin{bmatrix}
			0\\
			1\\
			2\\
		 \end{bmatrix}
    \end{cases}}
$$

# rank nullity

![](https://cdn1.byjus.com/wp-content/uploads/2022/03/Rank-and-nullity1.png)

$$
A \in R^{m\times n} \\
rank(A)+nullity(A)=n\\
rank(A^T)+nullity(A^T)=m
$$

## rank

the number of non-zero pivot column

$$
rank(A)=dim(Col(A))\\
rank(A)=rank(A^T)
$$

## nullity/kernel

the number of zero pivot column

$$
nullity(A)=dim(Nul(A))
$$

# Eigenvector and Eigenvalue

$$
\lambda= \text{eigenvalue (nature number could be zero)}\\b## null svfvvvvbgvvvvnv

\end{bmatrix}\\ould be zero)}\\b## null svfvvvvbgvvvvnv

\end{bmatrix}\\
\lambda =0 \ or \ 9 \\
Av=\lambda v\\
\begin{bmatrix}
		6 & 9\\
		2 & 3\\
\end{bmatrix}
\begin{bmatrix}
\end{bmatrix}=9
\begin{bmatrix}
		x\\
		y\\
\end{bmatrix}\\
\begin{cases}
6x+9y=9x\\bn
2x+3y=9y\\
\end{cases}\\
Av=\lambda v\\
\begin{bmatrix}
		6 & 9\\
		2 & 3\\
\end{bmatrix}
\begin{bmatrix}
\end{bmatrix}=9
\begin{bmatrix}
		x\\
		y\\
\end{bmatrix}\\
\begin{cases}
6x+9y=9x\\
2x+3y=9y\\
6x=18y \rightarrow x=-3y \\
Av=\lambda v\\
\begin{bmatrix}
		6 & 9\\
		2 & 3\\
\end{bmatrix}
\begin{bmatrix}
		x\\
		y\\
\end{bmatrix}=0
\begin{bmatrix}
		x\\
		y\\
\end{bmatrix}\\
x \in R\\
y \in R\\
v=\begin{bmatrix}
		3\\
	    1\\
\end{bmatrix}or
\begin{bmatrix}
		a\\
	    b\\
\end{bmatrix}
$$

# diagonalization

$$
\text{Find P and D that}\\
A=PDP^{-1}\\
\text{So }
A^2=(PDP^{-1})(PDP^{-1})\\
A^2=PD^2P^{-1}\\
A^n=PD^nP^{-1}\\
\underset{n\times m}{P}=\begin{bmatrix}
		V1_{EigenVector} & V2_{EigenVector}& & V3_{EigenVector} &...\\
\end{bmatrix}\\
\underset{n \times m}{D}=\begin{bmatrix}
		\lambda1_{EigenValue}   &0  &0&... \\
        0 & \lambda2_{EigenValue} & 0&...\\
        0 & 0 &\lambda3_{EigenValue} &...\\
        \vdots & \vdots &\vdots & \ddots \\
\end{bmatrix}
$$

# orthogonal

$$
\text{If } a\cdot b=0 \text{ then }a \perp b \text{ (orthogonal)}\\
\begin{bmatrix}
1\\
2\\
\end{bmatrix}\cdot
\begin{bmatrix}
-8\\
4\\
\end{bmatrix}=1\times-8+2\times 4=0\\
\begin{bmatrix}
1\\
2\\
\end{bmatrix}\perp
\begin{bmatrix}
-8\\
4\\
\end{bmatrix}
$$

## dot

[comment]: <> ( )
[//]: # ( )

$$
\underset{n*m}{A}\cdot \underset{n*m}{B}\\
\text{columns space vector: }A\cdot B=A^T\times B\\
\text{rows space vector: }A\cdot B=A\times B^T\\
$$

## |A|

### vector

$$
|A|=\sqrt{\sum_{i=1}^{n}\sum_{j=1}^{m}{{(A_{ij})}^2}}\\
|A-B|=|A|-2A\cdot B+|B|\\
$$

### matrix

[link](https://math.stackexchange.com/questions/507742/distance-similarity-between-two-matrices)

$$
|A-B|=\text{B to A distance or Similarity between two matrices}\\
distance=\sum_{i=1}^{n}\sum_{j=1}^{m}{|A_{ij}-B_{ij}}|\\
distance=\sqrt{\sum_{i=1}^{n}\sum_{j=1}^{m}{{(A_{ij}-B_{ij})}^2}}\\
$$

## orthogonal vs orthonormal matrix

### orthogonal

$$
\text{If column vector are orth to each other}\\
$$

### orthonormal

$$
\text{If column vector are orth to each other and the lenght of  column vector is 1  then is orthonormal}\\
\text{then is orthogonal matrix}\\
\begin{bmatrix}
\frac{1}{\sqrt{3}} \\
\frac{1}{\sqrt{3}} \\
\frac{1}{\sqrt{3}} \\
\end{bmatrix} \perp
\begin{bmatrix}
1 \\
1 \\
-2 \\
\end{bmatrix} \perp
\begin{bmatrix}
-3 \\
3 \\
0 \\
\end{bmatrix}
\\
\left|
\begin{bmatrix}
\frac{1}{\sqrt{3}} \\
\frac{1}{\sqrt{3}} \\
\frac{1}{\sqrt{3}} \\
\end{bmatrix} \right|=1\\
\begin{bmatrix}
\frac{1}{\sqrt{3}} & 1 & -3\\
\frac{1}{\sqrt{3}} & 1 & 3\\
\frac{1}{\sqrt{3}} & -2& 0\\
\end{bmatrix}\text{is orthogonal matrix}\\
\text{if A is orthogonal matrix then } A^T \times A=I \\
A^T=A^{-1}
$$

## find orth basis(gram-schmidt process)

## erivative of a Matrix

$$
A=\begin{bmatrix}
1 &2\\
3 &4\\
\end{bmatrix}\\
Ax=\begin{bmatrix}
1 &2\\
3 &4\\
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
\end{bmatrix}=
\begin{bmatrix}
1x_1+2x_2 \\
3x_1+4x_2 \\
\end{bmatrix}\\
f_1(x_1,x_2)=1x_1+2x_2\\
f_2(x_1,x_2)=3x_1+4x_2\\
\frac{d}{dx}Ax=
\begin{bmatrix}
\frac{d}{dx_1}f_1 &\frac{d}{dx_2}f_1 \\
\frac{d}{dx_1}f_2 &\frac{d}{dx_2}f_2 \\
\end{bmatrix}=
\begin{bmatrix}
1&2 \\
3&4 \\
\end{bmatrix}=A\\
\therefore\frac{d}{dx}Ax=A\\
X^TAX=
\begin{bmatrix}
x_1 & x_2 \\
\end{bmatrix}
\begin{bmatrix}
a_{11}x_1+a_{12}x_2 \\
a_{21}x_1+a_{22}x_2 \\
\end{bmatrix}=\begin{bmatrix}
a_{11}{x_1}^2+a_{12}x_1x_2+a_{21}x_1x_2+a_{22}{x_2}^2 \\
\end{bmatrix}\\
f_3(x_1,x_2)=a_{11}{x_1}^2+a_{12}x_1x_2+a_{21}x_1x_2+a_{22}{x_2}^2\\
\frac{d}{dx}X^TAX=
\begin{bmatrix}
\frac{d}{dx_1}f_3 &\frac{d}{dx_2}f_3 \\
\end{bmatrix}=
\begin{bmatrix}
2x_1+a_{12}x_2 & 2x_2+a_{21}x_1 \\
\end{bmatrix}
\\
\because z \neq x \\
$$

## perjection

$$
\hat{y}=\frac{y\cdot A}{y \cdot y}\times y\\
\text{define } z=y-\hat{y}\\
z=y(1-\frac{y\cdot A}{y \cdot y})\\
so\begin{cases}
y=\hat{y}+z\\
\hat{y}\perp z\\
\hat{y}\in \text{A columns space}\\
\end{cases}
$$

## curve fitting | regression | normal eqution

$$
(\dim \beta)n=2,
\text{(test number)}m=4\\
\text{(x,y)   y= }\beta_0+x\beta_1\\
\text{(2,1)   1= }\beta_0+2\beta_1\\
\text{(5,2)   2= }\beta_0+5\beta_1\\
\text{(7,3)   3= }\beta_0+7\beta_1\\
\text{(8,3)   3= }\beta_0+8\beta_1\\
\\
A\times \beta=y\\
\underset{A[m\times n]}{\begin{bmatrix}
1&2 \\
1&5 \\
1&7 \\
1&8 \\
\end{bmatrix}}\times
\underset{\beta[n\times 1]}{\begin{bmatrix}
\beta_0 \\
\beta_1 \\
\end{bmatrix}}=
\underset{y[m\times 1]}{\begin{bmatrix}
1 \\
2 \\
3 \\
3 \\
\end{bmatrix}}\\
\hat{y}=y \text{ projection on }A\\
z=y-\hat{y}\\
z\in \text{nul }A^T\\
\text{distance of y to A columns space is } z(\text{because } z \perp A)\\
$$

### way 1

$$
\text{Find } \beta \ let \ {|A\beta - y|}^2 \text{have} \min\\
{|A\beta - y|}^2=(|A\beta|-2A\beta\cdot y+|y|)^2\\
{|A\beta - y|}^2=(|A\beta|-2A\beta\cdot (\hat{y}+z)+|\hat{y}+z|)^2\\
{|A\beta - y|}^2=(|A\beta|-2A\beta\cdot (\hat{y}+z)+|\hat{y}+z|)^2\\
$$

### way 2

$$
\text{Find } \beta \ let \ {|A\beta - y|}^2 \text{have} \min\\
\text{if erivative }f^{'}(a)=0 \ then \ f(a)\text{ is max or min value }\\
\frac{d}{d\beta}{|y-A\beta|}^2=0\\
2{|y-A\beta|}\times\frac{d}{d\beta}|y-A\beta|=0\\
2{|y-A\beta|}\times\frac{d}{d\beta}(|y|-2y\cdot A\beta+|A\beta|)=0\\
2{|y-A\beta|}\times (A+|A\beta|)=0\\
$$

### way 3

$$
\text{Find } \beta \ let \ {|A\beta - y|}^2 \text{have} \min\\
|A^Ty-A^TA\beta|=A^T\times distance\\
|A^T(\hat{y}+z)-A^TA\beta|=A^T\times distance\\
|A^T\hat{y}+A^Tz-A^TA\beta|=A^T\times distance\\
|A^T\hat{y}-A^TA\beta|=A^T\times distance\\
\hat{y}\in \text{A columns space so can find }A\beta =\hat{y} \\
|A^T\hat{y}-A^TA\beta|=0\\
A^Ty=A^TA\beta\\
$$
