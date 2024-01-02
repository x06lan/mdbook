# hw4 110590049

tags `db` `database`

[2023 database-systems HW4.pdf](../../assets/pdf/database_systemsHW4.pdf)

# 1
$
\{A,B\} \rightarrow \{C\}\\
\{A\}\rightarrow \{D,E\}\\
\{D\} \rightarrow \{I,J\}\\
\{B\}\rightarrow \{F\}\\
\{F\} \rightarrow \{G,H\}\\
$
## 1.a
$A,B$ is Key because
* $A,B$ can get $C$
* $A$ can get $\{D,E,I,J\}$
* $B$ can get $\{F,G,H\}$

## 1.b
* 2NF:no partial dependcy

$
\{A,B\} \rightarrow \{C\}\\
\{A\}\rightarrow \{D,E\}\\
\{D\}\rightarrow \{I,J\}\\
\{B\}\rightarrow \{F\}\\
\{F\} \rightarrow \{G,H\}\\
$

## 1.c
$
\{A,B\} \rightarrow \{C\}\\
\{A\}\rightarrow \{D,E\}\\
\{D\} \rightarrow \{I,J\}\\
\{B\}\rightarrow \{F\}\\
\{F\} \rightarrow \{G,H\}\\
$

# 2
FD1={Course_no} → {Offering_dept, Credit_hours, Course_level}

FD2={Course_no, Sec_no, Semester, Year} → {Days_hours, Room_no, No_of_students, Instructor_ssn}

FD3={Room_no, Days_hours, Semester, Year} → {Instructor_ssn, Course_no, Sec_no}

## 2.a

1NF because:
* FD1 have partial function since Course_no is not key

## 2.b
* {Course_no, Sec_no, Semester, Year}
* {Room_no, Days_hours, Semester, Year}

## 2.c
use {Course_no, Sec_no, Semester, Year} as PK

loss FD3
R1 = {Course_no, Offering_dept, Credit_hours, Course_level}

R2 = {Course_no, Sec_no, Semester, Year, Days_hours, Room_no, No_of_students, Instructor_ssn}}

is BCNF
# 3
* Caching: move disk data to RAM or SSD
* Indexing: use B-trees or hash indexes to speedup the time of searching
* organization of data on disk: keep related data on continuous block
# 4
## 4.a
$$
R=30+9+9+40+10+8+1+4+4+ 1(\text{deletion marker})=116\\
$$
## 4.b
$$
\begin{aligned}
bfr&=\frac{block}{record}\\
&=\frac{512}{116} \approx 4
\end{aligned}\\
\begin{aligned}
\text{disk block }&=\frac{r}{bfr}\\
&=7500
\end{aligned}\\
$$
## 4.c
### 4.c.i
$$
bfri=\frac{Block size}{\text{Index record size =(Block pointer + SSN) }}=34.13 \approx 34\text{ bytes}
$$
### 4.c.ii

$$
\text{ number of first-level index entries }=\text{disk block }=7500\\
\text{number of first-level index blocks}
=\frac{7500}{bfri}=220.58
\approx 221
$$
### 4.c.iii
$$
level=log_{34}{(7500)}=2.53 \approx 3
$$
### 4.c.iv
$$
\begin{aligned}
\text{level1}&=\frac{7500}{34}=220.58 \approx 221\\
\text{level2}&=\frac{221}{34}=6.5 \approx 7\\
\text{level3}&=\frac{221}{34}=0.295 \approx 1\\
\end{aligned}\\
221+7+1=229
$$
### 4.c.v
$$
\text{block access}=level+1=4
$$
## 4.d
### 4.d.i
$$
bfri=\frac{Block size}{\text{Index record size =(Block pointer + SSN) }}=34.13 \approx 34\text{ bytes}
$$


### 4.d.ii
$$
\text{number of first-level index blocks}
=\frac{30000}{bfri}=882.35
\approx 883
$$
### 4.d.iii
$$
level=log_{34}{(30000)}=2.92 \approx 3
$$
### 4.d.iv
$$
\begin{aligned}
\text{level1}&=\frac{30000}{34}=882.35 \approx 883\\
\text{level2}&=\frac{883}{34}=25.97 \approx 26\\
\text{level3}&=\frac{26}{34}=0.764 \approx 1\\
\end{aligned}\\
883+26+1=910
$$
### 4.d.v
$$
\text{block access}=level+1=4
$$

# 5
* **primary index**: must be defined on an ordered key field.
* **clustered index**: must be defined on an order field (not keyed) allowing for ranges of records with identical index field values.
* **secondary index**: is defined on any non-ordered (keyed or non-key) field.
