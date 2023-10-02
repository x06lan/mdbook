# hw1

[2023 computer-networking HW1.pdf](../../../assets/pdf/computer_networkingHW1.pdf)

## 1.
Determine the bottleneck link, which is the link with the lowest throughput. In this case, the bottleneck link is the first hop with a throughput of 500 kbps.
### 1.b Repeat 1.a, but now with R3 reduced to 200 Kbps.
The bottleneck link is the first hop with a throughput of 200 kbps.
## 2. 
### 2.a 
$$
2Mbps/100Kbps=20
$$
### 2.b
$$
0.2
$$
### 2.c
$$
X\sim B(N, 0.1)\\
P(N,x)=\text{C}^{N}_{x}\times p^{x}\times(1-p)^{N-x}\\
P(n)=\text{C}^{40}_{n}\times p^{n}\times(1-p)^{40-n}\\
$$

### 2.d
$$
P(n\geq 21)=1-P(n\leq 20)\\
P(n\geq 21)=1-\sum_{x=0}^{20}P(x)\\
P(n\geq 21)=0.00000502
$$


## 3. 
$$
delay(n)=\frac{Ln}{R}\\
\begin{aligned}{}
\text{average delay}&=\frac{1}{N}\sum_{n=0}^{N-1}delay(n)\\
&=\frac{(N-1)\times L}{2R}\\
\end{aligned}
$$

## 4. 
$$
\begin{aligned}{}
\text{end to end delay}&=\text{delay}_{proc_{\ 4000km}}+\text{delay}_{trans}+\text{delay}_{queue}+\text{delay}_{prop_{\ 1000km}}+\text{delay}_{trans}\\
&=\frac{4000\times 10^3}{2\times 10^8}+\frac{1000\times 8}{2\times 10^6}+10^{-3}+\frac{1000\times 10^3}{2\times 10^8}+\frac{1000\times 8}{2\times 10^6}\\
&=(0.02+0.004+0.001+0.005+0.004)s\\
&=0.034s\\
\end{aligned}
$$

## 5. 
### Physical Layer: 
rincipal responsibilities: Hardware layer, such as cables, connectors, and network interface cards.
### Link Layer: 
rincipal responsibilities: link two directly connected nodes, and the protocols that they use to communicate.
### Network Layer: 
rincipal responsibilities: provide the functional and procedural means of transferring variable length data sequences from a source to a destination via one or more networks, while maintaining the quality of service functions.
### Transport Layer:
rincipal responsibilities: transport data between two hosts, such as connection-oriented communication and connectionless communication.
### Application Layer:
rincipal responsibilities: let application programs that use the network, such as web browsers, email clients, remote file access, etc.
