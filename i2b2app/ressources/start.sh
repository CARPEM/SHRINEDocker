#!/bin/bash
echo 'checking if i2b2 is deployed ...'

dep=$(cat /opt/deploy/deployed)
cat deployed
echo $dep
if [ "$dep" = "false" ]; then
echo 'deploying i2b2 app'
  sh parametrage.sh
echo 'i2b2 deployed'
else
  echo 'Already deployed true'
fi

/opt/jboss/wildfly/bin/standalone.sh -b 0.0.0.0
