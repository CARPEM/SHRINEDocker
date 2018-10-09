/* Audit db tables in adapterAuditDB */
create table `queriesReceived` (`shrineNodeId` TEXT NOT NULL,`userName` TEXT NOT NULL,`networkQueryId` BIGINT NOT NULL,`queryName` TEXT NOT NULL,`topicId` TEXT,`topicName` TEXT,`timeQuerySent` BIGINT NOT NULL,`timeReceived` BIGINT NOT NULL);
create table `executionsStarted` (`networkQueryId` BIGINT NOT NULL,`queryName` TEXT NOT NULL,`timeExecutionStarted` BIGINT NOT NULL);
create table `executionsCompleted` (`networkQueryId` BIGINT NOT NULL,`replyId` BIGINT NOT NULL,`queryName` TEXT NOT NULL,`timeExecutionCompleted` BIGINT NOT NULL);
create table `resultsSent` (`networkQueryId` BIGINT NOT NULL,`replyId` BIGINT NOT NULL,`queryName` TEXT NOT NULL,`timeResultsSent` BIGINT NOT NULL);

