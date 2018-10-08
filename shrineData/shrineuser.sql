insert into PM_USER_DATA
(user_id, full_name, password, changeby_char, status_cd)
values
('shrine', 'SHRINE User', '9117d59a69dc49807671a51f10ab7f', 'i2b2', 'A');
  
-- The password hash you see above is for 'demouser'
 
insert into PM_PROJECT_USER_ROLES
(PROJECT_ID, USER_ID, USER_ROLE_CD, STATUS_CD)
values
('SHRINE', 'shrine', 'USER', 'A');
 
insert into PM_PROJECT_USER_ROLES
(PROJECT_ID, USER_ID, USER_ROLE_CD, STATUS_CD)
values
('SHRINE', 'shrine', 'DATA_OBFSC', 'A');
