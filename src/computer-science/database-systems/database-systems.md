# database systems

# Three-schema Architecture
* Internal level
  * how data actually store in database
* Conceptual level
  * use some ER Diagram to desc main conceptual of data structure
* External level
  * how to present to out world (interface)

# Database constraint
* Implicit Constraints or Inherent constraint
  * Constraints that are applied in the data model
* Schema-Based Constraints or Explicit Constraints
  * Constraints that are directly applied in the schemas of the data model, by specifying them in the DDL(Data Definition Language).
* Semantic Constraints or Application based
  * Constraints that cannot be directly applied in the schemas of the data model. We call these Application based or .
# Database Independence
* Logical Data Independence:
  * The capacity to change the conceptual schema without having to change the external schemas and their associated application programs
* Physical Data Independence:
  * The capacity to change the internal schema without having to change the conceptual schema.
# Three-tier client-server architecture
* presentation layer
  * GUI, web interface
* busincess layer
  * application programs
* database services layer
  * database management system
# superkey
![](https://media.geeksforgeeks.org/wp-content/uploads/20230314093236/keys-in-dbms.jpg)

# null
A special null value is used to represent values that are unknown or not available (value exist) or inapplicable (value undefined) in certain tuples.
# EER diagram


## total vs partial | disjoint vs overlapped
|                         | total                 | partial     | disjoint    | overlapped        |
| ----------------------- | --------------------- | ----------- | ----------- | ----------------- |
| EER diagram             | double line           | single line | d           | o                 |
| super class inheritance | at least one subclass | can be none | at most one | can more than one |

* specialization:
  * top down conceptual refinement process
  * arrow to subclass
* generalization:
  * bottom up conceptual synthesis process
  * arrow to superclass
* shared subclass:
  * multiple super class
  * multiple inheritance from diff super class
  * presend subclass is intersection of super class
* Categories (UNION TYPES):
  * presend subclass is union of super class
  * use "U" as symbol in EER diagram
# sql
```sql
HOTEL(hotelNo, hoteName, City);
ROOM(roomNo, hotelNo, type, price);
BOOKING(hotelNoguestNo, dateFrom, dateTo, foomNo);
GUEST(guestNo, guestName, guestAddress);
```
## List the price and type of all rooms that hotelName is Howard Hotel.
```sql
SELECT r.price, r.type
FROM ROOM r
INNER JOIN HOTEL h ON r.hotelNo = h.hotelNo
WHERE h.hotelName = 'Howard Hotel';
```
```sql
SELECT price, type
FROM ROOM
WHERE hotelNo = (SELECT hotelNo FROM HOTEL WHERE hotelName = 'Howard Hotel');
```

## List the details of all rooms at the Howard Hotel, including the name of the guest staying in the room if the room is occupied.
```sql
SELECT r.roomNo, r.type, r.price, g.guestName
FROM ROOM r
LEFT JOIN BOOKING b ON r.roomNo = b.roomNo
LEFT JOIN GUEST g ON b.guestNo = g.guestNo
INNER JOIN HOTEL h ON r.hotelNo = h.hotelNo
WHERE h.hotelName = 'Howard Hotel';
```
## List all single rooms with a price below 3,000 per night. ) (4%) List all guests currently staying at the Howard Hotel.
```sql
SELECT r.roomNo, r.price
FROM ROOM r
WHERE r.type = 'single' AND r.price < 3000;

```
## list all guests currently staying at the "Howard Hotel,"
```sql
SELECT DISTINCT g.guestName
FROM GUEST g
INNER JOIN BOOKING b ON g.guestNo = b.guestNo
WHERE b.hotelNo = (SELECT hotelNo FROM HOTEL WHERE hotelName = 'Howard Hotel');
```
## join vs. sub-query
In general join have better performance because of optimisers.

# 正規化 (normalization)
1. candidate key: If a relation schema has more than one key, each is called a candidate key
1. Prime attribute: Prime attribute must be a member of some candidate key
## Functional Dependencies
$\{x,y\}\rightarrow\{z\}\\$
mean if get x and y can get z
## partial dependency
$\{x,y\}\rightarrow\{z\}$ but $ \{x\}\rightarrow\{z\}\\$
x alone can get z then it is partial dependency
## transitive dependency
$\{x\}\rightarrow\{y\}\\$
$\{y\}\rightarrow\{z\}\\$
and y is not candidate key then it is transitive dependency
## multivalued dependency

$\{x\}\rightarrow\{y\}\\$
if y is the subset of x then this is multivalued dependency
## join dependency
## 1NF
*  must be a primary key for identification
*  no duplicated rows or columns
## 2NF
* 1NF
* no partial dependency
* every non-prime attribute $y$ in R is fully functionally dependent on the primary key
## 3NF
* 2NF
* no transitive partial dependency(遞移相依)

## BCNF or 3.5NF (Boyce-Codd Normal Form)

* 3NF
* all key of table cant depend on another non-key columns

## 4NF
* if, for every nontrivial multivalued dependency x is superkey
* not only can save on storage, but also avoid the update anomalies

## 5NF
* The constraint states that every legal state r of R should have a non-additive join decomposition into R1, R2, ..., Rn; that is, for every such r we have

## NF example
2NF

![](https://imgur.com/iohrUvO.png)

3NF

![](https://imgur.com/MLKsKtS.png)

4NF 5NF

![](https://imgur.com/TPJqzyP.png)
# disk
* Blocking factor (bfr): refers to the number of records per block
## record
* fixed length
* variant length

## spanned
* Spanned Records:a record can be stored in more than one block
* unspanned Records:no record can span two blocks
<!-- ## Operations on Files -->

## unorder file
* linear search
* heap or pile file
* Record insertion is quite efficient
* deletion marker
## order file
* sequential
* sorted
* binary search

### clustered index(B-Tree)
primary index is leaf index of tree
![](https://imgur.com/6Ix8crC.png)
### not clustered index
![](https://imgur.com/5MTXQN2.png)
## hash file
### deal with collision
* Chaining :use link list to chaining data
* Rehashing
* Open Addressing
  * linear probing
  * Quadratic Probing
  * Double Hashing


### Dynamic Hashing or extendible hashing
problem of static probing: when system need scale bucket it will  spend a lot time to move data and cant access data
