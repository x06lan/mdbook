# hw5

[2023 computer-networking HW5.pdf](../../assets/pdf/computer_networkingHW5.pdf)

## 1.
* False.
* Router sends its link information, it is not limited to only those nodes directly attached as neighbors. OSPF routers use a process called "flooding" to share routing information throughout the entire OSPF domain.

## 2.
* No
* based on reachability information and policy router may not be shortest path

## 3.
UDP:
* stateless
* faster then TCP






 <!--
 0   | 1   | 5   | 4   |     |     |
 1   | 0   | 3   |     | 1   |     |
 5   | 3   | 0   |     | 1   | 2   |
 4   |     |     | 0   | 1   | 2   |
     | 1   | 1   | 1   | 0   | 4   |
     |     | 2   | 2   | 4   | 0   |
-->




## 4.
| iter | visited       | 1   | 2   | 3   | 4   | 5   | 6   |
| ---- | ------------- | --- | --- | --- | --- | --- | --- |
| 0    | {}            | 0   |     |     |     |     |     |
| 1    | {1}           | 0   | 1   | 5   | 4   |     |     |
| 2    | {1,2}         | 0   | 1   | 4   | 4   | 2   |     |
| 3    | {1,2,5}       | 0   | 1   | 3   | 3   | 2   | 6   |
| 4    | {1,2,5,3}     | 0   | 1   | 3   | 3   | 2   | 5   |
| 5    | {1,2,5,3,4}   | 0   | 1   | 3   | 3   | 2   | 5   |
| 6    | {1,2,5,3,4,6} | 0   | 1   | 3   | 3   | 2   | 5   |

## 5.

|     | x   | y   | w   | u   |
| --- | --- | --- | --- | --- |
| x   | 0   | 4   | 2   | 7   |
| y   | 4   | 0   | 2   | 6   |
| w   | 2   | 2   | 0   | 5   |
| u   | 7   | 6   | 5   | 0   |
### a.
|     | x   |
| --- | --- |
| y   | 4   |
| w   | 2   |
| u   | 7   |

### b.
When the function c(x,w) changes, node x will need to recompute the distances to its neighbors. Subsequently, it must send these recalculated distances back to neighbors and receive new distances from neighbors. Then x may have new minimum-cost path.
