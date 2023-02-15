create table student(
    id int,
    name text,
    intake int,
    dept text
)partition by list(dept);
create table dept1 partition of student
    for values in ('cse');
create table dept2 partition of student
    for values in ('eee');
create table dept3 partition of student
    for values in ('bba');
