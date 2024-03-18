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

- ordinary pipes are better when

  - communication between two specific processes on the same machine

- named pipes are better when
  - we want to communicate over a network
  - relation is bidirectional and there is no parent child relationship between processes.

# programming exercises

## 2.24

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void Copy(char *out, char *in)
{

  int c;

  FILE *inPtr = fopen(in, "r");
  FILE *outPtr = fopen(out, "w");

  if (!inPtr)
  {
    perror("Source file can't be opened: ");
    exit(1);
  }

  if (!outPtr)
  {
    perror("Destination file can't be opened: ");
    exit(1);
  }

  // Copy file one char at a time and terminate loop when c reaches end of file (EOF)
  while ((c = fgetc(inPtr)) != EOF)
  {
    fputc(c, outPtr);
  }

  // if all the above lines get executed, then the program has run successfully
  printf("Success!\n");

  // close files
  fclose(inPtr);
  fclose(outPtr);
}

int main(int argc, char *argv[])
{
  if (argc < 3)
  {
    fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
    return EXIT_FAILURE;
  }
  printf("copy %s to %s\n", argv[1], argv[2]);

  Copy(argv[2], argv[1]);
  return EXIT_SUCCESS;
}
```

## 3.19 part 1

share memory

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>

#define SHM_SIZE  sizeof(struct timeval)

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <command>\n", argv[0]);
        return EXIT_FAILURE;
    }

    struct timeval *start_time_ptr;
    int shm_fd;
    pid_t pid;
    void *shm_ptr;

    // Create shared memory
    shm_fd = shm_open("/time_shm", O_CREAT | O_RDWR, 0666);
    if (shm_fd == -1) {
        perror("shm_open");
        return EXIT_FAILURE;
    }
    // Set the size of the shared memory segment
    ftruncate(shm_fd, SHM_SIZE);
    // Map the shared memory segment to the address space of the process
    shm_ptr = mmap(0, SHM_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shm_ptr == MAP_FAILED) {
        perror("mmap");
        return EXIT_FAILURE;
    }

    start_time_ptr = (struct timeval *)shm_ptr;

    pid = fork();

    if (pid == -1) {
        perror("fork");
        return EXIT_FAILURE;
    } else if (pid == 0) {  // Child process
        gettimeofday(start_time_ptr, NULL);
        execvp(argv[1], &argv[1]);
        // execvp only returns if an error occurs


        perror("execvp");
        exit(EXIT_FAILURE);
    } else {  // Parent process
        wait(NULL);
        struct timeval end_time;
        gettimeofday(&end_time, NULL);
        struct timeval start_time = *start_time_ptr;
        // Calculate elapsed time
        long elapsed_sec = end_time.tv_sec - start_time.tv_sec;
        long elapsed_usec = end_time.tv_usec - start_time.tv_usec;
        if (elapsed_usec < 0) {
            elapsed_sec--;
            elapsed_usec += 1000000;
        }
        printf("Elapsed time: %ld.%06ld seconds\n", elapsed_sec, elapsed_usec);
    }

    // Cleanup
    munmap(shm_ptr, SHM_SIZE);
    close(shm_fd);
    shm_unlink("/time_shm");

    return EXIT_SUCCESS;
}
```

## 3.19 part 2

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define READ_END 0
#define WRITE_END 1

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <command>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int pipe_fd[2];
    pid_t pid;
    struct timeval start_time, end_time;

    if (pipe(pipe_fd) == -1) {
        perror("pipe");
        return EXIT_FAILURE;
    }

    pid = fork();

    if (pid == -1) {
        perror("fork");
        return EXIT_FAILURE;
    } else if (pid == 0) {  // Child process
        close(pipe_fd[READ_END]);  // Close the read end of the pipe
        gettimeofday(&start_time, NULL);
        write(pipe_fd[WRITE_END], &start_time, sizeof(struct timeval));
        close(pipe_fd[WRITE_END]);
        execvp(argv[1], &argv[1]);
        // execvp only returns if an error occurs
        perror("execvp");
        exit(EXIT_FAILURE);
    } else {  // Parent process
        close(pipe_fd[WRITE_END]);  // Close the write end of the pipe
        wait(NULL);
        read(pipe_fd[READ_END], &start_time, sizeof(struct timeval));
        close(pipe_fd[READ_END]);
        gettimeofday(&end_time, NULL);
        // Calculate elapsed time
        long elapsed_sec = end_time.tv_sec - start_time.tv_sec;
        long elapsed_usec = end_time.tv_usec - start_time.tv_usec;
        if (elapsed_usec < 0) {
            elapsed_sec--;
            elapsed_usec += 1000000;
        }
        printf("Elapsed time: %ld.%06ld seconds\n", elapsed_sec, elapsed_usec);
    }

    return EXIT_SUCCESS;
}

```
