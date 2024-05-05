# hw3

[OS_HW3.pdf](../../assets/pdf/operating_system_HW3.pdf)

## 7.8

The reason for the policy is that holding a spinlock while attempting to acquire a semaphore can lead to a deadlock scenario. 
**example**
* Process A holds a spinlock and is trying to acquire a semaphore. 
* Process B holds the semaphore that Process A is trying to acquire and is trying to acquire the spinlock held by Process A.


## 8.20


* a:
  * safely
* b
  * unsafely
  * the remain resource may not able to complete task
* c
  * unsafely
  * resource may not able to fulfill task request
* d
  * safely
* e
  * unsafely
  * resource may not able to fulfill task request
* f
  * safely

## 8.27
| task  | allocation | max     | need    |
| ----- | ---------- | ------- | ------- |
|       | A,B,C,D    | A,B,C,D | A,B,C,D |
| $P_0$ | 1,2,0,2    | 4,3,1,6 | 3,1,1,4 |
| $P_1$ | 0,1,1,2    | 2,4,2,4 | 2,3,1,2 |
| $P_2$ | 1,2,4,0    | 3,6,5,1 | 2,4,1,1 |
| $P_3$ | 1,2,0,1    | 2,6,2,3 | 1,4,2,2 |
| $P_4$ | 1,0,0,1    | 3,1,1,2 | 2,1,1,1 |

* a
  * safe
  * $P_4(3,2,2,4) \rightarrow  P_0(4,4,2,6) \rightarrow  P_3(5,6,2,7) \rightarrow  P_1(5,7,3,9) \rightarrow  P_2(6,9,7,9)$
* b
  * safe
  * $P_4(5,4,1,2) \rightarrow  P_1(5,5,2,4) \rightarrow  P_2(6,7,6,4) \rightarrow  P_3(7,9,6,5) \rightarrow  P_0(8,11,6,7)$


## 8.30
```c++

semaphore bridgeAccess = 1

// northbound farmers
function crossBridgeNorth() {
  wait(bridgeAccess)
  
  deliver_to_neighbor_town();

  signal(bridgeAccess)
    
}

// southbound farmers
function crossBridgeSouth() {
  wait(bridgeAccess)
  
  deliver_to_neighbor_town();

  signal(bridgeAccess)
}
```

## 9.15


| Issues                     | Contiguous Memory     | Allocation	Paging           |
| -------------------------- | --------------------- | --------------------------- |
| (a) External fragmentation | High                  | Low                         |
| (b) Internal fragmentation | Low                   | Less then contiguous memory |
| (c) Ability to share code  | complex to implement. | Easy                        |


## 9.24

* a
  * $2^{32}/ 2^{13}=2^{19}$
* b
  * $2^{30}/ 2^{13}=2^{17}$


# programming problems

## 7.15
```c
#include <pthread.h>
#include <stdio.h>

#define MAX_FIBONACCI_NUMBERS 200

// Structure to hold data shared between threads
struct ThreadData {
    int sequence[MAX_FIBONACCI_NUMBERS];
    int count;
	int current;
};

// Function to generate Fibonacci sequence
void *generateFibonacci(void *arg) {
    struct ThreadData *data = (struct ThreadData *)arg;
    int n = data->count;
    
    data->sequence[0] = 1;
	data->current=0;
    data->sequence[1] = 1;
	data->current=1;
    
    for (int i = 2; i < n; i++) {
        int temp = data->sequence[i-2] + data->sequence[i-1];
        data->sequence[i] = temp;
		data->current=i;
    }
    
    pthread_exit(NULL);
}

int main (){
	int n;
	printf("fb:");
	scanf("%d",&n);
	pthread_t tid;
	struct ThreadData data;
	data.count=n;
	data.current=-1;
	pthread_create(&tid, NULL, generateFibonacci, (void *)&data);


    printf("Fibonacci sequence:");
	int i=0;
	while(1){
		if(i<=data.current){
			printf(" %d", data.sequence[i]);
			i++;
		}
		if(i>=n)
			break;
	}
    printf("\n");

    pthread_join(tid, NULL);

    return 0;

}
```


## 8.32

```c
#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define FARMERS 25

// Structure to hold data shared between threads
struct ThreadData {
    char *name;
    int id;
};
pthread_mutex_t bridge_mutex;
//pthread_cond_t cond;


// Function to generate Fibonacci sequence
void *farmer(void *arg) {
    struct ThreadData *data = (struct ThreadData *)arg;

	int waitTime = (float)rand()/(float)(RAND_MAX)*1000*100;
	//0 to 100 ms
	pthread_mutex_lock(&bridge_mutex);
	//run thought bridge
	usleep(waitTime);
	printf("%2d:%s Farmer cross in %2dms\n",data->id,data->name,waitTime/1000);
	pthread_mutex_unlock(&bridge_mutex);
    
    pthread_exit(NULL);
}

int main (){


	pthread_t tid[FARMERS];
	struct ThreadData data[FARMERS];

	for(int i = 0;i<FARMERS;i++){
		data[i].id=i;
		if(i%2==0)
			data[i].name="northbound";
		else
			data[i].name="southbound";
		pthread_create(&tid[i], NULL, farmer, (void *)&data[i]);
	}


	for(int i = 0;i<FARMERS;i++){
    	pthread_join(tid[i], NULL);
	}


	pthread_mutex_destroy(&bridge_mutex);

  return 0;

}
```

## 9.28

```c
#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>


int main (int argc, char *argv[]){

	if(argc<2){
		printf("argment not fulfill");
		return 0;
	}

	unsigned int address = atoi(argv[1]);
	unsigned int page_size=1<<12;
	unsigned int page_id=address/page_size;
	unsigned int offset=address-page_size*page_id;

	printf("page number=%d\n",page_id);
	printf("offset=%d\n",offset);

    return 0;

}
```