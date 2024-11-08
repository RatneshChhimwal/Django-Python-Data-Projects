use abcd;
Select * from investors;
select * from partners;
Select * from share_holders;

select * from partners inner join share_holders where partner_id=holder_id;

SELECT city, COUNT(*) AS city_count
FROM partners
GROUP BY city;


create table EMPLOYEE (Ecode int, Name varchar(30), Designation varchar(20), S_Grade varchar(10), DOB date, DOJ date);

insert into EMPLOYEE values (101, 'Vikrant', 'Executive', 'S03', '2003-03-23', '1980-01-13'),
(102, 'Ravi', 'Head-IT', 'S02', '2010-02-12', '1987-07-22'),
(103, 'John Cena', 'Receptionist', 'S03', '2009-06-24', '1983-02-24'),
(105, 'Azhar Ansari', 'GM', 'S02', '2009-08-11', '1984-03-03'),
(108, 'Priyam Sen', 'CEO', 'S01', '2004-12-29', '1982-01-19');

SELECT 
    Ecode, Name, Designation, S_Grade, DOB, DOJ,
    COUNT(*) as duplicate_count
FROM EMPLOYEE
GROUP BY Ecode, Name, Designation, S_Grade, DOB, DOJ
HAVING COUNT(*) > 1;


-- TO DELETE DUPLICATE ENTRIES IN CASE WE RUN THE INSERT INTO EMPLOYEE TABLE QUERY MULTIPLE TIMES --

SET SQL_SAFE_UPDATES = 0;

WITH CTE AS (
    SELECT 
        *, 
        ROW_NUMBER() OVER (
            PARTITION BY Ecode, Name, Designation, S_Grade, DOB, DOJ 
            ORDER BY Ecode
        ) AS row_num
    FROM EMPLOYEE
)
DELETE FROM EMPLOYEE
WHERE Ecode IN (
    SELECT Ecode FROM CTE WHERE row_num > 1
);

-- END --

Select * from EMPLOYEE;

create table SALGRADE (S_Grade varchar(10), Salary int, HRA int);

insert into SALGRADE values ('S01', 56000, 18000), ('S02', 32000, 12000), ('S03', 24000, 8000);

Select * from SALGRADE;


select * from EMPLOYEE order by DOJ desc;
select Name, Designation from EMPLOYEE where S_Grade in ('S02', 'S03');
select Name, Designation, S_grade from EMPLOYEE where DOJ like '2009-%';
Select S_Grade, salary*12 as Annual_salary from SALGRADE;
Select S_Grade, count(*) from EMPLOYEE group by S_Grade;
Select E.Name, E.Designation, S.Salary, S.HRA from SALGRADE S left join EMPLOYEE E on S.S_Grade = E.S_Grade where S.Salary <=50000;
Select min(DOJ), max(DOB) from EMPLOYEE;
