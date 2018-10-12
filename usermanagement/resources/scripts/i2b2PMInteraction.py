# -*- coding: utf-8 -*-
"""
Created 2019/010/08

@author: Vianney Jouhet

fonction : Interact with PM Cell (create user, add user to projetc, set user as admin)

"""

import requests


class i2b2_pm_interaction:

    def __init__(self,pm_user,pm_password,pm_domain,pm_host,pm_port,webclient_host,webclient_port) :
        self.xmlPmHeader="""<i2b2:request xmlns:i2b2="http://www.i2b2.org/xsd/hive/msg/1.1/" xmlns:pm="http://www.i2b2.org/xsd/cell/pm/1.1/">
            <message_header>
                       <proxy>
                    <redirect_url>http://"""+pm_host+""":"""+pm_port+"""/i2b2/services/PMService/getServices/getUserAuth</redirect_url>
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
        			<domain>"""+pm_domain+"""</domain>
        			<username>"""+pm_user+"""</username>
        			<password>"""+pm_password+"""</password>
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
                <project_id>"""+pm_domain+"""</project_id>
            </message_header>
            <request_header>
                <result_waittime_ms>100000</result_waittime_ms>
            </request_header>
            """
        # port_str=""
        # if webclient_port!='80' :
        #     port_str = ":"+webclient_port
        self.pm_user=pm_user
        self.pm_url="http://"+webclient_host+":"+webclient_port+"/webclient/index.php"
        print(self.pm_url)

    def post_to_pm(self,data) :
        print('post to pm')
        r=requests.post(self.pm_url,data)
        print(r.status_code, r.reason)
        # print(r.text[:])

    def adduser (self,user_name,password,user_full_name,is_admin,user_email):
        print('adduser ==> ' + user_name)
        xmlSetUser=self.xmlPmHeader+"""
            <message_body>
                <pm:set_user>
                    <user_name>"""+user_name+"""</user_name>
                    <full_name>"""+user_full_name+"""</full_name>
                    <email>"""+user_email+"""</email>
                    <admin>"""+is_admin+"""</admin>
                    <password>"""+password+"""</password>
                </pm:set_user>
            </message_body>
        </i2b2:request>
        """

        self.post_to_pm(xmlSetUser)

    def addrole(self,user_name,role,project_id):
        print('addrole ==>' + user_name)
        xmlSetRole=self.xmlPmHeader+"""
            <message_body>
                <pm:set_role>
                    <user_name>"""+user_name+"""</user_name>
                    <role>"""+role+"""</role>
                    <project_id>"""+project_id+"""</project_id>
                </pm:set_role>
            </message_body>
        </i2b2:request>
        """
        self.post_to_pm(xmlSetRole)

    def setadmin(self,user_name) :
        print('setadmin ==> ' + user_name)
        self.addrole(user_name,"ADMIN","@")

    def deleteuser(self,user_name):
        print('deleteuser ==> ' + user_name)
        xmlDeleteUser=self.xmlPmHeader+"""
            <message_body>
                <pm:delete_user>"""+user_name+"""</pm:delete_user>
            </message_body>
        </i2b2:request>
        """

        self.post_to_pm(xmlDeleteUser)

    def deleteuserrole(self,user_name,role,project_id):
        print('deleteUserRole ==> ' + user_name)
        xmlDeleteUserRole=self.xmlPmHeader+"""
            <message_body>
                <pm:delete_role>
                    <user_name>"""+user_name+"""</user_name>
                    <role>"""+role+"""</role>
                    <project_id>"""+project_id+"""</project_id>
                </pm:delete_role>
            </message_body>
        </i2b2:request>
        """

        self.post_to_pm(xmlDeleteUserRole)

    def setuserparam(self,user_name,param_name,param_type,param_value):
        print('setuserparam ==> ' + user_name + ' - ' + param_name)
        xmlSetUserParam=self.xmlPmHeader+"""
        <message_body>
            <pm:set_user_param>
                <user_name>"""+user_name+"""</user_name>
                <param datatype=" """+param_type+""" " name=" """+param_name+""" ">"""+param_value+"""</param>
                </pm:set_user_param>
        </message_body>
        </i2b2:request>
        """

        self.post_to_pm(xmlSetUserParam)

    def setpassword(self,password):
        print('setpassword ==> ' + self.pm_user)
        xmlSetPassword=self.xmlPmHeader+"""
            <message_body>
                <pm:set_password>"""+password+"""</pm:set_password>
            </message_body>
        </i2b2:request>
        """

        self.post_to_pm(xmlSetPassword)
