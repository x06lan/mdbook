
# hw1
## 1
* a. 
    * The CPU can initiate a DMA (Direct Memory Access) operation by writing values into special registers that can be independently accessed by the device.
* b.
    * When the device is finished with its operation, it interrupts the CPU to indicate the completion of the operation. 
* c.
    * Yes, If the DMA and CPU access the memory at same time may generate coherency issue since it have different value with caches.



## 2.15
* message-passing model
    * pros: simple
    * cons: only apply for smaller amounts of data
* shared-memory model
    * pros: need to avoid race condition
    * cons: apply for large amoung data
## 2.19
* Pros:
    * Easier to extend a microkernel
    * Easier to port the OS to new architectures
    * More reliable (less code is running in kernel mode)
    * More secure
* Cons:
    * Performance overhead of user space to kernel space communication
* How do user programs and system services interact in a microkernel architecture?
    * Communication takes place between user modules using message passing
## 3.12
the system save the state of the old process and load the saved state for the new process via a context switch
## 3.18

* ordinary pipes are better when
    * communication between two specific processes on the same machine

* named pipes are better when
    *  we want to communicate over a network 
    * relation is bidirectional and there is no parent child relationship between processes.

# programming exercises


## 2.24
## 3.19