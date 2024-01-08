
# hw1 110590049

tags `db` `database`

[2023 database-systems HW1.pdf](../../assets/pdf/database_systemsHW1.pdf)

# 1.

install steps

<image src="https://imgur.com/IyVRggv.png" width="80%">

<image src="https://imgur.com/mqVzdkG.png" width="80%">

<image src="https://imgur.com/8xrKhqQ.png" width="80%">

commands

<image src="https://imgur.com/6Inwvgt.png" width="80%">


# 2. main characteristies
* **Self-describing**: <br> A DBMS catalog stores the description of a particular database (e.g. data structures, types, and constraints) 
* **Insulation between programs and data**: <br> program-data independence

# 3.a data model
Set of concepts to describe the structure of a database,
the operations for manipulating these structures, and
certain constraints that the database should obey.

# 3.b database schema
The description of a database. Includes descriptions of the database structure,
data types, and the constraints on the database.

# 4.Three-Schema Architecture
* **Internal schema**: at the internal level to describe physical storage structures and access paths
* **Conceptual schema**: at the conceptual level to describe the structure and constraints for the whole database for a community of users.



# 5.For the binary relationships below,suggest cardinality ratios based on common-sense meaning of the entity types. Clearly state any assumptions you make

| Entity1   | Cardinality Ratio | Entity2 | Reason                                                                                                          |
| --------- | ----------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| Student   | 1:N               | Book    | A book can only be own by one person at the same time.                                                          |
| Student   | N:1               | Advisor | One advisor can have multiple students, but a student can only be connected to one advisor at a time.           |
| ClassRoom | N:M               | Wall    | Walls can be shared by multiple classrooms, and a class can have multiple walls.                                |
| Student   | N:M               | Course  | Reason: Students can be enrolled in multiple courses, and a course can have multiple students at the same time. |
| Car       | 1:1               | Engine  | One car should only have one engine at a time.                                                                  |


# 6.a
| Entity1        | Cardinality Ratio | Entity2                       | Reason                                                      |
| -------------- | ----------------- | ----------------------------- | ----------------------------------------------------------- |
| Student ID No. | 1:1               | ID No.                        | one person only have one ID number                          |
| Student ID No. | 1:1               | Name                          | one student only have one name                              |
| Student ID No. | 1:1               | Cellphone                     | one student only have one phone                             |
| Student ID No. | 1:1               | Signature                     | one student only have one signature                         |
| Student ID No. | 1:N               | No.                           | one student can have multiple suspension                    |
| No.            | 1:1               | Class                         | only suspension one class at time                           |
| No.            | 1:1               | Date of application           | one form only have one application time                     |
| No.            | 1:1               | Date of Resumption            | one form only have one resumption time                      |
| No.            | 1:1               | Application                   | one form can only have one type of application              |
| No.            | 1:1               | Department/Graduate Institute | one form can only have one Department or Graduate Institues |
| No.            | 1:1               | Reason for Suspension         | one form only have one reason of suspension                 |
| No.            | 1:1               | Suspension                    | one form only have one status of suspenstion                |
| No.            | 1:1               | Sigend by Parent              | one form only have one signed                               |
| No.            | 1:1               | Address                       | one form only have one address                              |


# 6.b
<img src="../../assets/image/database_ERdiagram.drawio.svg">