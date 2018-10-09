#!/bin/bash
echo 'checking if webserver is deployed ...'

dep=$(cat deployed)
cat deployed
echo $dep
if [ "$dep" = "false" ]; then
echo 'deploying i2b2 app'
 ./parametrage.sh
echo 'i2b2 deployed'
else
  echo 'Already deployed true'
fi

apachectl -D FOREGROUND
