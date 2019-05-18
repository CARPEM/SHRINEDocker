#!/bin/bash

source $SECRETS

python /opt/dataLoader/scripts/data_pivot_transfert2.py

export t=$(date +"%Y-%m-%d_%H-%M-%S")
echo $t
# mkdir /opt/data_to_load/loaded_$t
# mv /opt/data_to_load/*.* /opt/data_to_load/loaded_$t
