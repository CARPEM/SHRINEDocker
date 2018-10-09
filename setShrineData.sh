sudo docker-compose -f docker-compose-dataloader.yml build shrinedataloader
sudo docker-compose -f docker-compose-dataloader.yml run shrinedataloader
sudo docker-compose -f docker-compose-dataloader.yml rm --force shrinedataloader

sudo docker-compose -f docker-compose-dataloader.yml build usermanagement
sudo docker-compose -f docker-compose-dataloader.yml run usermanagement /opt/resources/setShrineUsers.sh
sudo docker-compose -f docker-compose-dataloader.yml rm --force usermanagement

# source ./set_env.sh
# source ./functions.rc
#
#
# replaceAllEnv  './shrineData/Dockerfile'
#
# sudo  sudo docker build shrineData/ --tag shrinedata
#
# reinitialiseAllEnv './shrineData/Dockerfile'
#
# sudo docker run -it --network dockeri2b2_default --name shrinedata shrinedata
# sudo docker rm shrinedata
