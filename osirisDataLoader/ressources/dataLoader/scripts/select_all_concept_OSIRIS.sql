select distinct concept_cd, name_char from i2b2demodata.concept_dimension where sourcesystem_cd = 'TEST_OSIRIS' and concept_cd like '%|%';
