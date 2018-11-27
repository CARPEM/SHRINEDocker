# Purpose and context
This project aims to automate the deployment of an i2b2 - shrine application.

Please visit [i2b2](https://www.i2b2.org/) and [SHRINE](https://open.med.harvard.edu/wiki/display/SHRINE) websites for more informations.

The installation process is mainly based on the [i2b2 installation guide](https://community.i2b2.org/wiki/display/getstarted/i2b2+Installation+Guide) and [shrine installation guide](https://open.med.harvard.edu/wiki/display/SHRINE/Installation)  and follows all the steps described within these documents.

You can see the [architecture](https://github.com/CARPEM/SHRINEDocker/wiki/Architecture) of the default built application (ports and hotname generated locally on the HOST machine) when set up within a private network and connecting to an external hub.

# Pre-requisites
Folowing commands must executed by a user within the sudoer group

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

## Adapt parameters within the secret.txt file
Edit secrets.txt and modify parameters :

* **SHRINE_HUB_HOST and SHRINE_HUB_PORT** should be provided to you by the HUB administrator
* **SHRINE_HOST and SHRINE_PORT** corresponds to the publicly accessible hostname for your shrine node.
* IS_HUB should be set to false

For testing purpose it is possible to leave other parameters. However it is highly recommanded to modifiy every login and passwords in order to secure the app.

**Remarque:** If your are behind an https reverse proxy read this [page](https://github.com/CARPEM/SHRINEDocker/wiki/HTTPS-reverse-proxy) 
## Build and start the APP
From the root directory of the project
```bash
sudo docker-compose build
sudo docker-compose -f docker-compose-dataloader.yml build
sudo docker-compose up
```

## Setup database and load data

**This part should not be executed if you deploy the app on the top of an existing i2b2 instance. Executing these script may break your instance !!!!! **

### Load demo data (i2b2)
Open another terminal
```bash
./setDemoData.sh
```

### Load demo data (shrine)
After i2b2 demo data are loaded
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
go to i2b2 ==> http://your_hostname/webclient ==> You should be able to execute a query

go to shrine ==> https://your_shrine_hostname:6443/shrine-webclient ==> At this stage you can not execute a query as your shrine node is not connected to the network.

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
*	His own https certificate (shrine-hub-https-ca.crt)
* Your signed certificate (<your_hostname>-signed.crt)

### Import the hub certificates and your signed certificate

* Put the hub certificate (shrine-hub-ca.crt) in the shrine/cert/ directory of the project.
* Put the hub https certificate (shrine-hub-https-ca.crt) in the shrine/cert/ directory of the project.
* Put your signed (<your_hostname>-signed.crt) certificate in the shrine/cert/ directory of the project.

Execute the following command
```bash
sudo docker-compose exec shrine /bin/bash
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

# Certificate Backup and restore
If you are connected to the network you can backup your certificates states. This will enable to restore certificates status if you have to update or re-install the shrine container

Execute the following command
```bash
sudo docker-compose exec shrine /bin/bash
```
```bash
./backup-cert.sh
```
```bash
exit
```

If you have to reinstall shrine you can restore your certificates status after installation.

Execute the following command
```bash
sudo docker-compose exec shrine /bin/bash
```
```bash
./restore-cert.sh
```
```bash
exit
```

# SHRINE Hub
This docker-compose application can also deploy a local hub.
You can find information [here](https://github.com/CARPEM/SHRINEDocker/wiki/HUB-management) for hub deployment and certificate management
