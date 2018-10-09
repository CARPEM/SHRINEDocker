# -*- coding: utf-8 -*-
"""
Created on 04/10/2018

@author: vianney jouhet
"""

import requests
from xml.etree.ElementTree import XML
from lxml import etree

xmlPmHeader="""<i2b2:request xmlns:i2b2="http://www.i2b2.org/xsd/hive/msg/1.1/" xmlns:pm="http://www.i2b2.org/xsd/cell/pm/1.1/">
    <message_header>
               <proxy>
            <redirect_url>http://i2b2app:8080/i2b2/services/PMService/getServices/getUserAuth</redirect_url>
        </proxy>
        <i2b2_version_compatible>1.1</i2b2_version_compatible>
        <hl7_version_compatible>2.4</hl7_version_compatible>
        <sending_application>
            <application_name>i2b2 Project Management</application_name>
            <application_version> 1.10 </application_version>
        </sending_application>
        <sending_facility>
            <facility_name>i2b2 Hive</facility_name>
        </sending_facility>
        <receiving_application>
            <application_name>Project Management Cell</application_name>
            <application_version> 1.10 </application_version>
        </receiving_application>
        <receiving_facility>
            <facility_name>i2b2 Hive</facility_name>
        </receiving_facility>
        <datetime_of_message></datetime_of_message>
		<security>
			<domain>i2b2demo</domain>
			<username>i2b2</username>
			<password>demouser</password>
		</security>
        <message_control_id>
            <message_num>11223453</message_num>
            <instance_num>0</instance_num>
        </message_control_id>
        <processing_id>
            <processing_id>P</processing_id>
            <processing_mode>I</processing_mode>
        </processing_id>
        <accept_acknowledgement_type>AL</accept_acknowledgement_type>
        <application_acknowledgement_type>AL</application_acknowledgement_type>
        <country_code>US</country_code>
        <project_id>i2b2demo</project_id>
    </message_header>
    <request_header>
        <result_waittime_ms>100000</result_waittime_ms>
    </request_header>
    """
xmlAuth =xmlPmHeader+"""
    <message_body>
        <pm:get_user_configuration>
            <project>i2b2demo</project>
        </pm:get_user_configuration>
    </message_body>
</i2b2:request>
"""

r = requests.post("http://localhost/webclient/index.php", data=xmlAuth)
print(r.status_code, r.reason)
# print(r.content)
response=etree.fromstring(r.content)
ns={"ns2":"http://www.i2b2.org/xsd/hive/msg/1.1/",
    "ns4":"http://www.i2b2.org/xsd/cell/pm/1.1/",
    "ns3":"http://www.i2b2.org/xsd/hive/msg/version/"}

for tokens in response.findall("./message_body/ns4:configure/user/password",ns) :
    token=tokens.text

xmlSetUser=xmlPmHeader+"""
    <message_body>
        <pm:set_user>
            <user_name>vj</user_name>
            <full_name>Vianney test</full_name>
            <email>mikem@i2b2.org</email>
            <admin>true</admin>
            <password>heyho</password>
        </pm:set_user>
    </message_body>
</i2b2:request>
"""


r = requests.post("http://localhost/webclient/index.php", data=xmlSetUser)
print(r.status_code, r.reason)
print(r.text[:])

xmlSetRole=xmlPmHeader+"""
    <message_body>
        <pm:set_role>
            <user_name>vj</user_name>
            <role>ADMIN</role>
            <project_id>@</project_id>
        </pm:set_role>
    </message_body>
</i2b2:request>
"""

r = requests.post("http://localhost/webclient/index.php", data=xmlSetRole)
print(r.status_code, r.reason)
print(r.text[:])

xmlSetRole=xmlPmHeader+"""
    <message_body>
        <pm:delete_user>mikem</pm:delete_user>
    </message_body>
