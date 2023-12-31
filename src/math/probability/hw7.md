# hw7 110590049
tags `probability`

[2023PB\_HW7.pdf](../../assets/pdf/2023PB_HW7.pdf)

## 1.a

$$
1=\int_{-\infty }^{\infty } ce^{-3x} \,dx={c\frac{e^{-3x}}{-3}}\Big|_{0}^{\infty}\\  \underset{x\rightarrow \infty}{\text{limit}}{\frac{1}{-3e^{3x}}}=0\\ 1=0-c\frac{1}{-3}\\ c=3\\
$$

## 1.b

$$
\int_{0}^{0.5}3e^{-3x}\,dx ={{-e^{-3x}}}\Big|_{0}^{0.5}\\ =-e^{-1.5}+1=0.776
$$

## 2.a

$$
g(x)=\begin{cases} 0,x<4\\ 32x^{-3},x\ge 4\\ \end{cases}
$$

## 2.b

$$
\int_0^{4} 0\,dx+\int_4^5 32x^{-3}\,dx=-16x^{-2}\Big|_4^5=\frac{9}{25}\\ \int_6^{\infty} 32x^{-3}\,dx=-16x^{-2}\Big|_6^\infty=\frac{4}{9}\\ \int_5^{7} 32x^{-3}\,dx=-16x^{-2}\Big|_5^7=0.313\\ \int_1^{3.5} 0\,dx=0
$$

## 3

$$
{\huge y=x^3}\\ p( x^3\le y)=p( x\le y^{\frac{1}{3}})=\int_{-\infty}^{y^{\frac{1}{3}}}\frac{1}{4}\,dx=\frac{1}{4}x\Big|^{y^{\frac{1}{3}}}_{-2}=\frac{1}{4}y^{\frac{1}{3}}+\frac{1}{2}\\ g(y)= \begin{cases} 0,y<-8\\ \frac{1}{4}t^{\frac{1}{3}}+\frac{1}{2},-8\le y \le 8\\ 0,y>8\\ \end{cases}\\ g'(y)=\begin{cases} 0,y<-8\\ \frac{1}{12}x^{-\frac{2}{3}},-8\le y \le 8\\ 0,y>8\\ \end{cases}\\ {\huge z=x^4}\\ p(x^4\le z)=p(z^{\frac{1}{4}}\le x\le z^{\frac{1}{4}})=\int_{-z^{\frac{1}{4}}}^{z^{\frac{1}{4}}}\frac{1}{4}\,dx=\frac{1}{4}x\Big|^{z^{\frac{1}{4}}}_{-z^{\frac{1}{4}}}=\frac{1}{2}z^{\frac{1}{4}}\\ g(z)= \begin{cases} 0,z<0\\ \frac{1}{2}z^{\frac{1}{4}},0\le z \le 16\\ 0,z>16\\ \end{cases}\\ g'(z)= \begin{cases} 0,z<0\\ \frac{1}{16}z^{\frac{-3}{4}},0\le z\le 16\\ 0,z>16\\ \end{cases}\\
$$

## 4

$$
y=x^{\frac{2}{3}}\\ p(0\le y\le t^{\frac{3}{2}})=\int_{0}^{t^{\frac{3}{2}}} \lambda e^{-\lambda x} \,dx=-e^{\lambda x}\Big|^{t^{\frac{3}{2}}}_{0}=1-e^{\lambda t^{\frac{3}{2}}}\\ g(t)= \begin{cases} 0,t<0\\ 1-e^{-\lambda t^{\frac{3}{2}}},0\le t < \infty \\ \end{cases}\\ g'(t)= \begin{cases} 0,t<0\\ \frac{3}{2}{\lambda}t^{\frac{1}{2}} e^{-\lambda t^{\frac{3}{2}}},0\le t < \infty \\ \end{cases}\\
$$

## 5

$$
E(e^x)=\int_{-\infty}^{\infty} e^x\times 3e^{-3x}\, dx=\int_{0}^{\infty} 3e^{-2x}\, dx =\frac{-3}{2}e^{-2x}\Big|^\infty_0\\ \lim_{x\rightarrow\infty}\frac{-3}{2}e^{-2x}=0\\ E(e^x)=0+\frac{3}{2}=\frac{3}{2}
$$

## 6

$$
E(x)=\int_{-\infty}^{\infty} x\times \frac{1}{2} e^{-|x|}\, dx\\ =\int_{0}^{\infty} \frac{1}{2}x e^{-x}\, dx+\int_{-\infty}^{0} \frac{1}{2}x e^{x}\, dx\\ =-\frac{1}{2}(x+1) e^{-x}\Big|^\infty_0 +\frac{1}{2}(x-1) e^{x}\Big|_{-\infty}^0 \\ =0+\frac{1}{2}-\frac{1}{2}+0=0\\ E(x^2)=\int_{-\infty}^{\infty}x^2\times \frac{1}{2} e^{-|x|}\, dx\\ =2\int_{0}^{\infty}\frac{1}{2} x^2e^{-x}\, dx=2\\ Var(x)=E(x^2)-E(x)^2=2-0^2=2
$$
