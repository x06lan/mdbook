# computer networking

## delay
![](https://imgur.com/rEb1odo.png)
$$
\text{transmission delay}=\frac{L(bits)}{R(bits/sec)}\\
\text{queueing delay}=\frac{L(bits)\times a(\text{average packet arrival rate})}{R(bps)}\\
\begin{aligned}\\
\text{delay}&=d_{\text{transmission}}+d_{\text{propagation}}+d_{\text{queueing delay}}\\
&=\frac{L}{R}+\frac{d}{s}
\end{aligned}\\
$$
## circuit switching(FDM,TDM)


### Frequency Division Multiplexing (FDM)
![FDM](https://imgur.com/Li4VtUz.png)

optical, electromagnetic frequencies divided into (narrow) frequency bands = each call allocated its own band, can transmit at max rate of that narrow band
### Time Division Multiplexing (TDM)
![TDM](https://imgur.com/Lf7C9Sv.png)

time divided into slots = each call allocated periodic slot(s), can transmit at maximum rate of (wider) frequency band, but only during its time slot(s)

## applicaion layer
### http
#### http/1.0
1. TCP connection opened
1. at most one object sent over TCP connection
1. Non-persistent HTTP。
#### http/1.1
1. pipelined GETs over single TCP connection
1. persistent HTTP。
#### http/2
1. multiple, pipelined GETs over single TCP connection
1. push unrequested objects to clien
#### http/3
This is an advanced transport protocol that operates on top of UDP. QUIC incorporates features like reduced connection and transport latency, multiplexing without head-of-line blocking, and improved congestion control. It integrates encryption by default, providing a secure connection setup with a single round-trip time (RTT).

#### persistent http
1. keep connetion of TCP
1. half time of tramit

### email SMTP POP3 IMAP
#### SMTP
mail server send to mail server
#### POP3
muil-user download email
#### IMAP
will delete email that user download

|              | http                                     | smtp                                       |
| ------------ | ---------------------------------------- | ------------------------------------------ |
|              | pull                                     | push                                       |
| encode       | ASCII                                    | ASCII                                      |
| multiple obj | encapsulated in its own response message | multiple objects sent in multipart message |
### DNS
1. hostname to IP address translation
1. host aliasing
1. mail server aliasing
1. take but 2 RTT(one for make connection one for return IP info) to get send IP back

## socket
use this four tuple to identified TCP packet<br>
(source IP, source port, destination IP, destination port)

## UDP
* no handshaking before sending data
* sender explicitly attaches IP destination address and port # to each packet
* receiver extracts sender IP address and port# from received packe
* transmitted data may be lost or received out-of-order

## TCP
* reliable, byte stream-oriented
* server process must first be running
* server must have created socket (door) that welcomes client’s contact
* TCP 3-way handshake

## Multimedia video:
* DASH: Dynamic, Adaptive Streaming over HTT
* CBR: (constant bit rate): video encoding rate fixed
* VBR: (variable bit rate): video encoding rate changes as amount of spatial, temporal coding changes


## principles of reliable data transfer
* finite state machines (FSM)
* Sequence numbers:
  * byte stream “number” of first byte in segment’s data
* Acknowledgements:
  * seq # of next byte expectet from other side
  * cumulative ACK
### Go Back N
the all the packet that behind is overtime or NAK
![](https://i.imgur.com/eoftyjT.png)
### Selective repeat
only resend the packet overtime or NAK
![](https://i.imgur.com/fAlaZsW.png)

### stop and wait
rdt(reliable data transfer)
#### rdt 1.0
* rely on channel perfectly reliable
![](https://i.imgur.com/vsfr4vl.png)
#### rdt 2.0
* checksum to detect bit errors
* acknowledgements (ACKs): receiver explicitly tells sender that pkt received OK
* negative acknowledgements (NAKs): receiver explicitly tells sender that pkt had errors
* stop and wait: sender sends one packet, then waits for receiver response
![](https://i.imgur.com/3B7r9op.png)
#### rdt 2.1
在每份封包加入序號(sequence number) 來編號，因此接收端可以藉由序號判斷現在收到的封包是不是重複的，若重複則在回傳一次ACK回去，而這裡的序號用1位元就夠了(0和1交替)。
* sender
![](https://i.imgur.com/O5I8H0g.png)
* receiver
![](https://i.imgur.com/r52Iw9D.png)
#### rdt 2.2
rdt2.2不再使用NAK，而是在ACK加入序號的訊息，所以在接收端的make_pkt()加入參數ACK,0或ACK,1，而在傳送端則是要檢查所收到ACK的序號。
#### rdt 3.0
* add timer .If sender not receive ACK then resend

## TCP flow control
receiver controls sender, so sender won’t overflow receiver’s buffer by transmitting too much, too fast
### window buffer size
if the receiver window buffer is fill then sender should stop sending until receiver window buffer is free again
### SampleRTT
* measured time from segment transmission until ACK receipt
* ignore retransmissions
* SampleRTT will vary, want estimated RTT “smoother” average several recent measurements, not just current SampleRTT
### TCP RTT(round trip time), timeout
* use EWMA(exponential weighted moving average)
* influence of past sample decreases exponentially fast
* typical value: $\alpha$ = 0.125
$$
\text{EstimatedRTT}=(1-\alpha)*\text{EstimatedRTT }+\alpha*\text{SampleRTT}\\
\text{TimeoutInterval} = \text{EstimatedRTT} + 4*\text{DevRTT(safety margin)}\\
\text{DevRTT} = (1-\beta)*\text{DevRTT} + \beta * |\text{ SampleRTT}-\text{EstimatedRTT } |
$$

## TCP congestion control AIMD(Additive Increase Multiplicative Decrease)
* send cwnd bytes,wait RTT for ACKS, then send more bytes
$$
\text{TCP rate} = \frac{\text{cwnd}}{\text{RTT}}\text{(bits/sec)}
$$


### slow start
increase rate exponentially until first loss event
* initially cwnd = 1 MSS
* double cwnd every RTT
* done by incrementing cwnd for every ACK received
### CUBIC (briefly)
use the cubic function(三次函數) to predict bottlenck
### 3 duplicate ack
if recevie 3 ACK of same packet then see as reach bottlenck
### congestion avoidance AIMD(Additive Increase Multiplicative Decrease)

## Network Layer:
* functions
  * network-layer functions:
    * forwarding: move packets from a router’s input link to appropriate router output link
    * routing: determine route taken by packets from source to destination
      * routing algorithms
  * analogy: taking a trip
    * forwarding: process of getting through single interchange
    * routing: process of planning trip from source to destination
* data plane and control plane
  * Data plane:
    * local, per-router function
    * determines how datagram arriving on router input port is forwarded to router output port
  * Control plane
    * network-wide logic
    * determines how datagram is routed among routers along end- end path from source host to destination host
    * two control-plane approaches:
      * traditional routing algorithms: implemented in routers
      * software-defined networking Software-Defined Networking((SDN): implemented in (remote) servers

### Data Plane(CH4)

#### Router
* **input port queuing**: if datagrams arrive faster than forwarding rate into switch fabri
* **destination-based forwarding**: forward based only on destination IP address (traditional)
* **generalized forwarding**: forward based on any set of header field values


<image src="https://imgur.com/I6mxtp2.png" width="80%">

##### Input port functions
<image src="https://imgur.com/jwMpl8L.png" width="80%">

###### Destination-based forwarding(Longest prefix matching)
* when looking for forwarding table entry for given destination address, use longest address prefix that matches destination address.

![](https://imgur.com/MqZHr2S.png)
![](https://imgur.com/GtNXmwl.png)



##### Switching fabrics
* transfer packet
  * from input link to appropriate output link
* switching rate:
  * rate at which packets can be transfer from


<image src="https://imgur.com/TedE1AM.png" width="80%">

##### Input Output queuing
* input
  * If switch fabric slower than input ports combined -> queueing may occur at input queues
    * queueing delay and loss due to input buffer overflow!
  * Head-of-the-Line (HOL) blocking: queued datagram at front of queue prevents others in queue from moving forward
* output
  * Buffering
    * drop policy:which datagrams to drop if no free buffers?
    * Datagrams can be lost due to congestion, lack of buffers
  * Priority scheduling – who gets best performance, network neutrality
##### buffer management
![](https://imgur.com/mybi2hI.png)
* drop: which packet to add,drop when buffers are full
  * tail drop: drop arriving packet
  * priority: drop/remove on priority basis
* marking: which packet to mark to signal congestion(ECN,RED)

$$
N=\text{flows},C=\text{link speed}\\
\text{buffer size}=\frac{RTT \times C}{\sqrt{N}}
$$

##### packet scheduling
* FCFS(first come, first served)
* priority
  * priority queue
  * ![](https://imgur.com/c0gdQQp.png)
* RR(round robin)
  * arriving traffic classified, queued by class(any header fields can be used for classification)
  * server cyclically, repeatedly scans class queues, sending one complete packet from each class (if available) in turn
  * ![](https://imgur.com/E3uUUDe.png)
* WFQ(Weighted Fair Queuing)
  * round robin but each class, $i$, has weight, $w_i$, and gets weighted amount of service in each cycle


#### IP (Internet Protoco)
##### IP Datagram
![](https://imgur.com/kjuR0Da.png)
![](https://imgur.com/TJy7dN0.png)
##### IP address
*  IP address: 32-bit identifier associated with each host or router interface
* interface: connection between host/router and physical link
  * router’s typically have multiple interfaces
  * host typically has one or two interfaces (e.g., wired Ethernet, wireless 802.11)
##### Subnets
* in same subnet if:
  * device interfaces that can physically reach each other without passing through an intervening router


![](https://imgur.com/FCAWoXP.png)


###### CIDR(Classless InterDomain Routing)
address format: a.b.c.d/x, where x is # bits in subnet portion of address

![](https://imgur.com/YS58NCh.png)
##### DHCP
host dynamically obtains IP address from network server when it
"joins" network

* host broadcasts DHCP discover msg [optional]
* DHCP server responds with DHCP offer msg [optional]
* host requests IP address: DHCP request msg
* DHCP server sends address: DHCP ack msg

![](https://imgur.com/nG833ln.png)
##### NAT(Network Address Translation)
* NAT has been controversial:
  * routers “should” only process up to layer 3
  * address “shortage” should be solved by IPv6
  * violates end-to-end argument (port # manipulation by network-layer device)
  * NAT traversal: what if client wants to connect to server behind NAT?
* but NAT is here to stay:
  * extensively used in home and institutional nets, 4G/5G cellular net

![](https://imgur.com/8pQh2Fj.png)
##### IP6
![](https://imgur.com/kkNzQau.png)
###### tunneling:Transition from IPv4 to IPv6
IPv6 datagram carried as payload in IPv4 datagram among IPv4 routers (“packet within a packet”)

![](https://imgur.com/mEzJH1z.png)


##### Generalized forwarding(flow table)


![](https://imgur.com/rmcjk71.png)


flow table entries

![](https://imgur.com/i7qwKaH.png)

* **match+action**: abstraction unifies different kinds of devices

| Device   | Match                         | Action                   |
| -------- | ----------------------------- | ------------------------ |
| Router   | Longest Destination IP Prefix | Forward out a link       |
| Switch   | Destination MAC Address       | Forward or flood         |
| Firewall | IP Addresses and Port Numbers | Permit or deny           |
| NAT      | IP Address and Port           | Rewrite address and port |
##### middleboxes
![](https://imgur.com/QnhkauT.png)






### Control Plane(CH5)













## Link layer and LAN(CH6)
### error detection, correction

* Internet checksum
* Parity checking
* Cyclic Redundancy Check (CRC)
#### Parity checking
![](https://imgur.com/34PJCaF.png)
#### Cyclic Redundancy Check (CRC)
$
r=\text{check bit length}\\
D=\text{raw data bits}\\
G=\text{bit pattern}=r+1\text{ bit}\\
R= (D\times 2^r) \ mod \ G\\
CRC=(D\times 2^r)+R\\
\text{if }CRC \ mod \ G \ \neq 0 \text{ then have error bit}
$
### MAC protocol(multiple access)

* channel partitioning
  * time division
  * frequency division
* random access MAC protocol
  * ALOHA, slotted ALOHA
  * CSMA, CSMA/CD, CSMA/CS
* takeing turns
  * polling
  * token passing
#### slotted ALOHA

* time divided into equal size slots (time to transmit 1 frame)
* nodes are synchronized
* if collision: node retransmits frame in each subsequent slot with probability $ p $ until success
* max efficiency = $e^{-1}$= 0.37

#### Pure ALOHA
![](https://imgur.com/4dJ8hQN.png)
#### CSMA
* CSMA:
  * if channel sensed idle: transmit entire frame
  • if channel sensed busy: defer transmission
* CSMA/CD(Collision Detection):
  * collision detection easy in wired, difficult with wireless
  * if collisions detected within short then send `abort`,`jam signal`
  * After aborting, NIC enters binary (exponential) backoff:
    * after mth collision, NIC chooses K at random from {0,1,2, …, 2m-1}. NIC waits $K\times 512$ bit times
    *  more collisions: longer backoff interval
### LAN
#### ARP: address resolution protocol
determine interface’s MAC address by its IP
address
* ARP table: each IP node (host, router) on LAN has table
* IP/MAC address mappings for some LAN nodes:< IP address; MAC address; TTL>
* TTL (Time To Live): time after which address mapping will be forgotten (typically 20 min)
#### switch
switch table

![](https://imgur.com/YhnHQyv.png)
