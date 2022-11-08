-- Write your T-SQL query statement below
-- https://leetcode.com/problems/department-top-three-salaries/discuss/797620/Three-solutions%3A-window-function-subquery-and-Join
-- better ans

SELECT Department.name as Department, 
    Employee.name as Employee,
    Employee.Salary
from (
SELECT MAX(Salary) as Salary, departmentId
    FROM Employee outEP
    Where Salary in (
        SELECT MAX(Salary) FROM Employee inEP
        Where inEP.departmentId = outEP.departmentId 
    )
    group by departmentId
UNION ALL 
SELECT MAX(Salary) as Salary, departmentId
    FROM Employee outEP
    Where Salary not in (
        SELECT MAX(Salary) FROM Employee inEP
        Where inEP.departmentId = outEP.departmentId 
    )
    group by departmentId
UNION ALL 

select MAX(Salary) , departmentId from (
    SELECT Salary , departmentId
    from Employee
    except
    select Salary , departmentId from (
    SELECT MAX(Salary) as Salary, departmentId
        FROM Employee outEP
        Where Salary in (
            SELECT MAX(Salary) FROM Employee inEP
            Where inEP.departmentId = outEP.departmentId 
        )
        group by departmentId
    UNION ALL 
    SELECT MAX(Salary) as Salary, departmentId
        FROM Employee outEP
        Where Salary not in (
            SELECT MAX(Salary) FROM Employee inEP
            Where inEP.departmentId = outEP.departmentId 
        )
        group by departmentId
    ) as tb_A
) as tb_B
group by departmentId
) as EP
LEFT JOIN Employee on EP.salary = Employee.salary and EP.departmentId = Employee.departmentId
LEFT JOIN Department on Department.id = EP.departmentId
