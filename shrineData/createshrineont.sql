create user shrine_ont with password 'demouser';
 
create schema authorization shrine_ont;
 
grant all privileges on all tables in schema shrine_ont to shrine_ont;
grant all privileges on all sequences in schema shrine_ont to shrine_ont;
grant all privileges on all functions in schema shrine_ont to shrine_ont;

