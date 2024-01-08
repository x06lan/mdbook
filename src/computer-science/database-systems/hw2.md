
# hw2 110590049

tags `db` `database`

[2023 database-systems HW2.pdf](../../assets/pdf/database_systemsHW2.pdf)

# 1.



The doctor could also be a patient. Additionally, the pharmacy can sell drugs from pharmaceutical companies at different prices compared to other pharmacies.
<image src="../../assets/image/database_ERdiagram_doctor.svg" width="80%">

The key icon stands for primary key. On the other side of the connection with the primary key is the foreign key.
<image src="../../assets/image/database_EERdiagram_doctor.svg" width="80%">



## 2.
<image src="../../assets/image/database_ERdiagram_baseball.svg" width="80%">

The key icon stands for primary key. On the other side of the connection with the primary key is the foreign key.
<image src="../../assets/image/database_EERdiagram_baseball.svg" width="80%">


## 3.
<image src="../../assets/image/database_ERdiagram_hw2-3.png" width="80%">

### 3.a
有違反 Semantic Integrity Constraints，Robert 的上司是 James(888665555) ，但 Robert 的薪水(58000)比上司(55000)還高
No integrity constraints are violated.
### 3.b
The DEPT_LOCATIONS number should be 5, but this operation inserts 2 into it, resulting in inconsistency in the DEPT_LOCATIONS number.
### 3.c
No integrity constraints are violated.
### 3.d
Delete the PROJECT "ProductX" from the PROJECT table, and also delete the tuple from the WORKS_ON table where "Pno" is "1."
### 3.e
No integrity constraints are violated.
### 3.f
If you modify the Pnumber from 30 to 40, you also need to change the row in the WORKS_ON table where Pno is 30 to 40. This will result in inconsistency within the WORKS_ON table.

## 4.

<image src="../../assets/image/database_ERdiagram_airplane.svg" width="80%">

