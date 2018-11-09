-- Querying Data
select  c_name, 'patient_dimension' as c_tablename,
        c_columndatatype,c_basecode

from i2b2metadata.osiris t
where sourcesystem_cd = 'TEST_OSIRIS' and c_fullname like ('\\i2b2\\OSIRIS\\patient%')
    union
select  c_name, 'visit_dimension' as c_tablename,
        c_columndatatype,c_basecode
from i2b2metadata.osiris t
where sourcesystem_cd = 'TEST_OSIRIS' and c_fullname like ('\\i2b2\\OSIRIS\\tumorPathologyEvent%');
