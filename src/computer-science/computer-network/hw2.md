# hw2

[2023 computer-networking HW1.pdf](../../assets/pdf/computer_networkingHW2.pdf)

## 1.
use UDP  because it is faster then TCP
## 2.
When a user requests an object, the cache checks if it has a copy of the object. If it does, the cache returns the object to the user without having to retrieve it from the original server
## 3.
The applications of HTTP, SMTP, and POP3 require more reliability than throughput, so they use TCP.
## 4.
total time= $RTT_0 + RTT_1 + … + RTT_n$<br>
This is because each DNS server visited create an RTT, and once the IP address is obtained, an additional RTT is incurred to establish a connection with the server containing the object. The total time elapsed is equal to the sum of all these RTTs 
## 5.a
$$
\begin{aligned}
\text{time}&=\text{connect time}&+&\text{trainsmission time}\\
           &=0 &+& 3\times\text{RTT}_0\\
           &=3 \times \text{RTT}_0\\
\end{aligned}
$$
## 5.b
$$
\begin{aligned}
\text{time}&=\text{connect time}&+&\text{trainsmission time}\\
           &=\text{RTT}_0\times 3&+&\text{RTT}_0\times 3\\
           &=6\times \text{RTT}_0\\
\end{aligned}
$$

## 5.c
$$
\begin{aligned}
\text{time}&=\text{connect time}&+&\text{trainsmission time}\\
           &=0&+&\text{RTT}_0\\
           &= \text{RTT}_0\\
\end{aligned}
$$