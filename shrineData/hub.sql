create table HUB_QUERY (
	NETWORK_QUERY_ID bigint not null,
    DOMAIN varchar(256) not null,
    USERNAME varchar(256) not null,
    CREATE_DATE timestamp not null default current_timestamp,
    QUERY_DEFINITION text not null,
	constraint hub_query_id_pk primary key(NETWORK_QUERY_ID),
    index ix_HUB_QUERY_username_domain (username, domain)
) engine=innodb default charset=latin1;

create table HUB_QUERY_RESULT (
	ID int not null auto_increment,
    NETWORK_QUERY_ID bigint not null,
    NODE_NAME varchar(255) not null,
    CREATE_DATE timestamp not null default current_timestamp,
    STATUS varchar(255) not null,
	constraint hub_query_result_id_pk primary key(ID),
	index ix_HUB_QUERY_RESULT_network_query_id (NETWORK_QUERY_ID),
	index ix_HUB_QUERY_RESULT_network_query_id_node_name (NETWORK_QUERY_ID, NODE_NAME)
) engine=innodb default charset=latin1;

