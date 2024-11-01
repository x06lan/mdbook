# hw1

[compiler HW1.pdf](../../assets/pdf/compiler_HW1.pdf)

## 1
```bash
gcc -S exercise1.c -o exercise1.s
sh run.sh exercise1.s

```

## 2~5
```bash
sh run.sh exercise2.s
sh run.sh exercise3.s
sh run.sh exercise4.s
sh run.sh exercise5.s
sh run.sh exercise6.s
```
## 6
```bash
gcc -S exercise6.c -o exercise6.s
sh run.sh exercise6.s
```
## 7
```bash
gcc -S matrix.c -o matrix.s
sh run.sh matrix.s
```
## run.sh
```bash
#!/bin/bash

# Check if file is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <assembly-file>"
    exit 1
fi

# Set the input file
asm_file=$1

# Get the base filename without the extension
base_filename=$(basename "$asm_file" .s)

# Assemble
# nasm -f elf64 "$asm_file" -o "$base_filename.o"
as "$asm_file" -o "$base_filename.o"
if [ $? -ne 0 ]; then
    echo "Error: Assembly failed"
    exit 1
fi

# Link
gcc -no-pie "$base_filename.o" -o "$base_filename.bin"
if [ $? -ne 0 ]; then
    echo "Error: Linking failed"
    exit 1
fi

# Execute
./"$base_filename.bin"
```

## 1.
```x86asm
	.file	"exercise1.c"
	.text
	.section	.rodata
.LC0:
	.string	"n = %d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$42, %esi
	leaq	.LC0(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (GNU) 14.2.1 20240910"
	.section	.note.GNU-stack,"",@progbits

```
## 2.
```x86asm
.text
    .globl main # make main visible for ld
main:
    pushq %rbp                # Save base pointer
    movq %rsp, %rbp           # Set up stack frame

    # 4 + 6
    movq $4, %rax             # Load first operand into RAX
    addq $6, %rax             # 4 + 6

    movq $msg, %rdi           # First argument: format string
    movq %rax, %rsi           # Second argument: result
    xorq %rax, %rax           # Clear RAX (no floating point args)
    call printf               # Call printf

    # 21 * 2
    movq $21, %rax            # Load first operand into RAX
    imulq $2, %rax            # 21 * 2

    movq $msg, %rdi           # First argument: format string
    movq %rax, %rsi           # Second argument: result
    xorq %rax, %rax           # Clear RAX 
    call printf               # Call printf

    # 4 + 7 / 2
    movq $7, %rax             # Load numerator into RAX
    xorq %rdx, %rdx           # Clear RDX for division
    movq $2, %rcx             # Load denominator into RCX
    idivq %rcx                # RAX = RAX / RCX (7 / 2)
    addq $4, %rax             # Add the result to 4

    movq $msg, %rdi           # First argument: format string
    movq %rax, %rsi           # Second argument: result
    xorq %rax, %rax           # Clear RAX 
    call printf               # Call printf

    # 3 - 6 * (10 / 5)
    movq $10, %rax            # Load numerator into RAX
    movq $5, %rcx             # Load denominator into RCX
    idivq %rcx                # RAX = RAX / RCX (10 / 5)
    imulq $-6, %rax           # RAX = RAX * (-6)
    addq $3, %rax             # Add 3 to the result

    movq $msg, %rdi           # First argument: format string
    movq %rax, %rsi           # Second argument: result
    xorq %rax, %rax           # Clear RAX (no floating point args)
    call printf               # Call printf

    # Exit
    movq $0, %rax             # Return code 0
    popq %rbp                 # Restore base pointer
    ret                       # Return from main

.data
msg:
    .string "n = %d\n"        # Format string for printf

```
## 3.

```x86asm
.text
    .globl main                    # make main visible for ld
main:
    pushq %rbp                     # Save base pointer
    movq %rsp, %rbp                # Set up stack frame

    # Evaluate true && false
    movq $1, %rax                  # Load true (1) into RAX
    andq $0, %rax                  # Perform logical AND with false (0)
    cmpq $0, %rax                  # Compare result with 0 (false)
    movq $false_msg, %rdi          # Assume false by default
    movq $true_msg, %rsi           # Assume true
    cmovne %rdi, %rsi              # If result is not 0, use true message
    call printf                    # Call printf

    # Evaluate 3 == 4 ? 10 * 2 : 14
    movq $3, %rax                  # Load 3 into RAX
    cmpq $4, %rax                  # Compare RAX with 4
    jne not_equal                  # Jump if not equal (3 != 4)
    movq $14, %rax                 # Load result for else case (14)
    jmp print_result               # Jump to print result

not_equal:
    movq $10, %rax                 # Load first operand (10)
    imulq $2, %rax                 # Multiply by 2 (10 * 2)

print_result:
    movq $int_msg, %rdi            # Load format string for integer output
    movq %rax, %rsi                # Second argument: result (product or 14)
    call printf                    # Call printf

    # Evaluate 2 == 3 || 4 <= (2 * 3)
    movq $3, %rax                  # Load 3 into RAX
    cmpq $2, %rax                  # Compare 2 with 3
    jne check_second_condition      # Jump if 2 != 3

    movq $1, %rbx                  # If 2 == 3, set RBX to true (1)
    jmp finish                     # Jump to finish

check_second_condition:
    movq $2, %rcx                  # Load 2 into RCX
    imulq $3, %rcx                 # Multiply 2 * 3 (result: 6)
    movq $4, %rax                  # Load 4 into RAX
    cmpq %rcx, %rax                # Compare 4 with 6
    jbe less_or_equal              # Jump if 4 <= 6

    movq $0, %rbx                  # If not, set RBX to false (0)
    jmp finish                     # Jump to finish

less_or_equal:
    movq $1, %rbx                  # If 4 <= 6, set RBX to true (1)

finish:

    cmpq $0, %rbx                  # Compare RBX with 0 (false)
    movq $false_msg, %rdi          # Assume false by default
    movq $true_msg, %rsi           # Assume true
    cmovne %rsi, %rdi              # If RBX is not zero (true), use true message
    call printf                    # Call printf

    # Exit program properly
    movq $0, %rax                  # Return code 0
    popq %rbp                      # Restore base pointer
    ret                            # Return from main

.data
false_msg:
    .string "false\n"              # String for false output

true_msg:
    .string "true\n"               # String for true output

int_msg:
    .string "%d\n"                 # Format string for integer output


```

## 4.

```x86asm
    .text
    .globl main               # Make main visible for the linker
main:
    pushq %rbp                # Save base pointer
    movq %rsp, %rbp           # Set up stack frame

    # Load x from memory
    movq x(%rip), %rax        # Move the value of x (2) into RAX

    # y = x * x
    imulq %rax, %rax          # Multiply x by itself (RAX = RAX * RAX, now RAX = 4)

    # Store the result of y in memory
    movq %rax, y(%rip)        # Move the result (y = 4) into the y variable

    # Load x and y from memory
    movq x(%rip), %rax        # Load x (2) back into RAX
    addq y(%rip), %rax        # Add y (4) to RAX (RAX = 4 + 2 = 6)

    # Prepare for the printf call
    movq $result_msg, %rdi    # Load the format string into RDI
    movq %rax, %rsi           # Move the result (6) into RSI
    xorq %rax, %rax           # Clear RAX for calling printf
    call printf               # Call printf to print the result

    # Exit the program
    movq $60, %rax            # syscall: exit
    xorq %rdi, %rdi           # status: 0
    syscall                   # invoke syscall

    popq %rbp                 # Restore base pointer
    ret                       # Return from main

    .data                     # Data section
x:  .quad 2                   # Allocate x in the data segment, initialized to 2
y:  .quad 0                   # Allocate y in the data segment, initialized to 0
result_msg: .string "%d\n"    # Format string for printf

```

## 5
```x86asm
        .data
result_msg: .string "%d\n"    # Format string for printf

    .text
    .globl main               # Make main visible for the linker
main:
    pushq %rbp                # Save base pointer
    movq %rsp, %rbp           # Set up stack frame

    ### First Instruction: print (let x = 3 in x * x)

    # Allocate space for x on the stack
    subq $8, %rsp             # Reserve 8 bytes on the stack for x
    movq $3, (%rsp)           # Set x = 3 (store on stack)

    # x * x
    movq (%rsp), %rax         # Load x into RAX
    imulq %rax, %rax          # Multiply x by itself (RAX = x * x)

    # Prepare for the printf call (result is 9)
    movq $result_msg, %rdi    # Load the format string into RDI
    movq %rax, %rsi           # Move the result (9) into RSI
    xorq %rax, %rax           # Clear RAX for calling printf
    call printf               # Call printf to print the result

    # Deallocate space for x
    addq $8, %rsp             # Free the space allocated for x on the stack

    ### Second Instruction: print (let x = 3 in ...)

    # Allocate space for x on the stack
    subq $8, %rsp             # Reserve 8 bytes on the stack for x
    movq $3, (%rsp)           # Set x = 3 (store on stack)

    # Inner block: let y = x + x in x * y
    subq $8, %rsp             # Reserve 8 bytes on the stack for y
    movq 8(%rsp), %rax      # Load x into RAX (from previous stack slot)
    addq %rax, %rax           # y = x + x (RAX = x + x)
    movq %rax, (%rsp)         # Store y on the stack 3

    movq 8(%rsp), %rax      # Load x into RAX again (from previous stack slot)
    imulq (%rsp), %rax        # Multiply x * y (RAX = x * y)
    movq %rax, (%rsp)         # Store y on the stack 18

    # Inner block: let z = x + 3 in z / z
    subq $8, %rsp             # Reserve 8 bytes on the stack for z
    movq 16(%rsp), %rcx     # Load x into RCX (from previous stack slot)
    addq $3, %rcx             # z = x + 3 (RCX = x + 3)
    movq %rcx, (%rsp)         # Store z on the stack

    xorq %rdx, %rdx           # Clear RDX (for division)
    movq (%rsp), %rax         # Load z into RAX (z = x + 3)
    idivq %rax                # z / z (RAX = z / z, which is 1)

    # Compute (x * y) + (z / z)
    addq %rax, 8(%rsp)      # Add z / z (which is 1) to x * y (from earlier)

    # Prepare for the printf call (result is 19)
    movq $result_msg, %rdi    # Load the format string into RDI
    movq 8(%rsp), %rsi        # Load the result (19) into RSI
    xorq %rax, %rax           # Clear RAX for calling printf
    call printf               # Call printf to print the result

    # Deallocate space for z, y, and x
    addq $24, %rsp            # Free the space allocated for z, y, and x

    ### Exit the program
    movq $60, %rax            # syscall: exit
    xorq %rdi, %rdi           # status: 0
    syscall                   # invoke syscall

    popq %rbp                 # Restore base pointer
    ret                       # Return from main

```

## 6
```c
#include <stdio.h>
int isqrt(int n)
{
    int c = 0, s = 1;
    // x^2 = (x-1)^2 + 2(x-1) + 1
    do
    {
        // Increment c and calculate s in one line
        s += (++c << 1) + 1;
    } while (s <= n); // Single branching instruction here
    return c;
}

int main()
{
    int n;
    for (n = 0; n <= 20; n++)
        printf("sqrt(%2d) = %2d\n", n, isqrt(n));
    return 0;
}
```
