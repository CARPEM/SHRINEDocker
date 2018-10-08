create table `queriesSent` (`shrineNodeId` TEXT NOT NULL,`userName` TEXT NOT NULL,`networkQueryId` BIGINT NOT NULL,`queryName` TEXT NOT NULL,`queryTopicId` TEXT,`queryTopicName` TEXT,`timeQuerySent` BIGINT NOT NULL);
create table `previousQueries` (`networkId` BIGINT NOT NULL,`userName` TEXT NOT NULL,`domain` TEXT NOT NULL,`queryName` TEXT NOT NULL,`expression` TEXT,`dateCreated` BIGINT NOT NULL,`deleted` BOOLEAN NOT NULL,`queryXml` TEXT NOT NULL,`changeDate` BIGINT NOT NULL);
create table `queryFlags` (`networkId` BIGINT NOT NULL,`flagged` BOOLEAN NOT NULL,`flagMessage` TEXT NOT NULL,`changeDate` BIGINT NOT NULL);
create table `queryResults` (`resultId` BIGINT NOT NULL,`networkQueryId` BIGINT NOT NULL,`instanceId` BIGINT NOT NULL,`adapterNode` TEXT NOT NULL,`resultType` TEXT,`size` BIGINT NOT NULL,`startDate` BIGINT,`endDate` BIGINT,`status` TEXT NOT NULL,`statusMessage` TEXT,`changeDate` BIGINT NOT NULL);
create table `queryBreakdownResults` (`networkQueryId` BIGINT NOT NULL,`adapterNode` TEXT NOT NULL,`resultId` BIGINT NOT NULL,`resultType` TEXT NOT NULL,`dataKey` TEXT NOT NULL,`value` BIGINT NOT NULL,`changeDate` BIGINT NOT NULL);
create table `queryResultProblemDigests` (`networkQueryId` BIGINT NOT NULL,`adapterNode` TEXT NOT NULL,`codec` TEXT NOT NULL,`stamp` TEXT NOT NULL,`summary` TEXT NOT NULL,`description` TEXT NOT NULL,`details` TEXT NOT NULL,`changeDate` BIGINT NOT NULL);

create index queryResultsChangeDateIndex on queryResults (changeDate);
create index queryResultsNetworkQueryIdIndex on queryResults (networkQueryId);
create index queryResultsAdapterNodeIndex on queryResults (adapterNode(255));

create index queryBreakdownResultsChangeDateIndex on queryBreakdownResults (changeDate);
create index queryBreakdownResultsNetworkQueryIdIndex on queryBreakdownResults (networkQueryId);
create index queryBreakdownResultsAdapterNodeIndex on queryBreakdownResults (adapterNode(255));

create index queryFlagsChangeDateIndex on queryFlags (changeDate);
create index queryFlagsNetworkQueryIdIndex on queryFlags (networkId);
