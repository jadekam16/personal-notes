# Data Modelling 

## Aims 
- describe what info is contained in the database 
- describe relos between data items 
- describe constraints on data 
  
## Design Process 
1. Start Simple 
2. Identify objects/properties, then relationships 
3. Find keywords in requirements, suggests data/relationships 
4. Consider all possible data 

### Exercise: Course Outline Data Model 
- Develop an informal data model for it by identifying:
 - data items involved (obj and their attributes)
   - Course: code, name, description, uoc, convenor(user), outcome*
   - Classes: types, day, starting, ending, where, course*
   - Users: zid, name, email, types
   - Assessment: name, description, weight, due_date
 - relationships between these data items 
   - Takes: user, class
   - Teaches: role, user, course
   - Equivalent: course1, course2
   - Excluded: course1, course2
   - Part_of: assessment, course
 - constraints on data and relationships 

### Exercise: Gmail Data Model 
- The data items involved (objects and their attributes)
- Relationships between these data items
- Constraints on the data and relationships

### Exercise: Instagram Data Model 
- The data items involved (objects and their attributes)
- Relationships between these data items
- Constraints on the data and relationships

## Entity-Relationship (ER) Data Modelling
- Collection of inter-related entities 
- Three major modelling constructs: 
  - **Attribute**: data item describing a property of interest 
  - **Entity**: collection of attributes describing object of interest
  - **Relationship**: association between entities (objects)
- Consists of:
  - collection of entity set definitions
  - collection of relationship set definitions
  - attributes associated with entity/relationship sets
  - connections between entity and relationship sets

! [er-model](/Personal%20Projects/personal-notes/comp3311/lectures/er-model.png)

**Relationship**: an association among several entities 
  - Customer (9876) is the owner of Account (12345)

**Relationship set**: collection of relationships of the same type 
**Degree**: # entities involved in relo 
**Cardinality**: $ associated entities on each side of the relo 
**Participation**: must every entity being in the relo?

! [participation](/Personal%20Projects/personal-notes/comp3311/lectures/participation.png)

### Relationship Degree
! [degree](/Personal%20Projects/personal-notes/comp3311/lectures/degree.png)


### Relationship Cardinality 
! [participation](/Personal%20Projects/personal-notes/comp3311/lectures/cardinality.png)

### Attribute Notations
! [notations](/Personal%20Projects/personal-notes/comp3311/lectures/notations.png)

### EXERCISE: Relationship Semantics 

! [semantics](/Personal%20Projects/personal-notes/comp3311/lectures/semantics.png)