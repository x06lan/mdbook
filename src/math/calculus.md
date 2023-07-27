# Calculus
tags `math` `calculus`

## Differential 
$$f'(x)=\lim_{h\rightarrow 0}\frac{f(x+h)+f(x)}{h}$$
$$f'(x)=\frac{d}{dx}f(x)$$
$$\frac{d}{dx}f(x)g(x)=f'(x)g(x)+f(x)g'(x)$$
$$\frac{d}{dx}\frac{f(x)}{g(x)}=\frac{f'(x)g(x)+f(x)g'(x)}{g(x)^2}$$
$$\frac{d}{dx}f(g(x))=f'(g(x))\times g'(x)$$
### example
$$\frac{d}{dx}cos(x)=-sin(x)$$
$$\frac{d}{dx}tan(x)=sec(x)^2$$
$$\frac{d}{dx}cot(x)=csc(x)^2$$
$$\frac{d}{dx}sin^{-1}(x)=\frac{1}{\sqrt{1-x^2}}$$
$$\frac{d}{dx}cos^{-1}(x)=\frac{-1}{\sqrt{1-x^2}}$$
$$\frac{d}{dx}tan^{-1}(x)=\frac{1}{1+x^2}$$

## intergrant
$$g(x)=\underset{_{k(x)}}{\int^{h(x)}}f(x) \ dx\\
g'(x)=f(h(x))h'(x)-f(k(x))k'(x)
$$
$$
\int f(x) \ d g(x)=f(x)g(x)-\int g(x) \ d f(x)
$$
### example
$$\int e^{f(x)} \ dx=\frac{e^{f(x)}}{f'(x)}+c$$
$$\int \ln(x) \ dx=x\ln(x)-x+c$$
$$\int \frac{1}{x} \ dx=\ln(x)+c$$
$$\int sin(x) \ dx=-cos(x)+c$$
$$\int tan(x) \ dx=-\ln(cos(x))+c$$
$$\int sec(x)^2 \ dx=tan(x)+c$$
$$\int \frac{2x}{1+x^2} \ dx=\ln(1+x^2)+c$$


## Taylor series 泰勒展開式
$$
% f(x)=a_0 x^0+a_1x^1+a_2x^2+a_3x^3 \cdots\\
% f'(x)=(1)a_1x^0+( 2 )a_2 x^1+(3 ) a_3 x^2\cdots\\
% f''(x)=( 2 )a_2 x^0+(6 ) a_3 x^1\cdots\\
f^{(n)}(a)=f(x)在x=a的n次導數\\
f(x)=\frac{f^{(0)}(a)}{0!}(x-a)^0+\frac{f^{(1)}(a)}{1!}(x-a)^1+\frac{f^{(2)}(a)}{2!}(x-a)^2 \cdots\\
f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n

$$
## find sin(x) Taylor series 
$$

\begin{alignedat}{}
f(x)=sin(x) \rightarrow &f^0(x)=sin(x)\\
& f^1(x)=cos(x)\\
& f^2(x)=-sin(x)\\
& f^3(x)=-cos(x)\\
& f^4(x)=sin(x)=f^0(x)\\
\end{alignedat}\\
\text{if }a=0\\
\begin{alignedat}{}
f(x)&=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n\\
    &=\sum_{n=0}^{\infty}\frac{sin(0)}{(4n+0)!}(x)^{4n}+\frac{cos(0)}{(4n+1)!}(x)^{4n+1}+\frac{-sin(0)}{(4n+2)!}(x)^{4n+2}+\frac{-cos(0)}{(4n+3)!}(x)^{4n+3}\\
    &=\sum_{n=0}^{\infty}\frac{cos(0)}{(4n+1)!}(x)^{4n+1}+\frac{-cos(0)}{(4n+3)!}(x)^{4n+3}\\
    &=\sum_{n=0}^{\infty}\frac{1}{(4n+1)!}(x)^{4n+1}+\frac{-1}{(4n+3)!}(x)^{4n+3}\\
    sin(x)&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}(x)^{2n+1}\\
\end{alignedat}\\
$$