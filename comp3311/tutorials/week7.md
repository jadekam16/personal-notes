# WEEK 7 TUTORIAL

## Aggregates 
- reduce a collection of values into a single result e.g. count(*), sum(col), avg(col) 
- commonly used with group by --> makes groups out of rows, aggregates will apply per group, rather than entire table

Pseudocode:
```
state = initial state
for each item T {
  state = updateState(State, T)
}
return makeFinal(state)
```

- Standard SQL doesn't have user-defined aggregates but PostgreSQL does.
```
CREATE AGGREGATE AggNmae (BaseType) (
  sfunc = UpdateStateFunction,
  stype = StateType,
  initcond = InitialValue,
  finalfunc = MakeFinalFunction
  sortop = OrderingOperator
)
```
stype = determine type of state
initcond = optional, default NULL
sfunc = describes how state updates row by row
finalfunc = defaults to identity func
sortop = optional, mainly used for min/max

Example: string concentation agg
```
in phone
```

TUTORIAL QUESTION 14
- how to compute the mean 
  - record a sum and count, iterate through each value and updating them 
  - then compute it after all the values by sum/count 

-- Step 1: Declare Type of State (stype)
```
create type AvgState as (sum numeric, count integer);
```

-- Step 2: Consider initial state (initcond)
```
initcond = (0, 0)
```

-- Step 3: Make function that iteratively updates the state (sum, count) (sfunc)
```
create or replace function mean_iterator(s AvgState, v numeric)
returns AvgState
as $$
  begin
    -- Do nothing if new value v is null
    if v is not null then
      s.sum := s.sum + v;
      s.count := s.count + 1;
    end if;
    return s;
  end;
$$ language plpgsql
```

-- Step 4: Final State to calculate final result (finalfunc)
```
create or replace function calculate_mean(s AvgState)
returns numeric 
as $$
  begin 
    -- if the count is 0, then return NULL
    if (s.count = 0) then
      return null;
    end if;
    return s.sum::numeric/s.count; 
  end;
$$ language plpgsql
```

-- Step 5: Create aggregate
```
CREATE AGGREGATE mean (numeric) as (
  stype = AvgState,
  initcond = '(0,0)',
  sfunc =  mean_iterator,
  finalfunc = calculate_mean
)
```

## Constraints and Assertions 
- Assertions are schema-level constraints 
  - Usually affects multiple tables 
  - used to assert a condition must always hold true 

Course at UNSW cannot have more than 999 enrolments
```
CREATE ASSERTION ClassSizeConstraint CHECK (condition) (
  not exists (
    select c.id from Course c, Enrolment e 
    where c.id = e.course
    group by c.id 
    having count(e.student) > 999 
  )
)
```

## TRIGGERS 
- lightweight way to implement schema-level constraints (assertions)
- comprised of trigger (when it happens) and a trigger func (what happens)
- event activates trigger, checks cond, if hold procedure executed 
- enforces constraints, rather than checking them 

```
CREATE TRIGGER TriggerName
{AFTER | BEFORE } Event1 [OR Event2 ...] 
ON TableName
FOR EACH {ROW | STATEMENT }
EXECUTE PROCEDURE FunctionName(args...);
```