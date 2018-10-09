sudo docker-compose -f docker-compose-dataloader.yml build i2b2dataloader
sudo docker-compose -f docker-compose-dataloader.yml run i2b2dataloader
sudo docker-compose -f docker-compose-dataloader.yml rm --force i2b2dataloader

sudo docker-compose -f docker-compose-dataloader.yml build usermanagement
sudo docker-compose -f docker-compose-dataloader.yml run usermanagement /opt/resources/setI2b2Users.sh
sudo docker-compose -f docker-compose-dataloader.yml rm --force usermanagement


# source ./set_env.sh
# source ./functions.rc


#replaceAllEnv  './i2b2data/Dockerfile'


# sudo docker build i2b2data/ --tag i2b2data

#reinitialiseAllEnv './i2b2data/Dockerfile'

# sudo docker run -it --network dockeri2b2_default --name i2b2data i2b2data
# sudo docker rm --force i2b2data
