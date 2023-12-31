# hw6

[2023 computer-networking HW6.pdf](../../assets/pdf/computer_networkingHW6.pdf)

## 1.
No.
* reliable delivery:  ensures that content or resources hosted on websites can be reliably accessed by users
* TCP: lower level, providing a reliable communication channel between two devices on the Internet.

## 2.
1. Broadcasting the ARP query ensures that the request reaches all devices on the network.
2. This targeted delivery is more efficient than broadcasting, as it minimizes unnecessary traffic on the network.
## 3.
$$
m=5\\
k \text{ from } 0 \ \text{ to } 2^m-1\\
\text{probability}=\frac{1}{2^5}=0.03125\\
\text{delay}=\frac{4\times 512 \ bit}{10Mbps}=0.2048ms\\
$$
## 4.
$$
D=11010111011\\
r=3\\
\frac{D\times 2^{r}}{1001}=\frac{11010111011000}{1001}=11001110101 \text{ remainder } 101\\
R=101\\
\text{bit pattern }=11010111011000+101=11010111011101
$$
## 5.
### 5.1
$$
\begin{align}
0&=\frac{d}{d \ p}Np(1-p)^{N-1} \\
0&=N(1-p)^{N-1}+Np\times{-(N-1)(1-p)^{N-2}} \\
0&=(1-p)^{N-1}+p(-N+1)(1-p)^{N-2} \\
0&=(1-p)^{N-2}((1-p)+p(-N+1))\\
\end{align}\\
\therefore p=1 \text{ or } (1-p+-pN+p)=0\\
$$
$$
\begin{align}
(1-p+-pN+p)&=0\\
(1-pN)&=0\\
p&=\frac{1}{N}\\
\end{align}
$$

### 5.2
$$
\begin{align}
\lim_{N\rightarrow \infty} Np(1-p)^{N-1}&=\\
\lim_{N\rightarrow \infty} \frac{N}{N}(1-\frac{1}{N})^{N}&=e^{-1}\\
\end{align}
$$
