#!/bin/bash

echo 'checking if shrine is deployed ...'

dep=$(cat /opt/shrine/deployed)
cat deployed
echo $dep
if [ "$dep" = "false" ]; then
echo 'deploying shrine app'
  cd /opt/shrine/tomcat
  ./build_shrine.sh
  echo 'shrine deployed'
  cd /opt/shrine
else
  echo 'Already deployed true'
fi




/opt/shrine/tomcat/bin/catalina.sh run
