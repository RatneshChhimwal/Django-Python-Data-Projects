create database IF NOT EXISTS college;
use college;
show tables;
describe student;
select * from student;
insert into student values (5,"Anita",33),(6,"Ritika",28);

-- WE CAN CHANGE THE ORDER OF VALUES BY DEFINING THE COLUMN NAMES IN THE NEW ORDER BEFORE DATA INSERTION --
insert into student (age,name,id) values (22,"Meghna",7);


-- Creating a new table subjects to later on submit marks in reference for --

create table if not exists subjects (id int primary key, subject_name varchar(100) NOT NULL);

insert into subjects values (1,"maths"),(2,"science"),(3,"english");

select * from subj
ects;


-- Creating a new table marks to store marks for students --

create table if not exists marks 
(student_id int NOT NULL, foreign key (student_id) references student(id) ON DELETE CASCADE ON UPDATE CASCADE, 
subject_id int NOT NULL,foreign key (subject_id) references subjects(id) ON DELETE CASCADE ON UPDATE CASCADE, 
subject varchar(100), marks int default 33);

select * from marks;

alter table marks drop column subject;

insert into marks (student_id, subject_id, marks) values (1,1,78),(2,1,54),(1,3,98),(3,1,43),(2,2,76),(1,2,56),(2,3,21),(3,2,64),(3,3,24);

select * from marks;

-- Quering marks greater than 50 for each student along with subject name using left join on all 3 tables (student, subjects, marks)

select st.id, st.name, st.age, m.marks, m.subject_id, sb.subject_name 
from student st inner join marks m 
on st.id = m.student_id 
inner join subjects sb 
on m.subject_id = sb.id 
where m.marks > 50;

-- QUERING STUDENTS USING 'LIKE'  and 'NOT EQUAL TO' OPERATORS --

select * from student where name like "%esh" AND age != 30;

-- QUERING STUDENT MARKS IN DESCENDING ORDER AND FINDING OUT THE TOP 3 MARKS --

select st.id, st.name, m.subject_id, m.marks from student st left join marks m on st.id = m.student_id order by m.marks desc limit 3;

-- ALTERING TABLE STUDENT TO ADD A NEW COLUMN 'CITY' --

alter table student add column (city varchar(50) NOT NULL);

-- QUERING 'city' AND 'count of students present in those city' WHILE ALSO USING 'having' OPERATOR --

select city, count(id) from student group by city having count(id) > 1 order by city;

-- UPDATE QUERIES --

update student set age = 25 where name = "Nitesh";
select * from student;

update marks set marks = marks+1;
select * from marks;

-- LEFT JOIN --

select st.id, st.name, st.age, st.city, m.marks, m.subject_id, sb.subject_name 
from student st left join marks m on st.id = m.student_id 
left join subjects sb on m.subject_id = sb.id;

alter table student add column (desk_partner varchar(50) UNIQUE);
select * from student;
alter table student modify desk_partner int UNIQUE;
describe student;

update student set desk_partner = "3" where id = 1;
update student set desk_partner = "6" where id = 2;
update student set desk_partner = "7" where id = 4;

select * from student;

-- SELF JOIN --

select a.id, a.name, a.age, a.city, a.desk_partner, b.name as desk_partner_name from student a JOIN student b on a.desk_partner = b.id;

-- SUB-QUERY --

select st.id, st.name, m.marks 
from student st left join marks m 
ON st.id = m.student_id 
where 
m.marks > (select AVG(marks) from marks);

-- ANOTHER SUB-QUERY --

SELECT st.id, st.name, m.marks
FROM student st 
JOIN marks m ON st.id = m.student_id
WHERE m.marks = (
    SELECT MAX(marks)
    FROM student st 
    JOIN marks m ON st.id = m.student_id 
    WHERE st.city = 'Delhi'
);




