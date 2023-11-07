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
2. at most one object sent over TCP connection
#### http/1.1
1. pipelined GETs over single TCP connection
#### http/2
1. multiple, pipelined GETs over single TCP connection
1. push unrequested objects to clien
#### http/3
adds security , per object error control (more pipelining) over UDP


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