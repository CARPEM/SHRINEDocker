insert into PM_USER_DATA
(user_id, full_name, password, status_cd)
values
('shrine_steward', 'SHRINE Data Steward User', '5f4dcc3b5aa765d61d8327deb882cf99', 'A');
  
-- The password hash you see above is for 'password'
 
insert into PM_PROJECT_USER_ROLES
(PROJECT_ID, USER_ID, USER_ROLE_CD, STATUS_CD)
values
('SHRINE', 'shrine_steward', 'USER', 'A');
 
insert into PM_PROJECT_USER_ROLES
(PROJECT_ID, USER_ID, USER_ROLE_CD, STATUS_CD)
values
('SHRINE', 'shrine_steward', 'DATA_OBFSC', 'A');
 
insert into PM_USER_PARAMS
(DATATYPE_CD, USER_ID, PARAM_NAME_CD, VALUE, CHANGEBY_CHAR, STATUS_CD)
values
('T', 'shrine_steward', 'DataSteward', 'true', 'i2b2', 'A');
