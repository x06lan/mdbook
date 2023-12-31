# hw8 110590049
tags `probability`

[2023PB\_HW8.pdf](../../assets/pdf/2023PB_HW8.pdf)

## 1

$$
p=\frac{1}{4}\\ P(x)=\text{C}_{x}^{15}p^x(1-p)^{15-x}\\ E(x)=\sum_{ i=0}^{15}{\{i\times P(x=i)\}}=3.75
$$

## 2

$$
x+y=k\\ P=(x>\frac{1}{3}k)\cap(y>\frac{1}{3}k) =\\(x>\frac{1}{3}k)\cap(1-x>\frac{1}{3}k)=(\frac{1}{3}k<x<\frac{2}{3})\\ P=\frac{1}{3}\\
$$

## 3

$$
P(-ln(1-x)<y)=P(x<1-e^{-y})=\int_{0}^{1-e^{-y}}1dx=(1-e^{-y})\\ g(y)= \begin{cases} (1-e^{-y})& 0\le y \le \infty\\ 0 &else\\ \end{cases}\\ g'(y)= \begin{cases} e^{-y}&0\le y \le \infty\\ 0&else\\ \end{cases}\\
$$

## 4

$$
\Phi (x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x}{ e^{\frac{-t^2}{2}}dt}\\ P(x<Z<x+\alpha)=\Phi (\frac{x+\alpha-\mu}{\sigma})-\Phi (\frac{x-\mu}{\sigma})\\ \frac{d}{dx}(\Phi (\frac{x+\alpha-\mu}{\sigma})-\Phi (\frac{x-\mu}{\sigma}))=0\\ (\frac{1}{\sqrt{2\pi}}e^{-t^2}\Big|_{\frac{x-\mu}{\sigma}}^{\frac{x+\alpha-\mu}{\sigma}})=0\\ x=-\frac{1}{2}\alpha
$$

## 5

$$
\mu=67,\sigma=\sqrt{64}\\ \Phi (x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x}{ e^{\frac{-t^2}{2}}dt}\\ P(x\ge90)=1- P(x<90)=1-\Phi(\frac{90-\mu}{\sigma})=0.00202\\ P(80<x\le90)=\Phi(\frac{90-\mu}{\sigma})-\Phi(\frac{80-\mu}{\sigma})=0.050\\ P(70<x\le80)=\Phi(\frac{80-\mu}{\sigma})-\Phi(\frac{70-\mu}{\sigma})=0.301\\ P(60<x\le70)=\Phi(\frac{70-\mu}{\sigma})-\Phi(\frac{60-\mu}{\sigma})=0.4553\\ P(x<60)=\Phi(\frac{60-\mu}{\sigma})=0.1907\\
$$

## 6

$$
P(|x-\mu|>k\sigma)=P(x-\mu>k\sigma)+P(-x+\mu>k\sigma)= \\ 1-\Phi (\frac{k\sigma+\mu-\mu}{\sigma})+\Phi (\frac{-k\sigma+\mu-\mu}{\sigma})=\\ 1-\Phi (k)+\Phi (-k)
$$

## 7

$$
P(x<y)=P(x^2<|y|)=P(-x^2<y<x^2) =\Phi(x^2)-\Phi(-x^2)=2\Phi(x^2)-1=2\times \frac{1}{\sqrt{2\pi}}e^{\frac{-(x^2)^2}{2}}-1\\ g(y)= \begin{cases} \frac{2}{\sqrt{2\pi}}e^{\frac{-y^4}{2}}-1 &y\ge 0\\ 0 &else \end{cases}\\ g'(y)= \begin{cases} \frac{-4y^{3}}{\sqrt{2\pi}}e^{\frac{-y^{4}}{2}} &y\ge 0\\ 0 &else \end{cases}
$$

## 8

$$
P(x\le t)= 1-e^{-\lambda t}\\ E(x)=\frac{1}{\lambda },E(x^2)=\frac{2}{\lambda^2}\\ \sigma=\sqrt{E(x^2)-E(x)^2}=\frac{1}{\lambda }\\ P(|x-E(x)|>2\sigma)=P(x-E(x)>2\sigma)+P(x-E(x)<-2\sigma)=\\ (1-1+e^{-\lambda(E(x)+\sigma)})+(e^{-\lambda (E(x)-2\sigma)})_{(-\frac{1}{\lambda}<0 )}= \\ (e^{-\lambda(\frac{2}{\lambda}+\frac{1}{\lambda})})=e^{-3}
$$

## 9

$$
P(\frac{n>x+1}{n > x})=P(x>1)=\\1-P(x\le 1)=1-\lambda e^{-\lambda} \\ p=1-\lambda e^{-\lambda}\\ g(x=i)=(1-\lambda e^{-\lambda})(\lambda e^{-\lambda})^{i-1}=\\ \lambda e^{-\lambda}-(\lambda e^{-\lambda})^i
$$
