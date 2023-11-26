# hw2

[2023 computer-networking HW1.pdf](../../assets/pdf/computer_networkingHW2.pdf)

## 1.
use UDP  because it is faster then TCP
## 2.
When a user requests an object, the cache checks if it has a copy of the object. If it does, the cache returns the object to the user without having to retrieve it from the original server
## 3.
The applications of HTTP, SMTP, and POP3 require more reliability than throughput, so they use TCP.
## 4.
total time=$\underset{\text{setup}}{RTT_0}+ \sum_{i=1}^n RTT_i + \underset{\text{return answer}}{RTT_0}$<br>
This is because each DNS server visited create an RTT, and once the IP address is obtained, an additional RTT is incurred to establish a connection with the server containing the object. The total time elapsed is equal to the sum of all these RTTs
## 5.a
$$
\begin{aligned}
total time&=\underset{\text{setup}}{2RTT}+ \underset{\text{requset 3 obj at same time}}{ 2 RTT}\\
&=4RTT
\end{aligned}
$$
## 5.b
$$
\begin{aligned}
total time&=\underset{\text{setup}}{2RTT}+ \underset{\text{requset 3 obj one by one}}{3\times 2 RTT}\\
&=8RTT
\end{aligned}
$$

## 5.c
$$
\begin{aligned}
total time&=\underset{\text{setup}}{2 RTT}+ \underset{\text{requset 3 obj at same time but cut half by Persistent HTTP}}{ RTT}\\
&=3RTT
\end{aligned}
$$
