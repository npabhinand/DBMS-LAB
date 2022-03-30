create database university;
use university;
create table student(name varchar(20),student_number int primary key,class int,major varchar(10));
create table course(course_name varchar(20),course_number varchar(20),Credit_hour int,department varchar(20));
alter table course modify column course_number varchar(20) primary key;
create table section(section_identifier varchar(20) primary key,course_number varchar(20),semester varchar(20),year int,instructor varchar(20));
use university;
alter table section add foreign key(course_number) references course(course_number);
