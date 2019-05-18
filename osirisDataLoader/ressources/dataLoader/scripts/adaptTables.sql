-- clean tables
Truncate table i2b2demodata.patient_dimension;
Truncate table i2b2demodata.patient_mapping;
Truncate table i2b2demodata.visit_dimension;
Truncate table i2b2demodata.encounter_mapping;
Truncate table i2b2demodata.observation_fact;



-- ajout dans patient_dim
-- Alter table i2b2demodata.patient_dimension add column lastnewsdate timestamp without time zone;
-- Alter table i2b2demodata.patient_dimension add column Gender varchar (40);
-- Alter table i2b2demodata.patient_dimension add column Ethnicity varchar (200);
-- Alter table i2b2demodata.patient_dimension add column LastNewsStatus varchar (200);
-- Alter table i2b2demodata.patient_dimension add column ProviderCenterId varchar (200);
-- Alter table i2b2demodata.patient_dimension add column OriginCenterId varchar (200);
-- Alter table i2b2demodata.patient_dimension add column CauseOfDeath varchar (200);
-- Alter table i2b2demodata.patient_dimension add column LastNewsDate timestamp without time zone;
-- Alter table i2b2demodata.patient_dimension add column LastNewsStatus varchar (200);
-- Alter table i2b2demodata.patient_dimension add column BirthDate timestamp without time zone;
-- Alter table i2b2demodata.patient_dimension add column DeathDate timestamp without time zone;

-- ajout dans visit_dim
-- Alter table i2b2demodata.visit_dimension add column Laterality varchar (200);
-- Alter table i2b2demodata.visit_dimension add column HistologicalGradeValue varchar (200);
-- Alter table i2b2demodata.visit_dimension add column StadeValue varchar (200);
-- Alter table i2b2demodata.visit_dimension add column TopographyCode varchar (200);
-- Alter table i2b2demodata.visit_dimension add column MorphologyCode varchar (200);
-- Alter table i2b2demodata.visit_dimension add column HistologicalGradeType varchar (200);
-- Alter table i2b2demodata.visit_dimension add column Type varchar (200);
-- Alter table i2b2demodata.visit_dimension add column DiagnosisDate varchar (200);
-- Alter table i2b2demodata.visit_dimension add column StadeType varchar (200);
-- Alter table i2b2demodata.visit_dimension add column G8 varchar (200);
-- Alter table i2b2demodata.visit_dimension add column PerformanceStatus varchar (200);
-- Alter table i2b2demodata.visit_dimension add column StartDate timestamp without time zone;
