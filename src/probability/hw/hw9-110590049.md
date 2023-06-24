# hw9 110590049

[2023PB\_HW9.pdf](../../assets/2023PB_HW9.pdf)

## 1.a

$$
\sum_{x\in {1,2,3}} \sum_{y\in {1,2}} P(x,y)=1\\ \sum_{x\in {1,2,3}} \sum_{y\in {1,2}}c(x+y)=1\\ 21c=1\\ c=\frac{1}{21}
$$

## 1.b

$$
P_x(x)=\frac{1}{21}(2x+3)\\ P_y(y)=\frac{1}{21}(3y+6)
$$

## 1.c

$$
P(x\ge2 \ | \ y=1)=\frac{P(x\ge 2 \ \cap \ y=1) }{P_y(y=1)}=\\ \frac{\frac{1}{3}}{\frac{3}{7}}=\frac{7}{9}
$$

## 1.d

$$
E(x)=\sum_{x\in {1,2,3}}x\frac{1}{21}(2x+3)=2.1904\\ E(y)=\sum_{2\in {1,2}}y\frac{1}{21}(3y+6)=1.5714
$$

## 2

$$
P(x,y)=\begin{array}{|c|c|c|c|c|c|c|} 
\hline x\setminus y &1&1 &2 &3 &4 &5 \\
\hline 2 &\frac{1}{36} &0&0&0&0&0\\
\hline 3 &0 &\frac{2}{36}&0&0&0&0\\
\hline 4 &\frac{1}{36} &0&\frac{2}{36}&0&0&0\\
\hline 5 &0 &\frac{2}{36}&0&\frac{2}{36}&0&0\\
\hline 6 &\frac{1}{36} &0&\frac{2}{36}&0&\frac{2}{36}&0\\
\hline 7 &0 &\frac{2}{36}&0&\frac{2}{36}&0&\frac{2}{36}\\
\hline 8 &\frac{1}{36} &0&\frac{2}{36}&0&\frac{2}{36}&0\\
\hline 9 &0 &\frac{2}{36}&0&\frac{2}{36}&0&0\\
\hline 10 &\frac{1}{36} &0&\frac{2}{36}&0&0&0\\
\hline 11 &0 &\frac{2}{36}&0&0&0&0\\
\hline 12 &\frac{1}{36} &0&0&0&0&0\\
\hline \end{array} \\\\
p_x(x)=\frac{1}{36}(6-|7-x|)\\ 
p_y(y)=\begin{cases} \frac{6}{36} & y=0\\ \frac{2}{36}(6-y) & 0<y\le 5\\ 
0 & else \end{cases}
$$

## 3.a

$$
f_{x}(x)={\int_0^x {2 } \ dy}=2y\Big|^x_0=2x \\ f_{y}(y)={\int_y^1 {2 } \ dx}=2x\Big|^1_y=2-2y \\
$$

## 3.b

$$
E(X)=\int_0^1\int_0^1 x\times f_x(x)\ dydx=\frac{2}{3}\\ E(Y)=\int_0^1\int_0^1 y\times f_y(y)\ dydx=\frac{1}{3}\\
$$

## 3.c

$$
P(x<\frac{1}{2})=\int_0^\frac{1}{2}2x \ dx=\frac{1}{4}\\ P(x<2y)=\int_0^1\int_{\frac{v}{2}}^v 2 \ dudv=\frac{1}{2}\\ P(x=y)=\int_0^1\int_{v}^v 2 \ dudv=0\\
$$

## 3.d

$$
f_{xy}\neq f_x(x)f_y(y)\\ \text{not independent}
$$

## 3.e

$$
f_{x|y}(x|y)=\frac{f(x,y)}{f_y(y)}=\frac{2}{2-2y}
$$

## 4

$$
p_x(x)= \begin{cases} \frac{3}{7} & x=1\\ \frac{4}{7} & x=2\\ 0 & else \end{cases}\\ p_y(y)= \begin{cases} \frac{5}{7} & y=1\\ \frac{2}{7} & y=2\\ 0 & else \end{cases}\\ p_{xy}(1,1)=\frac{1}{7}\\ p_x(1)p_y(1)=\frac{15}{49}\\ p(x,y)\neq p_x(x)p_y(y)\\ \text{not independent}
$$

## 5

$$
E(x^2y)=\int_0^\infty\int_0^\infty {x^2y\times 2e^{-(x+2y)}} \ dxdy=1
$$

## 6

$$
P_{x|y}(x|y)=\frac{f(x,y)}{f_y(y)}\\ P_y(y)=\begin{cases} \frac{5}{25}&y=0\\ \frac{7}{25}&y=1\\ \frac{13}{25}&y=2\\ 0& else\\ \end{cases}\\ P(x=2|y=1)=\frac{f_{x,y}(x=2,y=1)}{p_y(y=1)}=\frac{\frac{5}{25}}{\frac{7}{25}}=\frac{5}{7}\\ E(x|y=1)=\sum_{x} x\times{f_{x,y}(x,y=1)}=\frac{12}{25}\\
$$

## 7.a

$$
\int_0^1\int_0^{1-x} \lambda \ dydx =1\\ \lambda=2
$$

## 7.b

$$
f_{x|y}(x|y)=\frac{f(x,y)}{f_y(y)}\\ f_y(y)=\int_0^{1-y}2 \ dx=2-2y\\ f_{x|y}(x|y)=\frac{1}{1-y}
$$

## 7.c

$$
E(X|Y=y)=\int_0^{1-y} x \times f_{x|y}(x|y) \ dx =\\ \int_0^{1-y} x \times \frac{1}{1-y} \ dx =\frac{x^2}{2(1-y)}\Big|_0^{1-y}=\frac{1-y}{2}\\
$$
