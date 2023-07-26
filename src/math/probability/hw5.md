# hw5 110590049

[2023PB_HW5.pdf](../../assets/pdf/2023PB_HW5.pdf)

## 1

$$
P(X=0)=\frac{6}{36},
P(X=1)=\frac{10}{36},
P(X=2)=\frac{8}{36},\\
P(X=3)=\frac{6}{36},
P(X=4)=\frac{4}{36},
P(X=5)=\frac{2}{36}
$$

## 2

$$
P(X<1)=F(1^-)=\frac{1}{2}\\
P(X=1)=F(1)-F(1^-)=\frac{1}{6}\\
P(0 \le X<1)=F(1^-)-F(0^-)=\frac{1}{4}\\
P(X>\frac{1}{2})=1-F(\frac{1}{2})=\frac{1}{2}\\
P(X=\frac{3}{2})=F(\frac{3}{2})-F(\frac{3^-}{2})=0\\
P(1<X\le6)=F(6)-F(1)=\frac{1}{3}\\
$$

## 3

$$
q=1-p=0.88\\
1-q^x\ge 0.6\\
q^x\le 0.4\\
0.88^x\le0.4\\
x\times ln(0.88)\ge ln(0.4)\\
x\ge 7.1,x=8
$$

## 4

$$
P(1)=\frac{11}{36},
P(2)=\frac{9}{36},
P(3)=\frac{7}{36}\\
P(5)=\frac{5}{36},
P(5)=\frac{3}{36},
P(6)=\frac{1}{36}\\
f(x)=\begin{cases}
0 &x<1\\
\frac{11}{36} & 1 \le x<2\\
\frac{5}{9} & 2 \le x<3\\
\frac{3}{4} & 3 \le x<4\\
\frac{8}{9} & 5 \le x<6\\
1 & 6 \le x\\
\end{cases}
$$

## 5

$$
\frac{200 0000}{2000000}*-1
+\frac{4000}{2000000}*30+\frac{500}{2000000}*800+\frac{1}{2000000}*1200000=-0.14
$$

## 6

$$
E[x(11-x)]=E[-x^2]+11E[x]\\
E[-x^2]=\sum_{i=1}^{10}\frac{-i^2}{10}=-38.5\\
11E[x]=11\sum_{i=1}^{10}\frac{i}{10}=60.5\\
E[x(11-x)]=22
$$

## 7

$$
\text{First one.}\\
\text{Because the standard deviation is smaller}
$$

## 8

$$
E[x]=\sum_{i=0}^{\infty}i*p(x=i),E[x^2]=\sum_{i=0}^{\infty}i^2*p(x=i)\\
E[x]=-3*\frac{3}{8}+0*\frac{3}{8}+6*\frac{1}{4}=\frac{3}{8}\\
E[x^2]=9*\frac{3}{8}+0*\frac{3}{8}+36*\frac{1}{4}=\frac{99}{8}\\
var(x)=E[x^2]-(E[x])^2=12.23\\
\sigma=\sqrt{var(x)}=3.498
$$

## 9

$$
E[x^2-2x]=E[x^2]-2E[x]=3\\
E[x^2]=5\\
var(x)=E[x^2]-(E[x])^2=5-1=4\\
var(-3x+4)=(-3)^2var(x)=9*4=36

$$