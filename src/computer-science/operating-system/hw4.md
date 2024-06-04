# hw4

[OS_HW4.pdf](../../assets/pdf/operating_system_HW4.pdf)

## 10.21
* Memory access time = 100 ns
* replace empty frame = 8ms
* replace modified frame = 20ms
* probability modified = 0.7
* Page fault service time =$(1-0.7)* 8ms + 0.7 * 20ms =16.4ms$
* effective access time = $(1-p)*100ns + p * (\text{Page fault service time})=16399900ns *p+100ns$
  *  16399900ns *p+100ns<200 ns
  *  p=$\frac{1}{163999}=0.00000609$


## 10.24


| page reference | FIFO frames | LRU frames | Optimal(OPT)  frames |
| -------------- | ----------- | ---------- | -------------------- |
| 3              | 3           | 3          | 3                    |
| 1              | 3,1         | 3,1        | 3,1                  |
| 4              | 3,1,4       | 3,1,4      | 3,1,4                |
| 2              | 2,1,4       | 1,4,2      | 2,1,4                |
| 5              | 2,5,4       | 4,2,5      | 5,1,4                |
| 4              | 2,5,4       | 2,5,4      | 5,1,4                |
| 1              | 2,5,1       | 5,4,1      | 5,1,4                |
| 3              | 3,5,1       | 4,1,3      | 5,1,3                |
| 5              | 3,5,1       | 1,3,5      | 5,1,3                |
| 2              | 3,2,1       | 3,5,2      | 2,1,3                |
| 0              | 0,2,1       | 5,2,0      | 0,1,3                |
| 1              | 0,2,1       | 2,0,1      | 0,1,3                |
| 1              | 0,2,1       | 2,0,1      | 0,1,3                |
| 0              | 0,2,1       | 2,1,0      | 0,1,3                |
| 2              | 0,2,1       | 1,0,2      | 0,2,3                |
| 3              | 0,2,3       | 0,2,3      | 0,2,3                |
| 4              | 0,4,3       | 2,3,4      | 0,2,4                |
| 5              | 0,5,3       | 3,4,5      | 0,5,4                |
| 0              | 0,5,3       | 4,5,0      | 0,5,4                |
| 1              | 1,5,1       | 5,0,1      | 0,5,1                |

## 10.37
* causes
  * Insufficient Physical Memory
  * Poor Page Replacement Policies
* detection
  *  Page-Fault Rate
* solution
  * local replacement policy
	* If actual rate too low, process loses frame
	* If actual rate too high, process gains frame

## 11.13

`2069,1212,2296,2800,544,1618,356,1523,4965,3681`

* FCFS
  * 2069,1212,2296,2800,544,1618,356,1523,4965,3681
  * $\text{total distance}=13011$
* SCAN
  * 2150,2296,2800,3681,4965,2069,1618,1523,1212,544,256
  * $\text{total distance}=7594$
* C-SCAN
  * 2150,2296,2800,3681,4965,256,544,1212,1523,1618,2069  
  * $\text{total distance}=9946$

## 11.20

* a
  * 2(1 block + 1 parity)
* b
  * 8(7 block + 1 parity)

## 11.21

* a
  * raid 1
    * Faster
  * raid 5
    * Slower
* b
  * raid 1
    * Faster for small to moderate block sizes.
  * raid 5
    * Can be faster for large contiguous blocks

## 14.14

|            | Logical-to-Physical Mapping | Accessing Block 4 from Block 10 |
| ---------- | --------------------------- | ------------------------------- |
| contiguous | start block + length        | 1                               |
| linked     | linked list pointer         | unknow                          |
| indexed    | index block + block pointer | 1 ( index block is in memory)   |

## 14.15

$$
\text{block pointer }=4KB/ 4\text{ Byte }=2048=2^{11}\\
\text{maximum size }=8KB\times (12+ 12\times 2^{11} + 12 \times 2^{22}+ 12 \times 2^{33}) \eqsim  768  GB
$$
