insert into PM_USER_DATA
(user_id, full_name, password, changeby_char, status_cd)
values
('qep', 'SHRINE QEP User', '5f4dcc3b5aa765d61d8327deb882cf99', 'i2b2', 'A');
  
-- The password hash you see above is for 'password'
 
insert into PM_PROJECT_USER_ROLES
(PROJECT_ID, USER_ID, USER_ROLE_CD, STATUS_CD)
values
('SHRINE', 'qep', 'USER', 'A');
 
insert into PM_PROJECT_USER_ROLES
(PROJECT_ID, USER_ID, USER_ROLE_CD, STATUS_CD)
values
('SHRINE', 'qep', 'DATA_OBFSC', 'A');
 
insert into PM_USER_PARAMS
(DATATYPE_CD, USER_ID, PARAM_NAME_CD, VALUE, CHANGEBY_CHAR, STATUS_CD)
values
('T', 'qep', 'qep', 'true', 'i2b2', 'A');
