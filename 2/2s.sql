select * from countries;
select email,phone_number from employees;
select * from employees where last_name='fay';
select employee_id,hire_date from employees where last_name='Grant'or last_name='Whalen';
use company;
select first_name from employees where job_id=(select job_id from jobs where job_title='Shipping Clerk');
select * from employees where department_id=8;
select * from departments order by department_id desc;
select * from employees where last_name like 'k%';
select first_name,last_name,hire_date from employees where hire_date between 1995 and 1997 order by hire_date asc;
select * from jobs where max_salary<5000;
select lower(email) from employees;
select first_name,last_name from employees where hire_date like '1995%'; 
insert into employees(employee_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id)values('42','paul','newton','newton@gmail.com','904840','1995-10-10',15,25000,101,11);
set sql_safe_updates=0;
set sql_foreign_key_checks=0;
delete from departments where department_name='shipping';
set sql_safe_updates=1;
set sql_foreign_key_checks=1;
select * from departments;
