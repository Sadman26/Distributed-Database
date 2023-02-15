create table person(
    age int,
    name text,
    city text,
    status text
)partition by range(age);
create table Kid_table partition of person
    for values from (0) to (17);
create table Adult_table partition of person
    for values from (18) to (100);