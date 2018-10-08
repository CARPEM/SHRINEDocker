# Pre-requisites
Folowing commands must executed by a user within the sudoer

## Install Docker
[installation guide](https://docs.docker.com/v17.12/install/)

## Install docker-compose
[Installation guide](https://docs.docker.com/compose/install/)

## Clone the project
```bash
git clone <url-repository>
```
# Setup config file
## copy secrets.template to secrets.txt
The secrets file will contain all credentials and sensitive data. This file should be readalble only by user that are able to run docker containers from the host machine (root, sudoers, docker group). This file can be encrypted or suppressed as soon as the application is up and running. However il will remain necessary to provide this file each time you will restart the application.

From dockeri2b2 root directory
```bash
cp secrets.template secrets.txt
```

## Adapt parameters within the set_env.sh
Edit secrets.txt and modify parameters :

* **SHRINE_HUB_HOST and SHRINE_HUB_PORT** should be adressed to you by the HUB administrator
* **SHRINE_HOST and SHRINE_PORT** corresponds to the publicly accessible IP for your shrine node.
IS_HUB should be set to false

For testing purpose it is possible to leave other parameters. However it is higly recommanded to modifiy every login and passwords in order to secure the app.

## Build and start the APP
From the root directory of the project
```bash
sudo docker-compose up
```

## Setup database and load data

### Load demo data (i2b2)
Open another bash
```bash
./setDemoData.sh
```

### Load demo data (shrine)
Afer i2b2 demo data are loaded
```bash
./setShrineData.sh
```

## Restart the APP (optionnal)
If you want to test shrine and i2b2 at this step you must restart the app
From the bash where APP is running
```bash
CTRL+C
sudo docker-compose up
```
go to i2b2 ==> http://your_hostname/webclient

go to shrine ==> https://your_shrine_hostname:6443/shrine-webclient

## Manage certificates

### Retrieve https certificate and csr
These files have been exported (on the host) in :
```bash
shrine/cert/${SHRINE_HOST}_HTTPS.cer
shrine/cert/$SHRINE_HOST.csr
```
### Send the files to the Hub administrator
The hub administrator will send you back:

*	His own certificate (shrine-hub-ca.crt)
* Your signed certificate (your hostname-signed.crt)

### Import the hub certificate and your signed certificate

* Put the hub certificate (shrine-hub-ca.crt) in the shrine/cert/ directory of the project.
* Put your signed (<your_hostname>-signed.crt) certificate in the shrine/cert/ directory of the project.

Execute the following command
```bash
sudo docker exec -it dockeri2b2_shrine_1 /bin/bash
```
```bash
./import-cert.sh
```
```bash
exit
```
## Restart the APP
From the bash where APP is running
```bash
CTRL+C
sudo docker-compose up
```

## It should work !!!!
