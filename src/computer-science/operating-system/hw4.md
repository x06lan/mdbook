# hw4

[OS_HW4.pdf](../../assets/pdf/operating_system_HW4.pdf)

## 10.21
* Memory access time = 100 ns
* replace empty frame = 8ms
* replace modified frame = 20ms
* probability modified = 0.7
* Page fault service tim$(1-0.7)* 8ms + 0.7 * 20ms =16.4ms$
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
  * $\text{total distance}=7494$
* C-SCAN
  * 2150,2296,2800,3681,4965,256,544,1212,1523,1618,2069  
  * $\text{total distance}=9919$

## 11.20

* a
  * 2(1 block + 1 mirror)
* b
  * 9(4 block + 1 parity + 3 block + 1 parity)

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



# code
## 10.44

```bash
g++ hw4_10.44.cpp && ./a.out  
```

```cpp
#include <iostream>
#include <random>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <array>

int FIFO(std::vector<int> &page_ref, int frame_size)
{
	std::queue<int> page_frames;
	std::unordered_set<int> frames;
	int page_faults = 0;

	for (int page : page_ref)
	{
		if (frames.find(page) == frames.end())
		{
			page_faults++;
			if (page_frames.size() == frame_size)
			{
				int front = page_frames.front();
				page_frames.pop();
				frames.erase(front);
			}
			page_frames.push(page);
			frames.insert(page);
		}
	}

	return page_faults;
}

int LRU(std::vector<int> &page_ref, int frame_size)
{
	std::vector<int> page_frames;
	int page_faults = 0;
	for (int i = 0; i < page_ref.size(); i++)
	{
		int page = page_ref[i];

		for (int j = 0; j < page_frames.size(); j++)
		{
			if (page_frames[j] == page)
			{
				page_frames.push_back(page);
				page_frames.erase(page_frames.begin() + j);
				break;
			}
		}

		if (page_frames.size() == 0 || page_frames.size() < frame_size && page_frames.back() != page)
		{
			page_faults++;
			page_frames.push_back(page);
			continue;
		}
		if (page_frames.back() != page)
		{
			page_faults++;
			page_frames.erase(page_frames.begin());
			page_frames.push_back(page);
		}
	}
	return page_faults;
}
int OPT(std::vector<int> &page_ref, int frame_size)
{
	std::vector<int> page_frames;

	int page_faults = 0;
	for (int i = 0; i < page_ref.size(); i++)
	{
		int page = page_ref[i];
		auto p = std::find(page_frames.begin(), page_frames.end(), page);
		if (p == page_frames.end())
		{
			page_faults++;
			if (page_frames.size() < frame_size)
			{
				page_frames.push_back(page);
				continue;
			}

			int index = 0;
			int max = page_frames.size();
			for (int j = 0; j < page_frames.size(); j++)
			{
				auto f = std::find(page_ref.begin() + i, page_ref.end(), page_frames[j]);
				if (f - page_ref.begin() > max)
				{
					max = f - page_ref.begin();
					index = j;
				}
			}
			page_frames[index] = page;
		}
	}
	return page_faults;
}
int main()
{
	int n = 0;
	printf("page frames:");
	scanf("%d", &n);

	std::vector<int> page_ref(50);
	for (int i = 0; i < page_ref.size(); i++)
		page_ref[i] = rand() % 10;

	printf("page ref:");
	for (int i = 0; i < page_ref.size(); i++)
		printf("%d ", page_ref[i]);
	printf("\n");

	int page_faults1 = FIFO(page_ref, n);
	int page_faults2 = LRU(page_ref, n);
	int page_faults3 = OPT(page_ref, n);

	printf("FIFO: %d\n", page_faults1);
	printf("LRU: %d\n", page_faults2);
	printf("OPT: %d\n", page_faults3);

	return 0;
}

```
## 11.27
```bash
g++ hw4_11.27.cpp && ./a.out 2150
```

```cpp
#include <iostream>
#include <random>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <array>

#define MAX_DISK 5000

int FCFS(std::vector<int> &req, int head)
{
	int dis = 0;
	for (int request : req)
	{
		dis += abs(request - head);
		head = request;
	}

	return dis;
}
int SCAN(std::vector<int> &req, int head)
{
	int dis = 0;
	std::sort(req.begin(), req.end());
	auto it = std::lower_bound(req.begin(), req.end(), head);

	std::vector<int> left(req.begin(), it);
	std::vector<int> right(it, req.end());

	for (auto it = right.begin(); it != right.end(); ++it)
	{
		dis += abs(*it - head);
		head = *it;
	}

	if (!left.empty())
	{
		dis += abs(MAX_DISK - head);
		head = MAX_DISK;

		for (auto it = left.rbegin(); it != left.rend(); ++it)
		{
			dis += abs(*it - head);
			head = *it;
		}
	}

	return dis;
}
int C_SCAN(std::vector<int> &req, int head)
{
	int dis = 0;
	std::sort(req.begin(), req.end());
	auto it = std::lower_bound(req.begin(), req.end(), head);

	std::vector<int> left(req.begin(), it);
	std::vector<int> right(it, req.end());

	for (auto it = right.begin(); it != right.end(); ++it)
	{
		dis += abs(*it - head);
		head = *it;
	}

	if (!left.empty())
	{
		dis += abs(MAX_DISK - head);
		dis += MAX_DISK;
		head = 0;

		for (auto it = left.begin(); it != left.end(); ++it)
		{
			dis += abs(*it - head);
			head = *it;
		}
	}

	return dis;
}
int main(int argc, char **argv)
{
	int n = argc > 1 ? atoi(argv[1]) : -1;
	if (n == -1)
	{
		printf("Please enter init position\n");
		return 0;
	}

	std::vector<int> req(1000);
	for (int i = 0; i < req.size(); i++)
		req[i] = rand() % MAX_DISK;


	int distance1 = FCFS(req, n);
	int distance2 = SCAN(req, n);
	int distance3 = C_SCAN(req, n);

	printf("FCFS: %d\n", distance1);
	printf("SCAN: %d\n", distance2);
	printf("C-SCAN: %d\n", distance3);

	return 0;
}

```
