# Relational Modelling
- collection of inter-connected relations (or tables)
- the relation model has one mechanism: relations 
  - each **relation** (denoted R, S, T, ...) has:
    - a name (unique within a given database) 
    - a set of attributes 
  - each **attribute** (denoted A, B etc.) has:
    - a name (unique within a given relation)
    - an associated domain (set of allowed values)

## Relational Data Model
### ER MODEL --> RELATIONAL SCHEMA 
[er-model](er-model-2.png)
[relational-schema](relational-schema.png)

### Integrity Constraints 
- to represent real-world problems, need to describe 
  - what values are/are not allowed 
  - what combinations of values are/are not allowed
- Constraints are logical statements that do this:
  - **domain constraints**: limit the set of values that attributes can take
    - employee.age attribute is defined as an *integer* but it is better modelled by adding extra constraint **(15 < age < 66)**
  - **key constraints**: identify attributes that uniquely identify tuples 
    - Student(id, ... ) is guaranteed unique
    - Class (..., day, time, location, ...) is unique
  - **entity integrity constraints**: require keys to be fully-defined.
    - Class(..., Mon, 2pm, Lyre, ...) is well-defined
    - Class(..., NULL, 2pm, Lyre, ...) is not well-defined
  - **referential integrity constraints**: require references to other tables to be valid 
    - describes references between relations (tables)
    - are related to notion of a **foreign key**

[foreign-key](foreign-key.png)

### Foreign Keys 
- A set of attributes F in relation R1 is a foreign key for R2 if:
  - the attributes in F correspond to the primary key of R2
  - the value for F in each tuple of R1
    - either occurs as a primary key in R2
    - or is entirely NULL
- the "glue" that links individual relations (tables)
- way to assemble query answers from multiple tables 
- relational representation of ER relationships 

### Describing Relational Schemas 
- need a language to express relational schemas; that's SQL!

```
CREATE TABLE TableName (
  attrName1 domain1 constraints1, 
  attrName2 domain2 constraints2,
  ...
  PRIMARY KEY (attr_i, attr_j, ...),
  FOREIGN KEY (attr_x, attr_y, ...)
              REFERENCES 
              OtherTable(attr_m, attr_n, ...), ...
)
```