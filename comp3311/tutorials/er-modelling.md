# Week 2 Tutorial Notes 

## ER Diagrams 
- Entity?sets : Objects denoted by a rectangle 
- Attributes: properties of entities: denoted by ovals
- Relationship?sets: describes how entities are linked together: denoted by diamonds.
- Unique attribute: primary key --> underlined 

## Relationships:
- relos can have attributes too 
- degree: # of entities associated with the relationship (usually 2)
- cardinality: describes how many entity instances a different entity instance can have a relo with 
  - many-to-many, one-to-many, or one-to-one
  - arrow pointing to entity - MAX ONE.  
- participation: determine if all instances of entitt need to be in relo or not 
  - bold: total - must have 1 or more instances 
  - otherwise: partial -- some instances do not have to have a relo instance (0 or more)

Requirements --> ER MODEL --> Relationshuip Model --> SQL

## Subclasses and Inheritance 
- subset of its superclass --> inherits all superclass attributes + may have their own specific attributes. 
  - use the "isa" notation 
- overlapping (o) --> superclass can be multiple classes at once
- disjoint (d) --> only be at most one subclass 
- total participation (bold) mean every instance in the entity must be at least one subclass --> partial means some do not have to be in a subclass.

## Weak Entities 
- only exist cos of an association with strong entities --> if strong entity is removed, no reason to exist. 
- dont directly have primary key --> use the key of strong entity (becomes a foreign key). 
- denoted by double boxes rather than one box --> relationship between weak and strong is denoted by double diamonds. 

