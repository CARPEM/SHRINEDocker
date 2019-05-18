select distinct modifier_cd, '' as name_char from i2b2demodata.modifier_dimension where sourcesystem_cd = 'TEST_OSIRIS' and modifier_cd like '%|%';
