# database systems

# Three-schema Architecture
* Internal level
  * how data actually store in database
* Conceptual level
  * use some ER Diagram to desc main conceptual of data structure
* External level
  * how to present to out world (interface)

# Database constraint
* Implicit Constraints
  * Constraints that are applied in the data model
* Schema-Based Constraints or Explicit Constraints 
  * Constraints that are directly applied in the schemas of the data model, by specifying them in the DDL(Data Definition Language).
* Semantic Constraints
  * Constraints that cannot be directly applied in the schemas of the data model. We call these Application based or .

# superkey
![](https://media.geeksforgeeks.org/wp-content/uploads/20230314093236/keys-in-dbms.jpg)

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
