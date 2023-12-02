# hw4

[2023 computer-networking HW4.pdf](../../assets/pdf/computer_networkingHW4.pdf)

## 1.
Because NAT converts the IP and port before sending or receiving requests from another user or server, it makes it impossible to know the IP of the client.


by using this can make P2P connection network with NAT
* Port Forwarding
* UPnP (Universal Plug and Play)

## 2.
* Subnets1 :223.3.16.0/25
* Subnets2 :223.3.16.128/26
* Subnets3 :223.3.16.192/26

## 3.
1. Private IP are internal IP for internal network that not should not expose on public network
2. No
3. If private information is exposed on a public network, hackers may gain access to the private network.
## 4.

a:Insert IP6 packet as payload in IP4 protocols

b:No ,The data link layer have to communication with physical layer
## 5.
1. the match plus action is the core mechanism of router and switch do thing eff
2.
   1. match :
      1. compares the destination IP address to the entries in its routing table.
   2. action :
      1.  forward the packet to the determined
3.
   1. fields can match :
      1. Source/Destination IP Address
      2. Protocol Type
   2. action :
      1. Forwarding
      2. Quality of Service (QoS)
