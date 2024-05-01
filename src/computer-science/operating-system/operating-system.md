# operating system

tags: `software` `hardware` `system`

# Chapter 1: Computer System

## Structure

![](https://imgur.com/WIg4WHA.png)

One or more CPUs, device controllers connect through
common bus providing access to shared memory

<!-- ![](https://imgur.com/zrdncP6.png) -->
![](https://imgur.com/hFMTIBI.png)


* Process Management
    * Creating and deleting both user and system processes
    * Suspending and resuming processes
    * Providing mechanisms for process synchronization
    * Providing mechanisms for process communication
    * Providing mechanisms for deadlock handlin
* Memory Management
    * Von Neumann architecture
        * To execute a program, all (or part) of the instructions must be in memory
        * All (or part) of the data that is needed by the program must be in memory
    * Allocating and deallocating memory space as needed
    * Keeping track of which parts of memory are currently being used and by whom
    * Deciding which processes (or parts thereof) and data to move into and out of memory
* file system management
    * Abstracts physical properties to logical storage unit - file
    * Access control on most systems to determine who can access what
* Mass-Storage Management
    * mounting and unmounting
    * fire-space management
    * storage allocation
    * disk scheduling
    * partitioning
    * protection
* caching management
    * Faster storage (cache)
    * mportant principle, performed at many levels in a computer (in hardware, operating system, software)
* I/O Subsystem
    * buffering(storing data temporarily while it is being transferred)
    * caching(storing part of data in faster storage for performance)
    * spooling

## operation
* I/O is from the device to local buffer of controller
* CPU moves data from/to main memory to/from local buffers
* **Device controller informs CPU that it has finished its operation by causing an interrupt**

## interrupt
* software-generated interrupt :execption
* Modern OS is interrupt-driven
* Interrupt architecture must save the address of the interrupted instruction



### Interrupt Handling

* The OS preserves the state of the CPU by storing the registers and the program counter
* type of interrupt
  * polling
  * vectored

![](https://imgur.com/ey7PR4G.png)


## I/O



### handling I/O



* Synchronous: After I/O starts, control returns to user program only upon I/O completion
  * wait instruction idles the cpu until the next interrupt
  * wait loop
* Asynchronous: After I/O starts, control returns to user program without waiting for I/O completion
  * system call:request to the OS to allow user to wait for I/O completion




## storage structure



* main memory 
  * cpu can access directly
  * Dynamic Random-access Memory (DRAM)
  * Typically volatile
* HDD
* Non-volatile memory (NVM)



![](https://imgur.com/GHJAvzl.png)

## Direct Memory Access(DMA) 
![](https://imgur.com/wWrbQVo.png)
* Used for high-speed I/O devices able to transmit information at close to memory speeds
* Device controller transfers blocks of data from buffer storage directly to main memory without CPU intervention
* Only one interrupt is generated per block, rather than one interrupt per byte

## Symmetric Multiprocessing Architecture

|          Dual-Core Design          |  Non-Uniform Memory Access System  |
| :--------------------------------: | :--------------------------------: |
| ![](https://imgur.com/1UF7oQL.png) | ![](https://imgur.com/uu6dde5.png) |

## Virtualization

have different kernel

![](https://imgur.com/WWoDBRe.png)

## cloud computing
![](https://imgur.com/W1HegDq.png)

* Software as a Service (SaaS) 
    * one or more applications available via the Internet (i.e., word processor)
* Platform as a Service (PaaS) 
    * software stack ready for application use via the Internet (i.e., a database server)
* Infrastructure as a Service (IaaS) 
    * servers or storage available over Internet (i.e., storage available for backup use)


## Kernel Data Structures

![](https://imgur.com/nSTFnOf.png)


# Chapter 2: Operating-System Service

## System Calls

* Programming interface to the services provided by the OS
* Typically written in a high-level language (C or C++)
* Mostly accessed by programs via a high-level Application Programming Interface (API) rather than direct system call
* System Call Parameter Passing
  * pushed, onto the stack by the program and popped off the stack by the OS
![](https://imgur.com/SmCvYm2.png)
<!-- ![](https://imgur.com/oKiVXUc.png) -->


### Types of System Calls

* Process control
  * create process, terminate process
  * end, abort
  * load, execute
  * get process attributes, set process attributes
  * wait for time
  * wait event, signal event
  * allocate and free memory
  * Dump memory if error
  * Debugger for determining bugs, single step execution
  * Locks for managing access to shared data between
* File management
  * create file, delete file
  * open, close file
  * read, write, reposition
  * get and set file attributes
* Device management
  * request device, release device
  * read, write, reposition
  * get device attributes, set device attributes
  * logically attach or detach devices processes
* Information maintenance
  * get time or date, set time or date
  * get system data, set system data
  * get and set process, file, or device attributes
* Communications
  * create, delete communication connection
  * send, receive messages if message passing model to host name or process name
    * From client to server
  * Shared-memory model create and gain access to memory regions
  * transfer status information
  * attach and detach remote devices


![](https://imgur.com/WYG0IUC.png)

## program stack 

![](https://imgur.com/bNDtDUq.png)

## Linker and Loader
* Source code compiled into object files designed to be loaded into
any physical memory location – relocatable object file
* Linker combines these into single binary executable file
  * Also brings in libraries
* Modern general purpose systems don’t link libraries into executables
  * Rather, dynamically linked libraries (in Windows, **DLLs**) are loaded as needed, shared by all that use the same version of that same library (loaded once


![](https://imgur.com/5J9qm6P.png)

## Operating System Structure

* Simple structure 
* Monolithic Structure More
* Microkernel
* Layered
* Hybrid



### Traditional UNIX System Structure 

* UNIX: 
  * limited by hardware functionality, the original UNIX OS had limited structuring
  * Consists of everything below the system-call interface and above the physical hardware
  * Provides the file system, CPU scheduling, memory management, and other OS functions; a large number of functions for one level

![](https://imgur.com/DphRDJr.png)


### Linux System Structure 
Monolithic plus modular design

![](https://imgur.com/oJfeysX.png)

### Microkernels
* Moves as much from the kernel into user space
* Mach is an example of microkernel
  * Mac OS X kernel (Darwin) partly based on Mach
* Benefits:
  * Easier to extend a microkernel
  * Easier to port the OS to new architectures
  * More reliable (less code is running in kernel mode)
  * More secure
* Detriments:
  * Performance overhead of user space to kernel space communication

![](https://imgur.com/01n47EV.png)

### Layered Approach

* The OS is divided into a number of layers (levels), each built on top of lower layers
    * The bottom layer (layer 0), is the hardware
    * the highest (layer N) is the user interface
* With modularity, layers are selected such that each uses functions (operations) and services of only lower- level layers

### hybrid systems

* Apple Mac OS X hybrid, layered, Aqua UI plus Cocoa programming environment


| macOS iOS                          | darwin                             | android                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| ![](https://imgur.com/gfCqyE7.png) | ![](https://imgur.com/aK4VIQE.png) | ![](https://imgur.com/On7lNGE.png) |



## System Boot

* When power initialized on system, execution starts at a fixed memory location
* Small piece of code 
  *  bootstrap loader, BIOS, stored in ROM or EEPROM locates the kernel, loads it into memory, and starts it
* Modern systems replace BIOS with Unified Extensible Firmware Interface (UEFI)
* Common bootstrap loader, GRUB

## tracing

* strace – trace system calls invoked by a process
* gdb – source-level debugger
* perf – collection of Linux performance tools
* tcpdump – collects network packets

![](https://imgur.com/tKHNWWx.png)


# Chapter 3: Processes

* The program code, also called text section
* Current activity including program counter, processor registers
* Stack containing temporary data
  * Function parameters, return addresses, local variables
* Data section containing global variables
* Heap containing memory dynamically allocated during run time
![](https://imgur.com/htrhvZO.png)

##  process state
* new 
* running
* waiting
* ready:the process is waiting to be assigned to a processor
* terminated

![](https://imgur.com/J2M646J.png)



## Process Scheduling
### Process Control Block (PCB) or task control block)

![](https://imgur.com/cykBgGg.png)

### scheduling
* Goal -- Maximize CPU use, quickly switch
* processes onto CPU core
  * Maintains scheduling queues of processes
  * ready queue
  * wait queue

![](https://imgur.com/g4kYgaz.png)

### context switch
* context-switch time is pure overhead; the system does no useful work while switching
  * The more complex the OS and the PCB  the longer the context switch
* Time dependent on hardware support
  * Some hardware provides multiple sets of registers per CPU  multiple contexts loaded at once

![](https://imgur.com/9YIOLxF.png)

## Operations on Processes


![](https://imgur.com/sRSoQ3J.png)

## Inter Process Communication(IPC)

* shared memory
* message passing

### IPC in Shared-Memory Systems
* An area of memory shared among the processes that wish to communicate
* The communication is under the control of the user processes not the OS

### IPC in Message-Passing Systems

* Blocking is considered synchronous
* Non-blocking is considered asynchronous

#### Ordinary pipes 
* unidirectional(single direction)
* cannot be accessed from outside the process that created it. 
  * Typically, a parent process creates a pipe and uses it to communicate with a child process that it created
#### named pipes
* Communication is bidirectional
* No parent-child relationship is necessary between the communicating processes


### Client-Server Systems

| sockets                            | Remote Procedure Calls (RPC)       |
| ---------------------------------- | ---------------------------------- |
| ![](https://imgur.com/XZ4RMYg.png) | ![](https://imgur.com/3ROwbAf.png) |


# Chapter 4: Threads & Concurrency
## Concurrency vs. Parallelism
![](https://imgur.com/k8WxgPK.png)
## Multicore Programming
* Data parallelism
  * different data, same operation on each data
* Task parallelism
  * different operation, same data


## Amdahl’s Law

$$
P=\text{parallel portion} \\
\text{speed up}= \frac{1}{(1-P)+\frac{P}{N}}
$$
![](https://imgur.com/MLmgi8p.png)

## Multithreading Models

* Many-to-One
  * One thread blocking causes all to block
  * example
    * solaris green threads
    * GUN portable threads
* One-to-One
  * More concurrency than many-to-one
  * example
    * windows
    * linux
* Many-to-Many
  * Windows with the ThreadFiber package
* two-level model
  * mix Many-to-Many and One-To-One

| Many-to-One                        | ono-to-one                         | Many-to-Many                       | two-level model                    |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| ![](https://imgur.com/SKAyDBk.png) | ![](https://imgur.com/0AwwxsV.png) | ![](https://imgur.com/Qdqesbf.png) | ![](https://imgur.com/aX6oEDw.png) |

## Implicit threading

* Thread Pools
  * Create a number of threads in a pool where they await work
* Fork-Join Parallelism
* OpenMP
* Grand Central Dispatch
  * dispatch queues
  * macOS,iOS


# Chapter 5: CPU Scheduling

## CPU scheduler

* CPU utilization 
  * keep the CPU as busy as possible
* Throughput 
  * of processes that complete their execution per time unit
* Turnaround time 
  * amount of time to execute a particular process
  * turnaround time = completion time – arrival time
* Waiting time 
  * amount of time a process has been waiting in the ready queue
  * waiting time = turnaround time  –  burst time
* Response time 
  * amount of time it takes from when a request was submitted until the first response is produce
  * response time = start time – arrival time


CPU scheduling decisions may take place when a process:
1. Switches from running to waiting state
2. Switches from running to ready state
3. Switches from waiting to ready
4. Terminates


### Preemptive

* preemptive
  * can result in race conditions 
  * linux,windows,MacOS
* nonpreemptive
  * only under circumstances 1 and 4

### Dispatcher

* witching context
* Switching to user mode
* Jumping to the proper location in the user program to restart that program

Dispatch latency =time it take to stop one process and start another running

### Scheduling Algorithm
* Max CPU utilization
* Max throughput
* Min turnaround time
* Min waiting time
* Min response time

#### Determining Length of Next CPU Burst
* exponential averaging
$$
t_n=\text{CPU burst time}\\
\tau_n = \text{predict CPU burst time}\\
\begin{aligned}
\tau_0&=t_0\\ 
\tau_{n+1}&=\alpha t_n +(1-\alpha) \tau_{n}
\end{aligned}
$$
![](https://imgur.com/Xe9SWHB.png)

#### First- Come, First-Served(FCFS) Scheduling

![](https://imgur.com/JyiYt2l.png)

$$
\text{Waiting time }P_1 = 0, P_2 = 24, P_3 = 27\\
\text{Average waiting time}= (0 + 24 + 27)/3 = 17
$$

* Convoy effect short process behind long process
  * Consider one CPU-bound and many I/O-bound processes
#### Shortest-Job-First(SJF) Scheduling
* minimum average waiting time for a given set of processes

#### shortest-remaining-time-first(Preemptive SJF)

| process | arrival time | burst time |
| ------- | ------------ | ---------- |
| $P_1$   | 0            | 8          |
| $P_2$   | 1            | 4          |
| $P_3$   | 2            | 9          |
| $P_4$   | 3            | 5          |

![](https://imgur.com/rX2gkk8.png)
$$
\text{Average waiting time}= \frac{(10-1)+(1-1)+(17-2)+(5-3)}{4} = 6.5
$$


#### Round Robin (RR)

* Each process gets a small unit of CPU time (time quantum q), usually 10-100 milliseconds
  * After this time has elapsed, the process is preempted and added to the end of the ready queue
* Typically, higher average turnaround than `SJF`, but better response

| process | burst time |
| ------- | ---------- |
| $P_1$   | 8          |
| $P_2$   | 4          |
| $P_3$   | 9          |

$$
\text{Time Quantum }= 4
$$

![](https://imgur.com/9BuK5sE.png)


#### Priority Scheduling
* The CPU is allocated to the process with the highest priority
* `SJF` is priority scheduling where priority is the inverse of predicted next CPU burst time


| process | burst time | priority |
| ------- | ---------- | -------- |
| $P_1$   | 10         | 3        |
| $P_2$   | 1          | 1        |
| $P_3$   | 2          | 4        |
| $P_4$   | 1          | 5        |
| $P_5$   | 5          | 2        |

![](https://imgur.com/c9WBCw6.png)

$$
\text{Average waiting time}= 8.2
$$


#### Priority Scheduling + Round-Robin

* Run the process with the highest priority
* Processes with the same priority run round-robin

| process | burst time | priority |
| ------- | ---------- | -------- |
| $P_4$   | 7          | 1        |
| $P_2$   | 5          | 2        |
| $P_3$   | 8          | 2        |
| $P_1$   | 4          | 3        |
| $P_5$   | 3          | 3        |

![](https://imgur.com/2APRd2W.png)

#### Multilevel Queue

![](https://imgur.com/dUAJQze.png)

### Multiple-Processor Scheduling

* Multicore CPUs
* Multithreaded cores
* NUMA(non-uniform memory access) systems
* Heterogeneous multiprocessing

#### SMP
* Symmetric multiprocessing (SMP) is where each processor is self-scheduling
  * (a) All threads may be in a common ready queue
  * (b) Each processor may have its own private queue of threads
* keep all CPUs loaded for efficiency
  * Load balancing 
    *  attempts to keep workload evenly distributed
  * push migration
    * pushes task from overloaded CPU to other CPUs
  * pull migration
    * idle processors pulls waiting task from busy processor
* processor affinity
  * Soft affinity 
    * the OS attempts to keep a thread running on the same processor, but no guarantees
  * Hard affinity 
    * allows a process to specify a set of processors it may run on

![](https://imgur.com/RoN2QeB.png)

##### hyperthreading
![](https://imgur.com/E5dFCfH.png)

### real-time scheduling
* Real-Time system
  * soft real-time system
    *  but no guarantee as to when tasks will be scheduled
  * hard real-time system
    * task must be serviced by its deadline
* latency
  * Interrupt latency
    * time of stop process to another process
  * Dispatch latency
    * take current process off CPU and switch to another CPU

#### Earliest Deadline First Scheduling (EDF)

* Priorities are assigned according to deadlines:
  * the earlier the deadline, the higher the priority
  * the later the deadline, the lower the priority

![](https://imgur.com/yJcNMLU.png)

## Operating System  Examples
### linux scheduling
* Completely Fair Scheduler (CFS)
  * CFS scheduler maintains per task virtual run time in variable vruntime
  * To decide next task to run, scheduler picks task with lowest virtual run time
* Linux supports load balancing, but is also NUMA-aware


### solaris scheduling
* priority-based scheduling
* Six classes available
  * Time sharing (default) (TS)
  * Interactive (IA)
  * Real time (RT)
  * System (SYS)
  * Fair Share (FSS)
  * Fixed priority (FP)

![](https://imgur.com/YoUCDym.png)


# Chapter 6: Synchronization Tools

## Race condition

![](https://imgur.com/64HhNAf.png)

* `critical section` segment of code
  * Process may be changing common variables, updating table, writing file, etc
  * When one process in critical section, no other may be in its critical section

## Critical-Section Problem 


* Mutual Exclusion
  * If process is executing in its critical section, then no other processes can be executing in their critical sections
* Progress
  * if not process in critical section and have process want to enter critical section then have to let the process
* Bounded Waiting
  * the time process wait to enter critical section have to limit(cant wait forever)

### software solution
* cant avoid shared variable be override value by another process
* Entry section: disable interrupts
* Exit section: enable interrupts
   
#### part of Solution


* Assume that the `load` and `store` machine-language instructions are `atomic`
  * Which cannot be interrupted
  
* `turn` indicates whose turn it is to enter the critical section
* two process have enter critical section in turn
![](https://imgur.com/wUlw82E.png)



#### Peterson’s Solution


* Assume that the `load` and `store` machine-language instructions are `atomic`
  * Which cannot be interrupted
* `turn` indicates whose turn it is to enter the critical section
* `flag` array is used to indicate if a process is ready to enter the critical section
* solve `critical section problem` 
  * Mutual exclusion
  * progress
  * bounded-waiting


![](https://imgur.com/HPf3Vfc.png)

#### Memory Barrier
* Memory models may be either:
  * Strongly ordered – where a memory modification of one processor is immediately visible to all other processors
  * Weakly ordered – where a memory modification of one processor may not be immediately visible to all other processors

![](https://imgur.com/Mmz1N51.png)


#### Mutex Locks
* First acquire() a lock
* Then release() the lock
* `busy waiting`
  * the process will be block and continuous check is lock 
  * `spinlock` when is lock free will automatic let the waiting process know

#### semaphore
* wait()
* signal()
* Counting semaphore
  * integer value can range over an unrestricted domain
* Binary semaphore 
  * integer value can range only between 0 and 1
  * Same as a mutex lock
* Must guarantee that no two processes can execute the `wait()` and `signal()` on the same semaphore at the same time
  
##### Semaphore Implementation with no Busy waiting
* block()
  * place the process invoking the operation on the appropriate waiting queue
* wakeup()
  * remove one of processes in the waiting queue and place it in the ready queue

### Synchronization Hardware

* Hardware instruction
  * Atomic Swap()
  * Test and Set()
* Atomic variables

#### Hardware instruction
#### Atomic variables
* atomic variable that provides atomic (uninterruptible) updates on basic data types such as integers and booleans



## deadlock
![](https://imgur.com/O58l3oJ.png)
* deadlock
  * two or more processes are waiting indefinitely for an event that can be caused by only one of the waiting processes
  * Starvation 
    * indefinite blocking
    * A process may never be removed from the semaphore queue in which it is suspended
  * Priority Inversion 
    *  Scheduling problem when lower-priority process holds a lock needed by higher-priority process
    * Solved via priority-inheritance protocol

# Chapter 7: Synchronization Examples
## Problems of Synchronization

Most of the synchronization problems do not exist in
functional languages

* Bounded-Buffer Problem (Producer-consumer problem)
* Readers and Writers Problem
* Dining-Philosophers Problem
  

## OS 
* windows
  * spinlocks
  * dispatcher object
* linux 
  * Atomic integers
  * Mutex locks
  * Spinlocks, Semaphores
  * Reader-writer versions of both
* POSIX
  * mutex locks
  * semaphores
    * named
      * can be used by unrelated processes
    * unnamed
      * can be used only by threads in the same process
  * condition variable




# Chapter 8: Deadlocks

## Deadlock Characterization

* Mutual exclusion
  * only one process at a time can use a resource
* Hold and wait
  * a process holding at least one resource is waiting to acquire additional resources held by other processes
* No preemption
  * a resource can be released only voluntarily by the process holding it, after that process has completed its task
* Circular wait
  * there exists a set {P0, P1, …, Pn} of waiting processes such that:




## Deadlocks Prevention

* mutual exclusion
  * not required for sharable resources (e.g., read-only files); must hold for non-sharable resource
* hold and wait
  * must guarantee that whenever a process requests a resource, it does not hold any other resources
* No Preemption
  * If a process that is holding some resources requests another resource that cannot be immediately allocated to it, then all resources currently being held are released
* Circular Wai
  * check is have circular wait or not 

## Deadlock Avoidance
* **Cant do Preventon，have to check in run time**
* The goal for deadlock avoidance is to the system must not enter an unsafe state.
* each process declares the maximum number of resources of each type that it may need
* deadlock-avoidance algorithm dynamically examines the resource-allocation state to ensure that there can never be a circular-wait condition

## safe state
* safe state 
  * no deadlock
* unsafe state
  * possibility of deadlock
* Avoidance Algorithms
  * Single instance of a resource type
    * `resource-allocation graph`
  * Multiple instances of a resource type
    * Banker’s Algorithm

![](https://imgur.com/1fRZ96o.png)

### Resource-Allocation Graph
![](https://imgur.com/1pkLAOD.png)

* graph contains no cycles
  * no deadlock
* graph contains a cycle
  * only one instance per resource type, then deadlock
  * several instances per resource type, possibility of deadlock

### Banker’s Algorithm
* Max: request resource count to finish task
* Allocation: currently occupy resource count 
* Need: Max-Allocation resource count
* Available: free count of resource type 



#### Resource-Request Algorithm

#### example
* total available A (10 instances), B (5 instances), and C (7 instances)
* safe sequence:$P_1, P_3, P_4, P_0, P_2$
* unsafe sequence:$P_1, P_2, P_4, P_0, P_3$
<!-- * when task finish will release allocation resource then will have more  -->



| task  | allocation | max   | need  | available                    | order |
| ----- | ---------- | ----- | ----- | ---------------------------- | ----- |
|       | A,B,C      | A,B,C | A,B,C | A,B,C                        |       |
| $P_0$ | 0,1,0      | 7,5,3 | 7,4,3 | 7,4,5=( (7,4,3) + (0,0,2) )  | 3     |
| $P_1$ | 2,0,0      | 3,2,2 | 1,2,2 | 3,3,2=( (10,5,7) - (7,2,5) ) | 0     |
| $P_2$ | 3,0,2      | 9,0,2 | 6,0,2 | 7,5,5=( (7,4,5) + (0,1,0) )  | 4     |
| $P_3$ | 2,1,1      | 2,2,2 | 0,1,1 | 5,3,2=( (3,3,2) + (2,0,0) )  | 1     |
| $P_4$ | 0,0,2      | 4,3,3 | 4,3,1 | 7,4,3=( (5,3,2) + (2,1,1) )  | 2     |

## Deadlock Detection
### Single instance
![](https://imgur.com/mhFVJYh.png)

### Multiple instances:
* Total instances: A:7, B:2, C:6
* Available instances: A:0, B:0, C:0

| task  | allocation | request/need |
| ----- | ---------- | ------------ |
|       | A,B,C      | A,B,C        |
| $P_0$ | 0,1,0      | 0,0,0        |
| $P_1$ | 2,0,0      | 2,0,2        |
| $P_2$ | 3,0,3      | 0,0,0        |
| $P_3$ | 2,1,1      | 1,0,0        |
| $P_4$ | 0,0,2      | 0,0,2        |


## Deadlock Recovery

* Process termination
  * Abort all deadlocked processes
  * Abort one process at a time until the deadlock cycle is eliminated
  * In which order should we choose to abort?
    * Priority of the process
    * How long process has computed
    * Resources the process has used
* Resource preemption
  * Selecting a victim 
    * minimize cost
  * Rollback
    * return to some safe state, restart process for that state
  * Starvation 
    *  same process may always be picked as victim, so we should include number of rollbacks in cost factor


# Chapter 9: Main Memory

* The only storage CPU can access directly
  * Register access is done in one CPU clock (or less)
  * Main memory can take many cycles, causing a stall
  * Cache sits between main memory and CPU registers

## Protection
* need to ensure that a process can only access those addresses in its address space
* we can provide this protection by using a pair of base and limit registers defining the logical address space of a process
* CPU must check every memory access generated in user mode to be sure it is between base and limit for that user

![](https://imgur.com/2FwxklS.png)

##  Logical vs. Physical Address
* Logical address/virtual address
  * generated by the CPU
* Physical address
  * address seen by the memory unit
* Logical and physical addresses are the same in compile- time and load-time address-binding schemes; they differ in execution-time address-binding scheme
### Memory-Management Unit 

![](https://imgur.com/D3qyVEv.png)



## How to refer memory in a program – Address Binding
![](https://imgur.com/0tMyZIO.png)
* compile time
* load time
* execution time

## How to load a program into memory – static/dynamic loading and linking

* Dynamic Loading
  * load function instruct when need to use
  * better memory space
* Static Linking
  * duplicate same function instruct to memory in `compile time`
* Dynamic Linking
  * runtime link function address
  * DLL(Dynamic link library) in window


| Dynamic Loading                    | Static Linking                     | Dynamic Linking                      |
| ---------------------------------- | ---------------------------------- | ------------------------------------ |
| ![](https://imgur.com/q5gW8TF.png) | ![](https://imgur.com/BrL1XIu.png) | ![](https://i.imgur.com/dDe4AEV.png) |




## Contiguous Memory Allocation
### Variable-partition
### Dynamic Storage Allocation Problem
* First-fit: Allocate the first hole that is big enough
* Best-fit: Allocate the smallest hole that is big enough; must search entire list, unless ordered by size
* Produces the smallest leftover hole
* Worst-fit: Allocate the largest hole; must also search entire list
* Produces the largest leftover hole
#### Fragmentation

* External fragmentation 
  * problem of variable-allocation
  * free memory space enough to size but is not contiguous
  * compaction
* Internal fragmentation
  * problem of fix-partition-allocation
  * memory not use by process
 
![](https://imgur.com/hUMguQT.png)

## Non-Contiguous Memory Allocation
### Paging

* Divide physical memory into fixed-sized blocks called `frame`
  * size is power of 2, between 512 bytes and 16M bytes
* Divide logical memory into blocks of same size called `pages`
* To run a program of size N pages, need to find N free frames and load program
* benefit
  * process of physical-address space can be non-contiguous
  * avoid external fragmentation

#### Page table

* Page table only contain the page own by process
* process cant access memory that is not in 
* Page table is kept in main memory
  * Page-table base register (PTBR) 
    * points to the page table
  * Page-table length register (PTLR) 
    * indicates size of the page table

![](https://imgur.com/vPdD4cn.png)

##### Translation Look-aside Buffer (TLB)
The two-memory access problem can be solved by the use of a special fast-lookup hardware cache called translation look-aside buffers (TLBs) (also called associative memory)
![](https://imgur.com/ono9w1b.png)


#### address translation scheme
![](https://imgur.com/8P3rtfY.png)

* Page number(p)
  * each process can have $2^n$ page (32-bit computer one process can use 4GB memory)
* Page offset(d)
  *  combined with base address to define the physical memory address that is sent to the memory unit

![](https://imgur.com/8r3OVMT.png)
* 給定一個 32-bits 的 logical address，36 bits 的 physical address 以及 4KB 的 page size，這代表？
  * page table size = $2^{32}$ / $2^{12}$ = $2^{20}$ 個 entries
  * Max program memory: $2^{32}$ = 4GB
  * Total physical memory size = $2^{36}$ = 64GB
  * Number of bits for page number = $2^{32}$/$2^{12}$=$2^{20}$ pages -> 20 bits
  * Number of bits for frame number =$2^{36}$/$2^{12}$= $2^{24}$ frames -> 24 bits
  * Number of bits for page offset = 4KB page size = $2^{12}$ bytes -> 12 bits



#### Shared Pages 

* Shared code
  * One copy of read-only (reentrant) code shared among processes 

![](https://imgur.com/aWcluQQ.png)

