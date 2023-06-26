# hw6 110590049

[2023PB_HW6.pdf](../../assets/2023PB_HW6.pdf)

## 1

$$
p=\frac{2}{12}\\
P(x=3)=\text{C}_x^6\times p^x \times (1-p)^{6-x}=0.0535
$$

## 2

$$
p=0.45\\
P(x)=\text{C}_x^{10}\times p^x \times (1-p)^{10-x}\\
\text{when x=4 the P(x) have maximum probability } 0.2383

$$

## 3

$$
p=0.999\\
P(x)=\text{C}_x^{8}\times p^{8-x} \times (1-p)^{x}\\
P(x=\{2,4,6,8\})=0.0000278324891609

$$

## 4

$$
p=0.025,E(x)=p*80 ,\lambda=E(x)\\
P(x)=\frac{e^{-\lambda}\times \lambda^x}{x!}\\
P(X>=2)=1-P(0)-P(1)=0.59399415029
$$

## 5

$$
p=\frac{3}{10},E(x)=p*35 ,\lambda=E(X)\\
P(x)=\frac{e^{-\lambda}\times \lambda^x}{x!}\\
P(x=10)=0.1236\\
P(x=10)^2=0.015278
$$

## 6

$$
P(x)=\frac{e^{-\lambda}\times \lambda^x}{x!}\\
P(x=1)=\frac{e^{-\lambda}\times \lambda^1}{1!}\\
P(x=3)=\frac{e^{-\lambda}\times \lambda^3}{3!}\\
\frac{P(x=3)}{P(x=1)}=\frac{\lambda^2}{3!}=1\\
\lambda=2.4494\\
P(x=5)=0.0634449
$$

## 7

$$
p=0.2\\
P(x,r)=\text{C}_{r-1}^{x-1} \times (1-p)^{x-r}\times p^r\\
P(8,3)=0.05505
$$

## 8

$$
P(x)=p^{x-1}*(1-p)\\
P(x\ge n)
=1-\sum_{i=1}^{n-1}P(i)
$$

## 9

$$
p=0.15\\

P(x)=\text{C}_{10-1}^{x+10-1}\times p^{10}\times(1-p)^{x}
$$

## 10

$$
p=\frac{50}{n},
X\sim Hgeo(n, 50, 50)\\
d=50,t=50\\
P(x)=\frac{\text{C}_x^d\text{C}_{t-x}^{n-d}}{\text{C}_t^n}\\
\frac{P_{n=624}(x=4)}{P_{n=625}(x=4)}\le1,\frac{P_{n=626}(x=4)}{P_{n=625}(x=4)}\le1\\\\
n=625

$$