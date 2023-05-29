drop schema if exists sharp_sight;
create schema sharp_sight;

use sharp_sight;

drop table if exists users;
create table users(
	id_user int primary key auto_increment unique,
    name_user varchar(50) not null default 'Not Name',
    last_name_user varchar(50) not null default 'Not Last Name',
    email_user varchar(70) not null unique default 'notMail@email.com',
    password_user varchar(254) not null
);

#insert into users (name_user, last_name_user, email_user, password_user) values ('Prueba','Prueba','Prueba','Prueba');

#select * from users where name_user='' and last_name_user='' and email_user='' and password_user='';

#select password_user from users where email_user='Prueba';