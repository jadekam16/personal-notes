# Week 4 Tutorial

## SET UP 
when in psql db, type \i filemame to import file (insert tables and data)

## SQL DDP Recap

```
CREATE TABLE name AS (
  attr1 domain1 constraint1
  attr2 domain2 constraint2
)
```

INSERTION 
```
INSERT INTO Table VALUES (1, 'data', ...) 
```

```
INSERT INTO Table(Attr1, Attr2,...) VALUES(1, 'data', ...) 
```

Constraints and Domains 
- varchar(int), char(int), date
- restrict the domain: check (salary > 100)
- PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE, NOT NULL, DEFAULT 

UPDATE
```
UPDATE TableName
SET Attribute = NewAttribute 
WHERR condition; 
```

**NOTE: USE SINGLE QUOTES FOR STRINGS** 
**NICKNAMES FROM TABLES => ... from parts p** 
**duplicates => ..... select  distinct c.sid** 

ALTERING TABLES 
```
ALTER TABLE Relation Modifications

i.e., 

ALTER TABLE Bars
  ADD phone char(10) DEFAULT 'Unlisted'; --> sets value for this attribute to Unlisted.
```

DELETION
```
DELETE FROM TableName WHERE condition;
DROP TABLE TableName;
```

There are three ways to handle the deletion:
  - Disallow the delete (default behaviour)
  - Delete all things that refer to it (ON DELETE CASCADE)
  - Set removed ID's to some default value (ON DELETE NULL or given default ON DELETE DEFAULT)

QUERIES
```
SELECT attribute(s)(all*)
FROM TableName
WHERE condition

GROUP BY grouping attributes
HAVING groupingConditions
ORDER BY orderingAtts
```

Order of execution: from, where, group by, having, select, order by, limit

VIEWS
```
CREATE (OR REPLACE) VIEW ViewName AS Query;
CREATE (OR REPLACE) VIEW ViewName(AttributeNames) AS QUERY; --> attribute names renames the columns
DROP VIEW (ViewName);
```

JOINS 
joins tables tgt

```
SELECT attribute(s)
FROM Table1
JOIN Table2 ON JoinCondition
WHERE condition
```
## INTERACT WITH DB

```
\d finds all tables
\d table find specific table 
select * from table; finds all columns of the table
```

## Tutorial Qs 
https://cgi.cse.unsw.edu.au/~cs3311/24T2/tutes/week04/index.php

Does the order of table declarations above matter?
- yes: departments has a foreign key that references manager which has a reference key that references employee tables. 

A new government initiative to get more young people into work cuts the salary levels of all workers under 25 by 20%. Write an SQL statement to implement this policy change.

```
UPDATE Employees
SET salary = salary * 0.8
WHERE age < 25;
```

The company has several years of growth and high profits, and considers that the Sales department is primarily responsible for this. Write an SQL statement to give all employees in the Sales department a 10% pay rise.

Add a constraint to the CREATE TABLE statements above to ensure that every department must have a manager.
```
...
manager integer not null
...
foreign key (manager) references Employees(eid) --> use this syntax for foreign keys 
```

Add a constraint to the CREATE TABLE statements above to ensure that no-one is paid less than the minimum wage of $15,000.
```
...
salary real check(salary >= 15000)
```

Add a constraint to the CREATE TABLE statements above to ensure that no employee can be committed for more than 100% of his/her time. Note that the SQL standard allows queries to be used in constraints, even though DBMSs don't implement this (for performance reasons).

Add a constraint to the CREATE TABLE statements above to ensure that a manager works 100% of the time in the department that he/she manages. Note that the SQL standard allows queries to be used in constraints, even though DBMSs don't implement this (for performance reasons).

When an employee is removed from the database, it makes sense to also delete all of the records that show which departments he/she works for. Modify the CREATE TABLE statements above to ensure that this occurs.

When a manager leaves the company, there may be a period before a new manager is appointed for a department. Modify the CREATE TABLE statements above to allow for this.

Consider the deletion of a department from a database based on this schema. What are the options for dealing with referential integrity between Departments and WorksIn? For each option, describe the required behaviour in SQL.

For each of the possible cases in the previous question, show how deletion of the Engineering department would affect the following database:

