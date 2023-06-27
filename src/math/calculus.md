# Calculus

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
$$\frac{d}{dx}cos(x)=-sin(x)$$
$$\int e^{f(x)} \ dx=\frac{e^{f(x)}}{f'(x)}+c$$
$$\int \ln(x) \ dx=x\ln(x)-x+c$$
$$\int \frac{1}{x} \ dx=\ln(x)+c$$
$$\int sin(x) \ dx=-cos(x)+c$$
$$\int tan(x) \ dx=-\ln(cos(x))+c$$
$$\int sec(x)^2 \ dx=tan(x)+c$$
$$\int \frac{2x}{1+x^2} \ dx=\ln(1+x^2)+c$$