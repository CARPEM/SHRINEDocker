sudo docker-compose -f docker-compose-dataloader.yml build osirisdataloader
sudo docker-compose -f docker-compose-dataloader.yml run osirisdataloader /opt/dataLoader/adaptTables.sh
sudo docker-compose -f docker-compose-dataloader.yml rm --force osirisdataloader


# source ./set_env.sh
# source ./functions.rc
#
#
# replaceAllEnv  './osirisOntologyLoader/Dockerfile'
#
# sudo docker build osirisOntologyLoader/ --tag osiris_metadata_loader
#
# reinitialiseAllEnv './osirisOntologyLoader/Dockerfile'
#
# sudo docker run -it --rm --network dockeri2b2_default --name osiris_metadata_loader osiris_metadata_loader python /opt/transfert_into_i2b2.py
