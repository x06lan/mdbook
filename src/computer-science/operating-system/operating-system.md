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
* Waiting time 
  * amount of time a process has been waiting in the ready queue
* Response time 
  * amount of time it takes from when a request was submitted until the first response is produce


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
  * Consider one CPU-bound and many I/O-bound processesP1
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
| $P_1$   | 4          | 3        |
| $P_2$   | 5          | 2        |
| $P_3$   | 8          | 2        |
| $P_4$   | 7          | 1        |
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