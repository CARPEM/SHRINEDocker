/* Working tables in shrine_query_history */
create table `problems` (`id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,`codec` TEXT NOT NULL,`stampText` TEXT NOT NULL,`summary` TEXT NOT NULL,`description` TEXT NOT NULL,`detailsXml` TEXT NOT NULL,`epoch` BIGINT NOT NULL);
create index `idx_epoch` on `problems` (`epoch`);

create table SHRINE_QUERY(
  id int not null auto_increment,
  local_id varchar(255) not null,
  network_id bigint not null,
  username varchar(255) not null,
  domain varchar(255) not null,
  query_name varchar(255) not null,
  query_expression text,
  date_created timestamp default current_timestamp,
  has_been_run boolean not null default 0,
  flagged boolean not null default 0,
  flag_message varchar(255) null,
  constraint query_id_pk primary key(id),
  index ix_SHRINE_QUERY_network_id (network_id),
  index ix_SHRINE_QUERY_local_id (local_id),
  index ix_SHRINE_QUERY_username_domain (username, domain),
  query_xml text
) engine=innodb default charset=latin1;
alter table SHRINE_QUERY change flag_message flag_message text;

create table QUERY_RESULT(
  id int not null auto_increment,
  local_id varchar(255) not null,
  query_id int not null,
  type enum('PATIENTSET','PATIENT_COUNT_XML','PATIENT_AGE_COUNT_XML','PATIENT_RACE_COUNT_XML','PATIENT_VITALSTATUS_COUNT_XML','PATIENT_GENDER_COUNT_XML','ERROR') not null,
  status enum('FINISHED', 'ERROR', 'PROCESSING', 'QUEUED') not null,
  time_elapsed int null,
  last_updated timestamp default current_timestamp,
  constraint QUERY_RESULT_id_pk primary key(id),
  constraint fk_QUERY_RESULT_query_id foreign key (query_id) references SHRINE_QUERY (id) on delete cascade
) engine=innodb default charset=latin1;

create table ERROR_RESULT(
  id int not null auto_increment,
  result_id int not null,
  message varchar(255) not null,
  CODEC varchar(256) not null default "Pre-1.20 Error",
  STAMP varchar(256) not null default "Unknown time and machine",
  SUMMARY text not null,
  PROBLEM_DESCRIPTION text not null,
  DETAILS text not null,
  constraint ERROR_RESULT_id_pk primary key(id),
  constraint fk_ERROR_RESULT_QUERY_RESULT_id foreign key (result_id) references QUERY_RESULT (id) on delete cascade
) engine=innodb default charset=latin1;


create table COUNT_RESULT(
  id int not null auto_increment,
  result_id int not null,
  original_count int not null,
  obfuscated_count int not null,
  date_created timestamp default current_timestamp,
  constraint COUNT_RESULT_id_pk primary key(id),
  constraint fk_COUNT_RESULT_QUERY_RESULT_id foreign key (result_id) references QUERY_RESULT (id) on delete cascade
) engine=innodb default charset=latin1;

create table BREAKDOWN_RESULT(
  id int not null auto_increment,
  result_id int not null,
  data_key varchar(255) not null,
  original_value int not null,
  obfuscated_value int not null,
  constraint BREAKDOWN_RESULT_id_pk primary key(id),
  constraint fk_BREAKDOWN_RESULT_QUERY_RESULT_id foreign key (result_id) references QUERY_RESULT (id) on delete cascade
) engine=innodb default charset=latin1;

create table PRIVILEGED_USER(
  id int not null auto_increment,
  username varchar(255) not null,
  domain varchar(255) not null,
  threshold int null, #Used to be not null. See SHRINE-1262
  override_date timestamp null,
  constraint priviliged_user_pk primary key(id),
  constraint ix_PRIVILEGED_USER_username_domain unique (username, domain)
) engine=innodb default charset=latin1;

CREATE TABLE `AUDIT_ENTRY` (
  `AUDIT_ENTRY_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PROJECT` varchar(254) NOT NULL,
  `USERNAME` varchar(254) NOT NULL,
  `DOMAIN_NAME` varchar(254) NOT NULL,
  `TIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `QUERY_TEXT` text,
  `QUERY_TOPIC` varchar(245) DEFAULT NULL,
  PRIMARY KEY (`AUDIT_ENTRY_ID`),
  KEY `IDX_AUDIT_ENTRY_DOMAIN_USERNAME_QUERY_TOPIC` (`DOMAIN_NAME`,`USERNAME`,`QUERY_TOPIC`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;