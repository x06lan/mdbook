# hw1

[2023 computer-networking HW1.pdf](../../../assets/pdf/computer_networkingHW1.pdf)

## 1. Suppose Host A wants to send a large file to Host B. The path from Host A to Host B contains three hops (links), with the link rates of these hops of rates R1 = 500 kbps, R2 = 2Mbps, and R3 = 1Mbps. That is, the file sent by Host A must pass through two immediate routers to reach Node B. 
### 1.a Assuming no other traffic in the network, what is the throughput for the file transfer.
Determine the bottleneck link, which is the link with the lowest throughput. In this case, the bottleneck link is the first hop with a throughput of 500 kbps.
### 1.b Repeat 1.a, but now with R3 reduced to 200 Kbps.
The bottleneck link is the first hop with a throughput of 200 kbps.
## 2. Suppose users share a 2 Mbps link. Also suppose each user requires 100 Kbps when transmitting, but each user transmits only 20% of the time in average. (You may review the concept of statistical multiplexing for solving this problem)
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


## 3. Consider the queuing delay in a router buffer (preceding an outbound link).Suppose all packets are L bits, the transmission rate is R bps and that N packets simultaneously arrive at the buffer every LN/R seconds. Find the average queuing delay of a packet. (Hint: The queuing delay for the first packet is zero; for the second packet L/R; for the third packet 2L/R. The Nth packet has already been transmitted when the second batch of packets arrives.)
$$
delay(n)=\frac{LN}{R}\\
\text{average delay}=\frac{1}{N}\sum_{n=0}^{N-1}delay(n)\\
$$

## 4. Consider a packet of length L which begins at end system A, travels over one link to a packet switch, and travels from the packet switch over a second link to a destination end system. Let di, s¡, and Ri denote the length, propagation speed, and the transmission rate of link i, for i = 1,2. The packet switch processes and delays each packet by dproc. Assuming no queuing delays, in terms of d¡, s¡, R¡, (i = l,2), and L, what is the total end-to-end delay for the packet? Suppose now the packet length is 1,000 bytes, the propagation speed on both links is $2\times 10^8 $m/s, the transmission rates of both links is 2 Mbps, the packet switch processing delay is 1 msec, the length of the first link is 4,000 km, and the length of the last link is 1,000 km. For these values, what is the end-to-end delay?

$$
\begin{aligned}{}
\text{end to end delay}&=\text{delay}_{proc_{\ 4000km}}+\text{delay}_{trans}+\text{delay}_{queue}+\text{delay}_{prop_{\ 1000km}}+\text{delay}_{trans}\\
&=\frac{4000\times 10^3}{2\times 10^8}+\frac{1000\times 8}{2\times 10^6}+10^{-3}+\frac{1000\times 10^3}{2\times 10^8}+\frac{1000\times 8}{2\times 10^6}\\
&=(0.02+0.004+0.001+0.005+0.004)s\\
&=0.034s\\
\end{aligned}
$$

## 5. What are the five layers in the Internet protocol stack? What are the principal responsibilities of each of these layers?
### Physical Layer: 
Hardware layer, such as cables, connectors, and network interface cards.
### Link Layer: 
link two directly connected nodes, and the protocols that they use to communicate.
### Network Layer: 
provide the functional and procedural means of transferring variable length data sequences from a source to a destination via one or more networks, while maintaining the quality of service functions.
### Transport Layer:
transport data between two hosts, such as connection-oriented communication and connectionless communication.
### Application Layer:
let application programs that use the network, such as web browsers, email clients, remote file access, etc.
